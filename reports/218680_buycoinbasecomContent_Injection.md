# [buy.coinbase.com]Content Injection

## Report Details
- **Report ID**: 218680
- **URL**: https://hackerone.com/reports/218680
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-05T06:36:34.082Z
- **Disclosed**: 2017-05-25T23:45:32.629Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
# Hello Coinbase

### Details

I'm not sure if this issue will count, i just want to make sure that is why i submit it. The parameter `code` is Vulnerable in Content Injection allowing me to inject any Text.

### Proof Of Concept

Here is my PoC:
{F173393}

and this which the text overlaps on the modal.
{F173394}

### PoC Link
`https://buy.coinbase.com/widget?code=<Content Injection here>&address=1234567890&crypto_currency=BTC`

Best Regards,
@phspade

## Attachments
- Content_Spoofing.png
- Content_Injection_2.png
