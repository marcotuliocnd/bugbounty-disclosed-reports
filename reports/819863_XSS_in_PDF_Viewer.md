# XSS in PDF Viewer

## Report Details
- **Report ID**: 819863
- **URL**: https://hackerone.com/reports/819863
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-16T02:01:22.673Z
- **Disclosed**: 2020-05-23T22:54:24.794Z

## Reporter
- **Username**: skewbed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
An outdated version of PDF.js in use allows for the CVE-2018-5158 vulnerability.

When the payload PDF is shown in the supplied PDF viewer, it can execute arbitrary JavaScript.

I have tested the payload PDF, and it is working in the Safari 13.0.5 (the latest version) and Firefox 74.0 (the latest version). Although, it does not work in the latest version of Chrome.

I could not find a way to test it on the desktop client. I assume that it would use the system PDF viewer.

Modifying the payload to fetch other code was luckily blocked because of a CORS policy.

The payload is from [https://bugzilla.mozilla.org/show_bug.cgi?id=1452075](https://bugzilla.mozilla.org/show_bug.cgi?id=1452075).
I have also included the PDF in the attachments.

The payload can be seen in action by checking the JavaScript console. It says "Hello, this is code running in" followed by the path to file where the vulnerability is.

## Impact

An attacker could execute arbitrary JavaScript code on a web browser when a PDF containing an exploit is opened.

## Attachments
- payload.pdf
