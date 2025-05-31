# tcpdump before 4.9.3 has a heap-based buffer over-read related to aoe_print in print-aoe.c and lookup_emem in addrtoname.c

## Report Details
- **Report ID**: 831353
- **URL**: https://hackerone.com/reports/831353
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-25T15:43:57.976Z
- **Disclosed**: 2021-07-23T05:14:50.320Z

## Reporter
- **Username**: dotsecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
There seems to be a heap-based buffer overread while running tcpdump on a crafted pcap file. A similar behavior is seen when tcpdump is listening on an interface and the contents of this file is relayed over the network.

Please find the detailed report on github
https://github.com/the-tcpdump-group/tcpdump/issues/645

CVE: https://nvd.nist.gov/vuln/detail/CVE-2017-16808

## Impact

Heap Over Read

## Attachments
No attachments
