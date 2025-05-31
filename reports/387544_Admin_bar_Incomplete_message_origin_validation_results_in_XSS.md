# Admin bar: Incomplete message origin validation results in XSS

## Report Details
- **Report ID**: 387544
- **URL**: https://hackerone.com/reports/387544
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-27T09:47:13.771Z
- **Disclosed**: 2018-11-07T14:39:24.605Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
This issue is very similar to https://hackerone.com/reports/381192, identical logic in a different script. The JavaScript code at https://cdn.shopify.com/s/assets/storefront/bars/admin_bar_injector-7461c2cab955bf9ef3df40acd10741df8c4e27c86d9dc323f65a4e786a1786f2.js (loaded by the shop front when the admin bar is active) installs a `message` event listener. The following check is used to reject invalid origins:

    var t=e.data,i=t.action,r=t.height,n=t.url,s=t.isCollapsed,a=e.origin;
    !i||
    o.returnObjectValues(this.POST_MESSAGE_ACTIONS).indexOf(i)<0||
    this.iframe.src.indexOf(a)<0||
    this.postMessageHandler(i,r,n,s)

With `this.iframe.src` being something like `https://foo.myshopify.com/admin/bar`, this *mostly* does the job correctly. However, `e.origin` doesn't end with a slash, meaning that for example `https://foo.my` is a possible origin and would be accepted here. Sending an `redirect_to_url` message allows the attacker to specify a URL to redirect to, supplying a `javascript:` URLs here will result in script injection, only to be prevented by the pop-up blocked - if active.

*Recommendation*: Changing the check into `this.iframe.src.indexOf(a + "/") != 0` should reliably reject all invalid origins.

This attack works against shop admins who have the admin bar enabled. If admin bar doesn't show up at the bottom of your shop, clear cookies and make sure you are logged into the admin interface. I assume here that your shop is located under `foo.myshopify.com` - change the host name appropriately.

1. Download the attached `ssl_server.py` script and `exploit_admin_bar.html` page to the same directory on your computer.
2. Edit `/etc/hosts` file (that's `%Windir%\Sysnative\drivers\etc\hosts` on Windows) and add the following entry: `127.0.0.1 foo.myshopify.co` (note that it has to end with `.co` instead of `.com`). The real attackers would register `myshopify.co` or `foo.my` instead to attack your shop.
3. Start `ssl_server.py` script (requires Python 3) to run a local SSL-protected web server. On Linux and macOS this script needs to be run with administrator privileges.
4. Open https://foo.myshopify.co/exploit_admin_bar.html in your browser and accept the invalid certificate (real attacker would actually own `foo.myshopify.co`, so they would be able to get a valid certificate for it).
5. Click the link on the page.

Your shop will open in a new tab. Note a message from the pop-up blocker (if enabled) saying that a pop-up was blocked. If you are careless enough to allow that pop-up (it comes from your own shop) or disable pop-up blocker, you will see the message "Hi, script running on foo.myshopify.com here!" - JavaScript code has been successfully injected into your shop front and can make its way to the admin interface from there.

## Impact

Shop admins can be easily lured to a malicious website, e.g. by reporting a supposed issue via support channels. Once a shop admin opens that website, it gets a chance to run JavaScript code in their shop. This JavaScript code can then open https://foo.myshopify.com/admin/ in a small pop-up window and abuse the active admin session to extract data from it (CSRF tokens, shop configuration) or maybe even change admin password to take over the account.

## Attachments
- ssl_server.py
- exploit_admin_bar.html
