# Password Policy Issue

## Report Details
- **Report ID**: 246042
- **URL**: https://hackerone.com/reports/246042
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-05T10:04:00.052Z
- **Disclosed**: 2017-07-06T15:46:42.440Z

## Reporter
- **Username**: chuu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Greetings **Wakatime,**

I just found a weak password policy in your login page.

Some websites prevents the users to use password constructed of character combinations that otherwise meet company policy, but should no longer be used because they have been deemed insecure for one or more reasons, such as being easily guessed, following a common pattern, or public disclosure from previous data breaches. Common examples are 123456, qwerty, or the word password itself.

###Steps to reproduce###
A. 
1. Go to https://wakatime.com/signup.
2. Create an account by typing your email address and your password same as your email.
3. Hit "Sign Up for WakaTime" button. 
4. Your account will be created.

B.
1. Go to https://wakatime.com/signup.
2. Create an account by typing your email address and password to 123456.
3. Hit "Sign Up for WakaTime" button.
4. Your account will be created.

Some policies suggest or impose requirements on what type of password a user can choose, such as:

* the use of both upper-case and lower-case letters (case sensitivity)
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* prohibition of words found in a password blacklist
* prohibition of words found in the user's personal information
* prohibition of use of company name or an abbreviation
* prohibition of passwords that match the format of calendar dates, license plate numbers, telephone 
* numbers, or other common numbers

Refer to this link: https://en.wikipedia.org/wiki/Password_policy

Thanks for the time and effort you spent for reading my report.

Regards,
_________

## Attachments
No attachments
