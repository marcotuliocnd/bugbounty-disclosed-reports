# open redirect in eb9f.pivcac.prod.login.gov

## Report Details
- **Report ID**: 798742
- **URL**: https://hackerone.com/reports/798742
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-02-18T11:03:46.716Z
- **Disclosed**: 2020-05-12T18:19:43.519Z

## Reporter
- **Username**: timwhite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
poc:
```
https://eb9f.pivcac.prod.login.gov/?nonce=wI0UglN84A06Q4z4JnkZVc3i1V8%3D&redirect_uri=https%3A%2F%2Fgoogle.com%23%40secure.login.gov%2Flogin%2Fpiv_cac
```
visit this and will redirect to google.com

## Impact

phishing

## Attachments
No attachments
