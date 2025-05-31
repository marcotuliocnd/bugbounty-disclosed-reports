# S3 bucket listing/download

## Report Details
- **Report ID**: 1173598
- **URL**: https://hackerone.com/reports/1173598
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-24T06:27:03.698Z
- **Disclosed**: 2021-08-19T19:03:26.575Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
It's possible to get a listing and download every file in the S3 bucket `██████████` and ``███████`` . 

### Supporting Material/References

https://hackerone.com/reports/278191

## Impact

An attacker can download files that are not intended to be public, both buckets are very big. 
An attacker can increase dramatically the bandwidth used by the bucket, programmatically and continuously downloading the entire bucket content setting a more expensive bill. 

Example: 
The attacker has a 600 Mbps internet connection (let's use an average of 500 Mbps)  and here's the data transfer cost:
```
**Data Transfer OUT From Amazon S3 To Internet**

Up to 1 GB / Month $0.00 per GB
Next 9.999 TB / Month $0.09 per GB
Next 40 TB / Month $0.085 per GB
Next 100 TB / Month $0.07 per GB
Greater than 150 TB / Month $0.05 per GB
```
Let's assume you are in the 'Next 40 TB/Month' category, if an attacker downloads the entire bucket in one day, that would increase the bill in the following way
```
 (500/8) [MB/s]* 3600 [s]* 24 [hrs] =  5,273 GB per day
 - 5,273 [GB] * 0.085 [$/GB]= 448 [$]
 - Month -> $13.447
```

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
## Steps To Reproduce

We can find the name of the buckets going to███ and ██████████

We can list all files using the aws CLI:
`` aws s3 ls s3://███``

We can calculate the size of the bucket 
```
aws s3 ls --summarize --human-readable --recursive s3://██████ |grep "Total Size"
 Total Size: 1.6 TiB
```
More importantly we can download the entire bucket: 
``aws s3 cp s3://███████ . --recursive``

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
