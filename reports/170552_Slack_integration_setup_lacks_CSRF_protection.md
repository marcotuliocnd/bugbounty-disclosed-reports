# Slack integration setup lacks CSRF protection

## Report Details
- **Report ID**: 170552
- **URL**: https://hackerone.com/reports/170552
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-09-19T21:16:55.829Z
- **Disclosed**: 2021-07-07T03:39:15.841Z

## Reporter
- **Username**: whhackersbr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Details:
**Summary:**

Cross-site Request Forgery in the `Integrations` (https://hackerone.com/[YOUR_TEAM]/integrations) feature for teams.

**Description (Include Impact):**

The `Integrations` flow is insecure, because it can be abused by CSRF.

PoC:

Request
```
GET https://hackerone.com/auth/slack HTTP/1.1
```

Response
```
Location: https://slack.com/oauth/authorize
?client_id=2174110321.11522100978
&redirect_uri=https%3A%2F%2Fhackerone.com%2Fauth%2Fslack%2Fcallback
&response_type=code
&scope=incoming-webhook
&state=379fd8f1baa8d80516e2f706f025057ad0ce2cca0bbbd56c
```

How can it be bad since you are using `state` parameter?

You are trusting in third-party security that is not under your control.
All the attacker needs is an XSS or Login CSRF or Clickjacking in the third-party system and he can compromise your system. With one of the previous mentioned vulnerabilities in the third-party system, the attacker can control the entire OAuth flow and connect his own accounts to the victim's HackerOne account.

Today, you have just one integration available (Slack).
If you implement more integrations in the future, the damage and the attack surface will grow significantly. Worst if you implement someday something like Login with Facebook / Login with Google / etc., because this bug will lead to account takeover.

**Fix:**

1) Protection against CSRF at the beginning of the OAuth flow:

e.g.:

```
GET https://hackerone.com/auth/slack?CSRF_TOKEN=bdea53bd9a8c73bd983847 HTTP/1.1
```

2) `Phabricator` approach of OAuth connections (a confirmation dialog after the end of the OAuth flow). Picture attached (F121473).

P.S.: Are you interested in Login XSRF in HackerOne?
How do you protect users against Login XSRF in your SSO flow?
Sorry, I can not fully test SSO because I need approval of SSO configuration every time.

## Attachments
No attachments
