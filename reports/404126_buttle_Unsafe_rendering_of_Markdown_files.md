# [buttle] Unsafe rendering of Markdown files

## Report Details
- **Report ID**: 404126
- **URL**: https://hackerone.com/reports/404126
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-02T19:45:30.201Z
- **Disclosed**: 2019-01-06T00:18:00.020Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Cross Site Scripting vulnerablity in buttle module
It allows to execute arbitary javascript due to unsafe rendering of markdown files.

# Module

**module name:** buttle
**version:** 0.2.0
**npm page:** `https://www.npmjs.com/package/buttle`

## Module Description

Another static file server? Why buttle? Well... if you came here looking for a blazing fast server of static files, something with caching and compression options then you're in luck, that does exist! It just isn't buttle.

Buttle is tailored for use in development. It has baked in live reloading for html and markdown files. It'll on-the-fly convert your LESS filess to CSS... and cache nothing because it assumes you're actively hacking away. With buttle you can test drive that angular app you just cloned or maybe have your test runner page refresh whenever a source file is changed.


## Module Stats

~0 weekly downloads

# Vulnerability

## Vulnerability Description

buttle uses `kramed` for parsing and rendering markdown. By default kramed does not sanitize html. An uninformed user may assume the output of markdown to be sanitized and thus become vulnerable to XSS by rendering malicious markdown files.
 
See https://github.com/jtrussell/buttle/blob/master/lib/mid-buttle.js

```js
// line no 8
  var md = require('kramed');
  md.setOptions({
    gfm: true
  });

return function(req, res, next) {
    var url = req.url;
    if(/\.md$/i.test(url) || /\.markdown/i.test(url)) {
      fs.exists(j(dir, url), function(exists) {
        if(exists) {
          fs.readFile(j(dir, url), {encoding: 'utf8'}, function(err, data) {
            if(err) { return res.end(err.message); }
            res.end(wrapInHtml(md(data)));
          });
        } else {
          next();
        }
      });
    } else {
      next();
    }
  };
```

## Steps To Reproduce:

* install buttle:
`$ npm i buttle`

* run buttle:
`./node_modules/buttle/bin/buttle -p 8080`

* add a malicious markdown file in the server directory (`test.md` attached) and open it in browser.

## Patch

`kramed` provides an option `sanitize` which is set to `false` by default.
Either set the `santize` option to `true` in line no 11 of [mid-buttle.js](https://github.com/jtrussell/buttle/blob/master/lib/mid-buttle.js) or inform the user to safely handle markdown files by displaying an apropriate warning.

## Supporting Material/References:

Yandex 18.7.0.2767 beta (64-bit)
Ubuntu 16.04
node v10.9.0
npm 6.4.1


# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N


PS: [`kramed`](https://github.com/GitbookIO/kramed) package is a fork of another library `marked` and is unmaintained since last 2 years.

## Impact

User is exposed to unsafely rendered markdown files which may lead to execution of arbitrary JS

## Attachments
- test.md
