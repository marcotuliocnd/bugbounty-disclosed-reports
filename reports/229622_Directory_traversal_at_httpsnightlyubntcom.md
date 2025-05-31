# Directory traversal at https://nightly.ubnt.com

## Report Details
- **Report ID**: 229622
- **URL**: https://hackerone.com/reports/229622
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-05-18T13:43:30.530Z
- **Disclosed**: 2017-10-10T06:11:49.525Z

## Reporter
- **Username**: grampae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
From within the http request function of the Acunetix and IronWasp programs I was able to view the passwd and hosts files at https://nightly.ubnt.com.  

Please see the attached screenshots for proof.

I have tried to reproduce from within firefox and internet explorer without much luck however if you need it I will try to come up with a work around.

For reference the response header is as follows:
HTTP/1.1 200 OK
Date: Thu, 18 May 2017 13:35:08 GMT
Content-Type: application/octet-stream
Content-Length: 1339
Connection: keep-alive
X-Powered-By: Express
Strict-Transport-Security: max-age=15552000; includeSubDomains
Last-Modified: Wed, 25 May 2016 20:30:37 GMT



## Attachments
- Screenshot_1.jpg
- Screenshot_2.jpg
- Screenshot_3.jpg
- Screenshot_4.jpg
