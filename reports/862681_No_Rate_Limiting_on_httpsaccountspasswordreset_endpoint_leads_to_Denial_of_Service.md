# No Rate Limiting on https://██████/██████████/accounts/password/reset/ endpoint leads to Denial of Service

## Report Details
- **Report ID**: 862681
- **URL**: https://hackerone.com/reports/862681
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-29T18:12:09.401Z
- **Disclosed**: 2020-05-27T14:14:05.231Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

No-Rate Limit on Password reset endpoint results mail-spam functionality to be abused.
Additionally, the password-reset link remain the same after each request.

**Description:**

Malicious user could Spear-target █████████ user mail and Spam it for as many requests as he would like.


Possible scenarios:
Attacker could use this vulnerability to bomb out the email inbox of the victim.
Attacker could send Spear-Phishing to the selected mail address.
Attacker might cause denial of service to the mail servers.

## Step-by-step Reproduction Instructions

1. Go to https://█████/█████/accounts/password/reset/
2.  Click on "Send Email" and Capture the request on burp.
3. Send to intruder, and start Sniping attack with NULL payloads.


## Suggested Mitigation/Remediation Actions
1. Limiting the password reset request to once every X minutes.
2. Use CAPTCHA verification after X requests.
3. Asserting random password-reset link for each request.

Similar reports:
https://hackerone.com/reports/764122
https://hackerone.com/reports/791498
https://hackerone.com/reports/441161

Best Regards,

Gal Nagli

## Impact

Attacker could use this vulnerability to bomb out the email inbox of the victim.
Attacker could send Spear-Phishing to the selected mail address.
Attacker might cause denial of service to the mail servers.

## Attachments
No attachments
