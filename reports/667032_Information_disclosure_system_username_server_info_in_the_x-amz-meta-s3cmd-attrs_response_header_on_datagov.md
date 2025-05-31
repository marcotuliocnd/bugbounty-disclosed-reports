# Information disclosure (system username, server info) in the x-amz-meta-s3cmd-attrs response header on data.gov

## Report Details
- **Report ID**: 667032
- **URL**: https://hackerone.com/reports/667032
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-04T09:41:20.270Z
- **Disclosed**: 2019-08-06T15:42:58.225Z

## Reporter
- **Username**: ninja_cyber007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hi Team,

I noticed, that the x-amz-meta-s3cmd-attrs  response header returns sensitive information, like system username on data.gov

x-amz-meta-s3cmd-attrs: uid:0/gname:root/uname:root/gid:0/mode:33184/mtime:1513269652/atime:1513269652/md5:2049644b6b833f5dbb826f60a4721f64/ctime:1513269652

Server: AmazonS3

Steps to reproduce:

1. POST  https://www.data.gov/app/plugins/advanced-custom-fields/core/api.php
2. Intercept the request in burp and see the response header values with system username information



Suggested fix
This issue lies in the s3cmd repository: https://github.com/s3tools/s3cmd/issues/67
where suggested fix is adding the -- no-preserve command.

## Impact

The attacker can gain sensitive information about system username. In this case it was root, so i marked impact as Low. Still, the developers can have a good reason to not expose this information in the response header.

## Attachments
- info_disclosure.PNG
