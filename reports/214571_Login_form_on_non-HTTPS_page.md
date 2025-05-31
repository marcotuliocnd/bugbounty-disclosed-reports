# Login form on non-HTTPS page

## Report Details
- **Report ID**: 214571
- **URL**: https://hackerone.com/reports/214571
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-18T22:57:53.641Z
- **Disclosed**: 2017-04-26T20:16:58.273Z

## Reporter
- **Username**: scraps
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Summary:
=======
A page on a microsite is not fully protected by an SSL certificate. This could allow an attacker in a Man-in-the-Middle position to obtain usernames and passwords of users visiting the site. 

Description:
=======
On the Red Dead Redemption subpage, the comments section on news articles allows registered social club users to post comments. When posting a comment, the user first has to login, which appears as if it is done over a non-secure page:

http://www.rockstargames.com/reddeadredemption/news/article/52645/rockstar-fan-art-gallery-gta-in-a-bottle-8-bit-bully-red.html/#comments

Note the warning in screenshot 1, firefox has identified that this page is not protected with an SSL certificate, therefore the username and password will be sent over a plaintext connection. In itself, this may be enough to put some users off using your page. 

Interestingly, if you manually change the address bar to be https, it does redirect to a https version of the same page, albeit with a mixed content error (screenshot 2). This indicates that an SSL certificate is in place for this page, however not all requests are sent through HTTPS by default. 

Once submit is pressed on the comment, it appears as though the request is sent over a HTTPS connection (when seen through Burp Suite or Wireshark), which suggests that the page does protect the username and password with SSL/TLS, see packets 167501-167519 in screenshot 3. Although this will work in most cases, there are techniques that can defeat this, such as using the [sslstrip][1] tool. There are several in-depth descriptions of how this works, such as this [one][2]

An example of using this is shown in screenshots 4 and  5 below, which was carried out solely on my own computer and against my own user account (scrapsH1).

[1]: https://moxie.org/software/sslstrip/ "sslstrip"
[2]: https://avicoder.me/2016/02/22/SSLstrip-for-newbies/ "one"

Steps to reproduce:
=============
1. On a Kali Linux machine, set up sslstrip as per screenshot 3
2. Set the browser settings to use the Kali machine as a proxy server. NB, this was done in this example for convenience. In a real-world attack, an attacker could force everyone on the network to use his machine as a proxy using a technique such as [ARP Spoofing][3], thereby requiring no interaction from the user
3. When the user submits a comment, rather than their POST request being protected by HTTPS, the attacking machine will negotiate the HTTPS connection with the rockstargames server, but trick the user machine into believing that the request should be sent as a HTTP request rather than HTTPS
4. As the request has been sent via HTTP, the POST request is now visible to sslstrip, which collects the credentials entered by the user, as per screenshot 5.

[3]: https://en.wikipedia.org/wiki/ARP_spoofing "ARP Spoofing"

Impact:
=====
If a user were to visit this page from a public or shared network (eg, starbucks, airport, library, etc) and submit a comment, a malicious user on the same network would be able to obtain that users username and password by conducting a Man-in-the-Middle attack using sslstrip and wireshark.

This would allow the malicious user complete access to the user's account. 

Remediation:
=========
1. If any part of a site is required to be protected by SSL, the entire site should be protected by SSL. Ts this would stop the attack outlined above from working, as a certificate error would be displayed to the user. 
2. HTTP Strict Transport [security][4] could be used to mitigate this attack, which would tell all browsers not to allow a HTTP connection to the rockstargames website

[4]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security "security"

## Attachments
- rockstar_screenshot1.png
- rockstar_screenshot2.png
- rockstar_screenshot3.png
- rockstar_screenshot5.png
- rockstar_screenshot4.png
