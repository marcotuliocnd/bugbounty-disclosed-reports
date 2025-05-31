# Call back number not verified

## Report Details
- **Report ID**: 243049
- **URL**: https://hackerone.com/reports/243049
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-25T14:58:59.408Z
- **Disclosed**: 2017-07-20T21:53:29.165Z

## Reporter
- **Username**: al7311
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: airbnb

## Vulnerability Information
The issue is with the "Confirm via call functionality" 

While adding mobile number,the application does not verify the number that is being called back. A malicious user can change the number to any premium rate numbers which charge particular amount from the caller.

It was further noticed that there was not limit to number of tries that can be made from the application. Even if the call is answered, same request can be used multiple times and the application still calls back.

The attached screenshot shows that the phone number value can be changed and premium rate numbers can be used. The number used while testing is a test call number for Eurocall24 (premium number provider).

An attacker can thereby steal money by manipulating the request to make call to premium numbers.

Affected functionality:  /phone_numbers/create

## Attachments
- calls.JPG
