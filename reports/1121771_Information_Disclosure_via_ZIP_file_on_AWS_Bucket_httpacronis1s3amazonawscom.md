# Information Disclosure via ZIP file on AWS Bucket [http://acronis.1.s3.amazonaws.com]

## Report Details
- **Report ID**: 1121771
- **URL**: https://hackerone.com/reports/1121771
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-09T20:14:51.346Z
- **Disclosed**: 2022-02-08T09:08:38.182Z

## Reporter
- **Username**: h4x0r_dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary

Hello, @acronis Team I hope you all doing well.

during My recon, I found OPEN S3 BUCKET  http://acronis.1.s3.amazonaws.com and this BUCKET has an ZIP file .
and this file contains sensitive information about the internal system of Acronis.

This Zip file Is from  2018.  And it looks like it was in the development environment. but some employees uploaded this backup to OPEN S3 BUCKET.
and An attacker can download this file and read it .


## Steps To Reproduce

  1. go to http://acronis.1.s3.amazonaws.com/sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip and download The Zip file .

by Extracting this Zip file you can see the sensitive information about the internal system.

### POC 

{F1224411}

## Recommendations

delete `sysinfo_AcronisAppliance_2018-08-01_15-16-21.zip` file from this OPEN S3 BUCKET.

## Impact

Information Disclosure About internal system.
HTTP logs Disclosure.
leak Admin JWT token 
{F1224410}

## Attachments
- Screenshot_from_2021-03-09_21-12-56.png
- 2021-03-09_21-10-01.mp4
