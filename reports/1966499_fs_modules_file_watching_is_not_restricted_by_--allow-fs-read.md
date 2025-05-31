# fs module's file watching is not restricted by --allow-fs-read

## Report Details
- **Report ID**: 1966499
- **URL**: https://hackerone.com/reports/1966499
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-29T22:43:56.166Z
- **Disclosed**: 2023-07-20T20:56:52.134Z

## Reporter
- **Username**: cjihrig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** [add summary of the vulnerability]
The `--allow-fs-read` flag of the permission system does not prevent file watching.

**Description:** [add more details about this vulnerability]
Attackers can watch files that they don't have read access to.

## Steps To Reproduce:
Run the following code with `--experimental-permission` and do not grant read access to `file.txt`. Modify `file.txt` in another process. Information is leaked to the attacker about a file they should not have access to.

```js
'use strict';
const fs = require('node:fs');

async function main() {
	fs.watchFile(__dirname + '/file.txt', () => {
		console.log('able to watch a file without any permissions');
	});
}

main();
```

## Impact: [add why this issue matters]

The permission system is bypassed. Attackers can receive events related to files they do not have access to.

## Supporting Material/References:

None

## Impact

The permission system is bypassed.

## Attachments
No attachments
