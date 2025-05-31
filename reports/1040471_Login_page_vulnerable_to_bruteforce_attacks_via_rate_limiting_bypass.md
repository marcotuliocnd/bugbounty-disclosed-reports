# Login page vulnerable to bruteforce attacks via rate limiting bypass

## Report Details
- **Report ID**: 1040471
- **URL**: https://hackerone.com/reports/1040471
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-22T09:12:05.839Z
- **Disclosed**: 2021-01-09T07:33:26.393Z

## Reporter
- **Username**: tomorrowisnew_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
#SUMMARY
This report consists of two vulnerabilities. 

#1st vulnerability:
I found out that there is a rate limiting in place after 25 failed attempts. Now that is good, but when i use other email address to bruteforce, The rate limit didnt preserve to the new email. This may looks like a minor issue but such vulnerabilities may lead to mass account bruteforce. I dont know if it is an intentional behaviour but it may pose a risk for your users. I included a video poc and the python poc file for the proof

#POC
{F1089532}
{F1089533}

#2nd vulnerability
I found a way to bypass the rate limit. While trying to bypass the rate limit, i tried adding spaces in the identifier parameter and to my surprise, that bypassed the rate limiting, i then dig deeper into it and i found out that the character \n also bypass it. Now whenever we got locked out, we can just simply add \n again. And it looks like there is no limit on how much \n we can add. This completely bypassed the rate limiting in place

#STEPS TO REPRODUCE
1. Go to khanacademy.org
2. Login with any creds and intercept the request
3. Send it to intruder and use null payloads and use 30 payloads
4. You will see that you will get rate limited on the email that you use. 
5. Now add \n after the email
6. You will see that the rate limit is not in place anymore

#POC
█████████

## Impact

This may allow an attacker to do bruteforce attacks on users that may leads to account takeover

## Attachments
- exploit.py
- bandicam_2020-11-22_16-26-42-774.mp4
