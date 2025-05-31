# Wrong implementation of Telegram link on the main page for PC users

## Report Details
- **Report ID**: 1194293
- **URL**: https://hackerone.com/reports/1194293
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-12T17:07:16.905Z
- **Disclosed**: 2021-06-12T18:35:56.538Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
 I found that there is a broken link for your telegram group.
When a PC user click on telegram icon on your main page he is redirected to tg://resolve?domain=sifchain instead of https://t.me/sifchain due to some errors in configuration(coding).
That idea is good for mobile view not deskptop.
## Steps To Reproduce:
Go to the main page and click on the Instagram link.
You will observe something like
{F1298980}

## Supporting Material/References:
{F1298980}

## Impact

Users will not be able to open your telegram group on PC through clicking your telegram icon on the main page

## Attachments
- PoC.webm
