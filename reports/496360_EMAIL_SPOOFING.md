# EMAIL SPOOFING

## Report Details
- **Report ID**: 496360
- **URL**: https://hackerone.com/reports/496360
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-15T05:12:04.563Z
- **Disclosed**: 2022-01-02T18:30:57.312Z

## Reporter
- **Username**: hackthedevil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hey KHANACADEMY,
I have found Email Spoofing type of Vulnerability in your Website.
Attacker can use your E-Mail to send emails to others.

Email spoofing is the creation of email messages with a forged sender address. Because the core email protocols do not have any mechanism for authentication, it is common for spam and phishing emails to use such spoofing to mislead the recipient about the origin of the message

Not Only contact@khanacademy.org involved in it, All the Emails develop in https://www.khanacademy.org/ may be affect by it...

Steps to Produce this Issue:
1) Goto: https://emkei.cz/
2) Add contact@khanacademy.org "From Email" in https://emkei.cz/
3) Click Send Button,
4) The Email from contact@khanacademy.org will be send to the Email you enter.

Another way,
<?php
$to = "hackthedevil@weareonhackerone.com";
$subject = "Email Spoofing Test";
$txt = "This is Email Spoofing";
$headers = "From: contact@khanacademy.org";
mail($to,$subject,$txt,$headers);
?>

Save this code in PHP file, & upload it on online server, Execute it & you can see The email will be send to your Desired Email

See Screenshots below, I received Email from your website.

Fix:
1.Improve Your Mailer, Turn on some more Security filters.
2. DMARC Policy Not Enabled-This Warning indicates that the DMARC record for this domain is not currently protected against phishing and spoofing threats. To resolve this Warning you will need to set a Quarantine or Reject policy on the domain's DMARC record. Setting a Quarantine or Reject value will prevent fraudsters from spoofing the domain as mail servers will Quarantine or Reject messages that fail authentication tests. (CHECK IT ON- https://mxtoolbox.com/SuperTool.aspx?action=mx%3akhanacademy.org&run=toolpage# )

Read More about Email Spoofing here:
http://searchsecurity.techtarget.com/definition/email-spoofing

## Impact

IT CAN BE USED TO STEAL USER DATA AND FAKE PAYMENT AND COSTUMERS.

## Attachments
- dmarc.png
