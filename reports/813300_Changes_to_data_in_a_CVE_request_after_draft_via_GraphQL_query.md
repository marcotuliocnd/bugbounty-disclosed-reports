# Changes to data in a CVE request after draft via GraphQL query

## Report Details
- **Report ID**: 813300
- **URL**: https://hackerone.com/reports/813300
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-08T20:42:00.136Z
- **Disclosed**: 2020-05-15T17:23:49.575Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Our team has conducted a number of studies (tests) in the field of CVE Request. We found several statuses of such requests
`Awaiting Publication`, `Pending HackerOne approval`, `Cancelled` .

At the time of creating the request , we can change the data. However, we noticed that we can 't change them in other statuses. However, due to incorrect GraphQL authorization settings, we can change these requests through It. 

## Steps To Reproduce:
1) Create real program (not sandbox)
2) Go to the page for creating CVE Request
3) Creating CVE Request

4)After sending the request , we will get the status sent to `Pending HackerOne approval`. In this status, we cannot change the data
For example : our request - `https://hackerone.com/hackerone_h1p_bbp1/cve_requests/1439/edit`

{F741383}

`Z2lkOi8vaGFja2Vyb25lL0N2ZVJlcXVlc3QvMTQzOQ==` - base64_decode() - `gid://hackerone/CveRequest/1439`

To change the data we use GraphQL query via mutation:

`{"query":"mutation Update_cve_request_mutation($input_0:UpdateCveRequestInput!,$first_1:Int!) {updateCveRequest(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on CveRequest {id} fragment F1 on UpdateCveRequestPayload {cve_request {id,cve_identifier,state,latest_state_change_reason,auto_submit_on_publicly_disclosing_report,report {title,id,_id,url,created_at,disclosed_at,weakness {name,id},structured_scope {asset_identifier,id}},vulnerability_discovered_at,weakness {name,id},product,product_version,description,references,...F0}} fragment F2 on UpdateCveRequestPayload {was_successful,_errors3exXYb:errors(first:$first_1) {edges {node {field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"cve_request_id":"Z2lkOi8vaGFja2Vyb25lL0N2ZVJlcXVlc3QvMTQzOQ==","product":"JOBERT","product_version":"JOBERT","report_id":804745,"weakness_name":"Information Disclosure","description":"JOBERT","references":["JOBERT"],"vulnerability_discovered_at":"2020-03-06","auto_submit_on_publicly_disclosing_report":true,"clientMutationId":"0"},"first_1":100}}`

{F741382}


5)If the H1 command cancels it , the request will take the `canceled` status. In this status, we cannot change the data
For example : our request - `https://hackerone.com/hackerone_h1p_bbp1/cve_requests/1438/edit`

{F741381}

`Z2lkOi8vaGFja2Vyb25lL0N2ZVJlcXVlc3QvMTQzOA==` - base64_decode() - `gid://hackerone/CveRequest/1438`

To change the data we use GraphQL query via mutation:

`{"query":"mutation Update_cve_request_mutation($input_0:UpdateCveRequestInput!,$first_1:Int!) {updateCveRequest(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on CveRequest {id} fragment F1 on UpdateCveRequestPayload {cve_request {id,cve_identifier,state,latest_state_change_reason,auto_submit_on_publicly_disclosing_report,report {title,id,_id,url,created_at,disclosed_at,weakness {name,id},structured_scope {asset_identifier,id}},vulnerability_discovered_at,weakness {name,id},product,product_version,description,references,...F0}} fragment F2 on UpdateCveRequestPayload {was_successful,_errors3exXYb:errors(first:$first_1) {edges {node {field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"cve_request_id":"Z2lkOi8vaGFja2Vyb25lL0N2ZVJlcXVlc3QvMTQzOA==","product":"JOBERT","product_version":"JOBERT","report_id":804745,"weakness_name":"Information Disclosure","description":"JOBERT","references":["JOBERT"],"vulnerability_discovered_at":"2020-03-06","auto_submit_on_publicly_disclosing_report":false,"clientMutationId":"0"},"first_1":100}}`

{F741380}

We also believe that this can happen after confirmation by the H1 command , when the CVE request takes the status of `HackerOne Approved`. We can 't verify this because Jobert said that there is no way to confirm this status for the test.

There is only one way left . This will ask You to look directly in the code itself .rb file where this mutation is registered. And if you do this check, we'd like to know if we were right about this or not.

Thanks , @haxta4ok00 !

## Impact

Changes to data in a CVE request after draft

## Attachments
- 1438_CVE_after.png
- 1438_CVE_before.png
- 1439_CVE_after.png
- 1439_CVE_before.png
