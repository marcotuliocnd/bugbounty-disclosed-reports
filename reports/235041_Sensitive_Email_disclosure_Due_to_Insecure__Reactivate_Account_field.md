# Sensitive Email disclosure Due to Insecure  Reactivate Account field

## Report Details
- **Report ID**: 235041
- **URL**: https://hackerone.com/reports/235041
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-31T19:39:54.167Z
- **Disclosed**: 2019-12-02T18:58:49.835Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker could discover the emails of accounts on ██████ through the reset field.
**Description:**
https://████/███/accounts/request_reactivation/ 
This password reset field has no rate limiting, it additionally allows an attacker to guess at user accounts such as admin and it will then expose the account user's email. For example, I used admin for my example and was given this email,████████.  Normally password reset fields keep the account emails hidden to prevent any attempt to directly attack the  user,  for example  phishing emails. 
## Impact
Medium
## Step-by-step Reproduction Instructions

1. Visit https://███/██████████/accounts/request_reactivation/
2. Enter admin  and then submit
3. You will receive the following text 

Activation Email Sent

We've sent an email to██████ containing a link that will reactivate your account.

If███████ is not your email address, please contact the GRiD team and we will be happy to assist you.

## Suggested Mitigation/Remediation Actions
I would recommend changing the account reset field to log any attempts for password resets to check for any malicious or abusive attempts to harvest account names, set a limit for amount of requests for the field, and additionally make a general message such as "We have sent the reset request to the email you used on registration" 

## Attachments
No attachments
