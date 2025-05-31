# AWS Credentials Disclosure at ███ 

## Report Details
- **Report ID**: 1704035
- **URL**: https://hackerone.com/reports/1704035
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-19T01:22:21.395Z
- **Disclosed**: 2023-02-24T18:43:57.957Z

## Reporter
- **Username**: 0r10nh4ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team!!
I found the config.json file, which contains sensitive information of AWS.

POC:
https://███████/config.json
```
{"aws": {
        "accessKeyID": "███████",
        "secretAccessKey": "██████████",
        "region": "███",
        "bucket": "██████",
        "endpoint": "https://s3.amazonaws.com"
    },
    "serverSettings": {
        "port": 443,
        "timeout": 18000000
    },
    "█████████": {
        "authorizationURL": "https://████/ms_oauth/oauth2/endpoints/oauthservice/authorize",
        "tokenURL": "https://████/ms_oauth/oauth2/endpoints/oauthservice/tokens",
        "clientID": "██████████",
        "clientSecret": "█████",
        "callbackURL": "https://████████/callback",
        "userProfileURL": "https://███/ms_oauth/resources/userprofile/me"
    }
}
```

## Impact

By using leaked AWS credentials or abusing credentials with misconfigured permissions, an attacker could try to gain access to sensitive information on the AWS account or perform arbitrary modification on the AWS resources.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Use a browser to navigate to: https://██████/config.json

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
