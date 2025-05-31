# Rate Limit Bypass on login Page

## Report Details
- **Report ID**: 224460
- **URL**: https://hackerone.com/reports/224460
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-27T19:04:24.907Z
- **Disclosed**: 2017-05-17T15:24:09.203Z

## Reporter
- **Username**: atruba
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

Your web authentication endpoint, https://demo.weblate.org/accounts/login/ (POST), currently protects against credentials brute-force attacks only by requests rate-limiting based on IP. It was found that if an attacker sends login requests faster than every 4 seconds from the same IP address, it would get blocked.  No additional protection mechanism such as Captcha (pre-auth) or account lockout requiring additional email/phone verification (pre- or post-auth) were identified at any time. 

Additionally, rate-limitation nowadays is not effective anymore to protect against brute-force. There are many botnets out there which can be used to overcome this hurdle, as well as cloud (VPS) services (e.g. Amazon AWS EIPs, DigitalOcean, ...), VPNs, proxies.

Many VPS providers today offer a whole /64 subnet range of IPv6 addresses (18.446.744.073.709.551.616 unique addresses), such as but not limited to:

RamNode: $15/year (https://www.ramnode.com/vps.php)
Hetzner: $3.9/month (https://www.hetzner.de/us/hosting/produktmatrix_vserver/vserver-produktmatrix)
Vultr: $5/month (https://www.vultr.com/pricing/)


One example of a similar vulnerability that was exploited by Black Hats in the past would be Apple's Celebgate scandal of January 2015, where celebrity passwords were brute-forced through an unprotected Apple authentication endpoint. In the case of Weblate, this could lead to the compromise of many accounts

Recommendation:Implement Captcha which will based on Email or username after a number of request tried to login from one email or username. Captcha should not based on IP.

So make brute force attack on login page and change IP on every 4 request.

Thanks,

## Attachments
No attachments
