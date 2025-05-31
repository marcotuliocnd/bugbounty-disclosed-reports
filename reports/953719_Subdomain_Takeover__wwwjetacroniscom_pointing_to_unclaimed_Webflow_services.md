# Subdomain Takeover – www.jet.acronis.com pointing to unclaimed Webflow services

## Report Details
- **Report ID**: 953719
- **URL**: https://hackerone.com/reports/953719
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-08T01:17:27.108Z
- **Disclosed**: 2021-06-18T17:09:23.211Z

## Reporter
- **Username**: sumgr0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi Team,

Greetings!

I've come across another subdomain**www.jet.acronis.com** of **acronis.com** pointing to an unclaimed Webflow service. Visiting the www.jet.acronis.com returned the default 404 page for Webflow service, thereby making it potential for subdomain takeover.
F940499

Similar to the previous report #952166, on checking at Webflow Portal using a basic paid plan, the **www.jet.acronis.com** was discovered to be currently unclaimed/expired and hence allowing anyone to register the same. On completion of the setup process on Amazon using the same sub-domain name, the person shall have full control over the content of the sub-domain of **acronis.com**. The attacker may then host malicious content on the website or may redirect the visitor to another malicious website to spread a malware/virus.


### PoC

- Visit https://www.jet.acronis.com
- You'll come a page with a generic message
- Check sources for the PoC message

F940501


### Steps to Reproduce:

1. Create webflow account
2. Upgrade to basic paid option to enable custom domain setup
3. Create a site
4. Go to Project Settings > Hosting
5. Scroll down to custom domains section and add www.jet.acronis.com to setup


### See also

- https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/  
- https://0xpatrik.com/subdomain-takeover/
- https://medium.com/@ajdumanhug/subdomain-takeover-through-external-services-f0f7ee2b93bd  
- http://yassineaboukir.com/blog/neglected-dns-records-exploited-to-takeover-subdomains/  


### Additional note

I've claimed the resource to prevent a bad actor from doing so in the meantime.


### Mitigation

- Claim the custom domain in Webflow portal, after confirmation of releasing the same by myself


Best,
@sumgr0

## Impact

Sub-domain Takeover may lead to below consequences:

- Phishing / Spear Phishing
- Malware distribution
- XSS
- Authentication bypass and more
- Credential stealing

Sub-domain Takeover may also allow for SSL certificate be generated with ease, since few certificate authorities like Let's Encrypt requires only domain verification.

## Attachments
- 2020-08-08_www.jet.acronis.com_error.jpg
- 2020-08-08_www.jet.acronis.com_poc.jpg
