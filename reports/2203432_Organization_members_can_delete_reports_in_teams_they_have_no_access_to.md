# Organization members can delete reports in teams they have no access to

## Report Details
- **Report ID**: 2203432
- **URL**: https://hackerone.com/reports/2203432
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-12T08:33:45.539Z
- **Disclosed**: 2023-11-22T11:46:38.432Z

## Reporter
- **Username**: kimingi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello team, 
While testing the analytics reports functionality for an organization, I realized that organization members can delete reports created for a team they have no access to.

If an organization has 2 teams and a member has access to both teams, when they view the reports page, they can see the reports created for both teams. But, if the member access is restricted to a single team, then they can only see the reports generated for that team, the reports for the other team are not displayed to the restricted member. 
However, the team member can delete these reports by using the ```DeleteAnalyticsReport``` and replacing the analytics report id.
I tried to edit the same report from the restricted team but it gives an error. 

The same control should also be applied in the delete report query.

### Steps To Reproduce

1. Using  a team member with access to 2 teams in your demo, navigate to https://hackerone.com/organizations/your_demo/analytics/reports
2. Create a report for one of your teams by specifying the filters. (I have 2 teams comb26_h1b and comb26_h1r, I created a report for comb26_h1r). copy the id for that report

{F2767458}{F2767459}
3. Remove access for that user from the team they have created the report.  (I removed all access to the comb26_h1r team and also removed the admin role)

{F2767464}
4. Go back to the reports section and notice that the report they created is not shown since they do not have access to that team.
5. Replace the id of the report you created in step 2 in the GraphQL request below:
```
{"operationName":"DeleteAnalyticsReport","variables":{"reportIds":[644],"product_area":"other","product_feature":"other"},"query":"mutation DeleteAnalyticsReport($reportIds: [Int!]!) {\n  deleteAnalyticsReport(input: {analytics_report_ids: $reportIds}) {\n    errors {\n      edges {\n        node {\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
6. Notice that the report is successfully deleted.

██████████

## Impact

Users without access to a team can delete reports in the restricted team

## Attachments
- bandicam_2023-10-12_11-17-43-204.jpg
- bandicam_2023-10-12_11-20-00-048.jpg
- bandicam_2023-10-12_11-32-51-461.jpg
