# [serve] Directory index of arbitrary folder available due to lack of sanitization of %2e and %2f characters in url

## Report Details
- **Report ID**: 307666
- **URL**: https://hackerone.com/reports/307666
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-21T15:44:02.801Z
- **Disclosed**: 2018-01-23T16:01:07.919Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

This report is about Arbitrary Directory Listing vulnerability I found in serve module.
Vulnerability does not allow to open arbitrary file due to ```send``` module which handles file reading and implements its own validation and protection against Path Traversal attacks.

However ```serve``` handles directory listing on its own and does not protect against listing of any directory on the remote server.

**Module:** 

```Serve``` is a module which allows to server static files and browse directories in the browser. The vulnerability exists in the latest available version (6.4.8)

Link to npm page: https://www.npmjs.com/package/serve

**Summary:** 

```Serve``` does not handle ```%2e``` (.) and ```%2f``` (/) and allows to use them in paths, which can be used do go up through directory tree and lists content of any directory.


## Steps To Reproduce:

- install ```serve```

```
$ npm install serve
```

- create simple application which uses ```http-pages``` for serving static files from local server:

```javascript
const serve = require('serve')

const server = serve(__dirname, {
    port: 4444,
    ignore: []
})
```

- run application:

```
$ node app.js
```

- open the browser and go to ```http://localhost:4444``` You should see all directories and files in the directory, where ```app.js``` was run:

{F256095}

- now, open the following url: ```http://localhost:4444/..%2f/..%2f/..%2f/..%2f/etc/``` (please adjust the number of ..%2f/ to reflect your system). You'll be able to see the content of ```/etc``` directory:

{F256096}


## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.2
- node 8.9.3
- npm 5.5.1
- curl 7.54.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability allows malisious user to list content of any directory on the remote machine, where ```serve``` runs. Although it's not enough to open and read arbitrary files, this still might expose some sensitive information which can be used in different attacks.

## Attachments
- 1.png
- 2.png
