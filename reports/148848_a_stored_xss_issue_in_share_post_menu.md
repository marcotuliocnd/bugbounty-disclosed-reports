# "a stored xss issue in share post menu"

## Report Details
- **Report ID**: 148848
- **URL**: https://hackerone.com/reports/148848
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-02T10:48:07.828Z
- **Disclosed**: 2017-06-25T00:03:46.211Z

## Reporter
- **Username**: securitythinker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
good day:

when a team mate named an xss  payload:
ex: "><img src=x onerror=alert(1)>
     "><img src=x onerror=alert(1)>
that xss payload will execute when making a post then share it, to a team that has an xss payload named.  that shared as a direct message please see screenshot 

when making post here:
https://hunter22.slack.com/files/create/space

## Attachments
- attackerteamate.png
- owner0.png
- owner3.png
- owner4xsspayloadexecuted.png
- ownertest.png
- ownertest2.png
