# Compromise of auth via subset/superset namespace names.

## Report Details
- **Report ID**: 778803
- **URL**: https://hackerone.com/reports/778803
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-21T06:10:38.317Z
- **Disclosed**: 2020-10-30T21:59:19.836Z

## Reporter
- **Username**: alex_orange
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Use of nginx.ingress.kubernetes.io/auth* annotations results in a file named {namespace}-{ingress}.passwd. If user knows the namespace and ingress of an ingress they want to compromise they need to be able to create a namespace that is some subset of {namespace}-{ingress}. Then they create an ingress with the remainder of the name and a passwd file of their choosing, this overwrites the other namespace's passwd file and effectively removes the auth layer provided by nginx ingress.

## Kubernetes Version:
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"16+", GitVersion:"v1.16.5-beta.0", GitCommit:"224be7bdce5a9dd0c2fd0d46b83865648e2fe0ba", GitTreeState:"archive", BuildDate:"2019-12-31T22:42:08Z", GoVersion:"go1.12.13", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"16", GitVersion:"v1.16.2", GitCommit:"c97fe5036ef3df2967d086711e6c0c405941e14b", GitTreeState:"clean", BuildDate:"2019-10-15T19:09:08Z", GoVersion:"go1.12.10", Compiler:"gc", Platform:"linux/amd64"}

Installed via kubeadm on gentoo (though I don't think this is relevant to vulnerability).

## Component Version:
quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.26.1

## Steps To Reproduce:
  1. Install nginx ingress
  2. Create namespace a and ingress b-c within a with an auth annotation.
  3. Create namespace a-b and ingress c within a-b with an auth annotation that overrides the passwd file from #2.
  4. Auth to ingress on a/b-c is now governed by the htpasswd file generated for a-b/c.

## Suggested Resolution:
1. Change line 141 of internal/ingress/annotations/auth/main.go to %v/%v/%v.
2. Create folder to go along with.
3. Check that the folder and file will actually be in the right location (.. is allowed as a namespace).

## Impact

Attacker can override the htpasswd file of another ingress effectively neutralizing the http authentication.

## Attachments
No attachments
