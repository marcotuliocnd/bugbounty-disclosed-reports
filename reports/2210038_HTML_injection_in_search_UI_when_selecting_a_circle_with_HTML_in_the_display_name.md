# HTML injection in search UI when selecting a circle with HTML in the display name

## Report Details
- **Report ID**: 2210038
- **URL**: https://hackerone.com/reports/2210038
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-10-15T21:41:08.966Z
- **Disclosed**: 2023-11-21T09:22:07.279Z

## Reporter
- **Username**: cx75fa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
HTML injection is a web security issue where attackers insert harmful code into a web application, affecting how it appears and functions. This can lead to data theft, phishing, malware distribution, and session hijacking, posing significant risks to users and the application's integrity. Prevention involves thoroughly checking and encoding user-generated content to ensure it's safe for rendering in web pages.

Reproduction Steps: 

1. Log in to the application using a low-privilege user account.
2. Access the "Contacts" section and initiate the creation of a new Circle.
3. When naming the Circle, insert the following payload: ``<meta http-equiv="refresh" content="2; https://evil.com/" />``.
4. Share the Circle with a user account having an "Admin" role.
5. Switch to the "Admin" user role and go to "Files" > "Shared with Circles."
6. Observe that the browser will redirect to a malicious website within a 2-second timeframe.

Video POC : 
{F2775888}

## Impact

HTML injection can have significant impacts, including:

Data theft
Phishing attacks
Malware distribution
Session hijacking
These consequences can harm both users and the application's security.

## Attachments
- HTMLInjection.mp4
