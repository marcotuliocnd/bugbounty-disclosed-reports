# fs.fchown/fchmod bypasses permission model

## Report Details
- **Report ID**: 2590608
- **URL**: https://hackerone.com/reports/2590608
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-09T02:34:38.858Z
- **Disclosed**: 2024-10-16T19:19:55.978Z

## Reporter
- **Username**: 4xpl0r3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello IBB team, i would like to submit a report about Node.js vulnerability that i have reported to the Node.js team, which was assigned to CVE-2024-36137  and disclosed today. Please check #2472071.

Modifier: I have proposed a fix(-25% shouldn't be apllied) and the feature is experimental (-50%), so I believe the final ratio is 50%.

## Details:
A vulnerability has been identified in Node.js, affecting users of the experimental permission model when the --allow-fs-write flag is used.

Node.js Permission Model do not operate on file descriptors, however, operations such as `fs.fchown` or `fs.fchmod` can use a "read-only" file descriptor to change the owner and permissions of a file.

This vulnerability affects all users using the experimental permission model in Node.js 20 and Node.js 21.

Please note that at the time this CVE was issued, the permission model is an experimental feature of Node.js.

## Impact

Node.js Permission Model do not operate on file descriptors, however, operations such as `fs.fchown` or `fs.fchmod` can use a "read-only" file descriptor to change the owner and permissions of a file.

## Attachments
No attachments
