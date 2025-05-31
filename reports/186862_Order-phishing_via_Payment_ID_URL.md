# Order-phishing via Payment ID URL

## Report Details
- **Report ID**: 186862
- **URL**: https://hackerone.com/reports/186862
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-30T13:21:13.847Z
- **Disclosed**: 2016-11-30T20:14:33.226Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
Hello. I discovered the endpoint, which allows the attacker conduct the fishing attack to other users and they can pay for attacker's order.
Why this can happen? 
On the site, order id parameter sends to the https://portswigger.net/CCPayment.aspx as POST, but attacker can append it as GET and it will works:

Example:
https://portswigger.net/CCPayment.aspx?id=DD6BE85CDD50DC829C0354F83E5C67

Steps to reproduce:
1) Go to the https://portswigger.net/buy/ and fill the form.
2) Click "Confirm details".
3) Click "Pay by credit card".
4) Catch the POST request from ССpayment.aspx with order id:

POST /CCPayment.aspx HTTP/1.1
[...Headers...]

id=05BC4BF36F9BB32E80F4B581BF4859

5) Now append the id as GET parameter. You will have link like https://portswigger.net/CCPayment.aspx?id=05BC4BF36F9BB32E80F4B581BF4859
6) Now you can conduct phishing attack with this link, and users can pay for your order.

## Attachments
No attachments
