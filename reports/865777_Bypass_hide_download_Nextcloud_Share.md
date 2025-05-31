# Bypass hide download Nextcloud Share

## Report Details
- **Report ID**: 865777
- **URL**: https://hackerone.com/reports/865777
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-04T14:12:42.165Z
- **Disclosed**: 2020-10-05T10:41:01.211Z

## Reporter
- **Username**: lawsoul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary
Hello everyone, accidentally browsing through nextcloud, I have found a small vulnerability on nextcloud server. This vulnerability allow download the file when the download function has been hidden
Here is the error details.
If anything is wrong please respond to me. Thanks you.
## Description
I sharing folder for another ( download not hide)
{F814529}
{F814531}
Of course, the download function is still enabled, I will have the download request as below
{F814536}
I then disabled download on the entire file folder  
{F814542}
{F814546}
But the download link created on the server does not change or change the permissions, I can completely download the file to continue
{F814548}
{F814549}
{F814552}

## Platform(s) Affected:
Nextcloud Server

## Impact

Sensitive documents after sharing that do not allow downloading will be reloaded even if disabled, for anyone

## Attachments
- Screenshot_2020-05-04_21-01-36.png
- Screenshot_2020-05-04_21-02-09.png
- Screenshot_2020-05-04_21-04-17.png
- Screenshot_2020-05-04_21-07-08.png
- Screenshot_2020-05-04_21-06-59.png
- Screenshot_2020-05-04_21-05-03.png
- Screenshot_2020-05-04_21-04-17.png
- Screenshot_2020-05-04_21-10-40.png
