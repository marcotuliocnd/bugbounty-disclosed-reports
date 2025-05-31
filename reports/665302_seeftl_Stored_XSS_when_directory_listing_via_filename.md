# [seeftl] Stored XSS when directory listing via filename.

## Report Details
- **Report ID**: 665302
- **URL**: https://hackerone.com/reports/665302
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-01T03:37:27.780Z
- **Disclosed**: 2019-12-31T14:05:17.695Z

## Reporter
- **Username**: luizviana
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Stored XSS via filename in directory listing in seeftl
It allows to inject malicious input in a filename that leads to stored XSS when directories listing.

# Module

**module name:** seeftl
**version:** 0.1.1
**npm page:** `https://www.npmjs.com/package/seeftl`

## Module Description

seeftl -- 一个简单的预览ftl文件的静态服务器（在anywhere基础上改的）

仅仅是通过在ftl同级目录写一个config文件，替换ftl里的变量和宏 达到实时预览的功能：

## Module Stats

[8] downloads in the last week

# Vulnerability

## Vulnerability Description

The XSS occurs due the module does not sanitize de representation of filename when directories listing.

## Steps To Reproduce:

install seeftl:
`$ npm install seeftl -g`

Create a file with the following name:
`" onmouseover=alert('xss') "`

{F544502}

run seeftl server in the path that you created the file with the malicious filename:
```
$ seeftl
Running at http://127.0.0.1:8000/
```

Open `http://localhost:8000/` in your browser.

{F544503}

Put the mouse over the filename and the event will be triggered and pop up the alert.

{F544504}

## Patch

Users input should be sanitized and dangerous characters should be HTML encoded before printing them on screen.

## Supporting Material/References:

- Kali Linux 2019.2 amd64
- v10.15.2
- 5.8.0
- Firefox ESR 60.7.2esr (64-bit)

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

It allows to inject malicious scripts in filenames and execute them in the browser via a XSS.

## Attachments
- img1.png
- img2.png
- img3.png
