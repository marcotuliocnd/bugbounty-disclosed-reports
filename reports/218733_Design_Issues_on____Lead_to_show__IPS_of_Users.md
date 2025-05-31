# Design Issues on ( ███ ) Lead to show ( IPS of Users ) 

## Report Details
- **Report ID**: 218733
- **URL**: https://hackerone.com/reports/218733
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-05T12:09:41.240Z
- **Disclosed**: 2017-04-05T12:41:43.408Z

## Reporter
- **Username**: m7mdharoun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello , 
 I know this Domain is maybe out of scope But it Connected to the main Website
 I have see it Cashable the Download IPS for Users Status.
As I saw that You active statics ( awstats ) That show me Full access to Status on the website .

                       ** POC **
https://███████/cgi-bin/awstats.pl?month=all&year=2017&config=██████&framename=mainright&output=unknownip

https://████████/cgi-bin/awstats.pl?output=alldomains&config=/../../../../../../../../../../proc/version&framename=index


███	18	27	100.26 MB	14 Feb 2017 - 23:55
█████████	18	26	208.19 MB	27 Mar 2017 - 10:26
█████████	18	19	644.44 MB	22 Feb 2017 - 10:36
████████	18	22	815.18 MB	21 Mar 2017 - 13:20
███████	18	27	99.94 MB	23 Mar 2017 - 13:06
█████████	18	36	306.92 MB	01 Mar 2017 - 18:28
███	18	77	1.05 GB	23 Mar 2017 - 09:27
█████	18	30	720.85 KB	01 Feb 2017 - 00:46
█████████	18	24	87.02 MB	22 Mar 2017 - 09:56


     
             ** Fix for Awstats  **

Restrict (or password protect) the access to directory or make it accessible only on the local interface.


## Attachments
No attachments
