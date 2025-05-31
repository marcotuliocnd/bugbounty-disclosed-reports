# Jira Credential Disclosure within Mozilla Slack

## Report Details
- **Report ID**: 2467999
- **URL**: https://hackerone.com/reports/2467999
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-04-17T17:46:50.781Z
- **Disclosed**: 2024-04-23T12:13:25.734Z

## Reporter
- **Username**: griffinf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
I was able to find Jira Admin API Keys disclosed within Mozilla's #███ Slack channel which was posted by a staff member of Mozilla.

## Steps To Reproduce:
  1.Navigate to the following file -█████
  2.Observe the exposed credentials on line 310-312 of the Python Script.
  3. Verify Groups with the following CURL request - `curl -u "██████:ATATT3xFfGF0V99l_█████████551CCC5D" -H "Content-Type: application/json" https://mozilla-hub.atlassian.net/rest/api/3/user/groups?accountId=████████`
 
4. Observe the following output which shows that the user is a Jira Administrator, Administrator and  Jira Service Desk user etc.

[{"name":"jira-servicedesk-users","groupId":"███","self":"███████:"jira-administrators","groupId":"████████","self":██████:"jira-software-users","groupId":"███","self":██████████:"jira-servicemanagement-customers-mozilla-hub","groupId":"██████████","self":███:"site-admins","groupId":"████████","self":██████:"administrators","groupId":"██████████","self":██████:"Managers","groupId":"█████","self":██████"}]

## Impact

## Summary:

Admin API credentials provide elevated privileges that can grant access to all projects, user accounts, configurations, and other sensitive data stored in Jira.

## Attachments
No attachments
