# Ticket Trick at https://account.acronis.com

## Report Details
- **Report ID**: 999765
- **URL**: https://hackerone.com/reports/999765
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-06T13:44:41.609Z
- **Disclosed**: 2020-11-10T09:14:47.056Z

## Reporter
- **Username**: sayaanalam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Hello dear team,
I found a serious issue in Acronis
This vulnerability is called ticket trick vulnerability which comes under critical category. Which can allow me to login on websites like atlassian,github,clouflare,choopa,..etc on behalf of support_mobility@acronis.com .

## Steps To Reproduce
Lets take an example to get your github account.

1. As Github send account register verification mails from noreply@github.com
2. I registered an account on acronis with same email.
3. Now your support system creates ticket of emails sent to  support_mobility@acronis.com .
4. So I registered an account  on github and logged into my acronis account with email noreply@github.com .
5. As Acronis allowed me to see support tickets without email verification , so I was able to see support tickets easily created by noreply@acronis.com .
6. On support ticket there was an email verification link sent to noreply@github.com .
7. In this way I was able to takeover many account registered with  support_mobility@acronis.com and many internal accounts that can be accessed with only @acronis.com

##POC

I was able to register a github account on your email address :-

{F1022537}

##Resources about this vulnerability:-
https://hackerone.com/reports/498964
https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c

## Impact

* Critical Email Takeover
* Ticket Trick


Thanks for reading my report.

Best Regards
Sayaan Alam

## Attachments
- Screenshot_2020-10-06_at_7.03.17_PM.png
