# CVE 2020 14179 on jira instance 

## Report Details
- **Report ID**: 1061204
- **URL**: https://hackerone.com/reports/1061204
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-17T21:01:21.809Z
- **Disclosed**: 2021-02-18T18:59:15.410Z

## Reporter
- **Username**: 0xanubiz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An remote attacker can view the custom sla fields used in the jira instance and also can use the sla fields to make a jql query. 

## Impact
Information disclosure of the custom sla fields, senstive information leakage throught he jql query parameter 

Read more about the impact here:
https://jira.atlassian.com/browse/JRASERVER-71536

## Step-by-step Reproduction Instructions

Copy the url mentioned below and paste it over the browser to see the name of the sla fields.
https://███████.mil/jira/secure/QueryComponent!Default.jspa

Use this url to check the execution of jql query.
https://███.mil/jira/secure/QueryComponent!Jql.jspa?jql=reporter=███████

## Product, Version, and Configuration (If applicable)

## Suggested Mitigation/Remediation Actions

## Impact

An attacker can make a jql query using the custom sla fields used in the web app. 
And also there are broken authentication. 
The endpoint is not califatong if the user or viewer is authenticated on not. 
https://jira.atlassian.com/browse/JRASERVER-71536

## Attachments
No attachments
