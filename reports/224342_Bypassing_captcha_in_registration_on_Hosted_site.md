# Bypassing captcha in registration on Hosted site

## Report Details
- **Report ID**: 224342
- **URL**: https://hackerone.com/reports/224342
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-27T14:05:38.032Z
- **Disclosed**: 2017-07-03T05:56:15.863Z

## Reporter
- **Username**: pavanw3b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello again,

I believe the captcha on the user registration form is very simple and can be easily bypassed to automatically register any number of accounts.

A program can read the math captcha, solve it and submit the form with the answer and the other required parameters & headers.

**Note:** I read the out of scope guideline about "rate limiting". I guess that's about rate limiting password change or other places. Want to make sure this bug is not neglected.

### Risk
A bad guy can automate the form submission. This has a potential to degrade the server performance as each submission invokes multiple database transactions like checking username, inserting the form data into user table etc.

### Proof of concept
I'm attaching a small python script to this report, which can completely automates the registration form submission. When you run the script, it asks how many accounts you want to register. Once you enter, it creates that many users and also prints user details, captcha challenge with question and the link to access the public email inbox.

### How to run the POC
* Open a command or Terminal if on mac
* Enter `python <PATH>/wl-captcha-bypass.py`
* Enter a small number for `How many accounts do you want to create?`
* Note the response. Follow the guide to verify the confirmation email. You can also verify at the backend.

### Requirement to run the POC Python Script
* python 2.7+
* request
* beautifulsoup
*Please refer the internet to set up*

### Suggested Fix
* Configure a hard captcha. You can consider Google's reCAPTCHA.

Let me know if any questions.

## Attachments
- wl-captcha-bypass.py
- weblate-automated-registration.png
