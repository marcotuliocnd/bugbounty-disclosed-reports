# [buttle] Path traversal in mid-buttle module allows to read any file in the server.

## Report Details
- **Report ID**: 358112
- **URL**: https://hackerone.com/reports/358112
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-05-27T14:40:36.614Z
- **Disclosed**: 2018-06-27T05:21:29.208Z

## Reporter
- **Username**: n0n4me
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hello Node.js third-party modules

I would like to report path traversal in buttle module
It allows me to read any file in the server if i know the path.

# Module

**module name:** buttle
**version:** 0.2.0
**npm page:** `https://www.npmjs.com/package/buttle`

## Module Description

Simple static file (+ markdown) server.

## Module Stats

[21] downloads in the last week

# Vulnerability

## Vulnerability Description

module mid-buttle.js uses regex to check the url containing the string ".markdown". I think, the right check of the author wants, is string ".markdown" located the end of the url. But he forgot the $ in the regex. That is the first vulnerability. The second is he does not check for path traversal (../). 

```
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
```
Link in github: https://github.com/jtrussell/buttle/blob/master/lib/mid-buttle.js#L16
## Steps To Reproduce:

install buttle
```
$ npm install -g buttle
```
start buttle
```
$ buttle ./
```
start the burpsuite. Enter the url contain string ".markdown" and ../ to traverse to the file you want.
{F302395}
## Patch

I recommend that:
1. Should filter ".." in url before using that for reading file. (check path traversal)
2. correct the specific string in the url for your check. (check logic bug)

## Supporting Material/References:

- Kali linux 4.15.0
- v8.11.2
- 6.1.0
- Burpsuite community

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

The malicious user can use this vulnerability to read some file containing credential, ssh key files, source code ...

## Attachments
- 1.__Buttle__PoC-Path_traversal.png
