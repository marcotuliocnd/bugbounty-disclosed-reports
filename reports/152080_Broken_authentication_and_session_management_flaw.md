# Broken authentication and session management flaw 

## Report Details
- **Report ID**: 152080
- **URL**: https://hackerone.com/reports/152080
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-18T16:08:54.964Z
- **Disclosed**: 2016-08-18T06:58:35.572Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coursera

## Vulnerability Information
In this Loop Hole The Application does not destroy session after logout.. means the cookies are working to login to user account & change account Information, The Cookies are usable after many hours of logout about after 1 day i'm able to access the account & edit info.

Steps To Reproduce This Issue:

1: go to coursera.org

2. Login to your account.......

3. Get the cookies using " Brub Suite" or "EditThisCookie" 

4: Logout from the account...

5: Clear all the cookies related to coursera.org

6: Save the cookies you copied in a text file...

7: Now Injact/Import Old Cookies to the coursera.org by "EditThisCookie"... 

8: as u can see.. you will be again logged In to coursera.org account.. using old session cookies..

For More Information about This Vulnerability You can check OWASP Guide 

https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en 

Thanks, 
khizer Javed


## Attachments
No attachments
