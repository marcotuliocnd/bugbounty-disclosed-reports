# Open S3 Bucket Accessible by any Aws User

## Report Details
- **Report ID**: 819278
- **URL**: https://hackerone.com/reports/819278
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-14T16:00:00.651Z
- **Disclosed**: 2020-05-01T07:24:01.976Z

## Reporter
- **Username**: kartarkat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: greenhouse

## Vulnerability Information
hi team,

vulnerable URL: http://grnhse-marketing-site-assets.s3.amazonaws.com/

There is no authentication required to access the AWS bucket of the website.
As your site was associated with AWS, any AWS user can view the content , navigate through directories and download files, public access is allowed.

proof of concept: Please refer the screenshots attached.

[ note: I haven't modified any existing resources or harm any content ]

## Impact

Impact
1.      Sensitive information Leakage.
2.      Information disclosure about all the data in the cloud.

I haven't tried this yet as it may delete the bucket. (it is possible)
an Attacker can delete the bucket using this command:-
$ aws s3 rb s3://<The_bucket_name>
and claim the bucket again to takeover the bucket 

solution:
secure the login access

## Attachments
- vulnerable_data_size.png
- download_access.png
- list_directory.png
- bucket_source.png
- navigating_through_files.png
- open_bucket.png
