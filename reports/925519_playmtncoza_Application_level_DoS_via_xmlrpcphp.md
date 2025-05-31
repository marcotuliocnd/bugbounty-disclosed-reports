# [play.mtn.co.za] Application level DoS via xmlrpc.php

## Report Details
- **Report ID**: 925519
- **URL**: https://hackerone.com/reports/925519
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-16T16:29:27.794Z
- **Disclosed**: 2021-09-10T16:21:26.230Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
**Description**
Wordpress that have xmlrpc.php enabled for pingbacks, trackbacks, etc. can be made as a part of a huge botnet causing a major DOS/SSRF. The website ``play.mtn.co.za`` has the ``xmlrpc.php`` file enabled and could thus be potentially used for such an attack against other victim hosts. hackerone refferals #761722

###Steps To Reproduce:
Open vulnerability URL ``play.mtn.co.za/xmlrpc.php/``
Chage request ``GET`` to ``POST`` 
Paste'a payloads-vulnerabilities , and check in responsive header

**Request**
```
POST /xmlrpc.php HTTP/1.1
Host: play.mtn.co.za
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 91

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>
```

## Impact

If the XMLRPC.php file is not being used, it should be disabled and removed completely to avoid any potential risks. Otherwise, it should at the very least be blocked from external access.

## Attachments
No attachments
