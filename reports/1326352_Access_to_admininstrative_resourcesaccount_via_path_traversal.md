# Access to admininstrative resources/account via path traversal

## Report Details
- **Report ID**: 1326352
- **URL**: https://hackerone.com/reports/1326352
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-31T21:38:19.831Z
- **Disclosed**: 2022-09-06T18:59:23.016Z

## Reporter
- **Username**: j4k3d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
A user can login as an administrator without the need of an ██████████ account, or an authenticated user can access and manipulate administrative resources without needing to login as an administrator. An ████████ (███████) account is required.
## References

## Impact

Exfiltration of sensitive data (IPs, system configurations, passwords, usernames, email addresses, names), website defacing, denial of service, potential rce, deletion of data.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
If you do not have an ██████(██████████) account:

Navigate to https://██████/
Login using your ████████ account. 
When you login you should be at the page https://██████/Saba/██████/CustomLogin.jsp with the error "There was an error while processing your request.  Please try again. If the problem persists, please contact the help desk at ████████".
Navigate to https://█████████/home
Your account name should say "Samba administrator"

If you do have an █████████(███████) account:

Navigate to https://█████/
Login using your ███████ account. 
Navigate to a page in the admin directory i.e. https://███████/Saba/Web_wdk/████████/platform/system/admin/systemMain.rdf  or https://██████████/Saba/Web_wdk/███████/Platform/system/admin/usersStatistics.rdf

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
