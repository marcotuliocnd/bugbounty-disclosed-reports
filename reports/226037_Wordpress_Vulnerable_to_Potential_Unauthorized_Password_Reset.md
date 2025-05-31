# Wordpress Vulnerable to Potential Unauthorized Password Reset

## Report Details
- **Report ID**: 226037
- **URL**: https://hackerone.com/reports/226037
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-04T08:31:19.072Z
- **Disclosed**: 2017-08-15T08:42:06.400Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,

Yesterday, a new 0day on wordpress core has been discovered by Dawid Golunski, so i want you guys to be aware of it to take an immediate action since nextcloud was using wordpress.

>Wordpress has a password reset feature that contains a vulnerability which
might in some cases allow attackers to get hold of the password reset link
without previous authentication. 
Such attack could lead to an attacker gaining unauthorised access to a 
victim's WordPress account.

Affected WP version is up to the latest one `4.7.4` , so while waiting for the release of the new version that will fix the issue, you may want to apply a temporary solution, enable `UseCanonicalName` to enforce static SERVER_NAME value.

You can see the full details of the issue on this URL: https://exploitbox.io/vuln/WordPress-Exploit-4-7-Unauth-Password-Reset-0day-CVE-2017-8295.html

Regards
Japz

## Attachments
No attachments
