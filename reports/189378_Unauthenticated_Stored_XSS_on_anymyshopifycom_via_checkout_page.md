# Unauthenticated Stored XSS on <any>.myshopify.com via checkout page

## Report Details
- **Report ID**: 189378
- **URL**: https://hackerone.com/reports/189378
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-12-08T02:57:40.937Z
- **Disclosed**: 2016-12-16T21:19:38.691Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,
I have found a stored cross site scripting vulnerability on `<any>.myshopify.com` through customer's first name in the checkout page after the order is completed.

#Details:
While processing an order on `checkout.shopif.com` customers are asked to enter their first name , last name , address details ..etc.
It's been found that the mentioned fields does not accept any HTML tags , so if you entered something like `<script>alert(2);</script>` , it will be rejected and you'll see a message saying `cannot contain HTML tags` . 
However, for some reason the only tag that you can include and it won't be rejected is `<html>` tag itself :D 
So , something like `<html onmouseover=alert(1)>` will be accepted.

After completing the order you'll land at a **thank** page saying that the order was confirmed , the XSS vulnerability lies in that page due to not sanitizing the first name of the customer inside the `<title>` tag.

#Steps to reproduce:
1. As an admin create a product with $0 price and $0 taxes on shipping so that you don't have to to enter any credit card details (the price doesn't matter , it's just to make testing easier).
2. As a user go to the product you created and buy it.
3. You'll be redirected to a page in `checkout.shopify.com` asking you to enter your details.
4. In the first name field enter `</title></head><html onmouseover=alert(2)>` .
5. Fill the other fields then click **Continue to shipping method** --> **Continue to payment method** --> **Complete order** 
6. XSS will trigger on `checkout.shopify.com` , to get the payload executed on `<your_store>.myshopify.com` , just go to `<your_store>.myshopify.com/0/checkouts/<checkout_id>/thank_you`

Here is a live PoC: `https://zh5402.myshopify.com/14372648/checkouts/5e566284338e71d6adc542b6567b4cf0/thank_you`
{F141546}


#Impact:
Through this vulnerability an attacker is able to execute arbitrary JavaScript at `<any>.myshopify.com` on admins and any other users to perform malicious actions such as fetching the CSRF token and using it to perform malicious requests , stealing sensitive information ..etc.

## Attachments
- xss_shopify.png
