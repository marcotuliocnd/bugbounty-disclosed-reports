# No Rate Limit in Login Page

## Report Details
- **Report ID**: 1322243
- **URL**: https://hackerone.com/reports/1322243
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-28T15:00:00.819Z
- **Disclosed**: 2023-10-09T12:59:36.039Z

## Reporter
- **Username**: mr_sparrow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: on

## Vulnerability Information
## Summary:

A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache. In case a client made too many requests within a given time frame, HTTP-Servers can respond with status code 429: Too Many Requests.

## Steps To Reproduce:

1) Go to https://partnerbootcamp.on-running.com/
2) Now go to login  and enter the victim's email id and some random password and click login.
3) Now capture this request using burpsuite and send it to the intruder and add the password field to attack.
4) Now set the payload.[Here I added 1000 payloads].
5) now start the attack.
---> All the wrong credential respond with 401 and the correct one respond with the status code 200.

## Impact

The attacker can easily takeover to the victim's account using this method.

## Mitigation:

As a best practice the site should be implemented with some ratelimit functionalities like after 5 or 10 wrong login attempts the server should block the ip address and should respond with status code 429 "Too Many Requests".

Regards,
aaruthra

## Attachments
- onrunn.png
