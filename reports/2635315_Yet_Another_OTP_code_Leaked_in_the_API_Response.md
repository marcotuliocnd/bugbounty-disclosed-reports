# Yet Another OTP code Leaked in the API Response

## Report Details
- **Report ID**: 2635315
- **URL**: https://hackerone.com/reports/2635315
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-08-01T16:12:48.721Z
- **Disclosed**: 2025-01-08T10:43:03.129Z

## Reporter
- **Username**: tinopreter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
This is much similar to my report here(https://hackerone.com/reports/2633888) , except it affects a different domain. The application requests a phone number for authentication, then sends an OTP code to the user. But the OTP is leaked in the response which defeats the whole purpose of it's implementation.



## Steps To Reproduce:

{F3486534}

## Supporting Material/References:
https://hackerone.com/reports/2633888

##Recommendation
Don't return the OTP code in the API's response

## Impact

It's possible to sign up with other users accounts. It's possible to log into other users accounts as well. Another thing I noticed is that, you can sign up with any 10-digit phone number since the OTP is in the response for you to use, makes creating junk accounts easily possible.

## Attachments
- OTP-Leaked-Response-Again_2024-08-01_155943.mp4
