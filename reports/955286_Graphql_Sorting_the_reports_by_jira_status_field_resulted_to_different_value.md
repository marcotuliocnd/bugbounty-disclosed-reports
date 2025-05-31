# Graphql: Sorting the reports by jira_status field resulted to different value

## Report Details
- **Report ID**: 955286
- **URL**: https://hackerone.com/reports/955286
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-10T23:02:01.524Z
- **Disclosed**: 2020-08-27T08:27:50.228Z

## Reporter
- **Username**: 0619
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Sorting the reports by jira_status yield to different result depicting the team is using jira even the user has no access.
**Description:**
A user with no access to jira information of any reports can somehow access the jira field using order_by through `jira_status`
Using the 2 graphql below we can see the discrepancies of `total_count` for the test teams i will mention:

__Test Teams:__
1.  █████████
order_by:field:`id` = `total_count: 10`
 order_by field:`jira_status`= `total_count :11`
2.  ██████████ : 
order_by:field:`id` = `total_count: 458`
 order_by field:`jira_status`= `total_count :466`
3.  ████
order_by:field:`id` = `total_count: 299`
 order_by field:`jira_status`= `total_count :309`
4. ███
order_by:field:`id` = `total_count: 109`
order_by field:`jira_status`= `total_count :110`


Graphql Query using field `id` in`order_by` as criteria it will yield same result except for the field of `jira_status`
```
{
  reports(where: {team: {handle: {_eq: "██████"}}}, order_by: {direction: ASC, field: id}) {
    total_count
    nodes {
      substate
      jira_escalation_state
      jira_escalation_last_state_change_at
      created_at
      disclosed_at
      extracted_report_data {
        hosts
      }
      title
      url
      team {
        handle
      }
      reporter {
        username
      }
    }
  }
}
 ```
Please change the field in `sort_by` to` jira_status` to display different result.

Below is part of the response using jira_status as the field, please notice that `jira_escalation_state`and `jira_escalation_last_state_change_at` has null values meaning a ==public user don;t have access to this information.==
{
  "data": {
    "reports": {
    =="total_count": 11, ==
      "nodes": [
        {
          "substate": "resolved",
          "jira_escalation_state": null,
          "jira_escalation_last_state_change_at": null,
          "created_at": "2019-09-18T11:57:36.488Z",
          "disclosed_at": "2020-04-21T02:53:04.699Z",
          "extracted_report_data": null,
          "title": "███",
          "url": "███",
          "team": {
            "handle": "████████"
          },
          "reporter": {
            "username": "█████"
          }
        },

Additional information: I dig more on the discrepancies and checked the returned reports 1 by 1 to  and compare result, in Team ███████, the report ███████ appeared twice because of the sort_by jira_status.


Thank you.
Ariel

## Impact

Due to improper access control in the `sort_by` of `jira_status` field any user can give an idea which report are using jira even if the user has no access jira information.

## Attachments
No attachments
