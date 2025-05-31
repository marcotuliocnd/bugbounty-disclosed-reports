# Incorrect logic when buy one more license which may lead to extend the expire date of existing license

## Report Details
- **Report ID**: 2461737
- **URL**: https://hackerone.com/reports/2461737
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-04-13T08:08:42.751Z
- **Disclosed**: 2024-04-16T07:41:26.935Z

## Reporter
- **Username**: liru
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Hi Team,

I noticed a bug in the licenses which may lead to extend the expire date of existing license. To be honest, it is hard for me to reproduce it. I was plan to see if the license still works after ███████. I think it's better to report this issue to you althought it may prove it is just a display issue. 

Background: 
when our company buy one more license with 5 years. Our existing license with 4 users will expire on ████. After we pay the money and got the new license. I revisit the following page and found something interesting. My existing license change from 4 users to 1 user, but the expire date is change to ███. 
██████

1. Make sure you have an existing license (in my case, we have a 4 users licenses which will expire on ██████████). 
2. Buy a new one user license with 5 years and pay it.
3. After you receive the license, check it on the following page.
█████

Observer result:
1. The existing license has change from 4 user to 1 user, but the expire date is █████████. I don't try to see if we can still use the left of the license because it will consume our licenses. 
2. The new license should expire at around ███████ but now it is ███. This means the new license expire date is extended. 

You can track my accout to debug this issue. If you need any help from me. Please feel free to let me know. Thanks!
████

User can use this way to extend the existing license. For example, you can just buy one year and it will expire next year. Then buy one more license which will expire 10 years. Now you have two license both will expire 10 years. 

## Attachments
No attachments
