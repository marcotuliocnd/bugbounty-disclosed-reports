# Broken Domain Link Takeover from kubernetes.io docs

## Report Details
- **Report ID**: 1434179
- **URL**: https://hackerone.com/reports/1434179
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-12-22T17:22:58.454Z
- **Disclosed**: 2022-04-03T04:47:16.175Z

## Reporter
- **Username**: 0xlegendkiller
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Kubernetes docs have Spanish translation available. One of the pages of the Portuguese doc has an external reference to a  website .
The website is not registered and can be purchased and used to host malicious content.

## Kubernetes Version:
NA

## Component Version:
NA
## Steps To Reproduce:

1. Go to https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/
2. Search for `contiv`
3. Click on 'Contiv`
You will be redirected to https://contiv.io/ which does not exist...

## Supporting Material/References:
1. https://contiv.io/
2.  https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=contiv.io

## Impact

As an attacker, I can host malicious content on the website.
I can also, host malicious sdk or softwares, which user will think is part of the deployment docs as its referred in kubernetes.io, this can lead to RCE for users who are referring to this doc.

## Attachments
- 1.1.png
- 1.png
- 3.png
- 2.png
