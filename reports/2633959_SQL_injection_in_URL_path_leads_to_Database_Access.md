# SQL injection in URL path leads to Database Access

## Report Details
- **Report ID**: 2633959
- **URL**: https://hackerone.com/reports/2633959
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-07-31T22:39:36.605Z
- **Disclosed**: 2025-01-08T10:40:53.785Z

## Reporter
- **Username**: tinopreter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
The application https://corporate.admyntec.co.za/ application has an SQL injection in the URL paths since it takes the ID numbers in there and insert them directly into the backend SQL query without sanitizing them. In the registration, user ID number(Passport or National ID), Organization number are requested, as well as relevant docs. These are all stored in the backend Database.

https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0

## Steps To Reproduce:

  1. Using the URL generated when we get displayed the Insurance.   

{F3484515}  

  2. Introduce a single quote next to the customerId number and you realize this breaks the backend query.

```
https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0  
```
{F3484523}  
  3. Send this URL to any SQL epxloitation tool like SQLmap, Add an asterisk to the customerId number to tell the tool that's the injection point.  We can dump the database now.

{F3484537}  

##Please Note That This Occurs throughout many URL paths in the application.

#Recommendation
If you are taking parameters and inserting them into the backend SQL query, sanitize them to do away with any special characters attached to them.

Consider putting the application behind a WAF to make a potential SQLi vulnerability exploitation a bit tedious for an attacker.

## Impact

An attacker can exploit this to dump and download the backend database. This will give them access user information.

## Attachments
- image.png
- image.png
- image.png
