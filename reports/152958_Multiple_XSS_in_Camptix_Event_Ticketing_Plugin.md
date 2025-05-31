# Multiple XSS in Camptix Event Ticketing Plugin

## Report Details
- **Report ID**: 152958
- **URL**: https://hackerone.com/reports/152958
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-21T17:28:05.212Z
- **Disclosed**: 2016-08-18T16:39:13.846Z

## Reporter
- **Username**: thezawad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi,
As discussed in #151561 submitting the report here.

I have got some more bugs in Camptix Event Ticketing plugin.

Well, the first one is a ticket page xss caused by the **Ticket Title**
And the second one is kind of self-xss, caused by also the **Ticket title** of the plugin but in the coupons page.
I have added a video *PoC* for your clarification with step by step reproduction.
As I have seen in #9391 you've fixed self-xss, I have created this report.

I think both of the bugs should be fixed.

I expect you fix both of them.


https://drive.google.com/open?id=0B0Ah8VhxGMynZXUwbGlaMm5iVDQ


--------
Zawad


## Attachments
No attachments
