# Access control missing while viewing the attachments in the "All boards"

## Report Details
- **Report ID**: 916704
- **URL**: https://hackerone.com/reports/916704
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-06T13:35:40.906Z
- **Disclosed**: 2020-09-29T12:38:59.226Z

## Reporter
- **Username**: dpx01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The vulnerability lies in the "view attachment" of the tasks . When a user uploads the file to the Task, the attachment is given a numeric number and is increased +1 on further uploads. It is easy for any user to view and download all the files uploaded to the tasks by any user. The access is not controlled with the session or csrf token.

Steps to Reproduce:
1. Connect to the server login with user A and visit the webpage. I used the provider "us.cloudamo.com"
2. Visit https://us.cloudamo.com/apps/deck and create a task.
3. Upload any file to the attachments and capture the request. The request will looks like "https://us.cloudamo.com/apps/deck/cards/8420/attachment/30" where 30 is the ID of the uploaded attachment. 
4. Login with  user B and access the URL and you should be able to view the attachment of user A.
5. Since the attachment IDs are numerical number with poor entropy can be easily brute-forced and  one can get all the uploaded attachments by all the users of the particular  provider.

## Impact

Unauthorized user can view and download the files of other users. This may leak the sensitive information of users.

## Attachments
- IDOR_01.png
- IDOR_02.png
