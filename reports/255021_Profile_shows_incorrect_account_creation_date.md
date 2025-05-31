# Profile shows incorrect account creation date

## Report Details
- **Report ID**: 255021
- **URL**: https://hackerone.com/reports/255021
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-30T17:47:25.104Z
- **Disclosed**: 2017-07-31T04:29:22.775Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team,

I get to know that you are using showing joined time. it's contain design issue. I think that you show for once user login in to their account and it should show from howmany minutes that user logged in?
but i can see here a design issue, is that whenever we refresh page https://app.legalrobot.com/account , it started from 0 seconds.

here i can see that function issue, that is reset to 0 after every page reset. (https://app.legalrobot.com/account). it should reset only at logout time.

Thanks,
Vishal.

## Attachments
No attachments
