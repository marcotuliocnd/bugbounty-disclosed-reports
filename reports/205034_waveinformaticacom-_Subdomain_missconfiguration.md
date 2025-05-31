# [wave.informatica.com]- Subdomain missconfiguration

## Report Details
- **Report ID**: 205034
- **URL**: https://hackerone.com/reports/205034
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-09T18:11:17.002Z
- **Disclosed**: 2017-02-19T14:26:36.778Z

## Reporter
- **Username**: mohammad-obaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
One of your subdomain https://wave.informatica.com has a CNAME record that resolved to ghs.google.com and shows 404 error when navigating to subdomain. You should remove CNAME entry for that subdomain pointing towards ghs.google.com. Although I couldnt verify the domain ownership process to fully takeover subdomain but it still possess thread in a sense that anyone can claim gsuite account using https://wave.informatica.com subdomain.For sake of poc I claim gsuite account with your subdomain name as shown in picture3. I will remove it if you want.
THREAD:
This could potentially prevent informatica from using services such as Google Drive, GMail, and Google Calendar with that particular subdomain.
POSSIBLE FIX:
To fully resolve the issue you need to remove the CNAME record and put in place a web forwarding rule for wave.informatica.com towards  new web landing page 

## Attachments
- pictures1.png
- pictures2.png
- gapps.png
- gapps2.png
