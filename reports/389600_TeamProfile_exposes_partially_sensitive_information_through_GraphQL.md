# TeamProfile exposes partially sensitive information through GraphQL

## Report Details
- **Report ID**: 389600
- **URL**: https://hackerone.com/reports/389600
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-02T12:13:33.345Z
- **Disclosed**: 2018-08-08T23:43:03.326Z

## Reporter
- **Username**: 0619
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
I noticed there is new field `team_profile` added and using the graphql below the latest serious report and reports received in three months were exposed
`{"query":"query Dashboard_report_severity_breakdown_table($first_0:Int!) {\n  query {\n    id,\n    ...F0\n  }\n}\nfragment F0 on Query {\n  _team4g1Zqs:team(handle:\"security\") {\n    _structured_scopes3TsuIg:structured_scopes(first:$first_0) {\n      edges {\n        node {\n          _id,\n          asset_identifier,\n          reports {\n            total_count,\n            count_by_severity\n          },\n          id\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    _reports42Gng6:reports(without_scope:true) {\n      total_count,\n      count_by_severity\n    },\n team_profile{_id,disclosed_reports_in_last_year_count,latest_report_created_at,latest_serious_report_created_at,reports_received_in_three_months_count},  _id, id\n  },\n  id\n}","variables":{"first_0":100}}`

If this is public information i can close this by myself (my reputation is very low) but i think it's not and worth to report it

## Impact

Information disclosure of no of reports received in 3 months time and other information not in the current UI

## Attachments
No attachments
