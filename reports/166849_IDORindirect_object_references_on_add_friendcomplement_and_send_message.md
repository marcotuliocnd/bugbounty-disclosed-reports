# IDOR(indirect object references) on add friend,complement and send message 

## Report Details
- **Report ID**: 166849
- **URL**: https://hackerone.com/reports/166849
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-08T14:14:07.347Z
- **Disclosed**: 2017-11-09T20:15:26.577Z

## Reporter
- **Username**: w3b7ricks73r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hi security ,

Description:
I found user id in encrypted form from there profile url 
https://www.yelp.com/user_details?userid=<user id's>

on intercepting request of add friend, complement and send message i can identify user id ..
when i change identified user ID to other user's ID then request of add friend is send to other user without any token and secession validation .. scenario for the complement and send message is same.

Impact:
->an attacker can add the authenticated user to his account or any others accounts ..
->can send message to any one by user's account 
->can complement on other users by victim user 

More information about this issue is available here:

https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References
https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)

Reproduction Steps:- for add friend 
1.>login to your test account 
2.>visit any two user's profile 
3.>click on add friend on user one 
4.>intercepting request 
5.>identify user id and change it to second user's id on each request 
6.>click on send
7.>intercept request and change user id 
8.>check the screen with the message od request is send to second user 
(request is send to another user)

Reproduction Steps:- for complement
1.>login to your test account 
2.>visit any two user's profile 
3.>click on complement of user one
4.>intercepting request 
5.>identify user id and change it to other user's id on each request 
6.>type the complement
7.>intercept request and change user id 
8.>check the screen with message that complement is send to second user
(complement is send to second user)

Reproduction Steps:- for send message 
1.>login to your test account 
2.>visit any two user's profile 
3.>click on send message of user one 
4.>intercepting request 
5.>identify user id and change it to other user's id on each request 
6.>type the message 
7.>intercept request and change user id 
8.>check the screen with message that complement is send to second user
(message is send to second user)

Please Find the video POC from the links

https://mega.nz/#!FR5CxSrD!wxqSN9BomoznTwDATDc-DiiAHsFj80W7VqNPklO4FYs

https://mega.nz/#!UQBBWY7C!85q0Nn9F9icsf_KXfuis_YNJVc7tIp6ebr4Javi6Za0


Regards 
Aaysha Khilji




    

## Attachments
No attachments
