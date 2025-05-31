# AWS hosting bucket for Legal Robots set as public browse and list contents: s3://legalrobot

## Report Details
- **Report ID**: 166861
- **URL**: https://hackerone.com/reports/166861
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-08T14:58:52.466Z
- **Disclosed**: 2021-02-24T01:55:38.602Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Good day, 

I hope it treats you kindly :)

Legal Robot looks to use AWS hosting for your website.


Description of issue:
=====================

The Amazon Bucket (s3://legalrobot) has been configured to allow Public users access to browse all files on the server.

This is a risk as described as it allows known file paths, file name, and internal content to be indexed by Google and other search engines.

Description of risks:

https://www.owasp.org/index.php/File_System#Insecure_Indexing
http://cwe.mitre.org/data/definitions/548.html


Proof of RISK:
==============

Directory Listing of your server:

                           PRE email/
                           PRE video/
2015-12-29 05:39:20     536901 Dan-sq-gray.jpg
2015-12-29 05:39:21     546125 Dan-sq.jpg
2015-10-07 05:35:54     363060 Gizmo-Foldable.pdf
2016-02-26 20:37:45      22945 Megan.jpg
2015-12-08 09:58:52     420926 logo_huge.png
2015-12-08 09:59:04      14714 logo_text_huge.png

A Copy of all files on server:

https://www.dropbox.com/s/e9gpmonzvnwihff/legalrobot.zip?dl=0


What Search Engines Can and currently are Indexing:

A List of All files on the server:
http://legalrobot.s3.amazonaws.com/


A Sample File:
http://legalrobot.s3.amazonaws.com/logo_text_huge.png


Steps to reproduce:
===================

From the Amazon Command Line Interface:

aws s3 ls s3://legalrobot


(Steps to install the Amazon Command Line Interface: http://docs.aws.amazon.com/cli/latest/userguide/installing.html)



Steps to Fix:
=============

1. Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/.
2. In the Buckets list, click the bucket whose properties you want to view.
3. Click Permissions, and change to disallow Everyone / Authenticated Users from Listing Content.

(http://docs.aws.amazon.com/AmazonS3/latest/UG/EditingBucketPermissions.html)

Thanks for treating the security of your users as a priority, and wish you well on your side of the screen :)

-Eric

## Attachments
No attachments
