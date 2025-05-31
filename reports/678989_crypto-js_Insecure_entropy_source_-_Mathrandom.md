# [crypto-js] Insecure entropy source - Math.random()

## Report Details
- **Report ID**: 678989
- **URL**: https://hackerone.com/reports/678989
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-22T01:06:03.749Z
- **Disclosed**: 2020-06-04T10:12:24.428Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Module

**module name:** crypto-js
**version:** 3.1.9-1
**npm page:** `https://www.npmjs.com/package/crypto-js`

## Module Description

> JavaScript library of crypto standards.

## Module Stats

> Replace stats below with numbers from npm’s module page:

184959 downloads in the last day
912568 downloads in the last week
3945947 downloads in the last month

# Vulnerability

## Vulnerability Description

`Math.random()` is not a cryptographically secure source of randomness, but it is used as the sole entropy source in `require('crypto-js').lib.WordArray.random`, which creates a "random" array of 32-bit words:
* https://github.com/brix/crypto-js/blob/3.1.9-1/core.js#L291-L330
* https://github.com/brix/crypto-js/blob/develop/src/core.js#L276-L315

## Steps To Reproduce:

E.g. to confirm that that is predictable given the same initial seed:
```
$ node --random_seed=42 -e "console.log(require('crypto-js').lib.WordArray.random(16))"
{ words: [ -1477405629, 964516052, 1254255372, 1089500106 ],
  sigBytes: 16 }
$ node --random_seed=42 -e "console.log(require('crypto-js').lib.WordArray.random(16))"
{ words: [ -1477405629, 964516052, 1254255372, 1089500106 ],
  sigBytes: 16 }
```

It could in theory be possible to recover the internal XorShift128+ Math.random seed by gathering enough observations.

Even if this method attempts to "mask" `Math.random` somehow perhaps in order to make extracting the seed harder, that could never be enough. For example, `Math.random` seed could be also recovered by observations over some other channel, e.g. if something else presents Math.random results to the user (e.g. not crypto-related).

## Patch

Use `window.crypto.getRandomValues` in browser and `require('crypto').randomBytes` in Node.js instead.

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Predict the values of `require('crypto-js').lib.WordArray.random`, which could be perceived as crypto-secure by users.

## Attachments
No attachments
