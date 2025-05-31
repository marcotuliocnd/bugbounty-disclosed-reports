# Bypass Email Verification using Salesforce -- Reproducible in gitlab.com

## Report Details
- **Report ID**: 617896
- **URL**: https://hackerone.com/reports/617896
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-18T07:51:06.730Z
- **Disclosed**: 2019-12-13T21:00:19.953Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
The salesforce login integration allows attacker to bypass email verification -- user is able to signup with any email domain they want, effectively bypass all email domain whitelist/blacklist restriction or any other 3rd party using gitlab instance's email address.

It is possible because salesforce allow admin to create user with arbitrary email, and I believe this is what gitlab engineer forgot to consider while implementing salesforce integration.

Please follow along to see how I was able to create an account `███████` in gitlab.com

### Steps to reproduce
- Visit https://bugcrowd-ngalog-3.oktapreview.com/
- Enter creds `██████████`:`██████████`
- Click salesforce to login salesforce
- Open new tab and visit https://gitlab.com/users/sign_in
- Click login with salesforce
- you will be logged in as `████` by visiting `https://gitlab.com/profile/emails`



### Impact
Bypass email domain restriction and able to signup with arbitrary email domain

### What is the current *bug* behavior?
Able to signup with any email domain

### What is the expected *correct* behavior?
should need email verification


### Relevant logs and/or screenshots
{F511255}

## Impact

described above

## Attachments
- Screen_Shot_2019-06-18_at_7.50.41_PM.png
