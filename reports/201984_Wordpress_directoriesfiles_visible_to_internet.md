# Wordpress directories/files visible to internet

## Report Details
- **Report ID**: 201984
- **URL**: https://hackerone.com/reports/201984
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-29T19:08:17.181Z
- **Disclosed**: 2017-03-08T14:13:46.151Z

## Reporter
- **Username**: tk0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
#Issue
During my testing I noticed that ubnt website `https://directory.corp.ubnt.com` seems to leak some data into internet. Wordpress directory `https://directory.corp.ubnt.com/wp-content/uploads/` is showing files which I suppose shouldn't be visible to internet. 

I noticed that these files include UBNT-employee email addresses (including personal?), pictures etc.

#Reproduction
Just open URL https://directory.corp.ubnt.com/wp-content/uploads/ and start browsing folders/files.
Most "juicy" stuff can be seen in these folders: ██████████

BR,
-Tomi

## Attachments
No attachments
