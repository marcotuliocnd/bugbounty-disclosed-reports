# fs.statfs bypasses Permission Model

## Report Details
- **Report ID**: 2051224
- **URL**: https://hackerone.com/reports/2051224
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-05T15:16:06.182Z
- **Disclosed**: 2023-09-10T15:26:01.801Z

## Reporter
- **Username**: rafaelgss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:**

`fs.statfs` is not limited by the permission model check

**Description:**

`fs.statfs` doesn't throw ERR_ACCESS_DENIED when accessing an restricted path, being able to get stat information of the file

## Steps To Reproduce:

```console
touch ./test.js
```

```js
// index.js
const fs = require('fs')

fs.statfs('./test.js', (err, stats) => {
  console.log('stats', stats)
})
```

```
$ node --experimental-permission --allow-fs-read=/path/to/index.js
(node:756097) ExperimentalWarning: Permission is an experimental feature
(Use `node --trace-warnings ...` to show where the warning was created)
stats StatFs {
  type: 61267,
  bsize: 4096,
  blocks: 56377128,
  bfree: 27380986,
  bavail: 24498982,
  files: 14393344,
  ffree: 12478020
}
```

## Impact

Even though it can't read the file contents, it's still can perform I/O against that file to retrieve file stats and to check if a file exists.

## Attachments
No attachments
