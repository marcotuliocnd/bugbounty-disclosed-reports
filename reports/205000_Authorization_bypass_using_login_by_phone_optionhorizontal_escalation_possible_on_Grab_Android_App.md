# Authorization bypass using login by phone option+horizontal escalation possible on Grab Android App

## Report Details
- **Report ID**: 205000
- **URL**: https://hackerone.com/reports/205000
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-09T15:59:33.227Z
- **Disclosed**: 2017-09-14T02:54:12.710Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
**Description:**
After my previous report about 2FA bypass on the Profile Edit endpoint i was interested to find enpoint, which will allow me horizontal privileges escalation.
So, I found the endpoint using android app `https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms` which allow me to bypass OTP code due to lack of rate limiting.
The root cause of the problem it that facts: resend code endpoint do not have rate limiting (it has only 30 seconds timing for resending possibility). But code activation on the `https://p.grabtaxi.com/api/passenger/v2/profiles/activate` has 3 attempts limit, then it will be expired.
Combined this two facts, i found that it is possible to succeed in the account takeover of any user using only phone number.
Method: we have only 3 code attempts, and we can reset the code every 30 seconds without rate limiting.
**This gave us 6 attempts in the minute, 360 attempts in the hour, and 8640 attempts in 24 hour**. Since codes range has only 9999 values (it is 4-digit), we will likely succeed with the correct code in the 24-72 hours.
Attacker just need to choose some 3 custom OTP codes, for example, 1056, 1057, 1058, and start trying to send them every 30 seconds. If all 3 codes will fail - reset it and try again in next 30 seconds. Sooner or later, Grab Server will throw some of this codes, and this code will be accepted, and we will have access to the victim's account. How it looks in the Web Debugger - you can see on the screenshot attached (`test.png`).
Example report, where used similar method: https://hackerone.com/reports/149598

##Impact

The attacker can bypass OTP verification on Grab android app on any mobile number using "Login with mobile number" option. Attacker can succeed in the account takeover of any user without any privileges, using only phone number and country code.

##Steps To Reproduce:

1. Use my POC tool, attached to the report (written on C#, requires .NET 4.0). Sources included.
2. Enter your test phone number  to the field (it must starts with country code without `+` and be the connected to the Grab account on Android app) - or you can use my test number `███` and press Start.
3. Tool will start sending 3 code attempts `1056, 1057, 1058` and refreshing the code in case of failing every 30 seconds. The process may take many hours, but sooner or later you will receive message with success response and session header. 


##Mitigation/Remediation Steps:
I suggest you implement a rate-limiting on this endpoint `https://p.grabtaxi.com/api/passenger/v2/profiles/activationsms`, for example, blocking code resending for some time after 5 or more resends.





## Attachments
- test.PNG
- prog.PNG
