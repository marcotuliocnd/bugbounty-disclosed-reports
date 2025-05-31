# possibility to create account without username

## Report Details
- **Report ID**: 420583
- **URL**: https://hackerone.com/reports/420583
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-08T11:13:12.415Z
- **Disclosed**: 2018-10-09T11:42:12.226Z

## Reporter
- **Username**: luthrax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
hi , 
infogram.com doesn't allow us to go next untill we give name of our account but i bypassed that. i am able to create an account without any name, just by modify response field.

#steps:-
1. create new account , when you reach page where you have to give your name.
2. give name and intercept the request , remove first name and last name and forward the request.
3. now you will get reponse with 400 bad gateway , you just need to remove it and modify with 200 and forward it , your account will be created.

here is the video poc  how to create account without any name 
{F357158}

regards

## Impact

bypass "name giving to account field to complete signup"

## Attachments
- infogram.mp4
