# Missing SPF Flags

## Report Details
- **Report ID**: 244432
- **URL**: https://hackerone.com/reports/244432
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-29T16:12:28.128Z
- **Disclosed**: 2017-07-01T21:45:07.656Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
I am just looking at your SPF records then found following. SPF Records missing safe check which can allow me to send mail and phish easily any victim.

#PoC:
```
<?php
$to = "VICTIM@example.com";
$subject = "Password Change";
$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";
$headers = "From: support@wakatime.com";
mail($to,$subject,$txt,$headers);
?>
```
The TXT records found for your domain are:
v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com ~all 

Checking to see if there is a valid SPF record. 

Found v=spf1 record for wakatime.com: 
>v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com ~all 

#Fix:
>v=spf1 include:_spf.google.com include:mailgun.org include:spf.sendinblue.com -all 

You can check yourself here http://www.kitterman.com/getspf2.py
You can refer this https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

Let me know if any further info is required.

Regards,
Mr_R3boot.

## Attachments
No attachments
