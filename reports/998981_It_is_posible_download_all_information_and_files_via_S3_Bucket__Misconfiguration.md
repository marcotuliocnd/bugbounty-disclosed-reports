# {███} It is posible download all information and files via S3 Bucket  Misconfiguration

## Report Details
- **Report ID**: 998981
- **URL**: https://hackerone.com/reports/998981
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-06T01:28:42.758Z
- **Disclosed**: 2020-11-23T18:09:17.787Z

## Reporter
- **Username**: z3ck3bug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Hi team!
 I´ve found a misconfiguration S3 Bucket:
Name Bucket = ██████████

I found this vulnerability after digging deep into the js files:

████████ 

**Description:**

Apparently wanting to enter the docs folder is impossible, since it is protected or disabled so that anyone can access the information.

███████ 

As you can see, the information is hosted on a S3 Bucket server:

█████

But if it is possible to access and download all the information contained in the Bucket through AWS Cli:

█████████

## Step-by-step Reproduction Instructions

In summary, I was able to perform the following actions:

1. It is possible to completely download the S3 Bucket:

aws s3 sync s3://███████ .

████

2. It is possible to list and view all files:

aws s3 ls s3://████/

████

3. It is possible to Check bucket disk size:

aws s3 ls s3://████ --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'

████████

These actions could be carried out due to a misconfiguration of the Bucket.


## Product, Version, and Configuration (If applicable)
N/A

## Suggested Mitigation/Remediation Actions

Check and change your Bucket´s Policy.

## Impact

Improper Access Control via S3 Bucket  misconfiguration, allow obtain and download all data of the Bucket.

## Attachments
No attachments
