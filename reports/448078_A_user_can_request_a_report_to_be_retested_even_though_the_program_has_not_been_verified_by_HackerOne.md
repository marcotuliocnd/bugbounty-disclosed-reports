# A user can request a report to be retested even though the program has not been verified by HackerOne

## Report Details
- **Report ID**: 448078
- **URL**: https://hackerone.com/reports/448078
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-11-21T10:10:46.947Z
- **Disclosed**: 2018-12-27T12:10:48.523Z

## Reporter
- **Username**: 0xelement
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey Team

 

I have some observations and issues which i found in my recent testing on h1 platform ( related to creation of a new private program ), So  here are my observations listed below - kindly have a look and revert back if you feel like these are valid and worth reporting issues.


1) Can A program without fully verified status have report retest feature active - (  Unnecessary disturbing the hackers of h1  - as the feature itself says that hackers will be paid 100$ for retest but here the program itself is not verified so who will be accountable to pay this 100$  )

 

I actually made a test program with handle  " █████ " ,  resolved a report onto it and then initiated the "Report Retest" feature which sent invitation to 5 hackers ( 2 of them actually tested and replied back )

 

Now current status of my test program "████████" is :

 

{{
 

A few items have prevented your program from being validated at this time. Please reach out to support@hackerone.com if you haven't received a message with next steps.

 

Email content :::

 

Hi 3thic4l,

Thanks very much for reaching out to HackerOne. I see you have requested to invite hackers and go live with a private program.

After review, your program (████████) is missing some key required elements for approval. In order to start a HackerOne program, you must have:

•             A valid Disclosure Policy that aligns with your reward structure

•             A valid attack surface for researchers to hack that is defined in your program's scope

•             A verified email address that matches your company domain

•             Our security team reserves the right to disallow any company whose properties it deems incompatible with the HackerOne program.

Best,

HackerOne Team

 

 

Your program is missing some required elements for approval.

See email from support@hackerone.com for additional detail.

 

}}

 And also 3 out of 5 researchers who got invited for retest are actually paid 100$ each , so I am not sure Weather it's intended feature or some bug.

2) Email bombing ( excessive spamming - I sent 50 mails in 1 minute using wearehackerone email handle ) in add participant  : ████████

Its like if a program sends an invitation to example@wearehackerone.com , then by using burp intruder multiple invitation email could be sent by altering address as example+1@wearehackerone.com  and so on.

 

3) No rate limit on group creation in a program : ████  ( Not really a security issue but there should be some rate limit - As i was able to create 20 groups in 5 secs through burp intruder )

 

4) Report Retest feature invites 5 hackers - now i am curious to know weather country check is in place in this feature ( ████ )

 

Waiting for your reply on the above mentioned issues.

Note : ( My user handle = 3thic4l  )

 

Regards

Ahmad

## Impact

Monetary loss to h1 -  coz the person/company accountable is not yet verified.

## Attachments
No attachments
