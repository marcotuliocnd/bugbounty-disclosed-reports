# A user can bypass approval step in Hacker Publishing feature, allowing them to publish reports immediately

## Report Details
- **Report ID**: 452959
- **URL**: https://hackerone.com/reports/452959
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-30T04:06:36.539Z
- **Disclosed**: 2018-12-05T04:55:40.392Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team
**Description:**
Hacker can request agree-on-going-public publish report
### Steps To Reproduce

1. Create publish report
2. 

https://hackerone.com/reports/bulk
POST
message=&reference=&add_reporter_to_original=false&reply_action=agree-on-going-public&reports_count=1&report_ids%5B%5D=██████████&bounty_currency=USD

███

## Impact

Hacker can request agree-on-going-public publish report
Hacker bypasses the check by the moderator

## Attachments
No attachments
