# [public] Stored XSS in the filename when directories listing

## Report Details
- **Report ID**: 329950
- **URL**: https://hackerone.com/reports/329950
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-26T10:40:55.911Z
- **Disclosed**: 2018-06-12T08:04:30.316Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Stored XSS issue in module **public**
It allows executing malicious javascript code in the user's browser.

# Module
**module name:** public
**version:** 0.1.3
**npm page:** https://www.npmjs.com/package/public

# Module Description
Run static file hosting server with specified public dir & port. Support a "direcotry index" like Apache httpd.

# Vulnerability
## Vulnerability Description
This issue happens because of the lack of output sanitization here:

```
files.forEach(function(file) {
    list.push('<li><a href="', path.join(base, file),'">', file, '</a></li>');
});
```   

# Steps To Reproduce:
* Install the module

`$ npm i public`

* Run

`$ ./node_modules/public/bin/public ./ 6060`

* In the target directory, create a file with name `"><svg onload=alert(3);`

`bash$ touch '"><svg onload=alert(3);'`

* In the browser, go to http://127.0.0.1:6060/, the XSS popup will fire.

{F278745}

# Supporting Material/References:
* macOS High Sierra 10.13.3
* node v8.10.0
* npm 5.6.0
* Chrome Version 65.0.3325.181 (Official Build) (64-bit)

# Wrap up
* I contacted the maintainer to let them know: N
* I opened an issue in the related repository: N

# Impact
It allows executing malicious javascript code in the user's browser

## Impact

It allows executing malicious javascript code in the user's browser.

## Attachments
- public.png
