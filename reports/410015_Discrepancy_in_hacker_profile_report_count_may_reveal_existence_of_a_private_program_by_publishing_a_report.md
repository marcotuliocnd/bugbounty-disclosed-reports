# Discrepancy in hacker profile report count may reveal existence of a private program by publishing a report

## Report Details
- **Report ID**: 410015
- **URL**: https://hackerone.com/reports/410015
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-15T06:49:14.116Z
- **Disclosed**: 2019-04-24T18:22:00.544Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi team , @pei, @jobert , @bencode

**Summary:**
Again

We have publish report page
https://hackerone.com/hacktivity/publish

But we have bypass query #401476 this

***description***
The profile page counts the number of created your reports. But it does not consider the reports that are created in the sandbox. Thus, after creating the report, we can find out whether the external program is a private program or a sandbox.



### Steps To Reproduce

1. Use query in report #401476
2. {"query":"mutation Create_external_report_mutation($input_0:CreateExternalReportInput!,$types_1:[ErrorTypeEnum]!) {\\n createExternalReport(input:$input_0) {\\n clientMutationId,\\n ...F1,\\n ...F2\\n }\\n}\\nfragment F0 on Team {\\n id\\n}\\nfragment F1 on CreateExternalReportPayload {\\n team {\\n id,\\n ...F0\\n }\\n}\\nfragment F2 on CreateExternalReportPayload {\\n was_successful,\\n new_report {\\n node {\\n _id,\\n disclosed_at,\\n id\\n },\\n cursor\\n },\\n _errors2S3JlH:errors(types:$types_1) {\\n edges {\\n node {\\n type,\\n field,\\n message,\\n id\\n },\\n cursor\\n },\\n pageInfo {\\n hasNextPage,\\n hasPreviousPage\\n }\\n }\\n}","variables":{"input_0":{"handle":"`***any_external_handle***`","title":"afterDisabledButtonPublish","vulnerability_information":"tset","hacker_summary":"test","reported_date":"2018-08-25T04:29:37.081Z","resolved_date":"2018-08-25T04:29:37.081Z","attachment_ids":[336812],"clientMutationId":"0"},"types_1":"ARGUMENT"}}
3. Next go to your page 

For example my
https://hackerone.com/haxta4ok00

`129
Bugs found`
F346555

4. Go to try use query and write handle - ██████████
F346562
5. Go to profile and check "Bugs found" - `130`
F346556
6. Go to try use query @cisco and @apache
F346559
F346560
7. Go to profile and check "Bugs found" -130
F346557
8. Go to try write █████████
F346561
9. Check "Bugs found" -`131`
F346558

██████ , ███████ have private page.

If after creating a report, this will be credited to your profile. So this program has a private page

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

disclosure of external programs with private

## Attachments
- 129.png
- 130.png
- 130After.png
- 131.png
- apache.png
- cisco.png
