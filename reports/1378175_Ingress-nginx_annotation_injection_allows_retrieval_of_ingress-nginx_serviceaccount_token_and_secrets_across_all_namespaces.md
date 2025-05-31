# Ingress-nginx annotation injection allows retrieval of ingress-nginx serviceaccount token and secrets across all namespaces

## Report Details
- **Report ID**: 1378175
- **URL**: https://hackerone.com/reports/1378175
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-10-22T03:49:19.404Z
- **Disclosed**: 2022-08-13T18:13:23.850Z

## Reporter
- **Username**: amlweems
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
I submitted the following report to security@kubernetes.io:
> I've been exploring CVE-2021-25742 and believe I've discovered a variant (although it appears there may be many). Most template variables are not escaped properly in `nginx.tmpl`, leading to injection of arbitrary nginx directives. For example, the `nginx.ingress.kubernetes.io/connection-proxy-header` annotation is not validated/escaped and is inserted directly into the `nginx.conf` file.
>
> An attacker in a multi-tenant cluster with permission to create/modify ingresses can inject content into the connection-proxy-header annotation and read arbitrary files from the ingress controller (including the service account).
>
> I've created a secret gist demonstrating the issue against ingress-nginx v1.0.4: https://gist.github.com/amlweems/1cb7e96dca8ada8aee8dc019d4163f2c

## Impact

An attacker with permission to create/modify ingresses in one namespace can inject content into the connection-proxy-header annotation and read arbitrary files from the ingress controller (including the service account). This service account has permission to read secrets in all namespaces.

## Attachments
No attachments
