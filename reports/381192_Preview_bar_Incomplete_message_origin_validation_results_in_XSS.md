# Preview bar: Incomplete message origin validation results in XSS

## Report Details
- **Report ID**: 381192
- **URL**: https://hackerone.com/reports/381192
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-13T10:22:00.991Z
- **Disclosed**: 2018-07-26T17:44:51.265Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The JavaScript code at https://cdn.shopify.com/s/assets/storefront/bars/preview_bar_injector-73a4756a265c637c998799750759ae548e7f68b136e8e93e83132904afc3d30d.js (loaded by the shop front when a theme is previewed) installs a `message` event listener. The following check is used to reject invalid event origins:

    this.iframeSrc.indexOf(event.origin) < 0

With `this.iframeSrc` being something like `https://foo.myshopify.com/preview_bar`, this *mostly* does the job correctly. However, `event.origin` doesn't end with a slash, meaning that for example `https://foo.my` is a possible origin and would be accepted here. Sending an `exit_preview` message allows the attacker to specify a URL to redirect to, supplying a `javascript:` URLs here will result in script injection.

*Recommendation*: Changing the check into `this.iframeSrc.indexOf(event.origin + "/") != 0` should reliably reject all invalid origins.

I demonstrate this attack against a random shop that is *not* under my control (roolee.com) to prove that no special knowledge is required. Steps to reproduce are:

1. Download the attached `ssl_server.py` script and `exploit_preview.html` page to the same directory on your computer.
2. Edit `/etc/hosts` file (that's `%Windir%\Sysnative\drivers\etc\hosts` on Windows) and add the following entry: `127.0.0.1 roolee.co` (note that this is `.co` and not `.com`). The real attackers would register `roolee.co` domain instead, it is for sale.
3. Start `ssl_server.py` script (requires Python 3) to run a local SSL-protected web server. On Linux and macOS this script needs to be run with administrator privileges.
4. Open `https://roolee.co/exploit_preview.html` in your browser and accept the invalid certificate (real attacker would actually own roolee.co, so they would be able to get a valid certificate for it).

A message saying "Hi, script running on roolee.com here!" shows up - that's JavaScript code successfully injected into the context of the roolee.com shop. Note that in order to trigger theme preview the URL https://roolee.com/?preview_theme_id=31994708068 is being loaded in the frame - the theme ID 31994708068 is the theme currently used by roolee.com and can be seen in the shop's HTML source code ("View Source" on the shop's homepage and search for `"themeId":`).

## Impact

Injecting JavaScript into the shop front can be used to attack both customers and admins. With the customers, one possible attack scenario would be a malicious website claiming huge discounts on TV sets in the foo.myshopify.com shop. If the person is interested, this website opens foo.myshopify.com in a new tab and injects JavaScript code that will redact the prices to make it look like there is a discount as well as replace the shipping address. If the customer isn't careful and doesn't check the confirmation mail, they will have bought the TV set for the full price with shipping to the attackers. This allows attackers to turn the TV set into money, and the shop owner gets the blame.

Attacking shop admins requires luring them to a malicious website, e.g. by reporting a supposed issue via support channels. Once a shop admin opens that website, it loads foo.myshopify.com in a hidden frame and injects JavaScript code into it. This JavaScript code can then open https://foo.myshopify.com/admin/ in a small pop-up window and abuse the active admin session to extract data from it (CSRF tokens, shop configuration) or maybe even change admin password to take over the account.

*Recommendation*: The second attack scenario is avoidable, XSS issues in the store front shouldn't compromise the admin interface. The admin interface should be located under a different subdomain, e.g. `admin.foo.myshopify.com`. This will make sure that code running in the shop front is forbidden from accessing it by the same-origin policy.

## Attachments
- ssl_server.py
- exploit_preview.html
