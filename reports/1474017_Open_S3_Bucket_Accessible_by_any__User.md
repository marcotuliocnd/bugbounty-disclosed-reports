# Open S3 Bucket Accessible by any  User

## Report Details
- **Report ID**: 1474017
- **URL**: https://hackerone.com/reports/1474017
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-02-08T06:17:56.353Z
- **Disclosed**: 2022-04-13T07:12:58.436Z

## Reporter
- **Username**: ravansurya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
hi team,
here i found Open S3 Bucket Accessible by any  User

vulnerable URL:
https://cdn2.omise.co/

bucket name  : `omise-cdn-2`

I haven't tried this yet as it may delete the bucket. (it is possible)
an Attacker can delete the bucket using this command:-
$ aws s3 rb s3://<The_bucket_name>
and claim the bucket again to takeover the bucket 

https://cdn2.omise.co/. (S3 misconfiguration), that allow to any user listing/read/download all folders/files.



i think somthing misconfiguration is happaening here, u cant read the bucket using Aws Cli but u can read it via browser.
and also u can download the file using both Aws Cli and Browser.

████████

download:

██████

## Impact

Sensitive information Leakage.
an Attacker can delete the bucket .and claim the bucket again to takeover the buckaet

## Attachments
No attachments
