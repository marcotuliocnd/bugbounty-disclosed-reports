# Web Cache poisoning attack leads to User information Disclosure and more

## Report Details
- **Report ID**: 631589
- **URL**: https://hackerone.com/reports/631589
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-28T18:46:28.485Z
- **Disclosed**: 2022-03-22T11:53:55.922Z

## Reporter
- **Username**: deksterh11
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lyst

## Vulnerability Information
Hello

Your Web-Server is vulnerable to web cache poisoning attacks.
This means, that the attacker are able to get another user Information.

If you are logged in and visit this website (For example):
https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css

Then the server will store the information in the cache, BUT with the logged in user information.
A non-logged-in user can then visit this website and see the information contained therein.

In that case, this url: https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css can be visited in Private Mode and still you will be shown as "LOGGED IN" and then check the Source code you will get your email, member id ,etc..


Some informations about the attack:
https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack.pdf

The screenshots with the steps are in the attachments.

## Impact

Web cache poisoning attack can be used to steal user informations like email, name and member id which is important for the login security feature.

## Attachments
- SourceCode_of_Attacker.png
- Normal_logged_in_user.png
- Attacker_logged_in_IncognitoMode.png
