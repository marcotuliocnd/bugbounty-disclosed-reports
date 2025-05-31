# Wordpress Users Disclosure (/wp-json/wp/v2/users/)  

## Report Details
- **Report ID**: 1663363
- **URL**: https://hackerone.com/reports/1663363
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-08T23:11:05.413Z
- **Disclosed**: 2022-08-11T20:46:19.020Z

## Reporter
- **Username**: hammodmt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: top_echelon_software

## Vulnerability Information
Hello Team @top_echelon_software
Information:
Using REST API, we can see all the WordPress users/author with some of their information.  

Step To Reproduce:
You can get user info by entering below url in your browser:
https://www.topechelon.com/wp-json/wp/v2/users/ 
███████

## Impact

Authors : LTR , LTREditor can be created scenario of doing bruteforce attacks to this users

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known)

## Attachments
No attachments
