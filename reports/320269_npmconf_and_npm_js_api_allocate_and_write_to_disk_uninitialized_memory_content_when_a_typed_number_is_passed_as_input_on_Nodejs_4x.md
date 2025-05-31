# `npmconf` (and `npm` js api) allocate and write to disk uninitialized memory content when a typed number is passed as input on Node.js 4.x

## Report Details
- **Report ID**: 320269
- **URL**: https://hackerone.com/reports/320269
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-27T13:52:05.982Z
- **Disclosed**: 2018-05-12T08:56:12.533Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Buffer allocation issue in `npmconf` (and `npm` package js api).
It allows to extract sensitive content from uninitialized memory by passing typed input to `setCredentialsByURI`, limited to Node.js 4.x and below.

# Module

**module name:** `npmconf`
**version:** 2.1.2
**npm page:** `https://www.npmjs.com/package/npmconf`

**module name:** `npm`
**version:** 5.6.0
**npm page:** `https://www.npmjs.com/package/npm`

## Module Description

> The config thing npm uses

## Module Stats

### npmconf

40 292 downloads in the last day
219 837 downloads in the last week
897 947 downloads in the last month

~1 0775 364 estimated downloads per year

`npmconf` is deprecated, but doesn't mention security issues and is still widely used, and the usage seems to *increase* over time.

### npm

`npm` download stats are not representive here, as it's mainly used as a CLI, not as JS api, but here they are (e.g. for comparison with `npmconf`):

141 545 downloads in the last day
1 067 194 downloads in the last week
3 701 192 downloads in the last month

~44 414 304 estimated downloads per year

# Vulnerability

## Vulnerability Description

When a number is passed to the `password` property of `config.setCredentialsByURI`, `npmconf`/`npm` allocate uninitialized Buffer instances during conversion to base64 (on Node.js 4.x) due to missing type checks before passing user input to the `new Buffer()` constructor.

Those Buffer instances could (and most likely will) contain sensitive information, see [Buffer-knows-everything.md](https://github.com/ChALkeR/notes/blob/master/Buffer-knows-everything.md).

Node.js 4.x is stated as supported in `npm`.

## Steps To Reproduce:

Use Node.js 4.x LTS or below.

### npmconf
```js
var URI = "https://registry.example.com:8661/";
require('npmconf').load({}, function (err, conf) {
  conf.setCredentialsByURI(URI, {username: 'foo', email: 'boo@example.com', password: 200});
  console.log(conf.getCredentialsByURI(URI)); // This just outputs the setting
  // conf.save('user', function() {}) // Warning: writes base64-encoded uninitialized buffer .npmrc
});
```

### npm
```js
var URI = "https://registry.example.com:8661/";
require('npm').load({}, function (err, npm) {
  npm.config.setCredentialsByURI(URI, {username: 'foo', email: 'boo@example.com', password: 200});
  console.log(npm.config.getCredentialsByURI(URI)); // This just outputs the setting
  // npm.config.save('user', function() {}) // Warning: writes base64-encoded uninitialized buffer .npmrc
});
```

## Supporting Material/References:

- Arch Linux
- Node.js v4.8.7 (latest in 4.x LTS branch)
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: Y
- I opened an issue in the related repository: N

I reported this initially on 2016-01-20 over email, but didn't receive any response.
Probably was deemed insignificant or out-of-scope, but I still think this should be fixed and disclosed.

## Impact

Read uninitialized memory, extracting sensitive information from it.
Cause a DoS by large Buffer allocation and conversion to string.

## Attachments
No attachments
