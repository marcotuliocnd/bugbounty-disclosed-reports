# Program admins could add verified domains to an organization

## Report Details
- **Report ID**: 2323303
- **URL**: https://hackerone.com/reports/2323303
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-01-17T12:00:37.626Z
- **Disclosed**: 2024-03-07T15:10:05.577Z

## Reporter
- **Username**: hillybot_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
in hackerone according to the documentation https://docs.hackerone.com/en/articles/8490190-domain-verification only an organization admin could add verified domain .but there is an bypass.

steps to reproduce:
1. create an sandbox
2.remove org admin permission(you must add program admin permission before removing org admin) 
3. go to the url
      https://hackerone.com/<program you are admin of>/domain_ownerships/new
4.from there you will be able to add verified domain in the org

## Impact

access of restricted feature
privilage escalation

## Attachments
No attachments
