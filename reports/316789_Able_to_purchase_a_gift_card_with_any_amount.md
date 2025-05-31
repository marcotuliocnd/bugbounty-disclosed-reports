# Able to purchase a gift card with any amount

## Report Details
- **Report ID**: 316789
- **URL**: https://hackerone.com/reports/316789
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-16T13:52:09.837Z
- **Disclosed**: 2018-07-20T20:10:42.471Z

## Reporter
- **Username**: qwacsawd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Description**
There is a vulnerability in card.starbucks.com.sg that allows an attacker to modify the purchasing value of a starbucks gift card such that he is paying the minimum amount for the maximum value of the gift card.

**Attack Summary**
An attacker is able to pay $0.01 for a $100 gift card and gift the card to himself thus allowing him to use the card.

**Steps to Reproduce**
1)Visit https://card.starbucks.com.sg/egift/cards.php?cat=Singapore%20Exclusive
2)Fill in the relevant values, set the emails to your starbucks account email and the input value to $300 at the start
3)Use a web proxy to monitor the web traffic and click on the check out button.
4)Change the original values of the request from 
txtAmount=300&amount=300&txtCustomAmount=300 to txtAmount=0.1&amount=0.1&txtCustomAmount=0.1 and submit the request
5)An encoded string of the value 0.1 will be displayed in the following request as vpc_Amount=XcfYhTj%2BHFIY5c9n8sSCzqDFAxXGgXXoZgF0VVUBvjM%3D, where =XcfYhTj%2BHFIY5c9n8sSCzqDFAxXGgXXoZgF0VVUBvjM%3D is the value 0.1
5)Copy that string and drop the entire request
7)Repeat step 1 to 4, this time change ONLY the value in the variable "amount" so the request would look like this:
txtAmount=300&amount=300&txtCustomAmount=300 to txtAmount=300&amount=0.1&txtCustomAmount=300
8)Proceed to click on the check out button and you will be brought from https://card.starbucks.com.sg/egift/checkout.php to https://card.starbucks.com.sg/egift/payment.php where the vpc_Amount is showed in the request. Change the original vpc_Amount value to the copied string XcfYhTj%2BHFIY5c9n8sSCzqDFAxXGgXXoZgF0VVUBvjM%3D
9)Proceed on to submit the request and you will be brought over to the payment page by either visa/mastercard
10)Continue payment as per usual and you will be paying $0.1 for a $300 starbucks card.
11)Since the recipient email is the attacker's email he checks his email to redeem the card and adds it into his starbucks account.
12)The attacker now has a $300 starbucks gift card that he only paid $0.1 for.

## Impact

By abusing this function, an attacker could gain unlimited values for his starbucks card.

## Attachments
No attachments
