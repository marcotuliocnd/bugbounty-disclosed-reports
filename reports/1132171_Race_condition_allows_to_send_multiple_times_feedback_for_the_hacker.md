# Race condition allows to send multiple times feedback for the hacker

## Report Details
- **Report ID**: 1132171
- **URL**: https://hackerone.com/reports/1132171
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-26T06:36:08.060Z
- **Disclosed**: 2021-09-22T19:21:30.016Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hello team!

We've found out that the program's should be able to send feedback only once per report which is very logical. However, the program user is able to send multiple parallels requests which will lead to the race condition situation and will send multiple feedback to the hacker.  
 
## Steps To Reproduce:

- Login as a hacker who are part of your program
- Submit report as this hacker user
- Login as program user who is able to change the state of report
- Set the state of the report which you just submitted to the `resovled`
- Send feedback to the hacker using `Yes, it was great!` or `Yeah, could have been better.` button
- Once you have filled everything you will see the following HTTP request:

```
POST /hacker_reviews HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-CSRF-Token: $token
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 112
Origin: https://hackerone.com
DNT: 1
Connection: keep-alive
Cookie: $cookies
Cache-Control: no-transform

hacker_username=kijkijkoijkijkijkijkijki&report_id=1132085&positive=false&behavior=rude&private_feedback=Testing
```

-  If you are using burp suite to reproduce then intercept this request, send it to the repeater and drop it. Do _not_ forward the request to the backend
- Use burp suites turbo intruder's builtin race condition code (`examples/race.py`)
- Add header `X: %s`
- Click `Attack`
- First the system will send multiple emails to the hacker:

{F1238270}

- All of these won't be transformed as a feedback. In this case the hacker got 8 emails but only 3 feedback were genarated:

{F1238269}

## Recommendation:

Make sure only one feedback request will be processed and handled.

## References:

`https://resources.securitycompass.com/blog/race-condition-web-applications`

## Impact

Race Condition allows to send multiple times report feedbacks to the hackers

## Attachments
- feedback.png
- ti-feedback.png
