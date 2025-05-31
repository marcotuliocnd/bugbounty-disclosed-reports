# Wordpress Takeover using setup configuration at http://████.edu [HtUS]

## Report Details
- **Report ID**: 1626205
- **URL**: https://hackerone.com/reports/1626205
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-05T14:01:40.869Z
- **Disclosed**: 2023-01-13T18:04:31.536Z

## Reporter
- **Username**: berserkbd47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Description:

The WordPress 'setup-config.php' installation page allows users to install
WordPress in local or remote MySQL databases. This typically requires a user
to have valid MySQL credentials to complete.  However, a malicious user can
host their own MySQL database server and can successfully complete the
WordPress installation without having valid credentials on the target system.


Reproduce step by step:

I found this vulnerable url:
http://███.edu/old/wp-admin/setup-config.php

Then i configured db 
I used this site https://www.freemysqlhosting.net/

After configure I got wordpress admin access

proof:
http://██████████.edu/old/rce.txt


Admin credentials that I set after installing the config
username: ████████
password: ███

Login Panel: http://████████.edu/old/wp-login.php

Video POC has been attached as well.

## Impact

Impact
Remote Code Execution/Total system compromise.
Attacker can upload webshell into the server. I did not upload any shell for security violation.

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass

## Attachments
No attachments
