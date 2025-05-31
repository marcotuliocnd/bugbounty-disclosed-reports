# Clickjacking on profile page leading to unauthorized changes

## Report Details
- **Report ID**: 1198907
- **URL**: https://hackerone.com/reports/1198907
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-16T17:16:19.520Z
- **Disclosed**: 2021-06-15T22:14:43.339Z

## Reporter
- **Username**: shivanshmalik2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary:
Any attacker could use iFrame options to connect remotely to the real website, And he can craft his own website using the iFrame options of the specific link and can lead to unauthorized changes if the user will be logged in.

## Steps To Reproduce:
1. Login to https://app.upchieve.org/profile
2. Download the attached file and run it on the same browser 
3. You will see a small window which shows us the profile page, Ive currently set the size to small
4. Attacker can make it bigger and gain info.

## Recommendations for Fixing/Mitigation
Use X-Frame Options in the HTTP Responses of the page, This will help content going straight to user and not a 3rd Party.

## Impact

Unauthorized control

## Attachments
- iframe.html
