# SSRF mitigation bypass using DNS Rebind attack

## Report Details
- **Report ID**: 1369312
- **URL**: https://hackerone.com/reports/1369312
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-13T13:27:58.085Z
- **Disclosed**: 2022-11-25T18:11:12.845Z

## Reporter
- **Username**: adrian_t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
We noticed that the upload functionality contains the ability to upload files from remote server, however there are some mitigations against accessing the AWS Instance Metadata service.

We've managed to bypass these mitigations using DNS rebinding and we've managed to fetch the AWS IAM keys when Concrete CMS is running in the cloud.

We've used http://1u.ms/ service for DNS rebinding, please see screenshots with evidence.

## Impact

An attacker can bypass the SSRF protections and he can fetch the AWS IAM keys under which the application is running. From here on he can do enumeration and mount other attacks.

## Attachments
- fetch_IAM_role.png
- DNS-rebinding.png
- IAM_keys.png
