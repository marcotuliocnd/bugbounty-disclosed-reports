# Denial of Service by requesting to reset a password

## Report Details
- **Report ID**: 812754
- **URL**: https://hackerone.com/reports/812754
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-07T13:51:40.910Z
- **Disclosed**: 2021-01-25T20:12:19.503Z

## Reporter
- **Username**: makerlab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Description:
I believe that this is posible due to the brute force protection that makes all request last for 30 seconds which in this case is using all the PHP workers avalible in the pool, so the only way to defend yourself is setting up a limit or having a lot of resources.

### How to reproduce:
* In the Nextcloud login screen click the "Forgot password?" button and then type something in the textbox (can be anything)
* Then open the developers tools and go to the network tab
* Hold the "enter" key after pressing the reset password button and in the network tab you will see a lot of request being made
* With just 1000 request I managed to make the demo server "https://demo2.nextcloud.com/" not respond for 1 hour

## Impact

The attacker could make an entire nextcloud installation or even the entire server where it is hosted not respond for a very long time
Also, this attack can be made by almost anyone

## Attachments
- Report2.png
- Report.png
