# Session not expired When logout [partners.uber.com]

## Report Details
- **Report ID**: 231041
- **URL**: https://hackerone.com/reports/231041
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-05-23T08:52:02.974Z
- **Disclosed**: 2017-05-26T22:56:44.653Z

## Reporter
- **Username**: hurthearts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi,

Summary
=========
partners.uber.com website is not expiring the user's session immediately after logout.

when user logout, the session not expired, and still can send request and the server respond response with OKAY

__Steps to Reproduce:__

- Log into the website - partners.uber.com
- Capture any request. For ex, profile edit page using burp proxy.
- Logout from the website.
- Replay the request captured in step 2 and notice it displays the proper response.

Thanks, 
tell me if you need video, i will create one !

## Attachments
No attachments
