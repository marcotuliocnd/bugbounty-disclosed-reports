# help.nextcloud.com: Known DoS condition (null pointer deref) in Nginx running

## Report Details
- **Report ID**: 145409
- **URL**: https://hackerone.com/reports/145409
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T14:10:20.459Z
- **Disclosed**: 2016-07-27T20:51:19.652Z

## Reporter
- **Username**: shoveller
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The https://help.nextcloud.com sub-site is running Nginx/1.10.0 which is vuln to a known issue (CVE-2016-4450) which allows a remote malformed HTTP request to cause the Nginx process to crash.

DoS testing is mentioned as not requested, but if you know of an issue give it a go .. 

You can determine the version running by requesting the IP of the site and getting the HTTP 301, eg: https://88.198.160.135

https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-4450

## Attachments
No attachments
