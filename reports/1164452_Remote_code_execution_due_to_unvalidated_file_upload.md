# Remote code execution due to unvalidated file upload

## Report Details
- **Report ID**: 1164452
- **URL**: https://hackerone.com/reports/1164452
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-13T20:39:14.582Z
- **Disclosed**: 2022-09-01T17:29:41.958Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello 
I found a critical vunerability in one of your site, where user can upload any file type as a profile picture (including php file)


## Steps To Reproduce:
1. Visit https://careers.mtn.cm and register as a user.
2. After successful registration, login and update your data.
3. When uploading profile photo, select any file type.
 4. When its updated, view the source code of the page, you will see your file with complete path.
5. Copy the file path and paste into your browser.
6. Boom your file will be executed



## Supporting Material/References:
Here i upload non-harmful file as a poc 
```
<?php
echo "proof of concept (PoC) by aliyugombe@wearehackerone.com";
?>
```
https://careers.mtn.cm/en/user/images/users/-13-04-2021-20-15-16-payload.php

## Impact

Attacker can upload malicious file and inject to your server or deface the entire website since its possible to upload php file and gain access to direct file path.

## Attachments
No attachments
