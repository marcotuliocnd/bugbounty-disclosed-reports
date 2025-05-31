# Web Cache Poisoning leading to DoS

## Report Details
- **Report ID**: 1346618
- **URL**: https://hackerone.com/reports/1346618
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-21T15:28:14.036Z
- **Disclosed**: 2021-11-08T04:06:31.854Z

## Reporter
- **Username**: letm3through
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
## Summary:
`acquisition-uat.gsa.gov` is vulnerable to web cache poisoning that can lead to Denial of Service (DoS) in the application.

## Steps To Reproduce:
1. Visit https://acquisition-uat.gsa.gov/?letme=4449 to make sure the service is available.
*Note: `letme=4449` is used as cache buster as we do not want to poison the application without parameter.*
2. Poison the link using `curl` command
```
curl https://acquisition-uat.gsa.gov/\?letme\=4447 -H "Host: acquisition-uat.gsa.gov:8888"
```
3. Visit https://acquisition-uat.gsa.gov/?letme=4449 to verify that application is in the state of DoS as it attempts to make plenty of requests to `acquisition-uat.gsa.gov:8888`.

## Impact

The attacker can carry out web cache poisoning to prevent others from accessing the application.

## Attachments
No attachments
