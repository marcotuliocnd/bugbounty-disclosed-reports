# secret leaks in vsphere cloud controller manager log

## Report Details
- **Report ID**: 966383
- **URL**: https://hackerone.com/reports/966383
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-25T00:29:42.516Z
- **Disclosed**: 2020-11-29T21:23:27.388Z

## Reporter
- **Username**: derek0405
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
When create k8s cluster over vsphere and enable vsphere as cloud provider. With logging level set to 4 or above, secret information will be printed out in the cloud controller manager's log.

## Kubernetes Version:
1.18.6

## Component Version:
legacy cloud provider

## Steps To Reproduce:
[add details for how we can reproduce the issue, including relevant cluster setup and configuration]

  1. Configure vsphere as cloud provider and set logging level to 4 or above (https://cloud-provider-vsphere.sigs.k8s.io/tutorials/kubernetes-on-vsphere-with-kubeadm.html)
  2. Check vsphere cloud provider log when a secret is created or udpated as the secret informer is registered with and will be print out when the logging level set to 4 or above.
  
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
Source codes that print out the secret info:
https://github.com/kubernetes/kubernetes/blob/6d0f4749a59099171540d4fd7c9523b029e71ceb/staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go#L1503

https://github.com/kubernetes/kubernetes/blob/6d0f4749a59099171540d4fd7c9523b029e71ceb/staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go#L1527

Calling code path:
1.cmd/kube-controller-manager/app/controllermanager.go -> Run()
2.cmd/kube-controller-manager/app/controllermanager.go -> CreateControllerContext()
3. cmd/kube-controller-manager/app/cloudproviders.go -> createCloudProvider()
4. vendor/k8s.io/cloud-provider/cloud.go ->SetInformers()
5. staging/src/k8s.io/legacy-cloud-providers/vsphere/vsphere.go -> func (vs *VSphere) SetInformers(informerFactory informers.SharedInformerFactory)

  * [attachment / reference]

## Impact

If any kubernetes users or service accounts has privileges (e.g. GET pods/log  in the kube-system namespace), he will be able to view all the secrets data when a secret is created or updated which may contain sensitive data such as password or private key. Further, is the secret is a service account token, then the user may escalate his privileges.

## Attachments
No attachments
