# Man in the middle leading to root privilege escalation using hostNetwork=true (CAP_NET_RAW considered harmful)

## Report Details
- **Report ID**: 899103
- **URL**: https://hackerone.com/reports/899103
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-16T00:26:19.428Z
- **Disclosed**: 2021-10-08T03:47:30.988Z

## Reporter
- **Username**: champtar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
CAP_NET_RAW capability is still included by default in K8S, leading to yet another attack.

An attacker gaining access to a hostNetwork=true container with CAP_NET_RAW capability can listen to all the traffic going through the host and inject arbitrary traffic, allowing to tamper with most unencrypted traffic (HTTP, DNS, DHCP, ...), and disrupt encrypted traffic.
In many cloud deployments the host queries the metadata service at http://169.254.169.254 to get many information including the authorized ssh keys.
This report contains a POC running on GKE, manipulating the metadata service responses to gain root privilege on the host.
The same attack should work on all clouds using similar metadata services to provision ssh keys (Amazon / Azure / OpenStack / ...)

The goal of this report is to ask the K8S team to make a breaking change by removing CAP_NET_RAW from the default capabilities,
as it allows way too many attacks.
K8S could enable `net.ipv4.ping_group_range` to still let users use ping (maybe 99% of CAP_NET_RAW usage)

## Kubernetes Version:
This was tested on a default GKE cluster (1.14.10-gke.36)

## Steps To Reproduce:

1. Create a GKE cluster
```
gcloud beta container --project "copper-frame-263204" clusters create "hostmitm" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.14.10-gke.36" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/copper-frame-263204/global/networks/default" --subnetwork "projects/copper-frame-263204/regions/us-central1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0
```

2. Create a hostNetwork=true pod
```
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-node
spec:
  hostNetwork: true
  containers:
    - name: ubuntu
      image: ubuntu:latest
      command: [ "/bin/sleep", "inf" ]
EOF
```

3. Copy our script
```
kubectl cp metadatascapy.py ubuntu-node:/metadatascapy.py
```
(download F869463)

4. Connect to the container
```
kubectl exec -ti ubuntu-node -- /bin/bash
```
(the next commands are in the container shell)

5. Install the needed packages
```
apt update && apt install -y python3-scapy openssh-client
```

6. Generate an ssh key (this is the key that we are going to inject and use to ssh into the host)
```
ssh-keygen -t ed25519 -f /root/.ssh/id_ed25519 -N ""
```

7. Launch the script, wait up to 2min, enjoy
```
python3 /metadatascapy.py
```
(If you see a kubeconfig and some certificates printed, it worked)

## Impact

An attacker able to execute code in a hostNetwork=true container with CAP_NET_RAW capability can, in cloud deployments, easily gain root privileges on the host.

## Attachments
- metadatascapy.py
