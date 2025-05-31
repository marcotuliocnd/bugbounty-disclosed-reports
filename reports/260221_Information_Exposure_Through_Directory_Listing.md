# Information Exposure Through Directory Listing

## Report Details
- **Report ID**: 260221
- **URL**: https://hackerone.com/reports/260221
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-15T06:09:26.557Z
- **Disclosed**: 2018-05-17T09:04:38.697Z

## Reporter
- **Username**: mobius07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello.

I found open directories on the site https://apps.nextcloud.com, which can be viewed by any unauthorized user. There is an error at https://apps.nextcloud.com/static/. F212856
All directories and files in them, starting with `/static/` can be viewed or downloaded with all the content. Perhaps there is some kind of confidential information. 

Decision:
Disable directory browsing.  If this is required, make sure the listed files does not induce risks.

Thank you

## Attachments
- apps.nextcloud.com_static_.jpg
