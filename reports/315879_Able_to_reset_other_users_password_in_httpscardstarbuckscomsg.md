# Able to reset other user's password in https://card.starbucks.com.sg/

## Report Details
- **Report ID**: 315879
- **URL**: https://hackerone.com/reports/315879
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-14T05:48:58.768Z
- **Disclosed**: 2018-07-23T17:42:34.870Z

## Reporter
- **Username**: qwacsawd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Description**
In the website https://card.starbucks.com.sg/ there is a password reset function (https://card.starbucks.com.sg/forgetPassword.php) that sends the password reset link to the user's email. By using a web proxy to monitor the request, the email address can be changed to allow the attacker to reset a victim(another email) password, thus allowing him to gain full access to the victim's starbucks account and starbucks card.

**Summary**
The attacker request a password reset and obtains the password reset link in his email. By using a web proxy, he can use the password reset token and modify the his own email to a victim's email and the password reset will be used for the victim instead of the attacker.

**Steps to Reproduce**
1)Attacker visits https://card.starbucks.com.sg/forgetPassword.php and enters his account's email
2)The link is sent to the attacks email's inbox and he clicks on the link while having a proxy monitor the request(burp)
3)The attacker then modifies the email to put the victim's email in these 2 requests as shown in the image below F263235 & F263234
4)Upon submitting the request, the password will be changed and the victim's password will be changed to the desired password

## Impact

This attack does not require the victim to perform any actions and yet the account can be taken over by the attacker and this leaks the victim's personal information and starbucks card which can be used to purchase items. The attacker can also capture the session id.

## Attachments
- 2.PNG
- 1.PNG
