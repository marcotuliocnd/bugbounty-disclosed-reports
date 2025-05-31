# Github Account Takeover from Docs page of `kubernetes-csi.github.io`

## Report Details
- **Report ID**: 1434967
- **URL**: https://hackerone.com/reports/1434967
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-12-23T13:52:04.138Z
- **Disclosed**: 2022-06-04T17:58:23.464Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Kubernetes in its docs https://kubernetes-csi.github.io have a drivers list.
One of the driver was pointing to an external github account. That github account was not registered on github.com
So I was able to takeover the account and host PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes-csi.github.io/docs/drivers.html
  2. Search for `MacroSAN`
  3. Click on  `MacroSAN`
  4. You will be taken to this repository https://github.com/macrosan-csi/macrosan-csi-driver
  5. You will see takeover message there

## Supporting Material/References:

- https://github.com/macrosan-csi/macrosan-csi-driver
- https://kubernetes-csi.github.io/docs/drivers.html

{F1556768}

## Reference

- https://hackerone.com/reports/1212853

## Impact

An attacker can takeover the repository and host malicious code on it, when any user or employee will refer the docs and tries to download the dirver, they will end up using malicious code which could lead to RCE.

## Attachments
- Screenshot_from_2021-12-23_19-20-35.png
