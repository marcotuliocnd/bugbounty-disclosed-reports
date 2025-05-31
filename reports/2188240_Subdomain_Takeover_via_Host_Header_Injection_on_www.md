# Subdomain Takeover via Host Header Injection on www.█████

## Report Details
- **Report ID**: 2188240
- **URL**: https://hackerone.com/reports/2188240
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-10-01T20:01:57.349Z
- **Disclosed**: 2024-06-18T16:57:53.269Z

## Reporter
- **Username**: ezequielpuig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Vulnerability Overview

**_Reported By_**: Ezequiel \[@ezequielpuig\]
**_Reported Date_**: 01/October/2023
**_Reported To_**: U.S. Department Of Defense
**_Vulnerability Type_**: Subdomain Takeover
**_Affected URL_**: www\.███████

Hello U.S. Department Of Defense Security Team, I hope this report finds you well. 

I want to bring to your attention a serious security issue that poses a significant risk to www\.████████. This is related to a subdomain takeover vulnerability, which could allow malicious individuals to gain control over the subdomain and potentially misuse it for malicious purposes.

_Overview:
The affected subdomain is www\.███, which currently points to an unclaimed CNAME record on the ████████.netlify.app. This situation allows anyone to potentially take ownership of the subdomain and manipulate its content. Since www\.█████████ has a CNAME record pointing to ██████████.netlify.app, by changing the Host header to www\.██████████, it is possible to visualize the malicious content hosted on █████████.netlify.app.

Here are a few scenarios where the Host header can be modified:

Proxy Servers: If you control a proxy server, you can intercept incoming requests and modify the Host header before forwarding the request to the intended destination. This is often done for load balancing, content caching, or security purposes.

DNS Spoofing: In a malicious context, an attacker might attempt DNS spoofing to redirect requests to a different server with a modified Host header.

Server-Side Scripting: If you have control over the server-side code that processes incoming requests, you can modify the Host header as part of your application logic.

Browser Extensions: Malicious browser extensions installed can modify the Host header for all outgoing requests.

_Proof of Concept (PoC):
This vulnerability materializes when an HTTP request is sent to www\.██████████ with a manipulated Host header.

PoC via curl:
`curl -skS https://www.███████ --header "Host: ███.netlify.app"`

PoC via Burp Suite:
█████████

_Impact:
Subdomain takeover can be exploited for various malicious purposes, including:

Malware distribution
Phishing / Spear phishing attacks
Cross-Site Scripting (XSS) attacks
Authentication bypass
And more.

_Mitigation:
To address this issue and prevent potential abuse, I recommend taking the following steps:

Remove the CNAME record from the DNS zone for www\.█████████.
Reclaim and register the affected subdomain (███.netlify.app) in the Netlify portal to prevent takeover by unauthorized entities.
I urge you to take swift action to remediate this vulnerability to safeguard the security and reputation of U.S. Department Of Defense.

//

Please feel free to reach out to me if you need any further information or assistance in resolving this matter.

Best regards,
Ezequiel Puig

HackerOne: https://hackerone.com/ezequielpuig
LinkedIn: https://linkedin.com/in/ezequielpuig
Mail: puigezequiel@gmail.com

## Impact

Impact detailed above.

## System Host(s)
www.██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Steps to reproduce detailed above.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
