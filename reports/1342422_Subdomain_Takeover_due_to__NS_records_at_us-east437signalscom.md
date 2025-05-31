# Subdomain Takeover due to ████████ NS records at us-east4.37signals.com

## Report Details
- **Report ID**: 1342422
- **URL**: https://hackerone.com/reports/1342422
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-17T10:50:58.899Z
- **Disclosed**: 2021-09-17T21:45:28.908Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
## Description
 
 Hi!
 I have discovered that  us-east4.37signals.com was pointing to an unclaimed ████ NS zone and I've managed to claim it in my account.
 
 ##POC
 
 http://nagli.us-east4.37signals.com/takeover.html
 

{F1451587}


 ## Remediation
 Make sure to configure the DNS records under us-east4.37signals.com
 
Best regards,
@ nagli

## Impact

Subdomain takeovers can be used for
 Account takeovers (cookies set to .█████████ will be shared with this subdomain and can be obtained)
 Stored XSS (arbitrary javascript code can be executed in a users browser)
 Phishing
 Hosting malicious content

Since you cannot control the content hosted on the site, your brand is at risk of being damaged.
Additionally, the vulnerabilities in these sites, such as XSS, RCE, etc could put your sites/users at risk of attack, since they would occur on your domain.

## Attachments
- Screen_Shot_2021-09-17_at_13.49.59.png
