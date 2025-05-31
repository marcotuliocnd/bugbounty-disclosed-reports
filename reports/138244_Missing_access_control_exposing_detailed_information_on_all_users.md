# Missing access control exposing detailed information on all users

## Report Details
- **Report ID**: 138244
- **URL**: https://hackerone.com/reports/138244
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-12T10:25:47.029Z
- **Disclosed**: 2016-10-17T23:40:44.282Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wp-api

## Vulnerability Information
The WP REST API WordPress plugin fails to apply access controls for the 'edit' context. This means that with a single HTTP request, an attacker can obtain the following information for every single registered user: username, email address, first name, last name, date of registration, and detailed privilege information. This is a treasure trove of information for someone planning an attack - they know exactly which email addresses to target in order to gain admin privileges and complete control over the webserver.

To replicate this issue, simply send the following request while unauthenticated:
GET /wp-json/wp/v2/users?context=edit

Please note that I've submitted this report to a couple of entities directly affected by this vulnerability so they can implement a workaround.

## Attachments
No attachments
