# Subdomain takeover in help.tictail.com pointing to Zendesk (a Shopify acquisition)

## Report Details
- **Report ID**: 869605
- **URL**: https://hackerone.com/reports/869605
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-09T15:28:39.857Z
- **Disclosed**: 2020-08-24T16:17:30.687Z

## Reporter
- **Username**: meow-hacker-meow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

Description:
---------------------

The subdomain at https://help.tictail.com  has an unclaimed CNAME record ( tictail.zendesk.com ) . I checked the username availability in the signup process at zendesk, it was observed that the subdomain is vulnerable to a subdomain takeover which allows an attacker could exploit such a situation by registering the expired subdomain and setting up a phishing page that mimics the company’s main support website.

This vulnerability is called subdomain takeover. You can read more about it here:

https://blog.sweepatic.com/subdomain-takeover-principles/
https://hackerone.com/reports/32825
https://hackerone.com/reports/175070
https://hackerone.com/reports/172137

Steps to Reproduce & Proof of Concepts:
---------------------

1. Using dig and and username availability check at zendesk, I was able to determine that the subdomain https://help.tictail.com was vulnerable to takeover. 

Screenshots : 
F821713
F821710

2. I went to zendesk.com and registered for a free trial. When I was asked what name I want the zendesk domain to have, i chose the name (tictail.zendesk.com). and it was available for takeover. (showed green mark)

Screenshot : F821718

3.After registering, I went to Settings > Account > Host mapping. Filled in the domain the vulnerable subdomain. ( https://help.tictail.com  )

Screenshot : F821717

4.I did enable SSL (under security)  on the domain to stop the redirect when browsing to the target's domain.

Screenshot : F821716

5.I created a guide Help Center (not published )

Screenshot : F821712

6.Added a test article called “POC”. (Not published)

Screenshot :  F821714

Supporting Material/References:
---------------------

Video of the full takeover process : F821719


Mitigation and How to fix :
---------------------

Remove the DNS record from the DNS zone if it is no longer needed.
Claim the domain name in a permanent DNS record so it cannot be used elsewhere.

## Impact

Subdomain takeover is abused for several purposes:
---------------------


1- As mentioned above, an attacker could exploit such a situation by registering the expired domain and setting up a phishing page that mimics the company’s main support website. 

### Example scenarios : 

### Scenario 1 : 

 An attacker would create the same helpdesk page (design, texts etc… ) as in https://help.shopify.com/ 
Redirect users to custom urls (phishing pages) to collect login details : 
(eg; This page contains custom urls (store owner) to other parts of the helpdesk website, an attacker can create the exact same page and add  a custom url to lead shopify  users to phishing pages that mimics all the company’s pages that requires logins. 
https://help.shopify.com/en/manual/your-account/manage-account#update-your-billing-information

Screenshots :
 https://prntscr.com/sdqkpr

###Scenario 2 : 

More than that, since the brand name “Tictail”is famous and trusted, an attacker can use that and  register domain name “ticctail.com” (available),  and create the same exact home page as the original tictail.com homepage, and this time the button will lead to a phishing pages (logins, password reset etc…), and of course with the help of some advanced SEO techniques, the phishing page and subdomain could be found easily.

This is how I found the vulnerable subdomain in question, it was the first result. Imagine what people will find when they will search for “tictail” (If SEO is applied well)

Screenshot : F821715 

2- Share malicious files using the sharing files option in zendesk
       etc...

Here's a write up of the vulnerabilities : https://0xpatrik.com/subdomain-takeover/

Regards, 

Mohmaed Ali Moujehed

## Attachments
- CNAME.PNG
- NOW.PNG
- Before.PNG
- POC.PNG
- search_result.PNG
- SSL.PNG
- subdomain.PNG
- username.PNG
- Takeover_steps.mp4
