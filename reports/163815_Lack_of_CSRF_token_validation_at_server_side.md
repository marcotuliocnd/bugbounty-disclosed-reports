# Lack of CSRF token validation at server side

## Report Details
- **Report ID**: 163815
- **URL**: https://hackerone.com/reports/163815
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-27T13:55:11.557Z
- **Disclosed**: 2017-07-10T10:00:17.097Z

## Reporter
- **Username**: yodha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Description: Gratipay is not validating csrf token at server side for few requests. So csrf protection is not implemented application wide.

Proof of concept (Video):https://drive.google.com/file/d/0B8z7y7DxxQbwUHY4YTduYzMxbnc/view?usp=sharing

Recommended Fix:
For CSRF Protection:
1. Each critical operation request must be accompanied with a "token"
•Token is:
- Long, Random, not repeated for application lifetime.
- Unique per session or even per operation
- Part of URL in GET
- Hidden Field in POST (forms)
- Attacker cannot know / predict this token and hence cannot create requests to exploit the operation.

## Attachments
No attachments
