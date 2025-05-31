# Repeated mediation requests and multiple emails possible on a report.

## Report Details
- **Report ID**: 156948
- **URL**: https://hackerone.com/reports/156948
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-05T19:23:10.331Z
- **Disclosed**: 2019-04-11T01:39:49.105Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

1) We can by pass used buttom Confirm on Request Mediation from HackerOne where is disable him

POC:
Edit html and delete disabled=""
<input type="submit" data-reactid=".8.0.1.0.6.1" disabled="" class="button button--success button--modal pull-right" value="Confirm">

<input type="submit" data-reactid=".8.0.1.0.6.1"  class="button button--success button--modal pull-right" value="Confirm">

And buttom in active.

2) Next catch request
https://hackerone.com/reports/nubmerreport/hacker_help
POST:
message=&mediation_type=resolution

If parametr message null , we can send multiple requests.  And spamming support
But if message is no null we have 404

PS Yes you page is write
Spamming other users with automated HackerOne emails or notifications (e.g. abusing the forgot password form).
But this problem is multiple requests.

thx,, sorry bad eng.

## Attachments
No attachments
