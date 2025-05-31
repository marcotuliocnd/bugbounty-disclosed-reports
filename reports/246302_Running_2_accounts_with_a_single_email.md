# Running 2 accounts with a single email

## Report Details
- **Report ID**: 246302
- **URL**: https://hackerone.com/reports/246302
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-06T05:35:07.799Z
- **Disclosed**: 2017-07-06T05:42:23.970Z

## Reporter
- **Username**: atruba
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi,

While testing, I found a logic flaw which made me to make two accounts with a single email

Reproduction Steps

1-Create one account with abc@gmail.com
2-another with abc+1@gmail.com or abc+2@gmail.com etc
3-Emails of both accounts will come at abc@gmail.com

fix:
Dont allow "+" in emails.

Thanks,

## Attachments
No attachments
