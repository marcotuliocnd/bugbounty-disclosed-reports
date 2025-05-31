# csrf token did not changed after login/logout many times

## Report Details
- **Report ID**: 361131
- **URL**: https://hackerone.com/reports/361131
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-02T16:53:08.720Z
- **Disclosed**: 2018-06-04T12:01:55.967Z

## Reporter
- **Username**: cryptographer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
hello team, 
your csrf token did not expired and after login and logout many times , i found that your csrf token is generated same as last one.

## Impact

if an attacker found an xss on your domain and you fixed it but attacker still has csrf token of user, attacker can use it to perform any action.

## Attachments
No attachments
