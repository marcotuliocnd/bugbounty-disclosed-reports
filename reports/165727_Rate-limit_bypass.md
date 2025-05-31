# Rate-limit bypass

## Report Details
- **Report ID**: 165727
- **URL**: https://hackerone.com/reports/165727
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-04T19:31:14.850Z
- **Disclosed**: 2016-11-28T21:26:03.523Z

## Reporter
- **Username**: imnarendrabhati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hello Slack,

This vulnerability is about a 2FA Bypass, On Slack Web Application there is rate limit implemented. After performing 4-6 failed 2FA Attempt, Rate limit logic will ge Triaged and ask user to wait for next attempt(preventing automated 2FA Attempts)

I tested the same using iOS App(iOS 9.3.3 iPad Air 2) and found that API Endpoint "/api/auth.signin" have no rate limit implemented.

Due to this an attacker can brute force the 2FA Valid Code to get into user(Victim`s account)
Vulnerable Endpoint - /api/auth.signin
Vulnerable Parameter = pin

Re-Production
I created the POC Video in 2 parts, Because creating this POC in singe Video will make a large size of video file.

POC Video Part 1 - https://www.youtube.com/watch?v=ZCOii-HIr4A
POC Video Part 2 - https://www.youtube.com/watch?v=d1dknJXCPy4

* Screen shot is also attached.

1) Using Slack iOS App, Sign into an account in which 2FA is enabled.
2) Intercept the 2FA enter code request and perform many numbers of attempts( In my POC i had performed 100 attempts, Due to size of POC Video) But you can perform as more as you can.
3) In attack windows you will see that all invalid code attempt came as same response code response message of "invalid_pin" but our valid code will came as different response length code response message like "{"ok":true,"token":"xoxs-62548102116-65394751110-76166043750-0a50252718","user":"U1XBLN338","team":"T1UG4303E"}"

If there was a rate limit implemented than i should get block after 4-6 failed just like Slack Web Application. 

Thanks
Narendra



## Attachments
- 2_code_attempt_list.png
- 3_error_response_.png
