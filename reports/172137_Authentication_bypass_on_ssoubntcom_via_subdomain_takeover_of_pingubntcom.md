# Authentication bypass on sso.ubnt.com via subdomain takeover of ping.ubnt.com

## Report Details
- **Report ID**: 172137
- **URL**: https://hackerone.com/reports/172137
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-09-26T15:18:13.317Z
- **Disclosed**: 2016-11-29T08:39:46.444Z

## Reporter
- **Username**: arneswinnen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
# Summary
This is not a standard vulnerability, but a chain of two more exotic vulnerabilities leading to a full authentication bypass of your SSO login system at sso.ubnt.com (via account.ubnt.com). The root cause of this authentication bypass is two-fold:

1. Subdomain ping.ubnt.com was pointing to Amazon Cloudfront CDN, but the hostname was not registered there anymore. This allowed me to fully takeover this domain. It is now serving content of my own webserver, both over http and https.
2. The session cookie of your SSO subdomain sso.ubnt.com is (deliberately?) shared with all https://*.ubnt.com subdomains through its "domain=.ubnt.com" attribute. This allows leakage of this high-value session cookie to the overtaken subdomain https://ping.ubnt.com in all modern browsers.

# Impact

The following attack scenario was invented: Assume that a victim is logged in in his/her browser to any of the `*.ubnt.com` services via the SSO system at account.ubnt.com, which uses sso.ubnt.com under the hood. If an attacker can then let the victim make a request to ping.ubnt.com in a second browser tab, either on purpose or unknowingly, the browser will transparently add the session cookie "UBIC_AUTH" set by sso.ubnt.com to this subdomain. Since the attacker has full visibility into incoming requests to his/her webserver (in this case, mine), the session cookie is now compromised. Once the attacker's got his/her hands on the session cookie, he/she can now hijack the victim's session on sso.ubnt.com. Since sso.ubnt.com is the centralized place where authentication occurs for all `*.ubnt.com` services (and perhaps even on other domains via OAuth?), this is a major risk, as an attacker can now impersonate the victim on **all** their Ubiquity services and connected devices who rely on SSO for authentication. 

In order for this depicted attack to work, the following questions still remain:
- Valid SSL Certificate: the "UBIC_AUTH" session cookie has the "secure" cookie attribute set, which instructs the browser to only send its value over a secured channel. This means that the browser will only send it to https://ping.ubnt.com but not to http://ping.ubnt.com, which now requires the attacker to have a valid SSL certificate for this domain. However, many Certificate Authorities support automated domain verification through hosting a specific HTML file in the root directory of a (sub)domain nowadays (e.g. [Lets Encrypt](https://letsencrypt.org/how-it-works/), [GoDaddy]( https://be.godaddy.com/help/verify-domain-ownership-html-or-dns-7452 ), ...). Since the subdomain takeover yields the attacker complete control over the webserver serving ping.ubnt.com, this would be trivial. This was not performed as a PoC to not upset you by generating a malicious SSL certificate for your domain and effectively deploying it on a production system, but feel free to give me a heads up if you would like me to actually proceed with this attack scenario. It is literally [one command with the certbot utility](https://certbot.eff.org/#ubuntutrusty-apache) and [free to deploy on AWS Cloudfront](https://aws.amazon.com/cloudfront/custom-ssl-domains/). 
- Request to ping.ubnt.com: In order for the attacker to convince his/her authenticated victim to make a request to the overtaken subdomain ping.ubnt.com, a number of techniques can be utilized:
 * Targeted attack: An attacker could simply send his/her victim a mail with an embedded 1x1 image hosted on https://ping.ubnt.com/ inside its HTML. Since email supports HTML by default, this would silently make a request to the overtaken subdomain when being rendered in the victim's browser. Another option would be to lure the victim to an arbitrary attacker-controlled domain which houses a hidden iframe to the overtaken subdomain. Again, the browser would stealthily make the request and leak the "UBIC_AUTH" session cookie of sso.ubnt.com to the attacker.
 * Mass exploitation: An attacker could again host a media resource on https://ping.ubnt.com/ and buy some advertisement space on popular websites to serve it. Every authenticated Ubiquity victim who browses here would leak his/her session cookie to the attacker unknowingly. However, to increase the likelihood that the victims are already authenticated to sso.ubnt.com, an attacker might just post a reply on https://community.ubnt.com with a hidden IMG tag and source https://ping.ubnt.com. Every logged-in reader of the reply would unknowingly make a request to the hijacked subdomain, which would go through IF there was a valid SSL Certificate installed (not currently). Here's the PoC link: https://community.ubnt.com/t5/Getting-Started-Product/2-week-old-wisp/m-p/1687239#M65439 (post of my testuser "ferrariverdasco" - see also attached screenshot "1. Waterhole community reply.png"). 

# 1. Subdomain takeover
The subdomain "ping.ubnt.com" was (and still is) a CNAME pointing to a AWS Cloudfront CDN server (depending on your location, the latter will resolve differently):
```
# nslookup ping.ubnt.com 8.8.8.8
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
ping.ubnt.com	canonical name = dl.ubnt.com.
dl.ubnt.com	canonical name = d2cnv2pop2xy4v.cloudfront.net.
Name:	d2cnv2pop2xy4v.cloudfront.net
Address: 54.192.96.244
```
However, the hostname "ping.ubnt.com" was not claimed anymore on Cloudfront, resulting in a Cloudfront error page when visiting the subdomain before the takeover (see screenshot "2. Before takeover.png"). Subsequently, a new Amazon Cloudfront CDN endpoint was created and linked to an attacker-controlled origin server. For the new Cloudfront CDN endpoint, "ping.ubnt.com" was designated as hostname successfully ("3. CNAME takeover.png"). This concluded the subdomain takeover (see screenshots "4. After takeover.png" and "5. After takeover - source.png"). PoC URL: http://ping.ubnt.com/34902385023958329058235.html (random filename chosen to not negatively affect Ubiquity's reputation during takeover period). 

# 2. Authentication bypass proof-of-concept
In the PoC below, the assumption is made that https://ping.ubnt.com is actually serving a valid certificate in the victim's browser, which currently is not the case (so there is currently no actual risk) - see above.

1. Open browser & navigate to https://ping.ubnt.com. Accept the invalid SSL certificate for PoC reasons.  Then launch an intercepting proxy tool and configure your browser proxy settings to see traffic going back & forth.
2. Browse to https://community.ubnt.com/t5/Getting-Started-Product/2-week-old-wisp/m-p/1687239#M65439. Find the request to https://ping.ubnt.com/imagefetch.php?f=thanks.png in the intercepting proxy and view its response (hidden in HTML comments). It should say "Cookie named 'UBIC_AUTH' is not set!".
2. Login to account.ubnt.com in a second browser tab with the victim's account. Notice the "UBIC_AUTH" cookie being issued by sso.ubnt.com after successful authentication, with "domain=.ubnt.com" attribute.
3. Refresh first tab https://community.ubnt.com/t5/Getting-Started-Product/2-week-old-wisp/m-p/1687239#M65439. Check in your intercepting proxy that a new request to https://ping.ubnt.com/imagefetch.php?f=thanks.png is made, with a bunch of cookies transparently added by the browser, among which UBIC_AUTH.
4. The HTML comment body of the response should now show the value of the UBIC_AUTH value, clearly demonstrating that the session cookie's value was well-received. However, this PHP page will make a request to endpoint https://sso.ubnt.com/api/sso/v1/user/self with this cookie and show its response. This should be a JSON array containing victim-account sensitive information, hereby proving that the session cookie can actually be hijacked and used from another system (my webserver in this case). 

In a real attack scenario, an attacker would probably want to store the received cookie locally and use a cookie addon for his/her specific browser, to inject the session cookie value in the browser more persistently, as opposed to in a webserver's PHP curl script. However, I believe this method was more clear for PoC purposes. From here on, an attacker has complete control over a victim's account. He/she can see and modify anything, as long as no extra verification is required (e.g. current password to update to a new password). This is a similar impact of a global XSS & CSRF vulnerability on all *.ubnt.com pages.

You can see all these PoC steps executed in attachment "6. Authentication Bypass PoC video.mp4". The code of the https://ping.ubnt.com/imagefetch.php page is also attached ("7. imagefetch.php"). 

# Recommendation
The root cause of the vulnerability is the dangling CNAME pointer to Cloudfront from the affected subdomain. It is advised to remove the DNS CNAME pointer from ping.ubnt.com to the Cloudfront CDN server. This will mitigate the root cause vulnerability. If you are interested in keeping the subdomain on the Cloudfront CDN, I'll have to release it first before you can reclaim it. In that case, just let me know.

Additionally, it is advised to investigate whether the session cookie "UBIC_AUTH" of sso.ubnt.com should really be shared among all subdomains. This makes subdomain takeovers significantly more impactful, as shown through this report. 

# References
- https://labs.detectify.com/tag/hostile-subdomain-takeover/

I know this is a very long and complex report for a non-standard issue. Please don't hesitate to contact me if I haven't explained something clearly enough, so I can elaborate. 

Regards,

Arne Swinnen
https://www.arneswinnen.net

## Attachments
- 5._After_takeover_-_source.png
- 4._After_takeover.png
- 3._CNAME_takeover.png
- 2._Before_takeover.png
- 1._Waterhole_community_reply.png
- 7._imagefetch.php
- 6._Authentication_Bypass_PoC_video.mp4
