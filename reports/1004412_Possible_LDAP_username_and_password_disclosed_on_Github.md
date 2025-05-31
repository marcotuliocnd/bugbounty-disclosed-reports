# Possible LDAP username and password disclosed on Github

## Report Details
- **Report ID**: 1004412
- **URL**: https://hackerone.com/reports/1004412
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-10T04:47:03.868Z
- **Disclosed**: 2021-08-17T17:15:17.971Z

## Reporter
- **Username**: vovohelo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The file hosted at https://github.com/mlanin/go/blob/3dbd856c3f542c54e512a295ac498c79cd952ed6/.env.testing  contains the following information:
**LDAP_DOMAIN=███
LDAP_BASE_DN=███
LDAP_ADMIN_USER=███████
LDAP_ADMIN_PASSWORD=██████**

## Recommendations
Verify if credentials are still in use if so remove the file from GitHub and reset passwords.

## NOTE
Please let me self-close this report if the credentials do not belong to Acronis or are not active. I took a better safe than sorry approach.

## Impact

Although I was not able to find any port open on the ███████ server, if the credentials are valid they can be used by insider threats for lateral movement and privilege escalation.

## Attachments
No attachments
