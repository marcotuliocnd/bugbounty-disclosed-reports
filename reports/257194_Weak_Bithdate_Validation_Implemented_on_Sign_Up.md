# Weak Bithdate Validation Implemented on Sign Up

## Report Details
- **Report ID**: 257194
- **URL**: https://hackerone.com/reports/257194
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-06T08:15:58.710Z
- **Disclosed**: 2017-08-14T16:11:31.055Z

## Reporter
- **Username**: paranoidglitch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
The Birthdate Field on the KhanAcademy's [Sign Up](https://www.khanacademy.org/signup) page for new users has the year range from 2017 to 1897. 
{F210177}
However, while signing up for a new account, I was able to set the year to 1033 by manipulating the data being sent to the server and the account was successfully created. I can also confirm the year by checking the settings page of my account. Please refer to the screenshots for information.
{F210178}
{F210179}
{F210180}
{F210181}

I was also able to create a Child account with the same bug. Attaching the screenshot where the system says "You don't have an email address connected to this Khan Academy account. Since you're **_1017 years old_**, you can connect an email address to your account, which will unlink it from your parent's account.".
{F210182}
{F210183}

Suggestion: Proper validation should be implemented on Birthdate field so that the user is not able to set any year other than what is being displayed on the dropdown.

## Attachments
- 01-daterange.png
- 02-accountsignup.png
- 03-originalpostdata.png
- 04-modifiedpostdata.png
- 05-settingspage.png
- 06-childaccount.png
- 07-1017yearsold.png
