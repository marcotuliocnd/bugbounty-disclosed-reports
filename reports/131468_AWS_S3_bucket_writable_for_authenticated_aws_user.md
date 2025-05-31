# AWS S3 bucket writable for authenticated aws user

## Report Details
- **Report ID**: 131468
- **URL**: https://hackerone.com/reports/131468
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-17T03:20:50.710Z
- **Disclosed**: 2017-01-05T01:34:01.511Z

## Reporter
- **Username**: dpgribkov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
Hey,

I found an open S3 Amazon bucket udemy-maven. While I can’t confirm if you own it or not, it appears that it is publicly writable using the aws cli.

When I write to udemy-maven, I get:
move: ./test.txt to s3://udemy-maven/test.txt

And also when I remove file, I get:
delete: s3://udemy-maven/test.txt

Assuming you own it, the security issue is that someone could delete files or write something malicious into the bucket and someone on your team unknowingly opening it.

## Attachments
No attachments
