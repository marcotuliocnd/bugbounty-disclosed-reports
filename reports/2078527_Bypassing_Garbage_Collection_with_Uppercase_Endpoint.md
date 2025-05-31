# Bypassing Garbage Collection with Uppercase Endpoint

## Report Details
- **Report ID**: 2078527
- **URL**: https://hackerone.com/reports/2078527
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-07-21T01:25:09.170Z
- **Disclosed**: 2023-10-04T10:37:25.533Z

## Reporter
- **Username**: h1xploit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
This report highlights a vulnerability in the garbage collection process, where the endpoint "/metrics" can be bypassed by using uppercase letters.
Additionally, it is important to note that if your system contains similar endpoints, they might also be susceptible to the same bypass method. This report aims to provide comprehensive information about the vulnerability and its potential impact.

##  Steps To Reproduce:
1. Make an HTTP request to the URL: https://injob.indriver.com/api/metrics
- ```curl -X GET "https://injob.indriver.com/api/metrics" -H "Content-Type: application/json"```
- Observe the response, which is expected to be "forbidden" (HTTP 403).
- {F2523755}

2.Make another HTTP request to the URL: https://injob.indriver.com/api/METRICS
- ```curl -X GET "https://injob.indriver.com/api/METRICS" -H "Content-Type: application/json"```

- Observe the response, which is expected to be "success" (HTTP 200).
- {F2523756}

## Impact

The impact of this vulnerability includes unauthorized access to sensitive information or resources, potential data manipulation, and a potential risk of further escalation in the system. Furthermore, if other endpoints with similar patterns exist in your system, they might also be vulnerable to the same bypass method, exposing the system to additional security risks.

## Attachments
- Screenshot_(39).png
- Screenshot_(40).png
