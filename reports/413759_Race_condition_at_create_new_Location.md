# Race condition at create new Location

## Report Details
- **Report ID**: 413759
- **URL**: https://hackerone.com/reports/413759
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-25T03:20:18.368Z
- **Disclosed**: 2018-10-05T04:49:12.421Z

## Reporter
- **Username**: zhurig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
User can bypas restriction and create more ctore location, than maximum depends store plan. Intercept request and send it multiple at once. See screensots
F350687 - requests
F350688 - results
I created 12 store location when 4 possible

## Impact

Bypass the limitations of the billing plan

## Attachments
- Requests.png
- result.png
