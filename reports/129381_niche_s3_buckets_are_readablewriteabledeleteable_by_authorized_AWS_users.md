# niche s3 buckets are readable/writeable/deleteable by authorized AWS users

## Report Details
- **Report ID**: 129381
- **URL**: https://hackerone.com/reports/129381
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-08T23:08:55.724Z
- **Disclosed**: 2017-04-02T14:48:02.066Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi All,
I've discovered that the AWS buckets by niche, niche-s3-production,  is accessible for authorized AWS users using the AWS command line tools.

##Issue
As such, I have confirmed:
- I can list all files in the bucket with the command ``` aws s3 ls s3://niche-s3-production```
- I can copy files from the server with the command ``` aws s3 cp s3://niche-s3-production/[PATH]/[FILE] ./```
- I can copy to the server with ```aws s3 cp test.txt s3://niche-s3-production```
- I can remove files with ``` aws s3 rm s3://niche-s3-production/[PATH]/[FILE]```

You will see that I have left the empty file test.txt in the bucket root.

This also impacts the niche-s3-development and niche-s3-staging buckets.

##Vulnerability
- Authorized AWS users can access any content in the publics (I only tested downloading one file from the compaign_posts path because files can have their own permissions)
- People can host and serve viruses from your buckets
- Twitter staff may unknowingly download a virus from what they think is a trusted bucket when they think files may have been placed in specific locations by other coworkers

##Remediation
Remediation is to review, audit and update all buckets owned by niche and the access control lists so this is not available to authorized users, only via the web through an authorized account controlled by the site.

Pete

## Attachments
No attachments
