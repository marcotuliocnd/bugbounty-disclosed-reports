# Authentication Bypass on https://███████/

## Report Details
- **Report ID**: 2414707
- **URL**: https://hackerone.com/reports/2414707
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-13T00:23:56.245Z
- **Disclosed**: 2024-07-19T15:08:46.280Z

## Reporter
- **Username**: bulldawg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
An authentication bypass vulnerability exists on https://████████/ which allows access to the site.

When visiting /███████/GxSessionIfc.php, this creates a valid session for the user and allows them to bypass the ████████ authentication requirement.

PoC:
1. Visit https://████/dncp/home.php, and see that you are automatically redirected to https://████████/dncp/█████.php, the authentication page.
2. Visit https://██████████/████████/GxSessionIfc.php, which redirects to https://████████/████████/GxAccessTokenIfc.php, and subsequently  https://██████████/dncp/home.php with a valid session.

I would be more than happy to continue testing this application from an authenticated perspective using this vulnerability to demonstrate further impact and severity as well as discover additional vulnerabilities that may be of value. However, I did not want to overstep and instead decided to stop testing and report the bug as-is. Please let me know if you would like me to continue testing, as I would be more than happy to provide that additional value.

## Impact

An unauthorized user, such as an attacker, would be able to gain unauthorized access to this site. This is a breach of confidentiality. In addition, based on the functionality within the site, the impact to integrity of data and availability of the system may vary.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://██████/dncp/home.php, and see that you are automatically redirected to https://██████/dncp/███.php, the authentication page as you are unauthenticated.
2. Visit https://████/███████/GxSessionIfc.php, which redirects to https://██████/█████/GxAccessTokenIfc.php, and subsequently  https://███████/dncp/home.php with a valid session. You can now see you are authenticated, bypassing the authentication mechanism.

## Suggested Mitigation/Remediation Actions
Enforce access controls on the endpoints that set valid sessions to unauthenticated users.



## Attachments
No attachments
