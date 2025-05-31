# Past payments using the Direct Debit method keep subscriptions active even if payments fail

## Report Details
- **Report ID**: 789260
- **URL**: https://hackerone.com/reports/789260
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-02-05T11:30:02.580Z
- **Disclosed**: 2020-02-21T11:27:54.857Z

## Reporter
- **Username**: zaitunoil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
I think this is a vulnerability that has no impact but it violates

I found many accounts that are actively subscribed even though the payment failed, this is because the payment uses the Direct Debit method, and you have deleted it.

Because Direct Debit payments have been deleted and no longer work or can be used or cannot be detected by the system, maybe because of this the system considers payments to be legitimate and gets a subscription.

Maybe you can deactivate all subscriptions for accounts that don't have successful payments.

I know this is not a vulnerability that I report, but this is an invasion of your site's privacy.

thanks.

## Impact

Payment failed but get a subscription.

## Attachments
- Annotation_2020-02-05_182108.png
- Annotation_2020-02-05_182137.png
