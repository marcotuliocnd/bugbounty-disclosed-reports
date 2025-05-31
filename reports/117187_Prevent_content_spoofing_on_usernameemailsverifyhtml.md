# Prevent content spoofing on /~username/emails/verify.html

## Report Details
- **Report ID**: 117187
- **URL**: https://hackerone.com/reports/117187
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-02-18T18:25:19.254Z
- **Disclosed**: 2017-06-16T06:32:21.346Z

## Reporter
- **Username**: ishahriyar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi,
When an user add his email  then a verification link has been sent to that email.
the link looks like this
https://gratipay.com/~exampleuser/emails/verify.html?email=example%40gmail.com&nonce=cb2487f6-61cf-4a8a-81af-c8fab6fe0f90

The link has three changeable things.
1. Username (ex: ~exampleuser)
2. User's requested email (ex: example%40gmail.com)
3. Nonce 

But here the Nonce token is working for any user. Also you have missed to verify the email format
So  anyone can send fake messages to any  gratipay user. 

Steps to reproduce
If you have an account on gratipay then navigate the url like this
https://gratipay.com/~[your-user-name]/emails/

Then put your email address and click the button named "Add email address"

You will get an email copy the link
https://gratipay.com/~exampleuser/emails/verify.html?email=example%40gmail.com&nonce=cb2487f6-61cf-4a8a-81af-c8fab6fe0f90

Now put some messages instead of your email in your link , Like this
https://gratipay.com/~exampleuser/emails/verify.html?email=You Has been Sent. Hi This is official. You can get pro account by sending us 10 USD through our official paypal example@example.com&nonce=cb2487f6-61cf-4a8a-81af-c8fab6fe0f90

Just find a user from gratipay and put his name in the url instead of  "exampleuser"
Let's we have found a user named victimsusername

So the url will be this

https://gratipay.com/~victimsusername/emails/verify.html?email=You Has been Sent. Hi This is official. You can get pro account by sending us 10 USD through our official paypal example@example.com&nonce=cb2487f6-61cf-4a8a-81af-c8fab6fe0f90

Now send the link to the victim.
Anyone can misuse your app by this scope to send fake messages.


If you need anymore information feel free to ask.
Thanks.


## Attachments
No attachments
