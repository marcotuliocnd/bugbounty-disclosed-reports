# [scores.ubnt.com] DOM based XSS at form.html

## Report Details
- **Report ID**: 158484
- **URL**: https://hackerone.com/reports/158484
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T14:53:50.729Z
- **Disclosed**: 2017-02-24T11:33:20.888Z

## Reporter
- **Username**: s_p_q_r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hello,

I would like to report that the #130889 bug hasn't been fixed completely.

The removeTags function has been added, however an attacker is still able to inject Javascript as parameter values without any HTML tags:

> https://scores.ubnt.com/form.html?uid=1&p=%27%20onmouseover=alert(document.domain)//

The script is triggered by the onmouseover event on the header.

Tested with latest Firefox and Chrome.

## Attachments
No attachments
