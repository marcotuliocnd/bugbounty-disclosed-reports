# [Screenhero] Subdomain takeover

## Report Details
- **Report ID**: 142096
- **URL**: https://hackerone.com/reports/142096
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-30T17:37:42.583Z
- **Disclosed**: 2017-01-21T17:25:56.100Z

## Reporter
- **Username**: yassineaboukir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi,

I found out some neglected DNS records that can be exploited to takedown the subdomain of Slack's acquisition `feedback.screenhero.com`

The security issue is that you have CNAME record that points `feedback.screenhero.com` to a `screenhero.uservoice.com`, but the problem is that the service is inactive, thus any malicious hacker would simply sign up for the service and claims the username `Screenhero` as his and no verification is done by the Service Provider, besides that the DNS-setup is already correctly set.

{F97017}

**Scenario attack :**
Attacker can now build a complete clone of the real site, add a login form, redirect the user, steal credentials (e.g. admin accounts), cookies and/or completely destroy business credibility for your company along with along with injecting malicious codes to steal their sensitive cookies, redirect them to malicious web pages etc.

**Mitigation :** To mitigate the threat you should remove CNAME DNS records for the services you don't use anymore.

**Reference:** http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/

Best regards.


## Attachments
- Capture_d_e_cran_2016-05-30_a__18.29.08.png
