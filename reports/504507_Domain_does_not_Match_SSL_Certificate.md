# Domain does not Match SSL Certificate

## Report Details
- **Report ID**: 504507
- **URL**: https://hackerone.com/reports/504507
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-03-03T16:43:58.910Z
- **Disclosed**: 2019-05-29T03:18:22.625Z

## Reporter
- **Username**: kittiesscript
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbandictionary

## Vulnerability Information
Hi Team,

While examining the domains that are in scope for Urban Dictionary, I noticed that https://urbandictionary.net is not currently protected by your SSL certificate. 


Steps to Reproduce:

1.  Open Chrome and copy/paste the following into the search bar:  https://www.urbandictionary.net    
2.  After you hit enter you will be transferred to a page that states:


Your connection is not private

Attackers might be trying to steal your information from www.urbandictionary.net (for example, passwords, messages, or credit cards). Learn more
NET::ERR_CERT_COMMON_NAME_INVALID


*Please note that you can also verify this error by visiting: https://www.whynopadlock.com/ and searching for: https://urbandictionary.net.  If you do, you will be informed that it is not currently one of your protected domains.


Recommended Solution:  Add https://urbandictionary.net to your SSL certificate.  


Hope this helps!

kittiesscript

## Impact

MITM Attacks - Information sent and received within https://urbandictionary.net is unprotected and it could potentially be stolen, read, or modified by attackers, hackers, and entities with access to internet infrastructure, such as Internet Service Providers (ISPs) and governments.

## Attachments
- Connection_Not_Private.png
