# Possible PII Disclosure via Advanced Vetting Process - ██████

## Report Details
- **Report ID**: 2421796
- **URL**: https://hackerone.com/reports/2421796
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-18T22:49:51.101Z
- **Disclosed**: 2024-05-13T14:45:44.506Z

## Reporter
- **Username**: darkc0d3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Description:**
It might be possible to extract PII from Hackerone Users' via **HackerOne Advanced Vetting** process. As I tested this functionality from a sandboxed program, I'm not fully sure. An unauthozied user can download the **Advanced Vetting** term acceptance data from the ███ link. The csv file contains `Name of Finder,Username,Advanced Finder Vetting,Address (optional),Finder's Country,Date signed`. Also it has been observed that any logged-in user can download the terms_acceptance_data.
███████

### Steps To Reproduce
1.  Login to the H1 account.
2.  Go to ████ & ████ URLs. The csv file will be contains the Advanced Vetting acceptance details. Even though you don't have access to `███████` & `████████` programs. 

██████
█████████

### HTTP Request
```js
GET /█████/terms_acceptance_data.csv HTTP/2
Host: hackerone.com
Cookie: XXXXX
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
```

## Impact

Possible PII Leakage.

## Attachments
No attachments
