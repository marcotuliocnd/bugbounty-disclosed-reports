# Rate limit bypass on passport.acronis.work using X-Forwarded-For request header

## Report Details
- **Report ID**: 2627062
- **URL**: https://hackerone.com/reports/2627062
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-27T00:21:02.547Z
- **Disclosed**: 2024-11-28T16:07:19.291Z

## Reporter
- **Username**: analyz3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
On https://passport.acronis.work/ you cannot attempt to login even if you have a valid email address, and theres also a rate limit which can make it impossible to perform brute force attack to find valid emails, and even if you have a valid you still cannot attempt login since you are not from the same location of the victims location.

While brute force attacks and user enumeration are both at out of scope, but please remember this vulnerability is actually an access control issue that allows the attackers to bypass the restriction of attempting logins, but it also allows attackers to spoof their ip addresses, spoofing ip addresses may allow attackers to use your employee ip addresses and act as them from un-authenticated endpoints.

Since the malicious header allows attacker to bypass the rate limit, attackers may also be able to bypass the otp when trying to login to a victims account, while the otp is a 12 character otp, but its actually doesn't  mean attackers aren't able to send much requests, and this is can lead to takeover your employee accounts which is actually a critical vulnerability.

So just in case, if you wanted to close the report or not interested, please remember that this vulnerability is actually an access control vulnerability not only brute forcing or user enumeration.

## Steps To Reproduce
Steps to bypass the rate limit:
1. try to attempt 10 failed logins, you must face the rate limit error, 429 status
2. now simply add `X-Forwarded-For: 12.34.56.78` header which is a malicious header, and you see you are able to submit 10 more requests
3. if you wanted to brute force the endpoint, you can use burp suites intruder, brute force both the ip address and the email, you see you are still able to submit requests even after 300 requests

Steps to bypass the restriction on login with victims email addresses:
1. in case you wanted to try to login to a victims account as attacker, such as `ab@acronis.com` which I found on snov.io you can't if you aren't from bulgaria, you will be restricted due to you are not from bulgaria and you see that error `ERR-B258C8`
2. on burpsuite, visit proxy settings, match and replace settings, replace nothing with `X-Forwarded-For: 109.104.192.0 ` (the ip is from bulgaria)
3. visit https://passport.acronis.work/login and try to login with the victims email, you see the restriction has been removed

Same bypass can be used to bypass the rate limit on the otp submit endpoint.

## Recommendations
Disable `X-Forwarded-For` header

# POC
{F3472107}

## Impact

Attackers able to bypass rate limit, also bypass restriction on attempting to login to employee accounts due to allowing a malicious http header.

Please let me know if you need more information, Thanks.

## Attachments
- Screen_Recording_2024-07-27_at_3.16.42_AM.mov
