# Obtain the username & the uid of the one doing the S3 sync on Hackerone

## Report Details
- **Report ID**: 173175
- **URL**: https://hackerone.com/reports/173175
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-30T15:20:47.708Z
- **Disclosed**: 2016-10-03T20:15:57.922Z

## Reporter
- **Username**: rbcafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information

**Obtain the username & uid of hackerone.com S3**

using GET, it's possible to obtain the username & uid of the one doing the S3 sync on Hackerone.

***Doing a GET on :***

     http://hackerone.com

***Give the following header :***

     content-security-policy = default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src www.youtube-nocookie.com a4l.hackerone-ext-content.com a5s.hackerone-ext-content.com b5s.hackerone-ext-content.com; connect-src 'self'; font-src 'self'; form-action 'self'; frame-ancestors 'none'; frame-src www.youtube-nocookie.com a4l.hackerone-ext-content.com a5s.hackerone-ext-content.com b5s.hackerone-ext-content.com; img-src 'self' data: www.google-analytics.com article-photos.hackerone-user-content.com cover-photos.hackerone-user-content.com profile-photos.hackerone-user-content.com hackerone-attachments.s3.amazonaws.com; media-src 'self'; script-src 'self' www.google-analytics.com; style-src 'self' 'unsafe-inline'; report-uri https://hackerone.report-uri.io/r/default/csp/enforce

***Doing a GET on :*** 

     a4l.hackerone-ext-content.com
     a5s.hackerone-ext-content.com 

***Give the following header :***
 
     x-amz-meta-s3cmd-attrs = uid:501/gname:staff/uname:martijn/gid:20/mode:33188/mtime:1473665474/atime:1473665475/md5:3ca417860c0cdf7f11a2ff30589631bf/ctime:1473665474

     uname:martjin

***Doing a GET on : http://b5s.hackerone-ext-content.com***

***Give the following header :***

     x-amz-meta-s3cmd-attrs = md5:358568d44a80bb9668c940414f4d8a01

**Note** :

x-amz-meta-s3cmd-attrs header stores information related to the computer and the user while syncing the information. Adding the parameter "--no-preserve" avoids the storage of the username.


## Attachments
No attachments
