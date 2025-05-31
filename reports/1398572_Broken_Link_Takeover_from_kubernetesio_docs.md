# Broken Link Takeover from kubernetes.io docs

## Report Details
- **Report ID**: 1398572
- **URL**: https://hackerone.com/reports/1398572
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-12T04:48:36.961Z
- **Disclosed**: 2021-12-16T00:31:22.858Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Kubernetes docs has Spanish translation available. One of the page of Portuguese doc has an external reference to a github repository.
The github account was not registered on github.com.
So I was able to takeover the page and host the PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/
  2. Search for `Multus`
  3. Click on `Multus`
  4. You will be taken to this repository https://github.com/Intel-Corp/multus-cni and you will see takeover message there

## Supporting Material/References:

- https://github.com/Intel-Corp/multus-cni
- https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/

{F1511425}

## Impact

As an attacker, I can host malicious content on the github repository.
I can also, host malicious sdk or softwares, which user will think is part of the deployment docs as its referreded in kubernetes.io, this can lead to RCE for users who are referring to this doc

## Attachments
- Screenshot_from_2021-11-12_10-17-44.png
