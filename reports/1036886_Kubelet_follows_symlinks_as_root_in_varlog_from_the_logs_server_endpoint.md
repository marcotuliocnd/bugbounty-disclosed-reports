# Kubelet follows symlinks as root in /var/log from the /logs server endpoint 

## Report Details
- **Report ID**: 1036886
- **URL**: https://hackerone.com/reports/1036886
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-17T16:54:29.509Z
- **Disclosed**: 2021-04-01T18:13:00.639Z

## Reporter
- **Username**: danielsagi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
Privilege escalation from a  pod, to root read permissions on the entire filesytem of the node, by creating symlinks inside /var/log.
The kubelet is simply serving a fileserver at /var/log:

_kubernetes\pkg\kubelet\kubelet.go:1371_
```golang
if kl.logServer == nil {
		kl.logServer = http.StripPrefix("/logs/", http.FileServer(http.Dir("/var/log/")))
	}
```
The kubelet naturally runs as root on the node, so this basically gives the ability for pods with write permissions to /var/log directory a directory traversal as a root user on the host (potentially taking over the whole cluster by getting secret keys)
An easy fix is checking the symlink destination, to figure out whether it is inside /var/lib/docker or other whitelisted paths to not break to mechanism of logs correlations

A while back, I discovered this bug, when you didn't had the Bug Bounty program. 
I Published the following blog:
https://blog.aquasec.com/kubernetes-security-pod-escape-log-mounts
Describing the vulnerability.

(it  requires RBAC permissions to read logs, or a kubelet configured with AlwaysAllow. and a mount point to any child directory inside /var/log)
I researched some log collectors projects in github, seems like alot of them are freely using this mount point.
As a user I would not imagine those projects can potentially take clusters. 

## Kubernetes Version:
All versions

## Component Version:
The kubelet

## Steps To Reproduce:
  1. create a pod with a mount path to `/var/log`
  1. create a symlink in the mount point: `/var/log/rootfs_symlink -> /`
  1. curl from within the pod: `https://<ip_of_node>:10250/logs/rootfs_symlink/etc/shadow`

## Supporting Material/References:
https://blog.aquasec.com/kubernetes-security-pod-escape-log-mounts
https://github.com/danielsagi/kube-pod-escape

## Impact

Root read permissions on the entire filesystem of the node

## Attachments
No attachments
