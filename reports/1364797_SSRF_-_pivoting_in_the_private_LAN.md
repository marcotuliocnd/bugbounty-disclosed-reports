# SSRF - pivoting in the private LAN

## Report Details
- **Report ID**: 1364797
- **URL**: https://hackerone.com/reports/1364797
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-10T08:28:56.840Z
- **Disclosed**: 2022-11-25T17:20:07.629Z

## Reporter
- **Username**: adrian_t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
The upload from remote servers features allows me to perform SSRF attack on the private LAN servers.

this features checks the following
* http response code needs to be 200 - easy, a non issue for attackers really
* checks the file exension   (can be bypassed with something like  http://192.168.1.148/index.php/test.png  - anything after index.php/  is ignorred and I control the file extension as well)
* some checks are performed on the IP, but any public and PRIVATE ips are allowed

I can read web  apps from the internal network, fingerprint them and exploit them (using GET only exploits).

This is how I've managed to read an phpinfo file from my local LAN:

http://192.168.1.157/info.php/test.html

The file is fetched, saved by the CMS locally (or S3) and then the output can be downloaded by the attacker as you can see in the attached screenshots.

ps: crayons

## Impact

An attacker can pivot in the private LAN and exploit local network apps.

## Attachments
- ssrf_file_dld.png
- ssrf_file_dld2.png
- ssrf_private_lan.png
