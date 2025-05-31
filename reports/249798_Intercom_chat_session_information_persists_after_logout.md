# Intercom chat session information persists after logout

## Report Details
- **Report ID**: 249798
- **URL**: https://hackerone.com/reports/249798
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-14T12:12:41.482Z
- **Disclosed**: 2017-07-18T16:42:30.889Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi team, 

While testing i look for session related issues but It seems that The Site is Will protected For such problems But a little Issue related to that i wanted to mention here...

When A user Sign-In to his account he can see a Little chat button on Bottom right corner of the page  (After Logging-In) And of he sends a Message to Support by this he is surely going to get reply on same location... 

Well when User logs out of his account he can't access the chat after logging-out but if he logs-in back he can again chat... 

Now if we get the user Session cookies And Logout the user from his account he can still use that session cookies to access the chat ( Only chat on the login page ) 

POC:

1) Login to your account at https://app.legalrobot.com/login
2) After that Copy the session cookies from export button on extension ( I used [Edit this cookie](http://www.editthiscookie.com/) chrome extension to get the cookies and perform the test ) I an attacker case he can use any Cookei grabber to grab the user cookies depends on attack scenario

3)  Now When u will get the cookies from the extension Logout from the account 
4) Now Load the page https://app.legalrobot.com/login again and Delete all cookies from your browser regarding the website 
5) Now add the cookies again from the Extension from import button, 
and then go to the page https://app.legalrobot.com/account
6) You will see that the page will take u back to Login page but a little difference it contains the same Chat button on the button that was not present  click on that button and You will see that all of the user chats are available their and if u send some message it will still be sent 


Fix: 

Possible fix Include to make it sure no cookies data from Last session is accessible after logout  

## Attachments
- 001.PNG
