# Email OTP/2FA Bypass

## Report Details
- **Report ID**: 2315420
- **URL**: https://hackerone.com/reports/2315420
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-01-14T19:44:28.986Z
- **Disclosed**: 2024-06-16T11:39:26.195Z

## Reporter
- **Username**: akhan8041
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drugs_com

## Vulnerability Information
The application has a functionality of 2FA by email OTP so i can bypass that 2FA and got the access of application without having any access of victim account. when a user try to login in the application and enter username and password, the 2FA page is available and application generate all the cookies like "PHPSESSID" or "bb_sessionhash"  at same time at 2FA page that is responsible for the user session but there is a cookie named "bb_refresh" if i delete that cookie and refresh the page again then i can successfully login to the application without 2FA. 

## POC:
1. Login with correct username and password
2. Right click and open inspect element and go to application tab 
3. Select Cookie form the left panel and select drugs.com
4. Delete the cookie named "bb_refresh"
5. Now refresh the page again and Boom !  You Logged In !

████████

## Impact

A 2FA bypass in a web application compromises user security, allowing unauthorized access. Attackers can exploit this vulnerability to gain control over accounts, leading to potential data breaches, privacy violations, and unauthorized actions.

## Attachments
No attachments
