# Unauthorized Access  Exposing Sensitive Data

## Report Details
- **Report ID**: 2858876
- **URL**: https://hackerone.com/reports/2858876
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-11-21T21:35:30.201Z
- **Disclosed**: 2024-12-18T19:38:09.342Z

## Reporter
- **Username**: moha1sd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The identified page allows unauthorized access to a user's profile management functionality without requiring authentication. Upon accessing the page, sensitive user details such as name, email address, and EDIPI, 10 digits are exposed. Additionally, an update function is available, suggesting potential for unauthorized data manipulation.

## Impact

Sensitive Data Exposure: Unauthorized parties can view critical personal identifiers
Data Manipulation: If the update function is exploitable  and Privacy and Security Risks

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1- go to the website https://████/
2 - will be asking to select certificate  Just **just click cancel ** Otherwise the server will response 403 - Forbidden: Access is denied
3-  Agree to the agreement and click on ██████████ will redirect to https://█████/███████/
4- click on login 
5- will  redirect you to https://████/███████/Dashboard

## Suggested Mitigation/Remediation Actions
Implement Authentication: Enforce strict authentication requirements



## Attachments
No attachments
