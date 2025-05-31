# Unrestricted file upload leads to Stored XSS

## Report Details
- **Report ID**: 880099
- **URL**: https://hackerone.com/reports/880099
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-21T22:44:05.566Z
- **Disclosed**: 2020-08-03T12:26:14.686Z

## Reporter
- **Username**: semsem123
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

i found that i can upload png file with JavaScript code and execute it in wiki page.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1-login to gitlab account
2-open  your project
3-open Wiki page.
4-Click "New page" button.
5-attach png file which contain below code
 `<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg onload="alert(1)" xmlns="http://www.w3.org/2000/svg">
<polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
</svg>`
6-Click "Create page" button.
7-Click on green triangle 
8-if The alert dialog not appears from first time just click on it one more time 



### Impact

If wiki pages created by using this vulnerability are visible to everyone (Wiki Visibility setting is set to "Everyone With Access") in "Public" project, there is a possibility that a considerable number of GitLab users and visitors click a malicious link.

### Examples
gitlab.com

tested on Google Chrome

https://gitlab.com/semsemhacker123/semsemtest/-/wikis/ssaa-home
https://gitlab.com/semsemhacker123/semsemtest/-/wikis/uploads/1308853a75502f77b3e22a2f9b0cc88a/1111111.png

### What is the current *bug* behavior?

The alert dialog appears after clicking "green triangle " in created page.

### What is the expected *correct* behavior?

the png file it must be not executed as  `image/svg+xml`

## Impact

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page

## Attachments
- 1111111.png
- gitlab_poc.png
