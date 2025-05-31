# App messaging can be hijacked by third-party websites

## Report Details
- **Report ID**: 387279
- **URL**: https://hackerone.com/reports/387279
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-26T18:56:22.668Z
- **Disclosed**: 2018-11-07T14:40:10.870Z

## Reporter
- **Username**: palant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The JavaScript code at https://cdn.shopify.com/s/assets/admin/index-c6e72fa910cd0182ab1d1e67ff823fb2e6ca61745c00797769410ce01aafc4d8.js installs a `message` event listener to receive messages from installed apps when these apps are displayed in a frame. The following check rejects invalid event origins:

    i.origin!==this.applicationOrigin&&!e(this.applicationOriginUri,Shopify.UrlMangler.getURL(i.origin))

Here function `e` is defined above as follows:

    e = function (e,t){
      return e.protocol === t.protocol &&
             e.port===t.port &&
             t.hostname.slice(-e.hostname.length) === e.hostname &&
             "" !== e.hostname;
    }

This logic is meant to accept messages from subdomains of the app's domain. It is flawed however: if the app is running from `example.com`, messages from `badexample.com` will be accepted as well.

*Recommendation*: Changing the condition into `t.hostname.slice(-e.hostname.length-1) === "." + e.hostname` will do the right thing.

To demonstrate this issue, my proof of concept exploits the app Trust Badge - it runs from "https://hektorcommerce.com", so anybody could register a domain name like `dehektorcommerce.com` and send messages to the admin interface which will then be accepted. This is not a flaw in the app however, any app not running from a subdomain can be exploited in the same way.

# Steps to reproduce

1. Make sure to install [Trust Badge app](https://apps.shopify.com/trust-badge) in your shop.
2. Download the attached `ssl_server.py` script and `exploit_app_comm.html` page to the same directory on your computer.
3. Edit `/etc/hosts` file (that's `%Windir%\Sysnative\drivers\etc\hosts` on Windows) and add the following entry: `127.0.0.1 dehektorcommerce.com`. The real attackers would register `dehektorcommerce.com` domain instead.
4. Start `ssl_server.py` script (requires Python 3) to run a local SSL-protected web server. On Linux and macOS this script needs to be run with administrator privileges.
5. Open `https://dehektorcommerce.com/exploit_app_comm.html` in your browser and accept the invalid certificate (real attacker would actually own dehektorcommerce.com, so they would be able to get a valid certificate for it).
6. Enter the host name of your shop into the input field and click "Do it!" button.
7. A new browser tab opens and the admin interface of your shop loads, only to be immediately replaced by a login form. You can enter something into the login form and click "Log in" - the page will respond with the message "Gotcha".

The fake login page is being displayed by sending a `Shopify.API.Modal.open` message in the name of the Trust Badge app, this allows overlaying the admin interface with an arbitrary web page. I didn't spend any time faking this login page look similar to the real one, but that would be trivial. Unlike with phishing pages, checking the address bar doesn't help - the URL really belongs to the Shopify admin interface.

## Impact

This issue allows attacking admins of a specific, e.g. by abusing support channels to send them a malicious link. Social engineering could be used to convince admins to enter their credentials into fake login page - the URL of the page won't tip them off that this page has been manipulated.

Displaying overlays on top of the Shopify admin interface is something that any app can do by itself of course. So it might be a good idea to disallow removing all hints showing that the content displaying there doesn't belong to Shopify (the `hideHeader` parameter is particularly problematic here).

However, abusing special privileges granted to some apps might be even more problematic. For example, messages like `Shopify.API.Cart.discount.add` are restricted to apps that received the necessary privilege. I'm not sure how much harm these messages could do, but this vulnerability allows third-party websites to send them.

## Attachments
- exploit_app_comm.html
- ssl_server.py
