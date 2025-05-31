# Reset password cookie leads to account takeover

## Report Details
- **Report ID**: 1004536
- **URL**: https://hackerone.com/reports/1004536
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-10T11:20:25.328Z
- **Disclosed**: 2020-10-12T12:16:42.379Z

## Reporter
- **Username**: homaa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi

There are 3 issues on this report lead to account takeover. 

1- When the user requests a reset password link, server sends a link for the user via email, whenever the user click on the link for the first time redirects to ***Reset password page*** but if the user close browser or tab and click again on the link the user will redirect to the wrong address `https://hosted.weblate.org/accounts/login` and receives the following error:

{F1030242}

#Remediation:
==The reset password link should always redirect the user to the reset password page.==

2- If the user tries to login the account couldn't log in with the current password and receives the following error:

{F1030244}

#Remediation:
==The user should access to her/his account after clicking on the reset password link, it might remember the current password and the user doesn't need to change password==

The above issues are logic issue but at the end leads to account takeover.

3- When the user request for reset password link, if click on the link and close the reset password page after clicking on the link redirects to the wrong address and couldn't log in via the current password.
After clicking on reset password link a cookie stores in the browser and remain for hours

{F1030251}

If the user uses a shared computer or someone access on the user's computer can go to the [Forgotten your password page](https://hosted.weblate.org/accounts/reset/) and change the user password.

#Remediation:
==1- The user should always redirect to correct link after clicking on the reset password link.
2- The cookie remain for hours on the computer, decreasing cookie expiration can decrease account takeover risk.==


For more clarification, please watch the following video:

████

If you have any questions, please let me know.

Knid regards.

## Impact

A combination of wrong redirection on reset password link and cookie expiration time can lead to account takeover.

## Attachments
- error1.png
- error2.png
- cookie.png
