# Subdomain takeover on rider.uber.com due to non-existent distribution on Cloudfront

## Report Details
- **Report ID**: 175070
- **URL**: https://hackerone.com/reports/175070
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-11T05:28:13.120Z
- **Disclosed**: 2016-12-12T23:48:13.024Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi,

3 hours ago, rider.uber.com was responding like this:
{F127137}

This happened on both HTTP and HTTPS. Now, as our blog post from last week says:
https://labs.detectify.com/2016/10/05/the-story-of-ev-ssl-aws-and-trailing-dot-domains/

This means that there's a high chance this domain does not have any distribution at all, and that anyone can now claim it.

I've done this as a PoC now, I haven't placed anything on the apex level, howevel if you use this URL:
http://rider.uber.com/login-poc

There's a PoC there:
{F127139}

You should immediately remove the DNS RR, or point it elsewhere, or tell me and I'll remove the Alternate CNAME again on my PoC-distribution.

Regards,
Frans


## Attachments
- Screen_Shot_2016-10-11_at_07.20.44.png
- Screen_Shot_2016-10-11_at_07.27.19.png
- Screen_Shot_2016-10-11_at_07.27.47.png
