# ClickJacking on IMPORTANT Functions of Yelp

## Report Details
- **Report ID**: 305128
- **URL**: https://hackerone.com/reports/305128
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-16T07:45:07.301Z
- **Disclosed**: 2020-08-21T20:41:41.078Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
##SUMMARY:
Few Important function of yelp.com are vulnerable to ClickJacking Attack.

##DESCRIPTION:
Please have an Introduction about the vulnerability Type: https://en.wikipedia.org/wiki/Clickjacking
ClikcJacking is similar to CSRF with just an extra involvement of the victim to click somewhere on the ClickJacked page (which is usually done very easily). 
It bypasses CSRF token protection & Its impact could be critical depending on the component/function it can affect. At yelp.com I have found the following functions to be vulnerable:

##1.) Report A profile  (With custom Message in it)
**Using URL:**
https://www.yelp.com/flag_content?message=This%20person%20is%20abusive&flag_id=aV0sVlYtxt7_2SJ7X_b-3A&flag_type=user_profile&previous_url=%2Fuser_details%3Fuserid%3DaV0sVlYtxt7_2SJ7X_b-3A

##2.) Follow a user
**Using URL:** 
https://www.yelp.com/following_user/add?dst_user_id=aV0sVlYtxt7_2SJ7X_b-3A&previous_url=/user_details?userid=aV0sVlYtxt7_2SJ7X_b-3A

##3.) Send A Compliment (With Custom message in it)**
**Using URL:**
https://www.yelp.com/thanx?message=go%20to%20hell&previous_url=/user_details?userid=aV0sVlYtxt7_2SJ7X_b-3A&user_id=aV0sVlYtxt7_2SJ7X_b-3A

##POC:
*PLEASE WATCH THE 1 minute POC VIDEO TO SEE HOW THESE URL ARE EMBEDDED INTO HIDDEN IFRAMES AND HOW THE VICTIM IS EXPLOITED. THE HTML FILES USED IN THE VIDEO ARE ATTACHED IN THIS REPORT*
*THE POC ALSO SHOWS THE IMPACT OF THE VULNERABILITY*

##MITIGATION
These attacks could be circumvented by using "X-Frame-Options" Header.

## Impact

Such vulnerability when exploited in the wild by the attackers would :
1.) Affect the users interaction on your platform. Such unintended behavior is definitely not wanted by any user.
2.) Such effect upon your users could significantly harm your overall reputation and customer loss.

## Attachments
- Dangerous_ClickJacking_Yelp.flv
- Follow_User.html
- Report_a_USER.html
- Send_a_Compliment.html
