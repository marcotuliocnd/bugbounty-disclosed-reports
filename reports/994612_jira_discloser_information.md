# jira discloser information 

## Report Details
- **Report ID**: 994612
- **URL**: https://hackerone.com/reports/994612
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-30T04:30:22.399Z
- **Disclosed**: 2022-10-03T13:03:54.800Z

## Reporter
- **Username**: isumitpatel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
The ticket raising system used by informatica suffers from an informational vulnerability where in an attacker can view certain details about open bugs or project information of informatica. Details include  names and potentially  and ticket names which an unauthorized personnel can view without login that can be very useful to an attacker.

endpoints:

https://infajira.informatica.com/secure/QueryComponent!Default.jspa

## Impact

attacker miss use this information

## Attachments
No attachments
