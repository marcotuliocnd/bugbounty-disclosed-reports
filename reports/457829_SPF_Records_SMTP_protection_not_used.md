# SPF Records (SMTP protection not used)

## Report Details
- **Report ID**: 457829
- **URL**: https://hackerone.com/reports/457829
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-07T06:51:28.898Z
- **Disclosed**: 2018-12-17T22:02:19.091Z

## Reporter
- **Username**: shantanu_kul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mycrypto

## Vulnerability Information
Hello MyCrypto Team ,

I am checking your website and found something is missing in SPF record.I don't find you have applied strict SMTP policy to stop spoofed email sending from your domain.

I would like to recommend you to read the following article :

https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

Problem description :

The above article strictly guide us about difference between soft mail and fail. MyCrypto should use fail because Soft mail allows anyone to send spoofed emails from your domains.

In your SPF record you should replace ~ with - at last before all , - is strict which prevents all spoofed emails except if you are sending. Your bug is that you are using ~ , you should use -

FIX :

Your SPF record : v=spf1 include:_spf.google.com ~all 

It should be : v=spf1 include:_spf.google.com -all 

Best Regards ,

Shantanu

## Impact

An attacker can send a Fake email from support@mycrypto.com saying that Please change your password, The victim is aware or not of phishing attacks, But when he sees that the mail originated from support@mycrypto.com , then he can blindly believe on it. Clicking on the link takes him to a website where certain JavaScript is executed which steals his PayPal id and password (SESSION COOKIE). 
Later results are more harmful.

<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: support@mycrypto.com";
mail($to,$subject,$txt,$headers);
?>

## Attachments
No attachments
