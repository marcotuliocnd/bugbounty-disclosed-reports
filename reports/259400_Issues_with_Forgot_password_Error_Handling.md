# Issues with Forgot password Error Handling 

## Report Details
- **Report ID**: 259400
- **URL**: https://hackerone.com/reports/259400
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-13T10:37:42.186Z
- **Disclosed**: 2017-09-26T01:10:37.034Z

## Reporter
- **Username**: goodhackonly
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hello @team,

I found a similar issue to #249695.Where user when giving an error email id it is not showing any error response.This is not of high impact but this might throw the users in confusing state as there is no error message user will be waiting for the server response.

Steps to reproduce:
1.go to url : https://app.legalrobot-uat.com/sign-in
2. go to forgot password option and give your email id
3.now click on the forgot password link.
4.give wrong email id and some password
5.now you will see that there is no server response .

How to resolve this?
Similar to login failure error message 403.we can also show the error message like this:
"password change failure.please check the details entered[403]" when the user is given wrong email id .
there is another issue here what if he is using this to user enumeration?that is not possible because of two reasons.
1)now legalrobot requests are turned to web socket messages it will be difficult to user enumeration
2)there wont be point of user enumeration because we will show 403 error for every registered and non-registered email id.Only for the forgot password requested email id it will show 200 ok response

Let me know if u need more information regarding this.
Thanks!


## Attachments
- Screenshot_(2895).png
