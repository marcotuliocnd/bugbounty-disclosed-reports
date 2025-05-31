# url.parse() hostname spoofing via javascript: URIs

## Report Details
- **Report ID**: 395845
- **URL**: https://hackerone.com/reports/395845
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-16T09:28:36.010Z
- **Disclosed**: 2020-01-15T09:00:13.685Z

## Reporter
- **Username**: bayotop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

Using [url.parse()](https://nodejs.org/api/url.html#url_url_parse_urlstring_parsequerystring_slashesdenotehost) in security sensitive checks is dangerous as an arbitrary hostname can be spoofed via `javascript:` URIs. 

**Description:**

[The original url.parse() API](https://github.com/nodejs/node/blob/master/lib/url.js) is dangerous as it allows to spoof an arbitrary hostname via a `javascript:` URI:

```bash
$ node -e 'console.log(require("url").parse("javAscript:alert(1);a=\x27@white-listed.com\x27"))'
Url {
  protocol: 'javascript:',
  slashes: null,
  auth: 'alert(1);a=\'',
  host: 'white-listed.com',
  port: null,
  hostname: 'white-listed.com',
  hash: null,
  search: null,
  query: null,
  pathname: '\'',
  path: '\'',
  href: 'javascript:alert(1)%3Ba%3D\'@white-listed.com\'' }

```

**Steps To Reproduce:**

  1. `node -e 'console.log(require("url").parse("javAscript:alert(1);a=\x27@white-listed.com\x27"))'`

After a quick look, I believe the issue stems from case-sensitive checks on lines [268](https://github.com/nodejs/node/blob/master/lib/url.js#L268) and [275](https://github.com/nodejs/node/blob/master/lib/url.js#L275)

**Additional notes:**

I didn't set the severity as I have no idea how widely the "Legacy API" is still used and the actual impact is hugely context-based. For the sake of completeness, I found this issue when testing a real world app.

This also affects [this npm package](https://www.npmjs.com/package/url). 
The WHATWG API handles this particular case well.

In might be a good idea to mention in the documentation that URL parsing shouldn't be relied on in security relevant context. Exact string matching or similarly simple concepts should be always preferred.

## Impact

This can be dangerous if used in security relevant access controls as follows:

```js
let parsedUrl = UrlHelper.parse(url); // url = javAscript:alert(1);a='@localhost/'
if (parsedUrl.hostname === 'localhost') { // parsedUrl.hostname = localhost
  return true; // and do something like window.location = url 
}
```

Although being a bad practice, developers will write this code and will introduce bypassable access controls. Given that the bypass works only with `javascript:` URIs this will likely lead to XSS in most cases.

## Attachments
No attachments
