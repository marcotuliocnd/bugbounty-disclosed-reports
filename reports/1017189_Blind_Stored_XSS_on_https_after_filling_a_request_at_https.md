# Blind Stored XSS on https://█████████ after filling a request at https://█████

## Report Details
- **Report ID**: 1017189
- **URL**: https://hackerone.com/reports/1017189
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-23T17:05:28.639Z
- **Disclosed**: 2021-03-11T20:55:55.396Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

When you submit a request at https://██████████, the content is being sent to the administrators of the application, and you will be presented with your request status at https://████

The Description field at the request status page is prone to stored xss and blind stored XSS injection, because there is no sanitization on the input being inserted.

As for now this is self (because the link is for the account), i'm 100% sure that when an administrator will check the request his details will get sent to my email, and i have a xss payload stored on my user.

████████

## Step-by-step Reproduction Instructions

1. Register to https://██████████ / login to my account (████)
2. Navigate to https://███
3. Craft your XSS payload on the description window
4. Submit your request
5. Navigate to https://█████████
6. The javascript will execute.

## Suggested Mitigation/Remediation Actions
Sanitizing the input being inserted into the description window field.

##Best regards
nagli

## Impact

Stored blind XSS  on the pac.whs.mil website which could lead to administrator credentials being leaked.

## Attachments
No attachments
