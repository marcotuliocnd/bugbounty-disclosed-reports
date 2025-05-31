# Stored XSS in [shop].myshopify.com/admin/orders/[id]

## Report Details
- **Report ID**: 214044
- **URL**: https://hackerone.com/reports/214044
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-03-17T00:21:07.090Z
- **Disclosed**: 2017-03-28T21:01:59.726Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,
I have found a stored XSS vulnerability in `[shop].myshopify.com/admin/orders/[id]` in conversion details links, it's the same as #55842 but this one is through landing page URL not the referrer.

**Steps to reproduce**: 
1. Navigate to `[shop].myshopify.com/` 
2. Modify `_landing_page` cookie value to `javascript:alert(1)`
{F169421}
3. Add a product to your cart then complete the checkout process.
4. Login with an admin account then navigate to `[shop].myshopify.com/admin/orders/[id]` and click the link for **The first page they visited** and `alert(1)` will be executed.
{F169422}

**Impact**:
This is a customer-to-admin XSS, so an attacker can target admins to do malicious actions such as fetching the CSRF token and using it to submit a request to add himself as an admin to takeover the store.

## Attachments
- cookie-edit.png
- xss.png
