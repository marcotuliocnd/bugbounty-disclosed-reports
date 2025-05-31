# CORS Misconfiguration

## Report Details
- **Report ID**: 1530581
- **URL**: https://hackerone.com/reports/1530581
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-04T19:36:18.950Z
- **Disclosed**: 2022-04-20T20:15:31.333Z

## Reporter
- **Username**: shirshak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Vulnerable Url: www.█████████
Summary: Cross-origin resource sharing (CORS) is a browser mechanism that enables controlled access to resources located outside of a given domain. However, it also provides a potential for cross-domain-based attacks, if a website's CORS policy is poorly configured and implemented. CORS can be exploited to trust any arbitrary domain attacker-controlled domain name and send the data to it.  Attackers can make an exploit and ask the domain to send data of the victim to the attacker domain.
Severity:  High  

As you can see when we run the above request in Burp Suite.

Access-Control-Allow-Origin: evil.com
Access-Control-Allow-Credentials: true

Complexity: Easy 

From : Remote / External


## References
https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny
https://www.geekboy.ninja/blog/exploiting-misconfigured-cors-cross-origin-resource-sharing/
https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

## Impact

An Adversary can carry out a CORS attack to exfiltrate the sensitive details of a victim.

## System Host(s)
www.████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Enter the domain name https://www.██████████ and add /wp-json after the url.
2. Intercept the request and add Origin header, type evil.com in it and send the request.
3. Use the exploit code given in the text file and save it as filename.html.

## Suggested Mitigation/Remediation Actions
All the REST Apis should be authenticated and the domain should not trust any other domains. Allow only selected, trusted domains in the Access-Control-Allow-Origin header.



## Attachments
No attachments
