# Stored XSS on upload files leads to steal cookie

## Report Details
- **Report ID**: 765679
- **URL**: https://hackerone.com/reports/765679
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-29T07:39:05.231Z
- **Disclosed**: 2020-04-18T12:39:36.397Z

## Reporter
- **Username**: homaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: palo_alto_software

## Vulnerability Information
## Summary:
There isn't a check mechanism on file format in Inbox which an attacker can send an SVG file as other formats such as png, gif or bmp by rename and change file format leads XSS attack and steal victim cookies.

## Steps To Reproduce:
You should create 2 accounts :
First account for the attacker and second one for the victim.

The attacker in my scenario: seq@seq.teamoutpost.com
The victim in my scenario: seq1@seq1.teamoutpost.com

  1. Please log in to the first account via this [link] (https://app.outpost.co/sign-in) 
  1. From Inbox create New Conversation and attached following files (Attached on this report) and send 
       These files are an SVG file which changes file format to png, bmp, gif
       If you want to see payload open file by notepad. you'll see payload like the following code :

```
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="2560.000000pt" height="1600.000000pt" viewBox="0 0 2560.000000 1600.000000"
 preserveAspectRatio="xMidYMid meet" onload="alert(document.cookie)">
```
  1. Whenever victim clicks on each file, open a new tab and XSS attack occurs and steal the victim's cookie.

## Supporting Material/References:

Browsers :
Mozilla Firefox 71.0
Google Chrome 79.0.3945.88

  * [attachment / reference]

For clarification, you can watch POC file (Attached on this report)

If you have any questions, let me know.

Best regards.

## Impact

Attacker can send malicious files to victims and steals victim's cookie leads to account takeover.

## Attachments
- 20191229POC.mkv
- Payload.bmp
- Payload.gif
- Payload.png
