# Name can't be numbers or email

## Report Details
- **Report ID**: 263196
- **URL**: https://hackerone.com/reports/263196
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-08-25T11:09:41.728Z
- **Disclosed**: 2017-08-25T17:27:07.361Z

## Reporter
- **Username**: swag01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team, 
I observe a strange behaviour in your registration form. When we are making account and entering the first and last name. According to security concerns you should force user to write their first and last names which actually looks like name for example your should force users that the first and last name should be alphabets like "Husnain Iqbal" It cant be a number or email. 
I noticed that in other websites show error if you written a number or email in first name or last name. 
so the thing is you also should error when a user enter a number or email in first name and last name for security reasons.

Reproduce steps: 
1. Go to registration Form 
2. Fill first name with 101001010 or hi101@gmail.com and last name like 101011991 or hi102@gmail.com 
3. Then fill the other fields of the registration form . 
4. Then click register and the account will successfully made. 

Poc: 

For Proof of concept i am attaching some screen shots. you can look at it.

Recommendation: 

Account Name Cant be numbers or email for security purposes. If a user enters an email in his name by which he/she is getting registered so it is easy for hacker to compromise the account. 

## Attachments
- Untitled.png
- Untitled2.png
