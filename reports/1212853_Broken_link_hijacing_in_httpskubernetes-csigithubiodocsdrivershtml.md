# Broken link hijacing in https://kubernetes-csi.github.io/docs/drivers.html

## Report Details
- **Report ID**: 1212853
- **URL**: https://hackerone.com/reports/1212853
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-30T04:22:32.989Z
- **Disclosed**: 2021-11-06T18:04:40.918Z

## Reporter
- **Username**: tendermint
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Summary : When a web application has any pages, sources, links to external 3rd party services and are broken then the attacker can claim those endpoints to successfully conduct the attack and claim those endpoints on behalf of the target website and impersonate his identity.

Steps To Reproduce
1) visit https://kubernetes-csi.github.io/docs/drivers.html
2) search for DriveScale
3) click on that link
4) you will be redirected to github and it shows 404 
5) change your username to  DriveScale
6) create k8s-plugins repository
7) When someone clicks on DriveScale link they will be redirected to attacker repository

References
https://hackerone.com/reports/1031321
https://hackerone.com/reports/1117079
https://edoverflow.com/2017/broken-link-hijacking/

For POC I have attached video

## Impact

The user will install wrong CSI driver which leads to impersonation attack. The attacker can install Ransomware, trojan etc.

## Attachments
- kubernetes_github_account_hijack_may_30.mp4
