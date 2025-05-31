# Blind SSRF External Interaction on ████████

## Report Details
- **Report ID**: 1220688
- **URL**: https://hackerone.com/reports/1220688
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-08T19:36:59.765Z
- **Disclosed**: 2022-08-21T08:40:51.584Z

## Reporter
- **Username**: error201
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hii Security Team,

I am S █████(Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and found Blind SSRF External Interaction on ██████████

What is SSRF?
Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's choosing.
In typical SSRF examples, the attacker might cause the server to make a connection back to itself, or to other web-based services within the organization's infrastructure, or to external third-party systems.
SSRF attacks often exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorized actions. These trust relationships might exist in relation to the server itself, or in relation to other back-end systems within the same organization.

Steps to reproduce:-

1.Navigate to the website █████
2.Now you can see at bottom on the right there is chat box or messanger box.
3.Click on it and paste the Burp Collaborator URL { Example : In this scenario the URL belike ██████ } and click on send
4.Now we will get HTTP and DNS interaction in Burp Collab and In HTTP requesting it is fetching the file ( test.png ) it means it is vulnerable to Blind SSRF

References:- Similar report which is reported by another researcher ███████

## Impact

Impact:--
This Vulnerability can lead to Attack Surface Analysis is about mapping out what parts of a system need to be reviewed and tested for security vulnerabilities.
The attacker can fetch malicious files which can infect the server
This will allow attackers to gain access to an internal IP of a website along with other sensitive information that may be leaked with the request

POC Attached Below :-

## Attachments
No attachments
