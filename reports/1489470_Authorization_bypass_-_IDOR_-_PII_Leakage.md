# Authorization bypass -> IDOR -> PII Leakage

## Report Details
- **Report ID**: 1489470
- **URL**: https://hackerone.com/reports/1489470
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-02-23T10:43:07.102Z
- **Disclosed**: 2022-04-07T20:02:38.596Z

## Reporter
- **Username**: lubak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team!
During testing ████ I found  javascript file containing administrative panel functionality.
It is accessible at: 
https://████/█████████
In this file I found an end point responsible for returning data about applications of the website users to the website administrators.
The returned data contains PII data (Full name, phone and email) of military personnel, and or their family members.


## References
Steps to reproduce:

Run following curl command to retrieve data:
curl https://███/███ -X POST -data="url=%2F████████" -k

Modifying ██████████ parameter result in different Application being returned.
I have tested retrieving following ids: █████.

Trying to retrieve record 60000 returns no information, so maybe ~50000 applications are accessible.

## Impact

PII leak of military personnel and family members

## System Host(s)
█████████

## Affected Product(s) and Version(s)
/█████████

## CVE Numbers


## Steps to Reproduce
Run following command to retrieve data:
curl https://███████/███ -X POST -data="url=%2F████████" -k

Modifying ██████ parameter result in different Application being returned.
I have tested retrieving following ids: ███.
Trying to retrieve record 60000 returns no information, so maybe ~50000 applications are accessible.

## Suggested Mitigation/Remediation Actions
1. admin.js should be available only after Administrator successfully logs in
2. all administrative end points must check if authorized administrator is requesting them



## Attachments
No attachments
