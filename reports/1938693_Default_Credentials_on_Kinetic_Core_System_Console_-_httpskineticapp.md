# Default Credentials on Kinetic Core System Console - https://█████/kinetic/app/

## Report Details
- **Report ID**: 1938693
- **URL**: https://hackerone.com/reports/1938693
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-04-07T19:31:53.668Z
- **Disclosed**: 2023-05-15T15:03:31.117Z

## Reporter
- **Username**: waterlord7788
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The Kinetic Core System Console application has weak credentials of **admin/admin**.

## References
[https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials)

## Impact

Potential attackers could identify technologies being used underneath. This would allow for them to find potential exploits.
In addition, the application is disclosing server logs, users in the database with their emails and names, system activity, and much more.
Check the uploaded image for additional information.
This information should not be available. 
With addition of sensitive data being shown, this is a serious issue.

## System Host(s)
█████

## Affected Product(s) and Version(s)
Kinetic Core System Console - 2.1.0-SNAPSHOT

## CVE Numbers


## Steps to Reproduce
1. Browse to the [Login page](https://████/kinetic/app/).
2. Login using credentials of **admin/admin**.
3. You should now be logged into an admin account.

## Suggested Mitigation/Remediation Actions
Change admin's password to something more secure.



## Attachments
No attachments
