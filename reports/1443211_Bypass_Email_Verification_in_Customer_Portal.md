# Bypass Email Verification in Customer Portal

## Report Details
- **Report ID**: 1443211
- **URL**: https://hackerone.com/reports/1443211
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-07T07:51:31.958Z
- **Disclosed**: 2022-02-26T08:20:49.145Z

## Reporter
- **Username**: 0dx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hi team hope you doing well :) 
i found a vulnerability [  OTP Bypass  ] on [ https://portal.test.cloud.mattermost.com ] .
Summery : 
I was able to use the otp that was sent to victim email and i used it in the attacker's email verify .when i tried this issue first time the server log me out  , and second time i do intercept for request and i was still in and click [next step ] on payment step and am still in without the server log me out and stop the burp after that and am in and i can using my account normally .

## Steps To Reproduce:

  1. [make two account :  victim / attacker]
  1. [ used otp that send to victim and inter it on attacker email verify and intercept the request  by burp. ]
  1. [when you doing intercept by burp click on next step and full the form and click enter and you can stop proxy and you can used the account normally.  ]


## Supporting Material/References:
[https://link.medium.com/xFYjx29xAmb]

## Impact

OTP bypass .

## Attachments
- victim_console.png
- victim_account_with_attacker_otp.png
