# Unclaimed official s3 bucket of tendermint(tendermint-packages) which is used by many other blockchain companies in their code

## Report Details
- **Report ID**: 1397826
- **URL**: https://hackerone.com/reports/1397826
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-10T20:38:07.423Z
- **Disclosed**: 2023-02-15T19:58:26.972Z

## Reporter
- **Username**: gaurav-bhatia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cosmos

## Vulnerability Information
## Summary:
I have found an official unclaimed s3 bucket of tendermint i.e. http://tendermint-packages.s3-website-us-west-1.amazonaws.com/ which is also used by many other blockchain companies and developers .

## Steps To Reproduce:

1. Create a s3 bucket with name tendermint-packages and us west1 region
2. Make the settings and change it as a static website
3. You have successfully taken the s3 bucket .

## POC
1. Link of s3 bucket which shows i have claimed the bucket: http://tendermint-packages.s3-website-us-west-1.amazonaws.com/

{F1510071}

2. Pic of github which shows the companies that is using the unclaimed s3 bucket of tendermint:

{F1510070}

##Remedition

Check your internal code if there is any usage of unclaimed s3 bucket and claim the unclaimed s3 bucket(let me know when i should unclaim it from my side)

## Impact

An attacker can host its contents and malicious files on the official bucket of tendermint which can cause harm to the companies or developers using your bucket for package installation and etc. This bug has a severe impact if  it is used internally by tendermint and other companies.

Regards,
Gaurav Bhatia

## Attachments
- tendermintpoc2.png
- tendermintpoc1.png
