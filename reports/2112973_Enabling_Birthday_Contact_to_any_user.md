# Enabling Birthday Contact to any user

## Report Details
- **Report ID**: 2112973
- **URL**: https://hackerone.com/reports/2112973
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-16T20:50:07.640Z
- **Disclosed**: 2023-11-21T05:23:11.954Z

## Reporter
- **Username**: nvz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Was able to enable ` Birthday Contacts ` any User, Admin, SuperAdmin. from a low privileged user.

## Steps To Reproduce:
- Navigate to Calendar. 
- At the very bottom find calendar settings 
- Click on `Enable Birthday Contacts ` 
- Intercept the following request 

```
POST /remote.php/dav/calendars/{userId}

<x3:enable-birthday-calendar xmlns:x3="http://nextcloud.com/ns"/>
```

## Impact

Users with low privileges enable the "Birthday Contacts" feature for any user, including Admins and SuperAdmins, within the Nextcloud application. By following a simple set of steps, an attacker could navigate to the Calendar section, access the calendar settings, enable the "Birthday Contacts" feature, and intercept a specific request to achieve this unauthorized action.

## Attachments
No attachments
