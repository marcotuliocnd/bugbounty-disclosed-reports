# A 10GB file is reachable

## Report Details
- **Report ID**: 416516
- **URL**: https://hackerone.com/reports/416516
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-09-30T15:22:21.964Z
- **Disclosed**: 2018-10-01T21:03:34.442Z

## Reporter
- **Username**: apt-mirror
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##

A file is 10GB is accessible on the following server: http://edge193.stream.highwebmedia.com:8080/.

## Steps To Reproduce:

  1. Open the following link: http://edge193.stream.highwebmedia.com:8080/download

## Additional notes:

I tried to download the file and analyze  it, but after 20 seconds the server interrupted the connection. However an attacker can download the whole file if he has 1Gb/s or faster internet connection.

To be honest I do not know exactly, what is this file because I was not able to download and analyze it. This require further investigation on the server.

## Impact

An attacker is able to download this file and also could be able to extract sensitive information from it.

## Attachments
- Screenshot_2018-09-30_16-58-51.png
