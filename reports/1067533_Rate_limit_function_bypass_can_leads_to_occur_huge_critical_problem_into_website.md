# Rate limit function bypass can leads to occur huge critical problem into website. 

## Report Details
- **Report ID**: 1067533
- **URL**: https://hackerone.com/reports/1067533
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-28T17:07:19.306Z
- **Disclosed**: 2021-01-08T09:19:21.201Z

## Reporter
- **Username**: basant0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
Hello team,
I have found a technique that can easily bypass rate limit system of website and with this bug we attacker can easily attack into login panel, Sent unlimited number of huge notification to victim, bypass OTP codes and takeover accounts etc. Basically i have added a header X-Forwarded-For: 127.0.0.1 which will bypass the rate limit and reset request limits . Every time rate limit exceeded just change IP to another one and rate limit will itself reset.

Step to Reproduce:
1. Visit https://www.trycourier.app/
2. Goto email section
3. Enter victims email address
4. Fire-up burp-suite and intercept the request
5. Now Continue Sent request , If rate limit reached and blocked you then add X-Forwarded-For:127.0.0.1 header. This will easily reset rate limit. You can change IP address to 127.0.0.2 ,3,4,5,6 every time website blocked you.

( With this bypass you can easily send unlimited amount of huge email notification to victim and make victim annoying )

## Impact

1. Brute forcing login panel
2. Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.
3. Brute force OTP codes etc.

## Attachments
- Rate_Limit_Bypass__Courier_.mp4
