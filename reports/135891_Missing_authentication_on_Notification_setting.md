# Missing authentication on Notification setting .

## Report Details
- **Report ID**: 135891
- **URL**: https://hackerone.com/reports/135891
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-03T05:22:31.076Z
- **Disclosed**: 2016-07-26T00:37:14.760Z

## Reporter
- **Username**: vijay_kumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi ,
Notification setting link works without cookies so an attacker can steal link from browser histroy and can change notification setting of victim.
Notification setting link does not expire even after logout.

Steps to reproduce :-
1.Log in as uber rider.
2.Go to profile.
3.Now go to "Manage your email subscription settings".
4.Copy link of this page and open this link in another browser , it works perfectly.
5.It also works after logout.

## Attachments
No attachments
