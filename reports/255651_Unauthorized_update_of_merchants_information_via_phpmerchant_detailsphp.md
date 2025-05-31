# Unauthorized update of merchants' information via /php/merchant_details.php

## Report Details
- **Report ID**: 255651
- **URL**: https://hackerone.com/reports/255651
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-02T00:18:29.320Z
- **Disclosed**: 2017-09-19T06:14:42.259Z

## Reporter
- **Username**: adibou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello!

I discovered an interesting file : 
`https://www.zomato.com/php/merchant_details.php`

If I add in post content :
`action=update-merchant&merchant_id=95292&type=1&email=update@hotmail.fr&contact=update@hotmail.fr&name=update`

With the report #255648, I was able to create a merchant, I should use this merchant to provide a screenshot like in a real situation.


I'm also able to change :
`address, pincode, city, email, phone tan_number, bank account name, company_id, payu_id, contact, restaurants` and more...


An attacker would change the mail to receive confidential mails it may can be leading to an merchant takeover if you use the mail to bound it with the account of the user. I couldn't try this scenario due to your rules about users data.

Do you have a test merchant_id i can play with to test that before you resolve the report?

Screenshot : updatehttp.png

If you have any questions...
nbsp


## Attachments
- updatehttp.png
