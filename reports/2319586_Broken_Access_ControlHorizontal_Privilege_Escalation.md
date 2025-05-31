# Broken Access Control(Horizontal Privilege Escalation).

## Report Details
- **Report ID**: 2319586
- **URL**: https://hackerone.com/reports/2319586
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-15T14:51:36.955Z
- **Disclosed**: 2025-01-31T11:09:43.240Z

## Reporter
- **Username**: aliyueka
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
SUMMARY
access controls are broken, unauthorized users may gain access to sensitive information, modify data, or perform actions that they shouldn't be allowed to. This can lead to various security risks, including data breaches, unauthorized privilege escalation, and other malicious activities.

STEPS TO REPRODUCE
STEP 1:
Go to https://mtn.ng/offers/ {F2982514}
Enter your number and click on Submit Button {F2982517}
Click on Ok {F2982518}



STEP 2:
Enter the OTP code sent to your number {F2982521}
Click on Validate



STEP 3:
MTN offer dashboard will automatically display  {F2982526}
https://mtn.ng/offers/list?phone=2348160817474


STEP 4:
I changed the number that i logged in with my alternative number and it works successfully
{F2982536}
https://mtn.ng/offers/list?phone=2349138557692

In this situation an attacker change the phone number to number of his choice

Example:
If you click on this link you will have access to my MTN number without an authentication
https://mtn.ng/offers/list?phone=2349138557692

## Impact

This vulnerability allow an attacker to access any MTN number in Nigeria and allow threat actors to subscribe data or airtime to the victims.

It can also allow attackers to send messages of their choice to their targeted victims and the victims might think that the message come from MTN.

## Attachments
- STEP1.PNG
- STEP2.PNG
- STEP3.PNG
- STEP4.PNG
- STEP5.PNG
- STEP6.PNG
- MTN_NG.mp4
