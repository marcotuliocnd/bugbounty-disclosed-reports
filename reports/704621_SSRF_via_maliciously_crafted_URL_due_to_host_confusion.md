# SSRF via maliciously crafted URL due to host confusion

## Report Details
- **Report ID**: 704621
- **URL**: https://hackerone.com/reports/704621
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-10-01T02:48:40.536Z
- **Disclosed**: 2021-01-08T21:03:17.955Z

## Reporter
- **Username**: jlleitschuh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

Curl is vulnerable to SSRF due to improperly parsing the host component of the URL compared to other URL parsers and the [URL living standard](https://url.spec.whatwg.org/).

## POC

`curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"`

Curl makes a request to `yahoo.com` instead of `google.com`.

## Supporting Material/References:
  * [Exact question to URL standards body](https://github.com/jsdom/whatwg-url/issues/137#issuecomment-536797948)
  * [CVE-2018-3774](https://nvd.nist.gov/vuln/detail/CVE-2018-3774) similar vulnerability in an NPM lib
    * See also: https://hackerone.com/reports/384029

To quote the standards body issue:

> Specifically the authority state deals with parsing the @ properly. However as you'll notice if it encounters the `\` beforehand, it'll go into the host state and reset the pointer at which point it won't consider `google.com:80\\` auth data for `yahoo.com` anymore.

## Other Libraries

```javascript
const whatwg_url = require('whatwg-url'); // Created by the RFC maintainers

const theUrl = new whatwg_url.URL("https://google.com:80\\\\@yahoo.com/");
const theUrl2 = new whatwg_url.URL("https://google.com:80\\@yahoo.com/");

const nodeUrl = new URL("https://google.com:80\\\\@yahoo.com/");
const nodeUrl2 = new URL("https://google.com:80\\@yahoo.com/");

console.log(theUrl.hostname); // Prints google.com
console.log(theUrl2.hostname); // Prints google.com
console.log(nodeUrl.hostname); // Prints google.com
console.log(nodeUrl2.hostname); // Prints google.com
```

## Impact

If another library implementing the URL standard is used to white/blacklist a request by host but the actual request is made via curl or the curl library, an attacker can smuggle the request past the URL validator thus allowing an attacker to perform SSRF or an open redirect attack.

## Attachments
No attachments
