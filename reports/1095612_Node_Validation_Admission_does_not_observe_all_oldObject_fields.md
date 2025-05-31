# Node Validation Admission does not observe all oldObject fields

## Report Details
- **Report ID**: 1095612
- **URL**: https://hackerone.com/reports/1095612
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-04T16:40:22.115Z
- **Disclosed**: 2021-09-05T23:17:03.481Z

## Reporter
- **Username**: ariellima
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
The Validating Admission webhook for Node Objects is passing oldObject fields incorrectly on AdmissionReview.Request. It was identified initially in metadata.labels, but a list of impacted fields follows below:
 
oldNode.Spec.PodCIDRs
oldNode.Spec.ProviderID
oldNode.Spec.ConfigSource
oldNode.Status.Config
oldNode.ObjectMeta
oldNode.Status.Capacity
oldNode.Spec.Unschedulable
oldNode.Status
oldNode.Spec.Taints

Those fields are being set with the same values as the new node object, potentially allowing users to bypass validating admission to update node labels, taints, and others.

## Kubernetes Version:
v1.19.x

## Component Version:
Validation Webhook for Nodes

## Steps To Reproduce:

1. Create a Validating Webhook Configuration for Node updates
2. Create an admission Webhook that outputs the content of oldNode and newNode from the admissionReview obejct
3. Run a patch that changes one of the fields mentioned above.
4. Look at the log output and compare the old and newObject CRs -- you will notice that the patch you just made appears on the new AND oldObject CRs logged.

## Supporting Material/References:
Validating Webhook we created -> https://github.com/ArielLima/managed-cluster-validating-webhooks/blob/nodelabels-webhook/pkg/webhooks/node/node.go#L145-L179

Dummy Validating Webhook -> https://github.com/openshift/generic-admission-server/pull/40/files#diff-ce34cccb3b86fc2740015cfa93de7e314262e3db76d54708d5e1c302e6986436R39

Potential issue location -> https://github.com/kubernetes/kubernetes/blob/c970a46bc1bcc100bbbfabd5c12bd4c5d87f8aea/pkg/apis/core/validation/validation.go#L4792-L4794

## Impact

Even though a validating admission webhook thinks that it is restricting actors from mutating certain fields like taints, labels, and schedulability it is not.  
Some examples of actions you could perform:
1. change labels to steer workloads
2. change labels to prevent scheduling any workload
3. change taints to push pods off a node

## Attachments
No attachments
