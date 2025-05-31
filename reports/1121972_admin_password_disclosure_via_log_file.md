# admin password disclosure via log file 

## Report Details
- **Report ID**: 1121972
- **URL**: https://hackerone.com/reports/1121972
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-10T04:54:17.625Z
- **Disclosed**: 2021-12-21T09:31:56.777Z

## Reporter
- **Username**: darkdream
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi
I have log file disclose admin password  on https://www.devicelock.com/log.txt
u can see md5 password in log file ,
```
2020-03-20 08:12:15 - main - <br>Module: change password (4.1.2)<br>change_password=yes;/forum/forum_auth.php;login=admin;md5=2bca2f877b7a727861b59f4a4039d2e9
```

## Impact

this information (admin password) can lead to admin account takeover

## Attachments
No attachments
