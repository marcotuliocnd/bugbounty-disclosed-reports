# Open S3 Bucket | information leakage

## Report Details
- **Report ID**: 1186897
- **URL**: https://hackerone.com/reports/1186897
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-06T16:58:21.826Z
- **Disclosed**: 2021-05-15T19:58:36.066Z

## Reporter
- **Username**: b29z
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hi

I found  an Open S3 Bucket.

- POC :

 aws s3 ls s3://amazon-eks/

Source : `https://github.com/Sifchain/sifnode/blob/bebbe9883560bbde4f452f81a2d85bdbc243636a/deploy/rake/dependencies.rake#21`

regards
oos

## Impact

information leakage

## Attachments
No attachments
