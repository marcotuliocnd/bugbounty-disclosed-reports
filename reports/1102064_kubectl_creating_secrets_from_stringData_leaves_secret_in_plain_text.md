# kubectl creating secrets from stringData leaves secret in plain text

## Report Details
- **Report ID**: 1102064
- **URL**: https://hackerone.com/reports/1102064
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-12T10:30:45.749Z
- **Disclosed**: 2021-08-21T07:32:11.123Z

## Reporter
- **Username**: max_lan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
kubectl creating secrets from stringData leaves secret in plain text

## Kubernetes Version:

    $ kubectl version
    Client Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.3", GitCommit:"1e11e4a2108024935ecfcb2912226cedeafd99df",GitTreeState:"clean", BuildDate:"2020-10-14T12:50:19Z", GoVersion:"go1.15.2", Compiler:"gc", Platform:"darwin/amd64"}
    Server Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.3", GitCommit:"1e11e4a2108024935ecfcb2912226cedeafd99df", GitTreeState:"clean", BuildDate:"2020-10-14T12:41:49Z", GoVersion:"go1.15.2", Compiler:"gc", Platform:"linux/amd64"}

## Component Version:
n/a

## Steps To Reproduce:

Create a secret using stringData and query it.

		$ cat sec.yaml 
		kind: Secret
		apiVersion: v1
		metadata:
		 name: stupid
		stringData:
		 user: clear
		 password: revealed

		$ kubectl get secret stupid -o yaml
		apiVersion: v1
		data:
		  password: cmV2ZWFsZWQ=
		  user: Y2xlYXI=
		kind: Secret
		metadata:
		  annotations:
		    kubectl.kubernetes.io/last-applied-configuration: |
		      {"apiVersion":"v1","kind":"Secret","metadata":{"annotations":{},"name":"stupid","namespace":"default"},"stringData":{"password":"revealed","user":"clear"}}
		  creationTimestamp: "2021-02-12T10:11:02Z"


Even if you update the secret, the new value is then shown in the last-applied-configuration.
Meaning the base64 "protection" against inadvertent disclosure is pointless.
kubectl should probably either obscure or base64 the values in last-applied for secrets.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

An attacker could oversee a non-obfuscated secret. 

(It seems fairly unlikely/minor but you've gone to the trouble of base64 encoding it for a reason. Why would that reason apply for the actual value but 2 lines further down no longer apply?)

## Attachments
No attachments
