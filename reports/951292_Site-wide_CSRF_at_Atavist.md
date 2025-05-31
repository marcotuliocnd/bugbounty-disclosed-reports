# Site-wide CSRF at Atavist 

## Report Details
- **Report ID**: 951292
- **URL**: https://hackerone.com/reports/951292
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-04T22:54:00.128Z
- **Disclosed**: 2020-11-18T14:21:01.478Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
I have a Atavist Magazine account. And there are no CSRF tokens on account settings.

For example ;
- When changing email (there is a user ID but they are sequential) : {F936597}

- Deleting credit card : {F936618}

- Cancelling subscription : https://magazine.atavist.com/cms/ajax/cancel_subscription.php?product_id=com.theatavist.atavist.subscription.membership - this endpoint sends an email with `We'll Miss You` title, but it doesn't cancel the subscription. (this is not related to CSRF, there is a CSRF but the endpoint is weird :-D)

I didn't want to create report for each endpoint, because this is a site-wide issue. I think you can add a header for root fix.

## Impact

Site-wide CSRF 

Thanks,
Bugra

## Attachments
- req.PNG
- reqcard.PNG
