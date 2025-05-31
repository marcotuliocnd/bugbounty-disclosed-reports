# Race Condition in account survey

## Report Details
- **Report ID**: 165570
- **URL**: https://hackerone.com/reports/165570
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-03T20:44:49.995Z
- **Disclosed**: 2017-11-12T11:25:59.583Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
There exists a race condition in the beginning survey, allowing a user to get $100 in credit multiple times. In my example, I made 2 asynchronous requests, and was credited with $200.

POC:

1. Create a new slack team.
2. Set your password, and find the account creation survey.
3. Complete the survey, and intercept the request using a proxy such as BurpSuite.
4. Repeat the request asynchronously, such as in the command line by executing `(command) & (command)`.
5. The survey will be credited to your account multiple times. See the attached screenshot.

Please let me know if you need any more information.

## Attachments
- Screen_Shot_2016-09-03_at_3.44.02_PM.png
