# Listing of Amazon S3 Bucket accessible to any amazon authenticated user (metrics.pscp.tv)

## Report Details
- **Report ID**: 278191
- **URL**: https://hackerone.com/reports/278191
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-17T12:58:16.375Z
- **Disclosed**: 2017-11-19T18:39:49.558Z

## Reporter
- **Username**: segumarc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
It's possible to get a listing of every files in the S3 bucket metrics.pscp.tv

**Description:** 
The problem is using the AWS command line, it's possible to get a listing of files in the Amazon S3 Bucket with an AWS authentication. See screenshot F230035. 

This user authentication is easy to get and it's free from Amazon. 

The good news is that the ACL on the files are set the way that's impossible at moment to create, remove or download any file from the bucket using my authentication.

A secure amazon S3 bucket would show Access Denied like the hackerone-attachements bucket in screenshot F230036

## Steps To Reproduce:
With the AWS command line installed and configured :
```
aws s3 ls s3://metrics.pscp.tv
```
## Impact: 
This give more information about your buckets to an attacker that are looking to attack you. 

Also, considering that it's possible to set the wrong ACL on a file that you may upload and may be confidential in the bucket, a secure bucket will remove the possibly to access it without a proper authentication. 




## Attachments
- Aws_ls_metrics.pscp.tv.PNG
- aws_ls_hackerone-attachements.PNG
