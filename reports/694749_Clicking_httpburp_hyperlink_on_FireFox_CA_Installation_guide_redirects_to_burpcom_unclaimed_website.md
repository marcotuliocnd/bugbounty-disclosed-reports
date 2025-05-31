# Clicking "http://burp" hyperlink on FireFox CA Installation guide redirects to "burp.com" (unclaimed website).

## Report Details
- **Report ID**: 694749
- **URL**: https://hackerone.com/reports/694749
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-14T05:54:32.668Z
- **Disclosed**: 2019-09-16T17:17:50.114Z

## Reporter
- **Username**: intelcorgi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Executive Summary
---------------------------------------------------
 I was in the process of installing Burp suite community edition on my recent machine where I believe I stumbled across a potential open redirect issue [on the CA certificate installation website](https://support.portswigger.net/customer/portal/articles/1783087-Installing_Installing%20CA%20Certificate%20-%20FF.html). This is a security concern due to the fact that if a user clicks the hyperlink without Burp Suite / proxy settings configured, they could be redirected to a phishing site and have sensitive data stolen. 
 
 It would be incredibly easy for a malicious actor to claim the domain redirected to by the hyperlink on the webpage. While "burp.com" is not a Portswigger subdomain or owned by Portswigger, it could be confusing to a user, especially if a phishing site used burp.com and the malicious actor mocked it up to look like the Portswigger website.

*Note: While for most redirection / sub domain takeover bugs the standard practice is to actually go out and register the unclaimed website / domain, I have chosen not to in this PoC because I think it is a much lower level security issue.* 


Links where security issue can be found
---------------------------------------------------
- [FireFox CA Installation Instructions](https://support.portswigger.net/customer/portal/articles/1783087-Installing_Installing%20CA%20Certificate%20-%20FF.html)

- [IE CA Installation Instructions](https://support.portswigger.net/customer/portal/articles/1783080-Installing_Installing%20CA%20Certificate%20-%20IE.html)

- [Safari Installation Instructions](https://support.portswigger.net/customer/portal/articles/1783096-Installing_Installing%20CA%20Certificate%20-%20Safari.html)


Test Conditions
---------------------------------------------------
-**Browser**: Firefox 69.0 (64-bit). No proxy activated and certificate not installed.

-**OS**: Windows 10

-**Burp Product**: Burp Suite Community Edition v2.1.02 (turned on, no settings changed).


Execution
---------------------------------------------------
1. I was following the instructions found [on the CA certificate installation website](https://support.portswigger.net/customer/portal/articles/1783087-Installing_Installing%20CA%20Certificate%20-%20FF.html) to install the CA for FireFox as a part of setting up Burp on my PC. 

2. I turned on Burp as instructed by the directions, and tried navigating to the page to download the certificate authority by clicking the hyperlink to http://burp as seen in this screenshot{F582570}. 

3. Upon clicking the hyperlink FireFox will either immediately direct you to "burp.com"(Which then sends you to inert.com, the seller of the domains), shown in this screenshot {F5825782}. "Burp.com" can be shown for sale in {F582571}. Sometimes, FireFox will throw an error on the redirect, but refreshing will eventually lead you to "burp.com => inert.com"

4. inert.com shows how easy it would be for a malicious attacker to register "burp.com". Any user then clicking on the "http://burp" hyperlink will be directed to malicious "burp.com".


Suggested Remediation
---------------------------------------------------
- Register "burp.com" domain, have it lead nowhere / black hole.
- Remove hyperlink HTML elements to avoid having a user accidentally click on it and cause the redirect.
- Add explicit instructions to turn on proxy settings on top of Burp simply being on.

## Impact

Open redirect vulnerabilities can be used as a tool to potentially phish user data. If a malicious actor claims the unclaimed URL which is embedded , a user could be redirected to the new website thinking it was registered by Portswigger and may input credentials, payment information, or other sensitive data. It could also be used to serve malicious payloads to the user.

## Attachments
- Page_w_Redirect.JPG
- Burp_for_sale.JPG
- Redirect_Destination.JPG
