# [ Spot Check ] Team members can edit a user's write-up

## Report Details
- **Report ID**: 2530242
- **URL**: https://hackerone.com/reports/2530242
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-01T13:55:01.946Z
- **Disclosed**: 2024-06-06T09:47:02.993Z

## Reporter
- **Username**: youstin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
This report was created as part of the investigation for the Spot Check about the Spot Checks feature.

Hi,

I discovered team members / hackerone staff can modify a user's spot check write-up. I believe this is not intended functionality for the following reasons:
1. There is no option to edit the hacker's write-up in the UI.
2. HackerOne previously fixed vulnerabilities where the team member / triager could edit a user's report.  ( #2061367, #2096271 )

### Steps to reproduce:

1. Submit a spot check write-up. 
2. Edit the write-up and intercept the GraphQL request. It should look like this:

```json
{"operationName":"EditSpotCheckReport","variables":{"input":{"spot_check_report_id":"Z2lkOi8vaGFja2Vyb25lL1Nwb3RDaGVja1JlcG9ydC81MDU=","executive_summary":"x","scope":"x","methodology_and_tooling":"X","findings_and_evidence":"none","time_spent":0,"files":[],"removed_attachment_ids":[],"report_ids":[]},"product_area":"hacker_dashboard","product_feature":"redirect_overview"},"query":"mutation EditSpotCheckReport($input: EditSpotCheckReportInput!) {\n  editSpotCheckReport(input: $input) {\n    spot_check_report {\n      id\n      _id\n      state\n      __typename\n    }\n    was_successful\n    errors {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```

3. Log in the organization account. Copy the graphQL request above and send it. You can modify parts of the body and you should see the write-up has been modified.

{F3318885}
{F3318886}

## Impact

Members and Triage can rewrite the story the hacker is trying to tell and edits are not transparant
- Give hackers a bad image in disclosed reports
- Tell a different story or lower impact artificially

## Attachments
- Screenshot_2024-06-01_at_16.52.33.png
- Screenshot_2024-06-01_at_16.51.32.png
