# Authenticated kubernetes principal with restricted permissions can retrieve ingress-nginx serviceaccount token and secrets across all namespaces

## Report Details
- **Report ID**: 1249583
- **URL**: https://hackerone.com/reports/1249583
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-01T22:51:28.226Z
- **Disclosed**: 2021-12-04T10:16:07.886Z

## Reporter
- **Username**: libio
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:

### Retrieving ingress-nginx serviceaccount token

ingress-nginx allows adding custom snippets of nginx configuration to Kubernetes `ingress` objects. These snippets can be applied to either the relevant `location {}` or `server {}` blocks with the following annotations, respectively.

* https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#configuration-snippet
* https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#server-snippet

Inside the `server {}` block we can add a custom snippet of lua-code that reads the serviceaccount token that is mounted inside the ingress-nginx pod. We then set it as an nginx variable and return it to the client at a configured location. This might look like this:

```yaml
    nginx.ingress.kubernetes.io/server-snippet: |
      set_by_lua $token '
        local file = io.open("/run/secrets/kubernetes.io/serviceaccount/token")
        if not file then return nil end
        local content = file:read "*a"
        file:close()
        return content
      ';

      location = /token {
        content_by_lua_block {
          ngx.say(ngx.var.token)
        }
      }
```

### Impact

The ingress-nginx serviceaccount has the permissions to `list` `secrets` across all namespaces. With the ingress-nginx serviceaccount's token a user, with otherwise restricted privileges, can at least:

* exfiltrate all kubernetes secrets
* get tokens of all kubernetes serviceaccounts; allowing an attacker to elevate his privileges to potentially cluster-admin

Vendors such as rancher-labs bundle ingress-nginx, or a forked version of ingress-nginx, with their software. Solutions provided by these vendors might also be vulnerable.

### kube-apiserver proxy

ingress-nginx can be configured to expose the Kubernetes kube-apiserver by creating a Kubernetes `Service` of type `ExternalName` and pointing it to `kubernetes.default`; the hostname at which the kubernetes api is available inside the cluster. This can expose an otherwise private and protected kube-apiserver to untrusted networks like the internet.

### Requirements to exploit

To successfully exploit this vulnerability an attacker would need access to an already authenticated user or serviceaccount that has the permissions to `create` the following resources inside kubernetes:

* `ingress`
* `service`

Additionally the attacker needs network access to the ingress-nginx-controller loadbalancer or in-cluster service to retrieve the ingress-nginx serviceaccount token. The hostname configured in the `ingress` object does not necessarily have to resolve to the ingress-nginx-controller's loadbalancer; ingress-nginx will also serve us the token if we manually add the `Host`-header.

## Kubernetes Version:

Any, as far as I am aware. This was tested with AWS EKS 1.20.

## Component Version:

Any, as far as I am aware. This was tested with the following release of ingress-nginx:

* chart: `ingress-nginx-3.33.0`
* application: `0.47.0`

## Steps To Reproduce:

I created a proof-of-concept (`poc.sh`) that requires the following:

* A kubernetes cluster with ingress-nginx installed; ingress-nginx should not be restricted to a single namespace
* A local kubeconfig file configured to communicate with the kubernetes cluster
* A user configured in the kubeconfig file with the permissions to `create` `ingress` and `service` objects in the namespace configured in the kubeconfig context

The proof-of-concept requires setting the `INGRESS_HOST` environment variable. This variable should contain a hostname that resolves to the ingress-nginx-controller's loadbalancer. This is made easy on clusters where a wildcard DNS-record is pointing to the loadbalancer.

When invoked, the script will:

1. Apply the required `ingress` and `service`;
   1. exposing the ingress-nginx serviceaccount token at `https://$INGRESS_HOST/token`
   2. proxying all requests to the kubernetes apiserver at `https://$INGRESS_HOST`
2. Retrieve the ingress-nginx serviceaccount token
3. Write a local kubeconfig;
   1. Using the kube-apiserver proxy
   2. Using the ingress-nginx serviceaccount token
4. Write `secrets` from all namespaces to a local file called `secrets.json`
5. For each serviceaccount token found in `secrets.json` check if the serviceaccount has cluster-admin privileges. If so, create a new user and context in the local kubeconfig file with the serviceaccount's token

## Supporting Material/References:

| file           | description                                                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ingress.yaml` | kubernetes manifest used to create required `service` and `ingress` objects                                                                        |
| `poc.sh`       | proof-of-concept written in bash                                                                                                                   |
| `output.png`   | output of running `poc.sh` against local test cluster<br>getting cluster-admin by finding the serviceaccount tokens of flux and flux-helm-operator |

## Impact

* exfiltrate all kubernetes secrets
* get tokens of all kubernetes serviceaccounts; allowing an attacker to elevate his privileges to potentially cluster-admin

## Attachments
- poc.sh
- ingress.yaml
- output.png
