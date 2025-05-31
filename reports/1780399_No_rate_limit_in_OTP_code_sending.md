# No rate limit in OTP code sending

## Report Details
- **Report ID**: 1780399
- **URL**: https://hackerone.com/reports/1780399
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-11-21T14:02:54.377Z
- **Disclosed**: 2024-10-21T10:12:57.007Z

## Reporter
- **Username**: mathara
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

There is no rate limit in sendind otp code. Thus, attacker can use this vulnerability to bomb out the mobile inbox of the victim.

## Steps To Reproduce:
Step 1.
Open burp suite, and click on "Intercept is on " button from Proxy tab.

Step 2.
Launch browser and visit  https://play.mtn.co.za/authorise/, and fill all the required fields, then submit.

Step 3.
Open burp suite window, and click on "HTTP history" under "Proxy" Tab, scroll on the history list and navigate on the history with https://play.mtn.co.za/authorise/ host and /nim/otp URL, and right click to "Send to Intruder".

Step 4.
Click on "Intruder" tab -> click "Position" -> click "Clear" button,
and click on "Payloads", under payload type -> Select "Null payloads", In generate input, enter 100 .

Step 5.
Click on "Attack" button, and click ok on the pop-up screen.

NOTE : I only limit the sms as 100 for testing, but attacker can send unlimited sms in short time.

## Impact

When Attacker Send To Unlimited SMS Code For Victem .

## Attachments
No attachments
