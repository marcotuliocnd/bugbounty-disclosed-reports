# Subdomain Takeover Via via Dangling NS records on Amazon Route 53 http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io

## Report Details
- **Report ID**: 746000
- **URL**: https://hackerone.com/reports/746000
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-25T15:47:06.080Z
- **Disclosed**: 2020-11-29T21:25:47.928Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Good day, I truly hope it treats you great on your side of the screen :)




I have found that your website http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io is pointed via Name Server records to AWS route 53.

These name server records have been deleted, I was able to create a matching zone file, and takeover full control of the domain, and all DNS records.

It is possible to create any subdomain, MX records, A, AAAA, txt, PTR any records to control the domain.

Please let me know any subdomain I can create if needed to show impact, I have used test.yourdomain to show the risk here.

I am able to make an email address at your domain and send and receive responses. This allows access to admin panels that are secured by needing an email address at your domain.takeover.
Google Docs, Slack Chats, anywhere the authentication needed is an email address at your domain is now accessible with this risk.

This also allows access to the postmaster account for the subdomain, which will allow me to whitelist SSL issuing aliases via email validation:

https://support.dnsimple.com/articles/ssl-certificates-email-validation/#requirements
https://www.digicert.com/ssl-support/validation/not-receiving-dcv-emails.htm


Please see my POC (Pug of Concept)
http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io

POC Video:
https://web.archive.org/web/20191125154616/http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/

Support for High Impact Rating: (7.5)

https://nvd.nist.gov/vuln/detail/CVE-2017-14389

Attack Vector (AV): Network
Attack Complexity (AC): Low
Privileges Required (PR): None
User Interaction (UI): None
Scope (S): Unchanged
Confidentiality (C): None
Integrity (I): High
Availability (A): None



Please verify your dns settings have been updated lag for domain propagation can take place.
https://dnschecker.org/#A/api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io

Options How to fix:

1) Remove the Name Server records that point to Name Servers you do not control.

2) Ask me to remove my registered Name Servers on AWS Route 53 and you can re register yours :)

May you be well on your side of the screen :)

-Eric

## Impact

Impact:

Cyber attackers can launch a phishing campaign leveraging your established (soon to be impacted) brand reputation.

The victim has no way of telling, whether the content is served by the domain owner or the cyber attacker.

Attackers can also chain higher severity attacks to this. Many applications expose session cookies to a wildcard domain (*.example.com),
so any subdomain can access them. An attacker can take a forgotten subdomain, trick the user to visit it, and extract cookies 
(even those with secure flag). This can be seen as an advanced version of XSS.

## Attachments
No attachments
