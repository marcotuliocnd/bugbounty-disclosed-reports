# Able to download any hosted content on AWS S3 bucket(stripo)

## Report Details
- **Report ID**: 739858
- **URL**: https://hackerone.com/reports/739858
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-11-18T16:32:42.288Z
- **Disclosed**: 2020-02-10T08:37:00.709Z

## Reporter
- **Username**: unchained_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
An AWS s3 bucket was found, with improper access controls, where all its contents could be downloaded.

Steps to reproduce:
1. List contents of the bucket with: ``aws s3 ls s3://stripo``
2. Download the hosted data with : ``aws s3 sync s3://stripo .``

## Impact

Any hosted data can be downloaded to an attackers personal storage.

## Attachments
- downloadable_data_from_bucket.png
