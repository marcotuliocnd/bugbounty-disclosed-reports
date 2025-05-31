# Code inject via nginx.ingress.kubernetes.io/permanent-redirect annotation

## Report Details
- **Report ID**: 2039464
- **URL**: https://hackerone.com/reports/2039464
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-06-26T23:46:37.276Z
- **Disclosed**: 2023-10-25T22:46:43.792Z

## Reporter
- **Username**: jkroepke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
The value of the `nginx.ingress.kubernetes.io/permanent-redirect` annotation will be not sanitized and passed into the nginx configuration. This leads into a code inject from any user that is allowed to create ingress objects.

## Kubernetes Version:
v1.26.3 (minikube)

## Component Version:
```
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v1.8.0
  Build:         35f5082ee7f211555aaff431d7c4423c17f8ce9e
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.21.6

-------------------------------------------------------------------------------
```

## Steps To Reproduce:

  1. Install ingress-nginx, using latest version and default values. For demo purpose, I set `allow-snippet-annotations=false`
        ```bash
        helm upgrade -i ingress-nginx ingress-nginx/ingress-nginx -f values.yaml # values.yaml is attached
        ```
  1. apply service and ingress object from attachments
        ```bash
        k apply -f ingress.yaml #ingress.yaml is attached
        ```
  1. Optional: If ingress-nginx is not exposed, run `kubectl port-forward deploy/ingress-nginx-controller 8080:80` and continue step 4 in a separate shell.
  1. Validate, if the code is injected. This demo uses the hostname `kubernetes.api`, use the `--resolve` parameter of curl to do an request for the hidden server instance. The code below expect that ingress-nginx is accessible trough 127.0.0.1:8080

        ```bash
        curl -v --resolve "kubernetes.api:8080:127.0.0.1" http://kubernetes.api:8080/api/v1/namespaces/kube-system/secrets/
        ```

## Supporting Material/References:

  * values.yaml - Used in step 1
  * ingress.yaml - Used in step 2

## Impact

All users with access to create or update ingress objects, are able to running commands on ingress-nginx-controller pod. Since the token of the ServiceAccount is mounted on filesystem, a user can call the Kubernetes API and fetch all secrets or config maps from the cluster. Additionally, the user can read or write files to the filesystem.

## Attachments
- values.yaml
- ingress.yaml
- demo.webm
