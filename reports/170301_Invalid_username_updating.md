# Invalid username updating

## Report Details
- **Report ID**: 170301
- **URL**: https://hackerone.com/reports/170301
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-18T23:56:51.907Z
- **Disclosed**: 2016-10-17T11:58:16.808Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
Hello Rubygems,

This is my first report on Hackerone, so please tell me if you need further information.

This vulnerability/glitch uses the 'Edit Profile' page.

How to do it:
1. Login to any account on Rubygems

2. Go to your profile

3. Go to 'Edit Profile'

4. In Handle, put the invalid username

5. Click 'Update'

6. It will show the "invalid username" error message, but in the top right corner, it will change the username to whatever you put it handle, whether it was valid or invalid. 

If it was invalid, when you leave that page/reload it, it will return the username to it's previous state, but this allows for any username in that space for a temporary amount of time, which could have potential for harmful code.

Another issue with this, besides the obvious glitch, is that in browsers with XSS blockers (Chrome, IE, etc.), it moves the avatar icon downward and the name section will be blank. (See pictures for an example)


Hopefully this has enough information. Thanks for reading

- Jack




## Attachments
- ce7ae003095a791c78072c41818a21ef.png
- 171da27bfd1d4996035255fe23fed6e2.png
