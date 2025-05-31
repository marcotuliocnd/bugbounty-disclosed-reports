# Access to Private Photos of Apps in App section(IDOR)

## Report Details
- **Report ID**: 318751
- **URL**: https://hackerone.com/reports/318751
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-22T20:01:57.103Z
- **Disclosed**: 2018-03-05T19:34:35.107Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
##Bug location :
 https://[MyShop].myshopify.com/admin/apps

##Description : 
Previewing the Photo In App section Request is vulnerable to IDOR attack where changing the ID leads to Disclose Link of Private photos. Also It discloses the Shop Domain details also. The request goes through exchange.shopify.com. 

##Vulnerable Request : 
GET /listings/hackeronevg1110/shop_screenshots/85952 HTTP/1.1
Host: exchange.shopify.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [Cookies]
Connection: close
Upgrade-Insecure-Requests: 1


Let me know if you need more info.

Regards,
Vijay Kumar

## Impact

Information disclosure.

## Attachments
No attachments
