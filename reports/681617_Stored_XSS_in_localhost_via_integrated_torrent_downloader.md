# Stored XSS in localhost:* via integrated torrent downloader

## Report Details
- **Report ID**: 681617
- **URL**: https://hackerone.com/reports/681617
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-25T12:34:31.859Z
- **Disclosed**: 2019-09-24T20:30:52.095Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Due to filename of downloading torrent file isn't sanitized, an attacker is able to execute arbitrary JavaScript on localhost:* by abusing crafted torrent file.

## Products affected: 

 * Brave 0.68.131 Chromium: 76.0.3809.100 (Official Build)

## Steps To Reproduce:

 1. Open https://exec.ga/browser/brave/xss.torrent in Brave Browser.
 1. Click "Start Torrent" button
 1. Copy link address of "Save File" button.
 1. Paste it to URL bar with only hostname and port (e.g. http://localhost:8080).
 1. Alert will be popped up.

**Note**: Since it can be embedded with iframe (and it's possible to brute force port number), Steps after 2 won't be needed in real attack.

## Video PoC
{F565161}

## Impact

Attacker will be able to store arbitrary JavaScript on localhost:* with service worker, so if victim run any software on same port after attack, any information in the website that on same port can be stolen.

## Attachments
- PoC.torrent
- PoC.mp4
