# DOM based XSS in the WooCommerce plugin

## Report Details
- **Report ID**: 507139
- **URL**: https://hackerone.com/reports/507139
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-09T13:00:35.475Z
- **Disclosed**: 2019-05-05T03:09:04.991Z

## Reporter
- **Username**: wild0ni0n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
I have found a stored DOM based XSS in the order page at WooCommerce 3.5.6.

The Data input from HTML element name `_shipping_state` and `_billing_state` in order page outputs data without escaping.When the victim read the page containing the payload, it executes the script.

# Steps to reproduce

1. From a Wordpress admin menu, naavigate to WooCommerce page.
2. Click to `Add order` (Or select to the exist order data, navigate to edit page.)
3. Click to pencil icon of  `Billing` or `Shipping` items, and expand input form.
4. Select to  `Select a country...` by Country item.
5. Input following value in State / Country item.

> "><img src=/ onerror="alert(location.host)"

6. Click Create button.(If navigated from the exist order, click update.)
7. Navigate to edit page, after then an alert displayed.
See also attached screenshot.

The security impact is the same as any typical XSS.

## Impact

The security impact is the same as any typical XSS.

## Attachments
- xss.png
