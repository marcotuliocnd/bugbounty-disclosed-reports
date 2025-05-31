# WooCommerce: Persistent XSS via customer address (state/county)

## Report Details
- **Report ID**: 530499
- **URL**: https://hackerone.com/reports/530499
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-07T09:06:52.809Z
- **Disclosed**: 2019-05-26T08:35:50.322Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Persistent XSS via customer address (state/county)
================================

CVSS
----

High 7.2 [CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N)

Description
-----------

The current version (3.5.7) of the WooCommerce WordPress plugin echoes the state/county of a customer in the admin backend without encoding, leading to persistent XSS.

For a successful attack, an attacker needs a customer account, though it is to be expected that account creation is available for users in a considerable amount of setups.

If the victim is an administrator on a default WordPress setup, an attacker can exploit the issue to gain code execution on the server by eg sending a request to edit a WordPress plugin file.

POC
---

Setup: Install the WooCommerce plugin & open registration / add a user (permissions do not matter, I used "customer"). 

To place the payload:

1. Login as a customer at http://192.168.0.101/wordpress/my-account/
2. To place a payload, either:
    - add an item to cart & proceed to checkout. Under "Billing Details", select UK as country and enter `'"><img src=x onerror=alert(1) x=y` as `County` (note the missing `>` which is required as tags are filtered).
    - Alternatively, simply change the address under account settings at `http://192.168.0.101/wordpress/my-account/edit-address/`.

To trigger the payload:

1. Go to `http://192.168.0.101/wordpress/wp-admin/users.php` and click on the customer, or directly visit `http://192.168.0.101/wordpress/wp-admin/user-edit.php?user_id=4`, where `4` is the customers ID.

## Impact

With a successful attack, an attacker can read data available to the attacked user or perform arbitrary request in the name of the attacked user. 

With a default setup, an attacker can gain code execution on the server by eg editing a WordPress plugin file.

## Attachments
- xss.png
