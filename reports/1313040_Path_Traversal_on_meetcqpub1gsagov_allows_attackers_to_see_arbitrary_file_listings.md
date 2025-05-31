# Path Traversal on meetcqpub1.gsa.gov allows attackers to see arbitrary file listings.

## Report Details
- **Report ID**: 1313040
- **URL**: https://hackerone.com/reports/1313040
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-20T09:29:43.811Z
- **Disclosed**: 2021-10-02T17:52:52.843Z

## Reporter
- **Username**: 0x0luke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:
Path Traversal on meetcqpub1.gsa.gov allows attackers to see arbitrary file listings from a directory of their choice.

I wasn't sure if this page was in scope of this program or the TTS program, hopefully this isn't a problem

## Steps To Reproduce:

  1. Navigate to the following URL - https://meetcqpub1.gsa.gov/bin/querybuilder.json.css?path=/home&p.hits=full&p.limit=-1
  2. The path parameter can be manipulated to show other directories on the system as well, for example /etc.

## Impact

An attacker is able to see files and directories present on the system, breaking the confidentiality section of the CIA Triad.

## Attachments
No attachments
