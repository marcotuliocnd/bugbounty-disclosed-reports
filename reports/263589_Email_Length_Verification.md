# Email Length Verification 

## Report Details
- **Report ID**: 263589
- **URL**: https://hackerone.com/reports/263589
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-26T12:36:33.068Z
- **Disclosed**: 2017-08-26T20:17:37.803Z

## Reporter
- **Username**: husnainiqbal01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team, 
Hope you are good. I found your website app.legalrobot.com vulnerable to this vulnerability.
Bug: Improper authentication - generic 
Description:
Dont know much about the websites that how they stored email address.Email addresses are stored as VARCHAR(128) But here your website legalrobot dont verify the length of an email address upon registration which allowed the attackers to bypass the allowed email-domains defined in auth.email-domains.

How to Exploit:
Exploiting this is much Easy
Get an email address of 128 characters long. StackOverflow answer indicates that the maximum length of an email address is 254 characters.Then register with your 128 character email address with @allowed-domain.com appended to it. The @allowed-domain.com part will be truncated because MySQL can’t store it, and you will receive a verification email on your 128 character email address.

It will be much easy if you are using gmail if we keep
ihusnain49@gmail.com, you will receive all mails sent to
ihusnain49+aaaaaaaaaaa…aaa@gmail.com.  

References: 
For reference watch this video : https://www.youtube.com/watch?v=o8-0hwaUB4I&feature=youtu.be and you will came to know about the vulnerability of your website. you can also see this report as a reference because this is the same vulnerability as this report is : https://hackerone.com/reports/2224 

I reccomended you two open both of the links. 

Reference 1:  https://www.youtube.com/watch?v=o8-0hwaUB4I&feature=youtu.be 

Reference 2 : https://hackerone.com/reports/2224 

Proof of concept:
I  register an account on legalrobot with this email ihusnain49+aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..aaa@gmail.com
and I received the mail on ihusnain49@gmail.com because the other part gets truncated. 

Screenshots for Proof of concept: 

Attaching some screen shots for proof of concept in which you can clearly see. 

Thanks 
Regards: 
Husnain Iqbal



## Attachments
- Emaillengthtest2.png
- Emaillengthtest.png
- truncatedd.png
