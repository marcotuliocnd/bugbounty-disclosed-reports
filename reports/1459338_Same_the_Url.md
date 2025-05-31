# Same the Url

## Report Details
- **Report ID**: 1459338
- **URL**: https://hackerone.com/reports/1459338
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-01-24T18:03:54.639Z
- **Disclosed**: 2022-04-21T18:54:25.218Z

## Reporter
- **Username**: 4lzhaf_1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
i found the /graphql path and /performance_report with the post method. when i will create page with name /graphql i am not allowed on the grounds it is reserved but i can create page with name performance_report.
although both use the same method but only /graphql cannot be created.

## Shops Used to Test:
https://linkpop.com/performance_report

## Steps To Reproduce:
1. login to https://linkpop.com
2. create page and use performance_report to profile page url.
3. and it will be created successfully

Best Regards,
@4bel

## Impact

It is clear that /performance_report should not be used like /graphql.

## Attachments
- graphql.PNG
- performance_report.PNG
- url_graphql.PNG
- url_performance_report.PNG
- link_performance_report.PNG
