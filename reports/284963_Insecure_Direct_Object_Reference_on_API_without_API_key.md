# Insecure Direct Object Reference on API without API key

## Report Details
- **Report ID**: 284963
- **URL**: https://hackerone.com/reports/284963
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-31T22:04:56.909Z
- **Disclosed**: 2018-03-13T14:20:39.170Z

## Reporter
- **Username**: scraps
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
It is possible to query the semrush API without specifying an API key. This allows anyone to query the API and retrieve information without having paid for a subscription. 

This is not a security vulnerability as such, but I believe it does undermine your business model in that a user does not have to pay for access to your API.

**Description:** 
Through google dorking, I discovered that there are two results in google for  subdomains of api.semrush.com (see F234928). 

By clicking either of the links, I realised that it is possible to change the domain parameter and get the information for that domain. This is all without specifying a valid API key. According to https://www.semrush.com/api-analytics/, a valid API key should be required to do these types of queries. 

I tried to further look at this by adding in other fields as per the API guide, and could submit any query I wished, such as: http://uk.api.semrush.com/?action=report&type=domain_rank&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=semrush.com (see F234936)

I noticed that this doesn't work against api.semrush.com, only uk.api.semrush.com or us.api.semrush.com. It also works against fr.semrush.com, ie, anytime a subdomain of api.semrush.com is specified:

http://us.api.semrush.com/?action=report&type=domain_rank&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=semrush.com&database=us
http://uk.api.semrush.com/?action=report&type=domain_rank&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=semrush.com&database=us
http://fr.api.semrush.com/?action=report&type=domain_rank&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=semrush.com&database=us

The above all work, but the following doesn't and specifies an error message saying: "ERROR 120 :: WRONG KEY - ID PAIR" (see F234935).

http://api.semrush.com/?action=report&type=domain_rank&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=semrush.com&database=us

This proves that it is only subdomains of api.semrush.com which have this problem.

**Browsers Verified In:**
  * Firefox 56.0.2

**Steps To Reproduce:** 
  1. Use the google dork site:*.api.semrush.com 
  2. Notice the two results that are returned 
  3. Clicking either result gives access to the result for that page and search result
  4. Experiment with other URLs, such as: 
http://us.api.semrush.com/?action=report&type=domain_rank&domain=hackerone.com
http://us.api.semrush.com/?action=report&type=domain_rank&domain=semrush.com
  5. Notice that results are returned in every case - there doesn't appear to be anything stopping a user from making as many queries as they want, or even scripting this. 

**Impact:**
If this is the vulnerability I think it is, it effectively allows anyone to query the semrush database without having to pay for it, which would completely undermine your business model. Again, not a security risk as such, but would be a commercial risk. 

**Remediation:**
 * On the API processing, ensure that a valid API key must be present for results to be returned (taken from https://www.semrush.com/api-analytics/)
 * Ensure that those two results are removed from google by using google webmaster tools to request their removal
 * Do not allow search engines to index the *.api.semrush.com domain. This can be achieved with a robots.txt file


## Attachments
- semrush_google.png
- semrush_google2.png
- semrush_google3.png
