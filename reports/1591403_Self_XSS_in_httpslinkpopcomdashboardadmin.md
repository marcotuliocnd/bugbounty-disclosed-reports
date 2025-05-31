# Self XSS in https://linkpop.com/dashboard/admin

## Report Details
- **Report ID**: 1591403
- **URL**: https://hackerone.com/reports/1591403
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-04T21:20:38.044Z
- **Disclosed**: 2022-10-13T21:20:37.442Z

## Reporter
- **Username**: hazemhussien99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:

Hello Shopify team,
Found a self XSS  https://linkpop.com/dashboard/admin, the steps to reproduce are below

## Steps To Reproduce:
1- Visit https://linkpop.com/dashboard/admin
2- Click on links => add links
3- add in the url  input `javascript:alert(document.cookie)`
{F1757141}
4- Click on the link that appeared on the phone image and the alert will appear
{F1757140}
{F1757142}

In your policy page you say that you guys accept self xss as long as its two steps, here its only paste payload in input and click on image so hopefully in scope :)

## Impact

Self XSS.

## Attachments
- click.png
- first.png
- alert.png
