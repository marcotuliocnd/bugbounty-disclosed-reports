# Several protocol parsers in before 4.9.2 could cause a buffer overflow in util-print.c:bittok2str_internal()

## Report Details
- **Report ID**: 800324
- **URL**: https://hackerone.com/reports/800324
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-20T06:27:05.183Z
- **Disclosed**: 2021-08-22T03:50:13.318Z

## Reporter
- **Username**: bags
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Length of a local buffer used to parse network packets was not validated against actual payload size leading to a classic buffer overflow.

P.S. I was not aware of this bounty program at the time of reporting. Is this report in scope? I have a few more reports that were originally sent to the tcpdump security mailing list, I could file a report for each of them here if that qualifies. I may have also helped fix some issues in 4.9.3 as well.

## Impact

I believe remote DoS is possible. Remote code execution remains a possibility but I have not checked this myself.

## Attachments
No attachments
