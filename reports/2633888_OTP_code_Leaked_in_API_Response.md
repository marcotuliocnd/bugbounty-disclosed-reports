# OTP code Leaked in API Response 

## Report Details
- **Report ID**: 2633888
- **URL**: https://hackerone.com/reports/2633888
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-07-31T20:43:55.733Z
- **Disclosed**: 2025-01-08T10:40:34.553Z

## Reporter
- **Username**: tinopreter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
The application https://corporate.admyntec.co.za allows users to sign up for device insurance. When you Get a Quote, it requires authentication via phone number. An OTP is sent to the phone number to further validate the action was initiated by the legit user. Except this same OTP code is returned in the OTP response.

## Steps To Reproduce:

  1.Vist https://corporate.admyntec.co.za/customerInsurance and get a quote. 
  2. Have a proxy interceptor tool like burpsuite running. Now enter any valid MTN number.
   3. Notice the OTP code is also returned in the API's response

{F3484295}

## Impact

It's possible to sign up with other users accounts. It's possible to log into other users accounts as well.

## Attachments
- OTP-Leaked-Response_2024-07-31_203040.mp4
