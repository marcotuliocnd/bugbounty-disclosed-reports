# SHA512 incorrect on most/many releases

## Report Details
- **Report ID**: 1130416
- **URL**: https://hackerone.com/reports/1130416
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-19T01:13:24.952Z
- **Disclosed**: 2021-05-09T20:16:48.395Z

## Reporter
- **Username**: ronald_petty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
SHA512 is incorrect for most versions of kubernetes.tar.gz releases (https://github.com/kubernetes/kubernetes/releases/).

## Kubernetes Version:
all

## Component Version:
all

## Steps To Reproduce:
[add details for how we can reproduce the issue, including relevant cluster setup and configuration]

curl -sLO https://github.com/kubernetes/kubernetes/releases/download/v1.20.0/kubernetes.tar.gz
shasum -a 512 kubernetes.tar.gz (mac)
openssl dgst -sha512 kubernetes.tar.gz (linux)
sha512sum kubernetes.tar.gz (linux)

All report:
ebfe49552bbda02807034488967b3b62bf9e3e507d56245e298c4c19090387136572c1fca789e772a5e8a19535531d01dcedb61980e42ca7b0461d3864df2c14

Per website, it should be:
cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

## Supporting Material/References:
https://github.com/kubernetes/kubernetes/releases/tag/v1.20.0

another example:

https://github.com/kubernetes/kubernetes/releases/tag/v1.19.5

Same SHA512:
cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

## Impact

I suspect its an automation release issue (hence same hash in all places).

* Impact 1: Can't verify artifact is correct artifact.
* Impact 2: Hacked?

## Attachments
No attachments
