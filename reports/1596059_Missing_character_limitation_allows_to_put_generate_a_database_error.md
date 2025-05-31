# Missing character limitation allows to put generate a database error

## Report Details
- **Report ID**: 1596059
- **URL**: https://hackerone.com/reports/1596059
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-09T16:44:23.385Z
- **Disclosed**: 2023-01-09T07:11:26.267Z

## Reporter
- **Username**: errorsec_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Security Team,
Summary:
=========
There is no limit to the number of characters in the display name, which allows a DoS attack. The DoS attack affects server-side.
Description
=========
On the input form of Username in nextcloud.com/settings/user there's no Input validation using this you can send more payload and may cause of Denial of service or error code 500 Internal Server Error/Internal Error
Proof of Concept
==============
1.Go and login to your account
2. Now go to setting and Deck ---> Add Boards section
3.Insert name and intercept it
4. Send to repeater replace it with payload the response code on the server side is 500 Internal Server Error

## Impact

Impact
=======
Remediation:
===========
+Implementing input validation
+Validating free-form Unicode text
+Define the allowed set of characters to be accepted.
+Minimum and maximum value range
Impact
======
Attacker can perform a DOS because of lack of input validation

## Attachments
- booard.png
- Board_Burp.png
