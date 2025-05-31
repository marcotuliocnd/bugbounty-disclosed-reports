# Bug Report : [ No Valid SPF Records ]

## Report Details
- **Report ID**: 1301696
- **URL**: https://hackerone.com/reports/1301696
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-08-12T16:49:11.482Z
- **Disclosed**: 2022-01-13T22:39:24.752Z

## Reporter
- **Username**: sohaib619
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi Team,  

Hope you are doing well. I found vulnerability in your web app

URL :  https://www.ruby-lang.org/en/s

Description :

There is an email spoofing vulnerability. Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to a solicitation.

Attack Scenario & PoC:

Once there is No SPF Records.An attacker can spoof email via any fake mailer Like Emkei.cz.An attacker can send email from name "Support" and Email: "support@target.com" with social engineering attack he can takeover user account let victim knows the phishing attack but when he see the email from the Authorized Domain. He got tricked easily.

Checking Missing SPF
There are various ways of checking missing SPF Records on a website But the Most Common and Popular way is kitterman.com

Steps to Check SPF Records on a website:-
Go to http://www.kitterman.com/spf/validate.html

Enter Target Website Ex: target.com (Do Not Add https/http or www)
Hit Check SPF (IF ANY)

I found :  


SPF record lookup and validation for: ruby-lang.org

SPF records are published in DNS as TXT records.

The TXT records found for your domain are:
_globalsign-domain-verification=6GywlC8PVV6mLfL6ToMeVqCDeqFk9IDu2uEqmYPqx3
v=spf1 +ip4:210.251.121.208/28 +ip4:221.186.184.64/28 include:_spf.google.com ~all

Checking to see if there is a valid SPF record.

Found v=spf1 record for ruby-lang.org:
v=spf1 +ip4:210.251.121.208/28 +ip4:221.186.184.64/28 include:_spf.google.com ~all

evaluating...
SPF record passed validation test with pySPF (Python SPF library)!


Screenshot and video:

image.pngimage.png



Remediation :

Replace ~all with -all to prevent fake email.

References :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability
Reference Report 

https://hackerone.com/reports/629087  
Hope you will fix that soon. Looking forward to your positive response. 

Thanks.



Kind Regards,
Sohaib

## Impact

Impact:
An attacker would send a Fake email. The results can be more dangerous.

## Attachments
- 2323.png
