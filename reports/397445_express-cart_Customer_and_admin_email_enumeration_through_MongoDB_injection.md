# [express-cart] Customer and admin email enumeration through MongoDB injection

## Report Details
- **Report ID**: 397445
- **URL**: https://hackerone.com/reports/397445
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-20T20:07:16.367Z
- **Disclosed**: 2018-09-10T22:58:42.734Z

## Reporter
- **Username**: becojo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report an injection in express-cart
It allows to enumerate the email address of the customers and the administrators.

# Module

**module name:** express-cart
**version:** 1.1.7
**npm page:** `https://www.npmjs.com/package/express-cart`

## Module Description

expressCart is a fully functional shopping cart built in Node.js (Express, MongoDB) with Stripe, PayPal and Authorize.net payments.

## Module Stats

31 downloads in the last week

# Vulnerability

## Vulnerability Description

The vulnerability is caused by the lack of user input sanitization in the login handlers. In both cases, the customer login and the admin login, parameters from the JSON body are sent directly into the MongoDB query which allows to insert operators. These operators can be used to extract the value of the field blindly in the same manner of a blind SQL injection. In this case, the `$regex` operator is used to guess each character of the token from the start. 

## Steps To Reproduce:

Use MongoDB `$regex` operator to test if each characters of the emails in the database.

The provided Python script exploits the customer login to find all the customer emails in the database. Some recursion is used to make sure all of the fields

The attached screenshot is the customer list currently in my database. The output of the script is the following:

```
$ python exploit.py 
alan.k@example.com
alice.r@hotmail.com
ben76543@gmail.com
bob@test.com
```

## Patch

Ensure the parameters are indeed strings before doing a MongoDB request. There are multiple ways this could be achieved. Using `toString` on the parameters is good enough. 
 
```
db.customers.findOne({email: req.body.loginEmail}, (err, customer) => { // eslint-disable-line
```
becomes
```
db.customers.findOne({email: req.body.loginEmail.toString()}, (err, customer) => { // eslint-disable-line
```

While a user can still trigger an exception by replacing `toString` with something else than a function, it effectively mitigates the vulnerability.

## Supporting Material/References:

- OS: Ubuntu 16.04.3 LTS
- Node.js version: 8.11.1 
- For the script: Python 2.7.12 and the requests package

# Wrap up
- I contacted the maintainer to let them know: No
- I opened an issue in the related repository: No

## Impact

Administrator emails could be used for phishing attemps and spam. Customers emails could be used by an adversary to deliver spam, steal customers and more. In this GDPR era, leaking customer emails is not very desirable.

## Attachments
- expressCart-admin-emails.png
- exploit.py
