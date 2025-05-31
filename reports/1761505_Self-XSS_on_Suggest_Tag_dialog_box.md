# Self-XSS on Suggest Tag dialog box

## Report Details
- **Report ID**: 1761505
- **URL**: https://hackerone.com/reports/1761505
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-03T18:18:35.051Z
- **Disclosed**: 2022-11-08T19:19:44.120Z

## Reporter
- **Username**: j3rry4unt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
## Summary:
Stored cross-site scripting  arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

vulnerable URL : https://www.xvideos.com/video57921571/friend_b._if_d.

Vulnerability Description : Application have a add tag functionality when i put java script like <script>alert(1)</script> after that stored XSS vulnerability arise.

Step to Reproduce : 
Step 1 : Go to following URL https://www.xvideos.com/video53284603/b.
Note : you don't need an account to do this
Step 2 : There is a add tag functionality insert the following information : <script>alert(1)</script>
Step 3 : Click the add button 
Step 4 : you will see a java script popup box showing your domain

Check the attached Video POC to see the actual XSS vulnerability

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user.
When the victim accesses the page containing the JavaScript payload, their browser will make a HTTP request to the attacker’s server

## Attachments
- Screenshot_(56).png
- XXS_xvideos.mp4
