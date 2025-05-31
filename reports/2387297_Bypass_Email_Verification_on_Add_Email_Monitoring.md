# Bypass Email Verification on Add Email Monitoring

## Report Details
- **Report ID**: 2387297
- **URL**: https://hackerone.com/reports/2387297
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-22T20:29:44.771Z
- **Disclosed**: 2025-01-07T16:57:55.681Z

## Reporter
- **Username**: dotxml
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Steps To Reproduce:

1. Login to https://monitor.firefox.com OR https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net and click **Add email address**
█████████

2. Fill the victim's email address (I'm use my personal email) and click **Send verification link**
██████

3. Check the request on your burp suite intercept and turn on **Response intercept** to this request
████████

4. Wait until we got the response from the server and search the victim's email address, we can get the **verification_token** on the response
███████

5. For make sure the victim's email address is need a verification.. refresh your browser
█████

6. Copy and Paste the **verification_token** from the response to this link: `https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/verify-email?token={verification_token}`

7.  Open the link on your browser, Done.. the victim's email address is already verified
██████

## Impact

Attacker can add the victim's email address without verification. And if attacker choose **Send all breach alerts to primary email address**, attacker will get a notification when victim's email address is leaked
{F3074332}

## Attachments
- impact.png
