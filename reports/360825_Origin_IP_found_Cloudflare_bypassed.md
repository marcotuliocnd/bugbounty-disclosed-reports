# Origin IP found, Cloudflare bypassed

## Report Details
- **Report ID**: 360825
- **URL**: https://hackerone.com/reports/360825
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-06-01T15:24:15.021Z
- **Disclosed**: 2018-06-02T12:54:49.236Z

## Reporter
- **Username**: europa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello team,
during the initial assessment of your assets I've come across what seems to be the unprotected origin server for **www.liberapay.com**.

### Description
The frontend currently resolves to `████` and `███`, both owned by Cloudflare, which act as your reverse proxy and WAF. By correlating your SSL Certificates to other hosts on the internet that serve the same content I was able to determine the current Origin Server as `██████████` and `██████`, both operated by Amazon's AWS services in the **EU-WEST-1** region.

By using these IP address as a resolver instead of the intended addresses I'm able to access the service without going through the WAF, thus I'm able to forward unfiltered payloads to the service, as well as avoiding the common protections offered by Cloudflare, also being able to perform crippling denial-of-services towards the origin.

### Suggestions
My recommendations fall in line with [Cloudflare's own guidelines](https://support.cloudflare.com/hc/en-us/articles/201897700-Step-4-Recommended-First-Steps-for-all-Cloudflare-users): the Origin server _must_ communicate exclusively with Cloudflare's IP address ranges, otherwise—as reported in [this post on Cloudflare's blog](https://blog.cloudflare.com/ddos-prevention-protecting-the-origin/), the protection offered by having a reverse proxy basically becomes useless.

## Impact

As reported in many other submissions, Cloudflare bypasses can have a significant impact, as any adversary is now able to communicate with the origin server directly, enabling them to perform unfiltered attacks (such as denial-of-service), and data retrieval.

## Attachments
No attachments
