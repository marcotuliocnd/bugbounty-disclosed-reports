# Stored XSS in Public Profile Reviews

## Report Details
- **Report ID**: 1398285
- **URL**: https://hackerone.com/reports/1398285
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-11-11T13:59:07.118Z
- **Disclosed**: 2023-02-01T03:30:06.150Z

## Reporter
- **Username**: vj1naruto
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Summary:
Stored XSS found in public profile review in which we can add product details in shop addition options. In description of shop product we can add data URI XSS in HTML format which is led to XSS once user click on HTML.
In data URI XSS payload is encrypted in base64

Steps To Reproduce:
  1. Login with registered username and go to profile.
  2. After that click on add recommendation and add product details and in it's description add below payload:
<a href="data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click Here</a>
{ Data URI XSS: data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=
(PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=) : <script>alert('XSS')</script> }
  3. Now save the form by filling rest columns.
  4. If any one views public profile and click on HTML tag, it will trigger XSS.

Proof Of Concept:
Video POC attached

## Impact

Attacker can execute XSS in the victim user using judge platform

## Attachments
No attachments
