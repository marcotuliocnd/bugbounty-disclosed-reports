# Sensitive information disclosure on grafana

## Report Details
- **Report ID**: 1448218
- **URL**: https://hackerone.com/reports/1448218
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-12T20:27:44.106Z
- **Disclosed**: 2024-02-26T22:02:26.158Z

## Reporter
- **Username**: asce21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jetblue

## Vulnerability Information
## Summary:

While running through scan I got some endpoints on jetblue subdomains which discloses sensitive information. I know these are out of scope but I think it is necessary to report them

## Steps To Reproduce:

  1. Visit the urls in browser

`https://████.jetblue.com/metrics`

███

Discloses  grafana metrics  to unauthorized users

```
https://█████████.jetblue.com/sap/public/info
https://████.jetblue.com/sap/public/info
```

██████

Disclose sensitive information about SAP  such as internal IP address and OS

`https://███████.travelproducts.jetblue.com/`

███████

aws bucket listing is enabled which discloses sensitive endpoints to unauthorized users

## Impact

Unauthorized user can access sensitive info about server resources.

## Attachments
No attachments
