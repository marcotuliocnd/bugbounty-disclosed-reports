# Subdomain Takeover at Landing.udemy.com 

## Report Details
- **Report ID**: 208719
- **URL**: https://hackerone.com/reports/208719
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-24T21:02:45.710Z
- **Disclosed**: 2017-03-30T04:09:01.874Z

## Reporter
- **Username**: computer-engineer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
**Target:**  `Landing.udemy.com`

###Details: 

The target subdomain points to _unbounce.com_ service, via a _DNS CNAME_ record. As a result of this, an attacker could potentially initiate a subdomain takeover by registering the subdomain on unbounce.com.

Additionally, 

Unbounce is a custom 404-page hosting service, therefore leveraging its functionality an attacker can host custom HTML/Javascript webpage on the domain which will look very legitimate to the end-user and can be used to conduct large-scale phishing/XSS attacks.

###Proof of Concept:

CNAME Record:
>**Cname:**	unbouncepages.com
>**Name:**	landing.udemy.com
>**Type:**  CNAME
>**Class:**	IN
>**TTL:**	300

I did not proceed with the takeover, Contacting the support and confirming from them was more sensible.

{F163493}

###Remediation:

Remove the CNAME entry or claim the domain by signing up on unbounce.com

~Regards



## Attachments
- unbounce_support_domain_not_linked_chat.JPG
