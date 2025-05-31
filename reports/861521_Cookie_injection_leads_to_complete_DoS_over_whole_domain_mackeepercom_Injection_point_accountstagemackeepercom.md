# Cookie injection leads to complete DoS over whole domain *.mackeeper.com. Injection point accountstage.mackeeper.com/

## Report Details
- **Report ID**: 861521
- **URL**: https://hackerone.com/reports/861521
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-28T14:42:51.068Z
- **Disclosed**: 2020-10-21T09:21:06.712Z

## Reporter
- **Username**: mayurudiniya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: clario

## Vulnerability Information
## Summary:
 The cookie bomb works by setting large cookies that are way too big making the server decline any request send with them for having a too long request header.

##PoC
1.  Open below link and click on link
https://unequaledfloor.htmlpasta.com/

2.  Now open https://accountstage.mackeeper.com/ or https://.mackeeper.com/ , these domains won't open anymore.

## Impact

The escape function is used, which means a value consisting of special symbols will become three times longer. For example ,,, will turn into %2C. That means an attacker can create a valid link of proper length accepted both by the browser and the server, which however will make the cookie too long.

## Attachments
No attachments
