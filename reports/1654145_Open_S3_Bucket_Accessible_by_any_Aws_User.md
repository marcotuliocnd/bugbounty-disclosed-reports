# Open S3 Bucket Accessible by any Aws User

## Report Details
- **Report ID**: 1654145
- **URL**: https://hackerone.com/reports/1654145
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-07-29T17:16:32.936Z
- **Disclosed**: 2022-07-31T03:02:18.139Z

## Reporter
- **Username**: x_sh4dow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
Description:
It has been observed that the amazon s3 bucket which i believe belongs to GoCD as it contains data related to GoCD █████ documents and all is misconfigured as a result any unauthenticated users can access it without any restrictions
Step-by-step Reproduction Instructions
1.Access following URL
https://█████████.s3.amazonaws.com/ 
so the bucket name is "███"
2.And we can see that we are successfully able to see all the contents present on it.Which confirms s3 bucket is misconfigured.
3.And to access contents of different directories we can use following cmd in terminal
aws s3 ls s3://s3://███/binaries/
aws s3 ls s3://s3://█████/repodata/
aws s3 ls s3://s3://█████████/repoview/

and in a similar way ,we can access content of root or any directory which contains sensitive manuals , document and media files 
Suggested Mitigation/Remediation Actions : 
configure s3 bucket properly to disable listing of such a sensitive files

## Impact

Any unauthenticated user can access and download sensitive files present on GoCD s3 storage.

## Attachments
No attachments
