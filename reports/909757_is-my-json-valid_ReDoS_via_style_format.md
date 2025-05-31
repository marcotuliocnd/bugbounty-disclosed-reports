# [is-my-json-valid] ReDoS via 'style' format

## Report Details
- **Report ID**: 909757
- **URL**: https://hackerone.com/reports/909757
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-27T15:07:22.309Z
- **Disclosed**: 2020-07-31T17:13:38.920Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a ReDoS in `is-my-json-valid`
It allows cause a denial of service if schema uses the built-in `style` format.

# Module

**module name:** `is-my-json-valid`
**version:** 2.20.1
**npm page:** `https://www.npmjs.com/package/is-my-json-valid`

## Module Description

> A JSONSchema validator that uses code generation to be extremely fast.

## Module Stats

1 250 253 weekly downloads

# Vulnerability

## Vulnerability Description

Classic ReDoS, polynomial time.

Note that https://www.npmjs.com/package/safe-regex is not free from false positives/negatives (as noted in its Readme) and does not catch this and other polynomial regexps (e.g. `/a*a*b/`).

## Steps To Reproduce:

```js
const imjv = require('is-my-json-valid')
const validate = imjv({ maxLength: 100, format: 'style' })
console.log(validate(' '.repeat(1e4)))
```

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

DoS if schema uses the `style` format.

## Attachments
No attachments
