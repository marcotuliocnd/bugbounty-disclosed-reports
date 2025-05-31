# Missing server side controls when editing the board’s sharing permissions per user

## Report Details
- **Report ID**: 827816
- **URL**: https://hackerone.com/reports/827816
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-24T11:17:34.706Z
- **Disclosed**: 2020-09-28T11:26:54.168Z

## Reporter
- **Username**: warsocks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Author: Silvia Väli, Clarified Security (https://www.clarifiedsecurity.com/silvia-vali/)
Date: 24th of March, 2020

**Description**:
When the regular user is visiting the Deck view, all created boards are displayed along with the ones that are shared with the user by others. Available functionality within each of the shared boards depends whether the user has received share, manage, edit permissions. 

Since the access control rules related to user’s permissions have only been applied on the client side and not on the server side, user can specify share/edit/manage permissions to be always true within the response (for example by using a proxy tool) when viewing board information. This way he can gain control over the board so he/she could apply the missing edit/manage permissions to him/herself directly from the UI.

**Version information**:
Nextcloud 18.0.2
Deck 0.8.0 enabled

**Pre-requisites as an admin user to follow the vulnerable path**:
- create 2 regular users in the next cloud, for example user silvia and user john. Users do not belong to the admin group.
- Install the Deck app (installed version 0.8.0)

**To reproduce the vulnerable path**:

**User: silvia**

1. Authenticate as user silvia and select Deck from the menu
2. Create new board -> name it (“board for testing”)
3.  Add a new stack (“test test”)
4. Click on “Show board for details”
5. Add the other user john and only give him Share permission. Uncheck Edit and Manage.

**User: john**

6. Now authenticate in the application as john -> click Deck from the menu and open the shared board “board for testing”. Since the board was only Shared and no edit permissions were granted, john cannot do much on the board. 
7. What john can do however is use a proxy tool such as Burp Suite to modify the response body. When john clicks on the Deck from the menu, following request is made:
```
GET /apps/deck/boards HTTP/1.1
Host: next.yy.ee
...
Connection: close
Cookie: …
```

8. In the response to that request, you can see that john only been given the permission to share which only allows to read the data and not modify it.
```
[{"title":"board for testing",
"owner":{"primaryKey":"silvia","uid":"silvia","displayname":"silvia"},"color":"0082c9","archived":false,"labels":[],"acl":[{"participant":{"primaryKey":"john","uid":"john","displayname":"john"},"type":0,"boardId":7,"permissionEdit":false,"permissionShare":true,"permissionManage":false,"owner":false,"id":4}],"permissions":{"PERMISSION_READ":true,"PERMISSION_EDIT":false,"PERMISSION_MANAGE":false,"PERMISSION_SHARE":true},"users":[],"shared":1,"stacks":[],"deletedAt":0,"lastModified":1585045324,"id":7}]
```

9.  john however uses a proxy tool such as Burp Suite and applies via proxy -> options -> Match and replace that every time the following line with permissions is seen modify all the options to be equal to true.
Original: `"permissionEdit":false,"permissionShare":true,"permissionManage":false,"owner":false`
Modified: `"permissionEdit":true,"permissionShare":true,"permissionManage":true,"owner":true`

10. If john now refreshes the Deck page and opens the board “board for testing” -> Show board details -> Sharing -> he can add himself the permissions to Edit, Share, Manage to take over the board which was initially only shared with him.

## Impact

Attacker would achieve control over the board and its data/attachment uploads etc.

## Attachments
- Report_SILVIA_V_LI_24.03.2020.pdf
