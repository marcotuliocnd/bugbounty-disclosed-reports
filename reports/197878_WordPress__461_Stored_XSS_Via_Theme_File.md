# WordPress <= 4.6.1 Stored XSS Via Theme File

## Report Details
- **Report ID**: 197878
- **URL**: https://hackerone.com/reports/197878
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-12T16:46:19.823Z
- **Disclosed**: 2017-01-13T02:43:57.000Z

## Reporter
- **Username**: madrobot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello __Team__,

__Description__:-
>Vulnerable code is located at /wp-admin/includes/class-theme-installer-skin.php

__POC__:-
https://nextcloud.com/readme.html

{F151887}



__FIX__:-
Upgrade wordpress to latest


__Refer__:-
>https://wpvulndb.com/vulnerabilities/8718
>https://www.mehmetince.net/low-severity-wordpress/

__Attack Scenario__:-
1 – Attacker uploads a theme as a zip file.
2 – Webmaster who just want to download a theme and then upload, takes a theme file.
3 – And upload it without verify content of zip file.


__Regards__,
Santhosh


## Attachments
- 16.png
