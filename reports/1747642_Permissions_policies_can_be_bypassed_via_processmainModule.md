# Permissions policies can be bypassed via process.mainModule

## Report Details
- **Report ID**: 1747642
- **URL**: https://hackerone.com/reports/1747642
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-10-24T11:29:58.157Z
- **Disclosed**: 2023-03-19T17:12:01.356Z

## Reporter
- **Username**: goums
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** 
Permissions policies module can be bypassed via `process.mainModule.require`

**Description:**
Permission policies allow to run a script with a specific set of authorized node js built-in modules.
However, the script could access non authorized modules by calling `process.mainModule.require()`

## Steps To Reproduce:

  1. Create `escape.js` file:
```
console.log(process.mainModule.require("os").cpus());
```
  2. Create `policy.json` file:
```
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

  3. Run:
```
node --experimental-policy=policy.json escape.js
```
4. You will see your os cpus listed in the console even though the `escape.js` file does not have the permission to import the node`os` module

## Impact: 
Permission policies are supposed to enforce imported modules to a limited whitelist.
This vulnerability allow a script to include any non-whitelisted module.

If you modify `escape.js` to use top level `require` statement, like this:
```
const os = require("os");
console.log(os.cpus());
```
and run again:
```
node --experimental-policy=policy.json escape.js
```
you'll now see this error:
```
Error [ERR_MANIFEST_DEPENDENCY_MISSING]: Manifest resource escape.js does not list os as a dependency specifier for conditions: require, node, node-addons
```
which is the expected behavior and should be enforced as well when using `process.mainModule.require`

## Impact

Any project that uses permission policies for arbitrary code execution are vulnerable to sandbox escaping.
This example show a non-critical permission gain (listing the machine cpu), but an attacker could do much more damage by accessing internal file system, running child processes, ...

## Attachments
No attachments
