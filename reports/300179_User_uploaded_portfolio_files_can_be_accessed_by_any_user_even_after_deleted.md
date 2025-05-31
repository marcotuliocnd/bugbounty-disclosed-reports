# User uploaded portfolio files can be accessed by any user even after deleted

## Report Details
- **Report ID**: 300179
- **URL**: https://hackerone.com/reports/300179
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-23T08:01:43.798Z
- **Disclosed**: 2019-02-27T23:40:35.604Z

## Reporter
- **Username**: tolo7010
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mavenlink

## Vulnerability Information
Reproduction:
=========

1. Login as a user, e.g: user1
2. Create a portfolio by going to https://app.mavenlink.com/users/1234567-user1/work_samples/new
note: replace 1234567-user1 with the actual user id/name endpoint.
3. Uploading any file to the new portfolio and click save. On the right side of profile info, you will see the created portfolio with attached file,
4. Click on the file, notic the link is https://app.mavenlink.com/attachments/xxxxxxxx Where xxxxxxxx is the file ID in 8 number lenght.
5. Copy the file link and open it in other browser with different login user, e.g: user2, you will see the file is accessible.
6. On user1, delete the file/portfolio.
7. The link is still accessible,

This is my uploaded portfolio file: https://app.mavenlink.com/attachments/79279255 (I've delete all the portfolio on the web interface),

Recommend fix:
- Provide mechanism to check if the uploaded file link is associated with coresponding account.
- Delete the uploaded file (in AWS?) with portfolio as user desired.

## Impact

As user profile and portfolio (with files) can only seen if the user is in the same team/group, otherwise the information should be private, as going throgh any profile link (https://app.mavenlink.com/profiles/[user-id]) getting "Private Profile" message

## Attachments
No attachments
