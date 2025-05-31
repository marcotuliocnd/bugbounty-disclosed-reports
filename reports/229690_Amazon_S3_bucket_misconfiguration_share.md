# Amazon S3 bucket misconfiguration (share)

## Report Details
- **Report ID**: 229690
- **URL**: https://hackerone.com/reports/229690
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-18T17:46:35.997Z
- **Disclosed**: 2017-05-18T17:57:47.078Z

## Reporter
- **Username**: glc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information

Hi,


## Description

I have discovered one of your Amazon S3 bucket and tested it via the AWS command line tool on Linux. It looks like permissions are not well configured and allow dangerous actions to everyone.

The vulnerable bucket is:
`zomato-share`


## PoC:

`aws s3 ls s3://zomato-share`
`aws s3 cp test s3://zomato-share`
`aws s3 rm s3://zomato-share/test`

See the attached screenshots.

{F185826}


## Risk:

- Company impersonation, serve datas using your name
- Illegal file hosting (like movies, mp3 or whatever...)
- Files can be deleted
- Files can be overwritten by shitty content (like porn)
- Files can be infected by malicious content in an attempt to infect users or staff

Since the bucket doesn't host any critical files, the impact is very low but still something you have to fix for the reasons previously mentionned.


## Remediation:

Check all buckets owned by your company and the ACL to forbid dangerous actions to unauthorized users.


## Additional note:

Since there is no way to check the owner of a bucket, it's possible that those buckets don't belong to you. In that case, I strongly apologize for the disturbance.



Best regards,



## Attachments
- 20170518-bucket-share2.png
- 20170518-bucket-share1.png
