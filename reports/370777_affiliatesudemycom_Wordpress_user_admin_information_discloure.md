# [affiliates.udemy.com] Wordpress user admin information discloure

## Report Details
- **Report ID**: 370777
- **URL**: https://hackerone.com/reports/370777
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-06-25T08:36:27.771Z
- **Disclosed**: 2019-04-28T06:33:07.115Z

## Reporter
- **Username**: toannc123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
### Summary
This website using Wordpress CMS, so developer forget to disable the link that can view information of admin user.
By access to this link, attacker can get all username and other information of user admin:
> http://affiliates.udemy.com/wp-json/wp/v2/users

{F312155}

Admin user list:
* hamza
* imanrana
* nupoora

## Impact

With this vulnerability, attacker can get username of user admin and only brute-force the password for logging in the system.

## Attachments
- admin_user_list.JPG
