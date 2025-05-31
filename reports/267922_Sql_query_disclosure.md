# Sql query disclosure,

## Report Details
- **Report ID**: 267922
- **URL**: https://hackerone.com/reports/267922
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-13T08:43:55.666Z
- **Disclosed**: 2017-09-18T07:11:33.549Z

## Reporter
- **Username**: utkarsh1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hi,

path:- https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=merge_ready&status=needs_information&status=needs_review&status=needs_revision&status=new&status=reopened&component=- Select a component&group=component&col=id&col=summary&col=component&col=status&col=type&col=priority&col=milestone&col=severity&col=time&col=points&col=reporter&col=keywords&desc=1&order=id&report=66

I have found that "In the report parameter, i can read out what the SQL query website uses to reveal out the information from the database which is really not good for your website, Now On your website attacker may be use heavy  tools for finding other vulnerability like SQL injection by injection the malicious query in your web application, which can cause web application slow down.

Kindly hide this error.

Thank you

## Attachments
No attachments
