# hosted.weblate.org display of unfiltered results

## Report Details
- **Report ID**: 1454552
- **URL**: https://hackerone.com/reports/1454552
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-01-19T20:49:17.777Z
- **Disclosed**: 2022-01-21T20:47:58.490Z

## Reporter
- **Username**: joshmcman08
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
able to request all changes of everything not just sandbox when inserting this %'s in author username on this page.  https://hosted.weblate.org/changes/?project=sandbox&lang=en&user=%25%27s&start_date=&end_date=

## Impact

no filter on request feels like elevated permissions. lets you do the search even though it throws error.

## Attachments
- Screenshot_2022-01-19_124720.png
- Screenshot_2022-01-19_124743.png
