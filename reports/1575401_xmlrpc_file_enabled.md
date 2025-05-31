# xmlrpc file enabled

## Report Details
- **Report ID**: 1575401
- **URL**: https://hackerone.com/reports/1575401
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-19T09:29:41.390Z
- **Disclosed**: 2022-06-16T19:02:47.543Z

## Reporter
- **Username**: happykira0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:

Hello team,
I have found a security vulnerability in ** restaurants.yelp.com/xmlrpc.php** which lets attacker to:
1: XSPA or PortScan
2: Bruteforce
3:DOS and much more
## Platform(s) Affected:
  https://restaurants.yelp.com

## Steps To Reproduce:
1: Go to https://restaurants.yelp.com/xmlrpc.php to check if it is enabled or not. so the server altought respons with 403 error but the xmplrpc is enabled just the error because The following request requires permissions for some Boths.

## Supporting Material/References:
         Reference:
https://medium.com/@the.bilal.rizwan/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32
https://medium.com/@protector47/how-to-hack-wordpress-website-via-xmlrpc-php-61c813fa3740
https://hackerone.com/reports/325040?fbclid=IwAR0qgG-Xfzfi8epruslb_aB91f-Nj8DitF0su8O9ibFKSFdvefJ8h_qWNyc
https://hackerone.com/reports/752073?fbclid=IwAR2i3AM4woHlr01MvyJR-Vu485XQg_gxb1doWmAhSBTfxPK9cUSRFxO2iFo

## Impact

This method is also used for brute force attacks to stealing the admin credentials and other important credentials
This can be automated from multiple hosts and be used to cause a mass DDOS attack on the victim.

## Attachments
No attachments
