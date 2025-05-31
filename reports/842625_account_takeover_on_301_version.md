# account takeover on 3.0.1 version

## Report Details
- **Report ID**: 842625
- **URL**: https://hackerone.com/reports/842625
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-07T15:36:39.138Z
- **Disclosed**: 2020-06-14T15:22:44.184Z

## Reporter
- **Username**: elfiman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
I find user reset password hash info and other security info on "/api/v1/[users.info](http://users.info)"  
note : I login on rocketchat with ldap account (my role : user)  
note: in request "[https://target/api/v1/users.info?username=[x]](https://target/api/v1/users.info?username=%5Bx%5D)" you should change usrname to userId

1- please login with user ldap account (role user)  
2- send a request to&nbsp;[https://target/api/v1/users.list](https://target/api/v1/users.list)&nbsp;and copy \_id value  
3- send a request to&nbsp;[https://target/api/v1/users.info?userId=[userId]](https://target/api/v1/users.info?userId=%5BuserId%5D)&nbsp;and copy email value (in response you can see important security information )  
4- logout and click "forget your password" link on&nbsp;[https://target/home](https://target/home)&nbsp;and send an email to above email address that you copied  
4- login with Your account and send a request to&nbsp;[https://target/api/v1/users.list](https://target/api/v1/users.list)&nbsp;and search the same email in response and copy \_id value  
5- send a request to&nbsp;[https://target/api/v1/users.info?userId=[userId]](https://target/api/v1/users.info?userId=%5BuserId%5D)&nbsp;and copy reset hash value  
6- logout your account and send a request to&nbsp;[https://target/reset-password/[reset\_hash]](https://target/reset-password/%5Breset_hash%5D)  
7- set new password  
8- login and enjoy

## Impact

account takeover

## Attachments
No attachments
