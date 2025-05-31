# Information Disclosure through .DS_Store in ██████████

## Report Details
- **Report ID**: 142549
- **URL**: https://hackerone.com/reports/142549
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-01T20:14:50.732Z
- **Disclosed**: 2016-12-12T18:58:51.313Z

## Reporter
- **Username**: lewerkun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hello!

Description:
The website located at █████████ suffers from an information disclosure through ".DS_Store" file, accessible to unauthorised external users.
In the Apple OS X operating system, .DS_Store is a file that stores custom attributes of its containing folder.

Reproduction Steps:
Guide for installing DS_Store parser - https://digi.ninja/projects/fdb.php

First link: (See pic 0 and 1)
███████.DS_Store

Second link: (See pic 2 and 3)
████Packages/.DS_Store
This directory contain tons of packages for MacOS
Including licence keys (See pic 4 and 5) 
██████████Packages/█████████
██████████Packages/████
and etc
Certificate for WIFI (See pic 6)
█████████Packages/█████
Twitter Root certificate (See pic 8)
█████████Packages/███████
And other juicy stuff which is intended only for Twitter employees

Third link (See pic 7)
██████████Scripts/.DS_Store
This directory contain tons of scripts for installation and configuring corporate computers.

In one case the attacker can just use Twitter licenses and etc (for obvious reasons, I didn't check whether this licences is still active ), in other this information can be useful for future attacks.

Please let me know if you need some extra information.
Thanks in advance!










## Attachments
No attachments
