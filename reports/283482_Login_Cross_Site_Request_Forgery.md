# Login Cross Site Request Forgery 

## Report Details
- **Report ID**: 283482
- **URL**: https://hackerone.com/reports/283482
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-27T10:36:11.988Z
- **Disclosed**: 2017-10-27T11:34:22.851Z

## Reporter
- **Username**: bluedangerforyou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Login form is not protected against Cross Site Request Forgery.
An attacker can craft html page containing POST information to have victim sign into an attacker's account, where the victim can add information assuming he/she is logged into the correct account, where in reality, the victim is signed into the attacker's account where the changes are visible to the attacker.

The real issue here, is that when the victim runs the html Proof of Concept, the account is logged in to attacker's without any visible warnings, thus the victim is capable of theft of data and potentially vulnerable to account takeover.

Steps to reproduce
1. Create victim account
2. Create attacker account
3. Run attached Proof of Concept in same browser as victim and press submit (The POF can be modified to look like a fake blog post relating to infogram as someone searching a blog post is likely logged in and using the web application already)
4. On the victim browser, he/she is logged in as an attacker without any indication unless the page is manually refreshed.
5. Go to library and add a facebook post, or a chart.
6. On attacker browser, refresh page and navigate to library. You will see the victims added, or edited projects.


Mitigation

Please add a csrf token to login request or make some type prompt that the session has ended when the new login from attacker occurs.

I have attached a video proof of concept with audio of my voice explaining and instructing.
I have also attached the HTML proof of concept.

## Attachments
- infogramLOGINCSRF.mp4
- infogramLOGINCSRF_POC.html
