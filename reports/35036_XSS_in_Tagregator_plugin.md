# XSS in Tagregator plugin

## Report Details
- **Report ID**: 35036
- **URL**: https://hackerone.com/reports/35036
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-11-09T01:08:39.052Z
- **Disclosed**: 2016-08-18T01:19:00.020Z

## Reporter
- **Username**: dia2diab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
This is a XSS in Tagregator plugin that affect on wordpress users
i'm making my test on alwaysdata host
target: http://diaa.alwaysdata.net/wordpress/wp-admin/post-new.php?post_type=tggr-flickr
infected input: post_title
payload: <script>alert("a7a");</script>
then get the Permalink that is generated for public user: http://diaa.alwaysdata.net/wordpress/?tggr-tweets=alerta7a
alerted !!!
 
tell me if you wanna any information
thank you 



## Attachments
No attachments
