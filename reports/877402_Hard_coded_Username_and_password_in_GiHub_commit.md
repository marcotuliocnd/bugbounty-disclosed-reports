# Hard coded Username and password in GiHub commit

## Report Details
- **Report ID**: 877402
- **URL**: https://hackerone.com/reports/877402
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-05-18T18:43:10.513Z
- **Disclosed**: 2020-07-24T00:43:07.805Z

## Reporter
- **Username**: njaysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
I was exploring the GitHub repository and I found some hard coded credentials in the commit history. These credentials are related to Vagrant  tool which is used to setup virtual machines environment, This is a very critical disclosure and can lead to bigger damages. So I am informing this to you guys, please let me know what do you guys think.


## Steps To Reproduce:
VISIT THESE LINKS
Repository :  kubernetes /kubernetes 
Commit Link : https://github.com/kubernetes/kubernetes/commit/5a0159ea00e082bc85bbec18d1ab7ae78d90fa4f
Repository Link : https://github.com/kubernetes/kubernetes/blob/5a0159ea00e082bc85bbec18d1ab7ae78d90fa4f/cluster/kubecfg.sh


## Supporting Material/References:

Reference:
https://hackerone.com/reports/124100

## Impact

Vagrant is a tool for building and managing virtual machine environments in a single workflow. This can give hacker access to the hacker to the automation tool to setup VMs and their environment, which he can use for further escalation.

## Attachments
- kub-cred1.png
