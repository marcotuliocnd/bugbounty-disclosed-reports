# Stored XSS on imgur profile

## Report Details
- **Report ID**: 484434
- **URL**: https://hackerone.com/reports/484434
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-23T06:16:47.088Z
- **Disclosed**: 2019-03-02T01:45:04.495Z

## Reporter
- **Username**: giddsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hello, I submitted a report on imgur, but the staff marked it as duplicate. #482841 I reviewed the report of the first submitted report. #381553 We are on the same situation and his case is already fixed because I tried visiting his site too which is https://12test.imgur.com/ and even redoing his steps to reproduce but no XSS is triggered. And I have a different bypass and my bypass succeed. I can still fire up XSS on the said webpage.

Sorry for double posting, but I think his case #381553 is already fixed and mine is different.

There are still bypasses exists in the imgur create album that can cause an Stored XSS. 
Try to visit my site: https://gidsumaya.imgur.com/ and XSS will trigger. F410962:

In my case, I bypassed the filtering using HTML entities for the alternation of <>, because I noticed that it's filtering the <>.
##Payload:
**”/>&_lt;_script>alert(1)&_lt;/scr_ipt&gt”/>** remove the underscores.

And I can still fire up XSS and anyone who visits the link, the XSS will trigger.

I acknowledge that there was another report, for the same issue but that I still have a way to bypass whatever fix they implemented.

## Impact

XSS can use to steal cookies, password or to run arbitrary code on victim's browser

## Attachments
- poc.PNG
