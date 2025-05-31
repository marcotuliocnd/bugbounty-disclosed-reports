# Private RSA key and Server key exposed on the GitHub repository

## Report Details
- **Report ID**: 876751
- **URL**: https://hackerone.com/reports/876751
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-17T23:02:39.364Z
- **Disclosed**: 2020-10-22T18:07:16.840Z

## Reporter
- **Username**: njaysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
I was searching for sensitive data in Kubernetes repository where I found these private keys. These are private RSA key and private server key, which could be used for unauthorized access.

## Steps To Reproduce:

VISIT THESE LINKS

Repository : kubernetes / kubernetes

https://github.com/kubernetes/kubernetes/blob/ce3ddcd5f691b5777e7b2f4d89cac1da316970b4/staging/src/k8s.io/legacy-cloud-providers/vsphere/vclib/fixtures/ca.key

https://github.com/kubernetes/kubernetes/blob/ce3ddcd5f691b5777e7b2f4d89cac1da316970b4/staging/src/k8s.io/legacy-cloud-providers/vsphere/vclib/fixtures/server.key

## Supporting Material/References:
https://hackerone.com/reports/50170
https://hackerone.com/reports/638401

## Impact

1).Private key leakage
2). All of the servers using this key will be compromised

## Attachments
- kub1.png
- kub2.png
