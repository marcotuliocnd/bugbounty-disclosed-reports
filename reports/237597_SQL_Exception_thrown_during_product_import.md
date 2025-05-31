# SQL Exception thrown during product import

## Report Details
- **Report ID**: 237597
- **URL**: https://hackerone.com/reports/237597
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-07T16:18:36.209Z
- **Disclosed**: 2017-07-12T00:44:11.203Z

## Reporter
- **Username**: pappan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Possible SQL Injection was observed when a descriptive error message was thrown in a mail sent to the user while importing products from csv. Used some special characters in csv to induce the error.

DATABASE FOUND TO BE MYSQL.

{F192274}

## Attachments
- sqlerror.png
