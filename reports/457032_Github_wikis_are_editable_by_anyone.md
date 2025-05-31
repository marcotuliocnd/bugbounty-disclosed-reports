# Github wikis are editable by anyone 

## Report Details
- **Report ID**: 457032
- **URL**: https://hackerone.com/reports/457032
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-06T19:02:24.008Z
- **Disclosed**: 2018-12-07T18:11:16.495Z

## Reporter
- **Username**: xiridium
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Github wikis on the following projects 

https://github.com/nextcloud/fulltextsearch
https://github.com/nextcloud/nextcloudpi
https://github.com/nextcloud/spreed
https://github.com/nextcloud/ocsms
https://github.com/nextcloud/nextcloud-snap
https://github.com/nextcloud/passman

can be edited by any logged in user in the system. This poses security and reputation risk for the company.

{F386595}

## Impact

As wikis listed above can be edited by any person on the internet, a malicious actor can accurately craft a message or a note which would lead a user to download a malicious component in a natural way.

For example: 
```
Please note that the current version is not stable due to the following line:
informat_note_send.c:4562
To ensure that the program won't crush in production, please consider installing this patch http://notsoevil.com.
In case of any following troubles, drop us an email at support@company.com
```

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.

## Attachments
- 2018-12-06_22-01-30_scrot.png
