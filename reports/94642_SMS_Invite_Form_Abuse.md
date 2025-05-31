# SMS Invite Form Abuse

## Report Details
- **Report ID**: 94642
- **URL**: https://hackerone.com/reports/94642
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-10-19T16:00:48.923Z
- **Disclosed**: 2017-03-21T20:58:04.329Z

## Reporter
- **Username**: xer0dayz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: whisper

## Vulnerability Information
whisper.sh fails to protect the invite form from abuse from attackers. If a malicious individual wants to abuse this functionality, they could send repeated/automated requests to the same phone number or range of phone numbers that do no actually belong to himself. This would result in lots of arbitrary SMS messages to a single user or large range of multiple users just by launching automated POST requests to wispher.sh.

POST /invite HTTP/1.1
Host: whisper.sh
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://whisper.sh/search?q=INJECTX
Content-Length: 24
Cookie: _ga=GA1.2.1840275725.1445267554; _cb_ls=1; _chartbeat2=DTMT5SBzHnwjDQlfSX.1445267560697.1445267560697.1; _gat=1
Connection: close
Pragma: no-cache
Cache-Control: no-cache

phoneNumber=518-373-1319


HTTP/1.1 200 OK
Date: Mon, 19 Oct 2015 15:51:43 GMT
Content-Type: text/plain; charset=utf-8
cache-control: max-age=0, private, must-revalidate
x-request-id: psJRqmJtkxpeW59Ms3en
X-Varnish: 111290474
Age: 0
Via: 1.1 varnish-v4
Connection: close
Accept-Ranges: bytes
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000;
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Length: 24

Invite sent successfully



To help prevent automated attacks, the form should utilize some form of captcha system that requires user knowledge in order to send repeat attempts and should block repeat requests to the same number multiple times. 

## Attachments
- Whisper_Form_Abuse.png
