# Stored XSS on apps.shopify.com

## Report Details
- **Report ID**: 1107726
- **URL**: https://hackerone.com/reports/1107726
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-20T00:25:42.552Z
- **Disclosed**: 2021-04-08T19:23:55.717Z

## Reporter
- **Username**: luc1d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Steps to reProduce:

1> Write payload `luc1d"><img/src="x"onerror=alert(document.domain)>@wearehackerone.com` as `Store contact email` in General Settings page`(*.myshopify.com/admin/settings/general)`

{F1202181}

-- Wait here around 60 mins (maybe more idk, it was 60 mins for me) for the change to reflect --
(You can confirm the change on here `https://apps.shopify.com/shops/<shopId>`)
2> Visit any app page like `https://apps.shopify.com/local-delivery`
3> Click `Get support` link on sidebar
{F1202116}

4> XSS will be triggered
{F1202211}

PoC Video,
{F1202215}

## Impact

Stored XSS

## Attachments
- Screen_Shot_2021-02-19_at_4.58.44_PM.png
- Screen_Shot_2021-02-19_at_6.24.27_PM.png
- Screen_Shot_2021-02-19_at_7.22.53_PM.png
- shopify_apps_xss.mov
