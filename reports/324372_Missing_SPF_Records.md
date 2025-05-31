# Missing SPF Records.

## Report Details
- **Report ID**: 324372
- **URL**: https://hackerone.com/reports/324372
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-11T09:47:22.078Z
- **Disclosed**: 2018-05-24T01:29:41.411Z

## Reporter
- **Username**: pradyumna1998
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mycrypto

## Vulnerability Information
What Is SPF/TXT Records?

An SPF record is a type of Domain Name Service (DNS) record that identifies which mail servers are permitted to send email on behalf of your domain. The purpose of an SPF record is to prevent spammers from sending messages with forged From addresses at your domain.
Checking Missing SPF:-
 There Are Various Ways of Checking Missing SPF Records on a website But the Most Common and Popular way is kitterman.com

Steps to Check SPF Records on a website:-
Go to http://www.kitterman.com/spf/validate.html

Enter Target Website Ex: target.com (Do Not Add https/http or www)
Hit Check SPF (IF ANY)

If You seem any SPF Record than Domain is Not Vulnerable But if you see Nothing Here then "HURRAY! You Found a Bug"
 
Attack Scenario & PoC:-
Once There is No SPF Records.An Attacker Can Spoof Email Via any Fake Mailer Like Emkei.cz.An Attacker Can Send Email From name "Support" and Email: "support@target.com" With Social Engineering Attack He Can TakeOver User Account Let Victim Knows the Phishing Attack but When He See The Email from the Authorized Domain.He Got tricked Easily. 


Vulnerable Domain - What Is SPF/TXT Records?

An SPF record is a type of Domain Name Service (DNS) record that identifies which mail servers are permitted to send email on behalf of your domain. The purpose of an SPF record is to prevent spammers from sending messages with forged From addresses at your domain.
Checking Missing SPF:-
 There Are Various Ways of Checking Missing SPF Records on a website But the Most Common and Popular way is kitterman.com

Steps to Check SPF Records on a website:-
Go to http://www.kitterman.com/spf/validate.html

Enter Target Website Ex: target.com (Do Not Add https/http or www)
Hit Check SPF (IF ANY)

If You seem any SPF Record than Domain is Not Vulnerable But if you see Nothing Here then "HURRAY! You Found a Bug"
 
Attack Scenario & PoC:-
Once There is No SPF Records.An Attacker Can Spoof Email Via any Fake Mailer Like Emkei.cz.An Attacker Can Send Email From name "Support" and Email: "support@target.com" With Social Engineering Attack He Can TakeOver User Account Lets say  Victim Knows the Phishing Attacks but When He Sees The Email from the Authorized Domain.He Gets tricked Easily. 


Vulnerable Domain - mycrypto.com


for testing i am forgering support@mycrypto.com

How to reproduce this 

1. go to https://anonymousemail.me/


2. fill all the details 
like 
Name - mycrypto
email - support@mycrypto.com
to - your email address 

etc 

send email 

3. it will directly send a mail from support@mycrypto.com to you

## Impact

Once There are no SPF Records.An Attacker Can Spoof Email Via any Fake Mailer Like Emkei.cz.An Attacker Can Send Email From name "Support" and Email: "support@target.com" With Social Engineering Attack He Can TakeOver User Account Lets say  Victim Knows the Phishing Attacks but When He Sees The Email from the Authorized Domain.He Gets tricked Easily.

## Attachments
- mycryptospf.mp4
