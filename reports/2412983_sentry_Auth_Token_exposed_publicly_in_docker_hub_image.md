# sentry Auth Token exposed publicly in docker hub image 

## Report Details
- **Report ID**: 2412983
- **URL**: https://hackerone.com/reports/2412983
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-03-11T22:00:29.266Z
- **Disclosed**: 2024-10-18T10:50:15.634Z

## Reporter
- **Username**: ghaazy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hi during my recon I found Sentry token which belongs to taskcluster
The token is still active.
## Steps

1. Go to https://hub.docker.com/r/taskcluster/taskcluster/tags
2. pull these images tags ```v15.0.0-20-g0eca18b7c``` and ``` c061025dc``` and ```ba7958766``` and ```v16.2.0-77-gd8577f62a``` may be this exist in more tags 
3. You will see this token 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9 in /app/node_modules/sentry-api/test.js
4. Try using the token with below curl request

curl -X GET -H "Authorization: Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" https://sentry.io/api/0/projects/

5. You will see api response.

{F3113306}
## Supporting Material/References:

  * https://www.invicti.com/web-vulnerability-scanner/vulnerabilities/sensitive-data-exposure-sentry-auth-token/

## Impact

## Summary:
Sentry exposes logs of the application which can contain sensitive information and PII.
This is basic impact.
But sentry contains application logs it can be used to find more vulnerabilities in the code base

## Attachments
- image.png
