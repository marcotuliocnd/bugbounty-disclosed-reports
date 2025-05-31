# Non-secure requests are not automatically upgraded to HTTPS

## Report Details
- **Report ID**: 158186
- **URL**: https://hackerone.com/reports/158186
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-10T14:56:50.794Z
- **Disclosed**: 2016-08-19T06:42:08.259Z

## Reporter
- **Username**: koenrh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Non-secure requests to `hackerone.com` (e.g. http://hackerone.com) are not automatically upgraded to HTTPS. This is not something you would notice when you use the latest version of modern web browsers such as Google Chrome or Firefox, because `hackerone.com` is [HSTS preloaded](https://hstspreload.appspot.com/). When a domain is preloaded, non-secure requests for these domains are internally upgraded to HTTPS. However, there are still browsers that either haven't implemented HSTS preload lists, or don't have `hackerone.com` on their HSTS preload lists (yet).

Take for example Safari on iOS, which doesn't have `hackerone.com` in its HSTS preload list. When you open http://hackerone.com in Safari and head over to the 'Sign in' page you will see that the connection is not upgraded to HTTPS. Moreover, if you enter your username and password, and hit 'Sign in', the form is sent in the clear over a non-secure connection.

Since non-secure requests aren't upgraded to HTTPS, the user will never receive instructions (via the `Strict-Transport-Security` header) to set the HSTS "cookie" for 'hackerone.com`. Which means a secure connection is not enforce until the first time the requests a resource over HTTPS, because that response will include the `Strict-Transport-Security` header.

## Steps to reproduce

### cURL

1. Send a `HEAD` request to `http://hackerone.com`: `curl -I http://hackerone.com`.
2. You will see that the server does not instruct the client to upgrade the connection to HTTPS. The server responds with a 200 OK status code instead of 301 status code with the response header `Location` set to `https://hackerone.com`.

### Firefox

1. Clear the `Site Preferences`: Click `History` --> `Clear Recent History...`, select `Everything`, tick`Site Preferences`, and hit `Clear Now`. This is to ensure Firefox forgets about an HSTS settings for `hackerone.com`.
2. Turn off the use of the HSTS preload list. Set `network.stricttransportsecurity.preloadlist`to `false` on the `about:config` page.
3. Open `http://hackerone.com`.
4. You will see that the non-secure connection is not upgraded to HTTPS.
5. Also note that when you click `Sign  in` in the top-right corner, enter your email address and password, and hit the green `Sign in` button that your credentials are sent in the clear to the non-secure endpoint http://hackerone.com/sessions.

## Exploitability and impact

Granted, it is kind of hard to exploit this vulnerability, because, first of all, it requires an attacker to be in a privileged network (he/she needs to be able to see what's going over the wire). Then the attacker would need to trick the victim into opening http://hackerone.com in a browser that doesn't have `hackerone.com` HSTS preloaded and which doesn't have any HSTS cookies for `hackerone.com` from a previous secure visit to `hackerone.com`. When all these conditions are met, an attacker could for example steal the victim's HackerOne credentials, or inject some malicious scripts into any page. This is possible because the connection is never upgraded, and the site allows forms such as the login form to be posted to a non-secure endpoint (see the screenshot attached to this report).

## Mitigation

Non-secure connections need to be upgraded to HTTPS as soon as possible using a permanent redirect. But since the website allowed me to send my username and password in the clear over a non-secure connection, I was also thinking that you would probably want to prevent forms from being posted to non-secure origins. One possibility is to enforce the client to only send AJAX requests to secure origins using the Content Security Policy `connect-src` directive.


## Attachments
- h1-http.png
