# Argo CD reconciles apps outside configured namespaces when sharding is enabled

## Report Details
- **Report ID**: 1847140
- **URL**: https://hackerone.com/reports/1847140
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-25T19:04:04.357Z
- **Disclosed**: 2023-03-05T16:49:51.098Z

## Reporter
- **Username**: czchen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The Application CRD outside configured namespace in Argo CD will be reconciled.

The following is how to reproduce the vulnerability:

* Enable `apps-in-any-namespace` and `sharding` features.
* Create an Application CRD in namespace not configured in Argo CD.
* Update the Application CRD, and Argo CD will reconcile the Application CRD, despite not in configured namespace.

## Impact

Attacker can use Argo CD permission to deploy resources in Kubernetes.

## Attachments
No attachments
