# Redirecting users to malicious torrent-files/websites using WebTorrent

## Report Details
- **Report ID**: 968328
- **URL**: https://hackerone.com/reports/968328
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-27T08:23:54.417Z
- **Disclosed**: 2022-06-30T17:46:17.743Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

An attacker can redirect a user to a malicious torrent file/website using a reverse tab-nabbbing flaw in WebTorrent.


##Description

WebTorrent allows user to open files after download of while they are being downloaded directly from the browser

{F965466}

An attacker can use this to redirect users to malicious websites and torrent files as the anchor tag allowing to open up the file is not prone to reverse tabnabbing attacks.

{F965467}

##Tested on

* Brave Version 1.12.114 Chromium: 84.0.4147.135 (Windows)

## Steps To Reproduce:

 * Visit the POC link https://php-demo-app-shibli.cfapps.io/brave/poc-bave.php?x=.torrent
* Click on "Start Torrent"
* Once the file starts downloading, try opening up the file
* You will see the previous tab will navigate to a different torrent file or website.

Please refer below video poc for better understanding.

{F965473}

## Impact

* An attacker can trick a victim to download a malicious file instead of the original file.
* An attacker can redirect a user to a malicious webpage for other harmful attacks.

## Attachments
- ss1.PNG
- ss2.PNG
- bandicam_2020-08-27_13-51-10-941.mp4
