# Login form on non-HTTPS page on http://stream.highwebmedia.com/auth/login/

## Report Details
- **Report ID**: 386735
- **URL**: https://hackerone.com/reports/386735
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-25T17:19:17.962Z
- **Disclosed**: 2018-09-20T04:08:39.695Z

## Reporter
- **Username**: gujjuboy10x00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Dear Team,

##Summary##
A page on a http://stream.highwebmedia.com/auth/login/ is not fully protected by an SSL certificate. This could allow an attacker in a Man-in-the-Middle position to obtain usernames and passwords of users visiting the site.

Note the warning in screenshot 1, firefox has identified that this page is not protected with an SSL certificate, therefore the username and password will be sent over a plaintext connection. In itself, this may be enough to put some users off using your page.
Once submit is pressed on the login, it appears as though the request is sent over a HTTPS connection (when seen through Burp Suite or Wireshark), which suggests that the page does protect the username and password with SSL/TLS, 

## Steps To Reproduce:
  1. go to http://stream.highwebmedia.com/auth/login and setup wireshark 
  2. you can get username , password is in clear text

##Mitigation
If any part of a site is required to be protected by SSL, the entire site should be protected by SSL. Ts this would stop the attack outlined above from working, as a certificate error would be displayed to the user.
HTTP Strict Transport security could be used to mitigate this attack, which would tell all browsers not to allow a HTTP connection to this website.

## Supporting Material/References:
Please find attachement

## Impact

If a user were to visit this page from a public or shared network (eg, starbucks, airport, library, etc) and submit a comment, a malicious user on the same network would be able to obtain that users username and password by conducting a Man-in-the-Middle attack using sslstrip and wireshark.

This would allow the malicious user complete access to the user's account.

## Attachments
- login_clear.PNG
