# Credentials leaked via Github

## Report Details
- **Report ID**: 1078373
- **URL**: https://hackerone.com/reports/1078373
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-14T09:45:42.756Z
- **Disclosed**: 2024-08-26T15:35:35.275Z

## Reporter
- **Username**: sheikh_chilli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi Team,

I have found the credentials on Github which leads to direct access to the portal.

Steps to reproduce:

Go to the below link: https://github.com/MasterHimself/Test/blob/2faa2990fe2d63ceb8b1577df792e0edc5d0bdba/Selenium/Behave/Examples/Steps/Steps.py

Observed the hardcoded credentials.
So, I visit the URL https://cloud.acronis.com/login & use the mentioned credentials.

 driver.find_element_by_xpath("//input[@name='login']").█████
 driver.find_element_by_xpath("//input[@name='password']").█████

Got the direct access and able to view the sensitive information.

## Impact

Hardcoded passwords are particularly dangerous because they are easy targets for password guessing exploits, allowing hackers and malware to hijack firmware, devices (such as health monitoring equipment), systems, and software.

Looking forward to your response.

regards
Alisha Sheikh

## Attachments
No attachments
