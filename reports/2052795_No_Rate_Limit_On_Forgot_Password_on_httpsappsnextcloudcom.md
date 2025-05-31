# No Rate Limit On Forgot Password on https://apps.nextcloud.com

## Report Details
- **Report ID**: 2052795
- **URL**: https://hackerone.com/reports/2052795
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-07-06T12:40:47.955Z
- **Disclosed**: 2023-09-26T09:44:00.790Z

## Reporter
- **Username**: cyber_world_01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,
     I have found no rate Limit on forgot password.

Summary:-
A rate limiting algorithm is used to check if the user session (or IP address) has to be limited based on the information in the session cache. In case a client made too many requests within a given time frame, HTTP servers can respond with status code 429: Too Many Requests. (wikipedia) I just realized that on the reset password page, the request has no rate limit which then can be used to loop through one request.

Step to reproduce:-
1-Go to https://apps.nextcloud.com/password/reset/.
2- Enter email address
3- Intercept burp and send request to intruder
4- Select the number 1 to 50 and click on start attack.
5- You will get 302 OK
6- I already attached the PoC video too if you don't understand my explanation and Sorry for inconvenience for video please do mute before watching video.

Suggested to fix:-
Use CAPTCHA verification if many requests are sent. 

Reference:-
https://hackerone.com/reports/751604

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk
Attackers could use this vulnerability to bomb out the email inbox of the victim.

## Attachments
- no-rate-limit.ogv
