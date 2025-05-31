# Disavowed an email without any authentication

## Report Details
- **Report ID**: 2088808
- **URL**: https://hackerone.com/reports/2088808
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-28T18:07:15.856Z
- **Disclosed**: 2023-07-31T07:32:17.151Z

## Reporter
- **Username**: hunterr0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hii team, I hope you are doing well.
While conducting my research I found that there are some URLs that leads to disavowing some account without any authentication.
It allows unauthorized users to disavow or dissociate an email address from an account without requiring proper authentication.

Steps to reproduce:
1. Put this command into your terminal:
waybackurls liberapay.com | grep disavow

This command will collect all the URLs related to liberapay.com and search for the specific keyword "disavow".

If you open one of the URLs you'll disavow an account without proper authorization.

## Impact

Unauthorized Account Access: Attackers can disassociate a legitimate email address from an account, potentially preventing the real owner from accessing their account.

Please let me know if you need more info.

Kind Regards
@sameersec

## Attachments
No attachments
