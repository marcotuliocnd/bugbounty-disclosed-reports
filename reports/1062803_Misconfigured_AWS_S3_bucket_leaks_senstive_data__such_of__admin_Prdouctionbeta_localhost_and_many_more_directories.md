# Misconfigured AWS S3 bucket leaks senstive data  such of  admin, Prdouction,beta, localhost and many more directories....

## Report Details
- **Report ID**: 1062803
- **URL**: https://hackerone.com/reports/1062803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-20T05:55:14.450Z
- **Disclosed**: 2021-03-24T20:51:48.159Z

## Reporter
- **Username**: i_am_no__one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
It has been observed that the amazon s3 bucket which i believe belongs to DoD as it contains data related to Dod prod,admin,localhost documents and all is misconfigured as a result any unauthenticated users can access it without any restrictions

## Step-by-step Reproduction Instructions

1.Access following URL
https://██████.s3.amazonaws.com/
so the bucket name is "█████████"
2.And we can see that we are successfully able to see all the contents present on it.Which confirms s3 bucket is misconfigured.
3.And to access contents of different directories we can use following cmd in terminal

aws s3 ls s3://███/
aws s3 ls s3://████/██████/
aws s3 ls s3://███████/███████████████/
aws s3 ls s3://██████████/███████/
aws s3 ls s3://██████████/████/

and in a similar way ,we can access content of root or any directory which contains sensitive manuals , document and media files 

## Suggested Mitigation/Remediation Actions
configure s3 bucket properly to disable listing of such a sensitive files

## Impact

Any unauthenticated user can access and download sensitive files present on DoD s3 storage.

## Attachments
No attachments
