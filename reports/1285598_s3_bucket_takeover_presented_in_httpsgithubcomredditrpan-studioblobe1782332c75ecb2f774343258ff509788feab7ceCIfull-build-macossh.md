# s3 bucket takeover presented in https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh

## Report Details
- **Report ID**: 1285598
- **URL**: https://hackerone.com/reports/1285598
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-31T17:51:58.825Z
- **Disclosed**: 2021-10-21T19:48:20.227Z

## Reporter
- **Username**: gaurav-bhatia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hey team,

## Summary:
 I have found that in the code of full-build-macos.sh in rpanstudio on github(https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/install-dependencies-osx.sh) contains a  s3 bucket which was unclaimed i.e (https://obs-nightly.s3-us-west-2.amazonaws.com)

## Steps To Reproduce:
1. Create a s3 bucket with name obs-nightly and us west 2 region
2. Upload files  with the name same as given in the code  (e.g. cef_binary_${1}_macosx64.tar.bz2)
3. Make the settings and change it as a static website 
4. You have successfully taken the s3 bucket and now when any user runs the code the url with s3 get executed and an attacker can spread dangerous malware.

## POC:

1. Link for the s3 bucket takenover :- https://obs-nightly.s3-us-west-2.amazonaws.com/index.html
{F1395337}

2. Github link that shows the s3 bucket :- https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/install-dependencies-osx.sh
{F1395340}
3. Github link that shows the s3 bucket :- https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh
{F1395338}

##Remediaton
You should remove the unclaimed s3 bucket as soon as possible from both the codes as it possess a critical risk

## Impact

An attacker can takeover the s3 bucket and can host his malicious content with the name (cef_binary_${1}_macosx64.tar.bz2) as presented in the code and can spread ransomware and many malicious files. This bug has a critical impact because the code of the tool that many people uses, contains unclaimed s3 bucket.

Regards,
Gaurav Bhatia

## Attachments
- reddits3poc1.JPG
- reddits3poc2.JPG
- reddits3poc3.JPG
