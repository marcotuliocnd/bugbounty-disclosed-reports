# Resource Injection - [████████]

## Report Details
- **Report ID**: 2297561
- **URL**: https://hackerone.com/reports/2297561
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-27T01:42:48.740Z
- **Disclosed**: 2024-03-22T17:38:24.212Z

## Reporter
- **Username**: geej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Swagger UI before 4.1.3 could allow a remote attacker to conduct spoofing attacks. By persuading a victim to open a crafted URL, an attacker could exploit this vulnerability to display remote OpenAPI definitions.

Affected host: `██████████`

████

## Impact

A threat actor can abuse the domain through phishing by injecting the crafted payload to the vulnerable host. The attacker may send out phishing emails or messages containing links, tricking unsuspecting users into providing sensitive information such as login credentials, credit card details, or personal data.

It was possible for an attacker to craft a URL that could introduce a payload to be run in the application context. Opens a vector for phishing attacks by abusing the trusted names/domains of self-hosted instances.

## System Host(s)
████████

## Steps to Reproduce

Navigate to the endpoint that hosts the Swagger UI, and insert the payload through “?configUrl=” GET parameters as following:

```
█████?configUrl=█████████
```

## Suggested Mitigation/Remediation Actions
Disable the feature of external import of definition files through
Keep Swagger UI to its latest version



## Attachments
No attachments
