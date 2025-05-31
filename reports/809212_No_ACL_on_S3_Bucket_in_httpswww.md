# No ACL on S3 Bucket in [https://www.██████████/]

## Report Details
- **Report ID**: 809212
- **URL**: https://hackerone.com/reports/809212
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-03T03:51:49.031Z
- **Disclosed**: 2020-05-14T17:56:32.379Z

## Reporter
- **Username**: 0xsnowmn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Hi team!,
* i was able to move and download all file in s3 bucket that's under ████ control cuz it didn't has ACL

## Step-by-step Reproduction Instructions
*  first we will try to access all files via browser by go to this `s3.amazonaws.com/files.████████`

## Now We Will try to download all files on the s3 bucket via aws cli:
1.  type this in ur terminal `aws s3 sync s3://files.█████████/ . --no-sign-request --region ██████`
1.  u will see that all files and folders starts to download!

## Now We will try to move a file into s3 bucket
1. i created a file and called the file `yghonem14.html`
1. now we will type this in terminal `aws s3 mv yghonem14.html s3://files.██████/  --no-sign-request --region ███████`

### PoC
* For more Proof i uploaded a file and u can access it by this url `https://s3.amazonaws.com/files.███/yghonem14.html` ████████

## Impact

* Attacker will be able to delete or move or access any file on the s3 bucket, Thanks!.

## Attachments
No attachments
