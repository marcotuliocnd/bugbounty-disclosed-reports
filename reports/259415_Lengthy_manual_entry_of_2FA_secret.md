# Lengthy manual entry of 2FA secret

## Report Details
- **Report ID**: 259415
- **URL**: https://hackerone.com/reports/259415
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-13T12:39:30.027Z
- **Disclosed**: 2017-08-15T05:19:50.873Z

## Reporter
- **Username**: goodhackonly
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hello @team,

I would like to report on some issue where users are going to face while 2FA authentication.We can see that users need to enter 52 bit code manually for 2FA authentication,which is taking a lot of time and it will be difficult for the user to enter the total 52 bits in the google authenticator app without mistakes.


why is this an issue?
we all know that our clients wont have that much  patience to enter such a lengthy code every time they want 2FA authentication .I've surveyed on other sites(paypa.com,stripe.com) who added the feature 2FA for their clients and Ive observed that users are requested to enter the 16 digit code manually so that it wont effect the time and probability for making mistakes in the google Authenticator. However attackers cannot bypass the  code or brute force because Legal robot took  necessary steps for this type of protection by implementing the web socket messages.

what is the best possible fix?
The best possible fix is to reduce the 52bit  "enter code manually code" to 16 bit.

why legal robot need this change?
--> 2FA authentication feature was newly added.If users using this feature  find this feature as a lot of time wastage they wont use this feature. As a result the impact might bring bad reputation to the entire legalrobot.

From my survey I have another image where other applications are providing 16 bit enter code manually code,which will be much easier for the users to enter in the google authenticator app.

Thanks!



## Attachments
- Screenshot_(2897).png
- Screenshot_(2898).png
