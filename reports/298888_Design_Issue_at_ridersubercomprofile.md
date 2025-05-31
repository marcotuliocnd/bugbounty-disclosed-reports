# Design Issue at riders.uber.com/profile

## Report Details
- **Report ID**: 298888
- **URL**: https://hackerone.com/reports/298888
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-12-17T06:42:51.939Z
- **Disclosed**: 2017-12-28T14:59:12.029Z

## Reporter
- **Username**: referrer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
## Summary
Hello,

This is not actually a security threat but a design issue. When a user logs into rush.uber.com, he will get an option called Account Information, when clicked on it takes the user to page https://riders.uber.com/trips#_ where user can edit his profile information. Here user can customize his Invite Code but upon customizing the Invite Code returns back to the initial value.

## Reproduction Steps
1) Login to rush.uber.com and select option Account Information.
{F247588}

2) Now you will be redirected to page https://riders.uber.com/trips#_ which has an option called Profile where you can change profile related information.

Here user gets an option to customize his Invite Code using the option Customize.
{F247591}

Now enter some Invite Code of your choice and click on Claim, and save. Now the new Invite Code will appear on your Profile page.
{F247593}

3)Once you have changed the Invite Code, click on any other option (eg: My Trips, Payment, etc) and then click on Profile option again. This time the profile page will show you the initial Invite Code. So it means the Invite Code customized by user is not getting stored and it reverts back to the old value.

I am not sure if this the way it was designed to work but I am reporting this to bring it to your notice. Sorry for wasting your time if the functionality is working as expected. Let me know if you need any further information.

## Impact

Design Issue

## Attachments
No attachments
