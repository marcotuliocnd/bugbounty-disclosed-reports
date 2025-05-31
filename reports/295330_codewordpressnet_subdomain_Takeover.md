# code.wordpress.net subdomain Takeover

## Report Details
- **Report ID**: 295330
- **URL**: https://hackerone.com/reports/295330
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-05T10:44:48.749Z
- **Disclosed**: 2018-03-11T20:53:27.428Z

## Reporter
- **Username**: sniperpex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hy Wordpress sec i found as it is posible to takeover this domain http://code.wordpress.net when you navigate it you will get this error msg:

Warning! Domain mapping upgrade for this domain not found. Please log in and go to the Domains Upgrades page of your blog to use this domain. 

$ host code.wordpress.net
code.wordpress.net is an alias for wpprojects.wordpress.com.
wpprojects.wordpress.com is an alias for lb.wordpress.com.
lb.wordpress.com has address 192.0.78.13
lb.wordpress.com has address 192.0.78.12

## Impact

The attacker can takeover this subdomain

## Attachments
No attachments
