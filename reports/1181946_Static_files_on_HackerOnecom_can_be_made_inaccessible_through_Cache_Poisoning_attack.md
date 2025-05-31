# Static files on HackerOne.com can be made inaccessible through Cache Poisoning attack

## Report Details
- **Report ID**: 1181946
- **URL**: https://hackerone.com/reports/1181946
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-01T13:20:16.469Z
- **Disclosed**: 2021-12-22T23:36:39.112Z

## Reporter
- **Username**: youstin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:

Hi,

The host hackerone.com uses cloudlfare to cache static files. The header x-forwarded-scheme can be used to cause a redirect loop, which will be cached by cloudflare. By taking down a JS file, it is possible to  cause a total loss of availability on hackerone.com 

### Disclaimer

No actual denial of service attack was caused in my testing. All the testing used cache-busters, meaning it did not affect the live website in any way

## Steps To Reproduce

1.  Send the following request:

```http
GET /assets/static/js/8.9572d249.chunk.js?hackerone=poc HTTP/2
Host: hackerone.com
x-forwarded-scheme: http

```

make sure to use a get parameter as a cachebuster

2.  You should notice a 301 redirect to the same page. Since the redirect poins to the same exact page, it will not be a redirect loop. The 301 is cached and removing the header will show the same redirect loop. 


### Video PoC

 ████

## Impact

The same attack that was reproduced on `/assets/static/js/8.9572d249.chunk.js?hackerone=poc` could be reproduced on the actual file without any random parameter. This would cause the file to no longer be accessible, hence causing a DoS on any pages relying on that js file. This works on any file that is cached on hackerone.com/*, including images, css files, js files  etc. Other than js files that would make the page unusuable, an attacker could also make images unavailable, etc.

## Attachments
No attachments
