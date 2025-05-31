# Some HTML Tags are Getting Executed in com.nextcloud.client

## Report Details
- **Report ID**: 631227
- **URL**: https://hackerone.com/reports/631227
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-06-28T05:16:33.282Z
- **Disclosed**: 2019-07-26T08:02:14.489Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
###What is the Vulnerability? 
HTML Tags such as <h1> , <small> , <href> and <img> are Getting Executed in Next Cloud Client Mobile Application for Android which can then Results to Code Injection.

###Reproduction Steps

1.) Using Next Cloud Client Mobile App on Android, Rename a Folder to ```<a href="google.com">test```
Our HTML tag Was Executed
{F518303}

2.)Rename the folder to ```small<h1>BIG```
Our HTML tag Was Executed
{F518304}

3.) Rename the Folder to ```normal<small>small<h1>BIG```
Our HTML tag Was Executed
{F518305}

## Impact

If successfully exploited, impact could cover loss of confidentiality, loss of integrity, loss of availability, and/or loss of accountability

## Attachments
- 28.png
- 29.png
- 30.png
