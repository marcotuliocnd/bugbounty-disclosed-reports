# Admin can create a hidden admin account  which even the owner can not detect and remove and do administrative actions on the application.

## Report Details
- **Report ID**: 1596663
- **URL**: https://hackerone.com/reports/1596663
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-10T08:27:06.602Z
- **Disclosed**: 2022-11-14T04:34:23.023Z

## Reporter
- **Username**: 41bin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
ads.reddit.com is an ads creating and managing application for reddit. The application has the feature to invite other members to the organization and give different roles at ad management.
Testing around the role management functionalities, I have noticed that a user with the same email can get invited to the same organization multiple times if the user is assigned with different roles.
So, taking advantage of this behavior I found the admin as an attacker can create an `undetectable/hidden admin account` and do administrative actions on the organization like remove other users and invite other users. Since this malicious account information  can not be seen in the `members` section, even the `owner` of the organization can not detect and remove this malicious user from the organization.

**Steps to reproduce:**
1) Login as admin from https://ads.reddit.com/
```
I know creating an owner account and then creating an admin account with in a limited time is  little-bit painful.
You can use the following credentials to login as admin

        email :██████████
        name: ███████
        password : ██████████
```
2) Go to https://ads.reddit.com/account/███/permissions and invite a user (malicious hidden user) by giving the role as `admin`
3) login to that account (malicious hidden user) from a different browser and accept the invite. 
4) Same as the second step, go to the admin account and invite the same malicious user by giving the role as `Analyst`.
5) Now go to the malicious user account and then go to https://ads.reddit.com/accounts.
6) You will see the new invitation arrived with the `Analyst` role. Accept the invitation.
7) From this account (malicious) go to https://ads.reddit.com/account/████████/billing while intercepting  the requests using burpsuite.
8) Look at the burp history and find out the `Authorization token` used by the account and copy it. (see `copy-the-auth-token.png`)
9) Now go to the normal admin account and change the permission of this malicious account to `None`   (It removes malicious account from the organization) and refresh the page to confirm that the malicious user is removed.
10) Using burpsuite repeater, change the email and send the following request by replacing the token which you copied from the 8'th step.
```
POST /api/v2.0/accounts/█████████/invitations HTTP/2
Host: ads-api.reddit.com
Content-Length: 87
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="102"
Accept: application/json
Content-Type: application/json
Authorization: ██████
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Origin: https://ads.reddit.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ads.reddit.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

{"data":{"recipient_email":"█████████","type":"ADMIN"}}

```
11) Now you are able to invite other users to the organization even though you are not a member of that organization.

## Impact

Let me explain the `impact` with different scenarios as an example.

1)
-  The owner invites an admin to the organization and the admin who knows about this issue creates an account in this way.
- Latter, the owner decide to change the role of this admin to `analyst`  or remove this admin from the organization due to some reasons
- Now the `admin as the malicious user`, can do sensitive actions in the organization like inviting or removing other users.
- When the `owner` goes to the `members` section, he will not find the malicious account there and even he `can not remove` that malicious account from the organization.

2)
- It also happens when the owner or admin invites other users accidentally in this way.  
- It is not complicated, the vulnerability arises when a user accepts multiple invitations assigned with different roles from a single organization.

## Attachments
No attachments
