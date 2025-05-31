# Lack of length validation on user address attribute

## Report Details
- **Report ID**: 161947
- **URL**: https://hackerone.com/reports/161947
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-08-21T15:15:42.421Z
- **Disclosed**: 2019-04-11T08:32:44.950Z

## Reporter
- **Username**: rohitdua
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi

The input fields for adding mailing address for swag delivery in ```https://hackerone.com/settings/swags``` are not restricted in input lengths.
I was able to add *(and read the contents via my own address page and the team page(who awards the swag))* over **585728 characters** in each of the input fields ```Name, Street, City, State/Province, Postal code, Country, Phone number``` without any restriction or error message.

{F113760}

This may lead to server side Denial Of Service attack or over memory consumption. You need to decrease input lengths( or add one if missing)

Thanks
Rohit Dua
https://github.com/rohit-dua
https://in.linkedin.com/in/rohitdua

## Attachments
- Screenshot_from_2016-08-21_20-17-27.png
