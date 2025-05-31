# Recently added 'Country' field doesn't send email notification when changed

## Report Details
- **Report ID**: 961841
- **URL**: https://hackerone.com/reports/961841
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-18T20:54:10.890Z
- **Disclosed**: 2020-08-25T10:57:33.247Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team,

This is a small bug report. Actually I think there is no important security issue but I wanted to report it ¯\\_(ツ)_/¯
If you change your 'Country' information on account settings, HackerOne doesn't send `Your profile was recently changed` email.

**Description:**
There is an email notification system at HackerOne. If you change any information in your account, you will get an email notification from HackerOne like that :

{F954222}

And recently, HackerOne added a field called ´Country´ to account settings for future features.

{F954224}

But if you change your country, you will not get an email notification. This is just a small bug, no need for immediate actions :)

### Steps To Reproduce

1. Go to your HackerOne account settings (https://hackerone.com/settings/profile/edit)
2. Change your ´Country´ information
3. Check your email, you won't get any email notification.

You can check other fields, you will get an email when you change them (like name, location etc.)

I know some fields don't send any notifications, like social media links etc. They are frequently changeable fields, but I think the country information not. Also, HackerOne even sends email notifications on any change at ´Location´ field. This is so similar to ´Country´ field.

## Impact

HackerOne doesn't send email notification when any change at ´Country´ field in account settings

Regards,
Bugra

## Attachments
- email.jpg
- feature.jpg
