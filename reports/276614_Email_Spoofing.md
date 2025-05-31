# Email Spoofing

## Report Details
- **Report ID**: 276614
- **URL**: https://hackerone.com/reports/276614
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-12T12:23:09.986Z
- **Disclosed**: 2018-03-13T14:18:59.155Z

## Reporter
- **Username**: protector47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
Hey SemRush,
It appears that spoofed email can be sent from 1 of your emails.

**The following email is vulnerable:**

mail@semrush.com

#Information:

>Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.

#Steps to Reproduce

1. Go to https://emkei.cz/.
2. Write down mail@semrush.com or any emails stated above to From Email field.
3. Write down the test address(where you want to check the spoofed email) to To field.
4. An email will be send to your test address from mail@semrush.com.

#Proof of Concept
Checkout the attached Screenshots.

Email from: mail@semrush.com

PS: As you can see, I used my Yahoo account as victim account and this is terrible to your clients who still using Yahoo (still a lot of them) as their email provider. It's because the email was sent directly to my inbox which is a trusted folder unlike spam so they will think that this spoofed email is legitimate.

Thank you for time and consideration you spent for reading my report.

Regards,

## Attachments
- em1.png
- emailSpoof.png
- em.png
