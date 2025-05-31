# SSRF in graphQL query (pwapi.ex2b.com)

## Report Details
- **Report ID**: 1864188
- **URL**: https://hackerone.com/reports/1864188
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-06T20:03:33.719Z
- **Disclosed**: 2023-07-24T21:12:10.112Z

## Reporter
- **Username**: kirtixs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exness

## Vulnerability Information
## Summary:
The query for `allTicks` allows setting the parameter `source` that is used to do `GET` requests,  this can be set arbitrarily .

## Steps to Reproduce:

  1. Use a service like burp collaborator to observer incoming requests. 
  2. Replace my domain with your burp collaborator domain and execute the graphQL request.

{F2158013}
  3. Observer incoming DNS and HTTP requests.

{F2158005}{F2158006}

Please note that the `source` parameter in the graphQL request can be a full URL so that any `GET` request is possible.

{F2158024}{F2158025}



## Impact
The SSRF vulnerability can be used to potentially compromise internal services that are exposed to internal network requests. Unfortunately, HTTP responses are not returned,  but an attacker can still gather information about open ports and perform blind HTTP `GET` requests against internal services, potentially help in finding more severe vulnerabilities on internal network services.

## Mitigation
The application must only accept servers on an explicit allow list. This will mitigate SSRF attacks.

## Impact

The SSRF vulnerability can be used to potentially compromise internal services that are exposed to internal network requests. Unfortunately, HTTP responses are not returned,  but an attacker can still gather information about open ports and perform blind HTTP get-reqeusts against services that are running on these ports, potentially help in finding more severe vulnerabilities on internal network services.

## Attachments
- http.png
- dns.png
- request1.png
- admin-example-1.png
- admin-example-2.png
