# SQL exception in JSON format

## Report Details
- **Report ID**: 225098
- **URL**: https://hackerone.com/reports/225098
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-30T11:18:15.867Z
- **Disclosed**: 2020-01-31T14:12:15.122Z

## Reporter
- **Username**: clizsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi, I know this is not critical, just a design issue,
but it will be better if it will not show up to the user as an error, maybe in log files readable to the www-user or to the root user in order to debug.

PoC:
----------------------
1. Create a user and confirm the password
2. Capture the packet
3. Replay the packet with a username bigger than 64 words in length two times in order to duplicate the user.
4. Receiving error.

This is working only when the input for the username is bigger than 64 words. (65 needed.)

### Example:
***Request*** -
POST http://172.16.1.68/nextcloud/index.php/settings/users/users HTTP/1.1
DATA: username=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&password=test123A

***Response*** -
```
{"message":"An exception occurred while executing 'INSERT INTO `oc_users` ( `uid`, `password` ) VALUES( ?, ? )' with params [\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\", \"1|$2y$10$gwzH19jqn8HveRpCb2haNurF7rycqsZeYYS7b1zPENnUInUyP35J2\"]:\n\nSQLSTATE[23000]: Integrity constraint violation: 1062 Duplicate entry 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' for key 'PRIMARY'"}
```

### Example:
***Request*** -
POST http://172.16.1.68/nextcloud/index.php/settings/users/users HTTP/1.1
DATA: username=aaaaaaa&password=test123A

***Response*** -
```
{"message":"A user with that name already exists."}
```

## Attachments
No attachments
