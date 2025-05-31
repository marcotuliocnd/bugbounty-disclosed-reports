# Stored XSS on Admin Access Page - Email field

## Report Details
- **Report ID**: 173501
- **URL**: https://hackerone.com/reports/173501
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-02T11:36:03.419Z
- **Disclosed**: 2017-08-02T05:58:41.882Z

## Reporter
- **Username**: pavanw3b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
"Cricetinae" :)

###Short Description

The **Email** field is not sanitized on **Inventory > Admin Access** page resulting in to Stored Cross-Site Scripting vulnerability.

###Vulnerability Details

Cross-Site Scripting issue let's one to run a javascript of choice. It helps most of the client side risks including but not limited to phishing, temporary deface, browser key-logger and others. Exploitation frameworks like BeEF eases the offensive attack.

Stored XSS is more risky than the reflected ones because of the fact that the malicious script is persisted across. It can affect all the time and all the users who has the access to the page.

### Attack Vector
As this is a stored XSS, the attack vector lies in one user phishing other users. If there are multiple administrators, one admin can get a javascript backdoor on another admin's browser.

### Steps to Reproduce
To effectively illustrate one user affect another user, please create 2 admin accounts and follow the below instruction:
* Login as `admin1`. Navigate to **Preferences** *>* **Change E-mail**
* Enter the current password and `admin1@example.com<script>alert('xss');</script>` for *Email address* field. Save and logout
* Login as `admin2`. 
* Navigate to **Inventory** *>* **Admin Access** and notice the alert box.

Attached screenshot for a reference.

### Test Environment Details
Version: Latest as on Oct 2: revive-adserver-4.0.0 downloaded from the official source
Setup type: local
Browser: Firefox 47.0
OS: Mac OS X


Cheers,
Pavan

## Attachments
- Screen_Shot_2016-10-02_at_4.47.08_PM.png
