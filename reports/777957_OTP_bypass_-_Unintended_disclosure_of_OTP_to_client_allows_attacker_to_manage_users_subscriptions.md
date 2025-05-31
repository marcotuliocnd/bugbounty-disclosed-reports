# OTP bypass - Unintended disclosure of OTP to client allows attacker to manage users' subscriptions

## Report Details
- **Report ID**: 777957
- **URL**: https://hackerone.com/reports/777957
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-19T18:32:44.020Z
- **Disclosed**: 2020-04-11T19:29:27.770Z

## Reporter
- **Username**: b5bb904ea6b315a566eb691
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
███████ authenticates subscribers via OTP before their subscriptions to be changed. However, the request which sends the OTP also returns the OTP in the network response, allowing an attacker to manage a user's usbscriptions.

## Steps To Reproduce:
  1. Visit ████████ and open network inspector (e.g., in Chrome)
  2. Type in a subscriber's number (here, I used a random number, 0787765562)
  3. Type in the `otpKey` in the network response into the OTP prompt field on the website
  4. The OTP prompt field has been bypassed

## Supporting Material/References:

* F689609 - Example of a network response

## Impact

Change a user's subscriptions. This might also be part of a larger issue if the send-otp/ endpoint is used elsewhere.

## Attachments
- Annotation_2020-01-19_183032.png
- Annotation_2020-01-19_183217.png
