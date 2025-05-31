# Stored XSS Using Media

## Report Details
- **Report ID**: 275386
- **URL**: https://hackerone.com/reports/275386
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-07T20:24:21.652Z
- **Disclosed**: 2017-11-26T20:42:04.020Z

## Reporter
- **Username**: dyoon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi,

Summary:
This exploits an XSS vulnerability on polldaddy.com

Steps to Reproduce:
1. Create a multiple-choice question quiz on Polldaddy
2. Insert stored XSS payload into Media Embed such that it matches the shortcode format
   Payload: [<img src="http://url.to.file.which/not.exist" onerror=alert("Hello!");>]
3. When someone goes on the quiz page through the quiz share link, the payload will execute. 

Proof of Concept (30-second video):
https://drive.google.com/file/d/0B_lsH7QMy9DkQnV5a3hHa05lSmM/view

## Attachments
No attachments
