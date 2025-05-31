# Object injection in `stripe-billing-typographic` GitHub project via /auth/login 

## Report Details
- **Report ID**: 1183335
- **URL**: https://hackerone.com/reports/1183335
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-03T22:14:22.713Z
- **Disclosed**: 2023-03-06T14:03:26.851Z

## Reporter
- **Username**: ph0r3nsic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
## Summary:
It is possible to use an object injection failure to achieve a sql injection, where attacker uses the means to bypass authentication, requiring only a valid password within the database.

The vulnerable code is:  https://github.com/stripe/stripe-billing-typographic

For a failure to occur, it is necessary that the environment is configuring with the mysql database.  

The same scenario is seen in the demonstration environment: https://typographic.io/

## Steps To Reproduce:

  1. Register a simple user in the application, with a password at your desire. Ex:
```
user: test@test.com
password:123
```
  2. Send a request to /auth/login like this:
```
POST /auth/login

{"email":{"email":1},"password":"1234"}
```
  3. You will then see that the login was performed without the need to provide a valid user!

{F1287585}


## Supporting Material/References:
Well, the failure occurs due to the possibility of an object reaching the query, which will be handled by a dependency called sqlstring, performing some scapes, where it will cause a confusion to the query.

Sqlstring will handle {,} replacing with `. 
So your login query will be:
```
SELECT * FROM `accounts` WHERE `email`=`email`=1
```
The sql string library is a dependency on the mysql library, which is used by knex.

## Mitigation

Is a simple step, use JSON.stringfy e resolve your problem, because JSON.stringfy will transform the malicious object into a string, preventing treatment during a query.

## Impact

This vulnerability to the applied scenario makes it easier for the attacker to acquire accounts, as the attacker only needs to discover a valid password to gain access to the victim's account.

## Attachments
- Captura_de_Tela_2021-05-03_a_s_18.05.45.png
