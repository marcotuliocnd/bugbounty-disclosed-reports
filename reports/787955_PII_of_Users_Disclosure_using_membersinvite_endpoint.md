# PII of Users Disclosure using "/members/invite/" endpoint

## Report Details
- **Report ID**: 787955
- **URL**: https://hackerone.com/reports/787955
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-03T03:58:18.179Z
- **Disclosed**: 2020-04-13T13:11:44.714Z

## Reporter
- **Username**: bonikia97
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
Hello!

I found PII Disclosue at https://connect.topcoder.com/projects/

#Steps to Reproduce.

1) Go to https://connect.topcoder.com/projects
2) Select an existing project, or create a new one.
3) Select the "Manage Invitations" option. (on the left sidebar).
4) Enter the Username/Email of the user you want to add.
5) Intercept two Request (GET & POST) with BurpSuite, and send this to Repeater.
6) With Requests: 

6.1)With GET Request: See that it is similar to a query in the database, you can manipulate them to get more information. Use this to get the ID of any user.

6.2)With POST Request: Put any userIds, and send the Request.

7) Look the Response, the email and more information of users can be seen.
 
Regards!

PoC: 
1) "PII Email TopCoder" Video.
2)  Image called "Manipulated Email Request",  In which you will see the manipulated request to get all users with email-domain "@wearehackerone.com".
(With this you could obtain the IDs of any user and any email domain by following the steps of the PoC in video.)


Regards!

## Impact

If the attacker wanted, he could see the information of the Admins, or any Member of TopCoder. It could collect internal information from the company and continue to feed its attack vectors.
If you check other endpoints, nowhere is the user's email shown.

## Attachments
- PII_Email_TopCoder.mkv
- Manipulated_Email_Request.jpg
