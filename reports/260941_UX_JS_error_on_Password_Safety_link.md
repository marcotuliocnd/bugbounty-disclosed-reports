# UX: JS error on Password Safety link

## Report Details
- **Report ID**: 260941
- **URL**: https://hackerone.com/reports/260941
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-17T06:13:18.954Z
- **Disclosed**: 2017-09-17T23:36:28.951Z

## Reporter
- **Username**: maximus-decimus-meridius
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
**steps**
https://app.legalrobot.com/account

I just signed up to legal robot 
In my  account settings 
There is a div that contains 

Password Safety
To keep your information secure, Legal Robot periodically checks your password against public lists of hacked passwords (**here's how**). Since your account is fairly new, we have not run this check yet.


In that **here's how** is displayed in <a> tag without any href associated to it 
{F213603}


## Attachments
- Screenshot_from_2017-08-17_11-42-15.png
