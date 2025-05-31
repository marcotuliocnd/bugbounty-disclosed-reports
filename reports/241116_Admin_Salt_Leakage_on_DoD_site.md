# Admin Salt Leakage on DoD site.

## Report Details
- **Report ID**: 241116
- **URL**: https://hackerone.com/reports/241116
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-18T02:20:55.198Z
- **Disclosed**: 2019-12-02T18:59:43.866Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there, the login page located at https://█████████/████████/adminapi/administrator.cfc is leaking administrator salt which is required at authentication purpose.

#PoC:
Navigate to `https://████/████████/adminapi/administrator.cfc?method=getSalt` which will show you the admin salt  `████████` which is required for further authentication.

#Impact:
With help of salt and some other info an attacker easily bypass login by using simple hash cracking tools and get access to admin panel

#Fix:
Direct access to getSalt method should be prohibited.

Let me know if any further info is required.

Regards,
Mr_R3boot.


## Attachments
No attachments
