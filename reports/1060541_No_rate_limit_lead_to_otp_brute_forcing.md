# No rate limit lead to otp brute forcing

## Report Details
- **Report ID**: 1060541
- **URL**: https://hackerone.com/reports/1060541
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-17T00:00:13.436Z
- **Disclosed**: 2021-08-16T19:57:01.452Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello.
There is no rate limit protection in the endpoint https://mtnonline.com/nim/submit , Which could lead to brute force otp code.

## How To Reproduce:
Visit https://mtnonline.com/nim and complete all the required field and submit.
when next page load, user will be ask otp code.
Enter any five digit number and intercept the request using burp suit.
Send the request to intruder and clear all the payload except for otp.
Select brute forcer in payload type and clear the alphabetic character in character set and leave only digit.
In the min. length and max. length enter 5.
Click on attact button.

In the attached image, all the response code where  303 which means see other, that is means try again.
If rate limit is working, from 3 to 4 request, their response should be 429 means too many request.

## Supporting Material/References:

  * [attachment / reference]


##Thanks

## Impact

Attacker can send unlimited request before code the code to expire and guess the correct otp since it can be 5 minutes to expire.

## Attachments
- Screenshot_at_2020-12-17_00-25-00.png
