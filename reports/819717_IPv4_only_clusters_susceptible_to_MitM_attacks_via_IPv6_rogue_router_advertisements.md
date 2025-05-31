# IPv4 only clusters susceptible to MitM attacks via IPv6 rogue router advertisements

## Report Details
- **Report ID**: 819717
- **URL**: https://hackerone.com/reports/819717
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-15T17:34:18.152Z
- **Disclosed**: 2021-11-07T03:52:50.936Z

## Reporter
- **Username**: champtar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
This bug report mostly concerns the default CNI plugins (https://github.com/containernetworking/plugins) but I believe affects many K8S clusters.
Because the CNI team still doesn’t provide an explicit way to report security bugs, I hope the K8S security team doesn’t mind doing the coordination job again as was done for CVE-2019-9946.
I understand this is out of scope for this bounty, and I understand if you want to close this report and prefer that I resend it via email to security@kubernetes.io or other.

## Summary:
In many K8S network configurations the container network interface is a virtual ethernet link going to the host (veth interface). In this configuration, an attacker able to run a process as root in a container can send and receive arbitrary packets to the host using the CAP_NET_RAW capability (present in default configuration).

In a K8S cluster with an IPv4 internal network, if IPv6 is not totally disabled on the host (via ipv6.disable=1 on the kernel cmdline), it will be either unconfigured or configured on some interfaces, but it’s pretty likely that ipv6 forwarding is disabled, ie /proc/sys/net/ipv6/conf/*/forwarding == 0. Also by default, /proc/sys/net/ipv6/conf/*/accept_ra == 1. The combination of these 2 sysctls means that the host accepts router advertisements and configure the IPv6 stack using them.

By sending “rogue” router advertisements, an attacker can reconfigure the host to redirect part or all of the IPv6 traffic of the host to the attacker controlled container.
Even if there was no IPv6 traffic before, if the DNS returns A (IPv4) and AAAA (IPv6) records, many HTTP libraries will try to connect via IPv6 first then fallback to IPv4, giving an opportunity to the attacker to respond.
If by chance you also have on the host a vulnerability like last year’s RCE in apt (CVE-2019-3462), you can now escalate to the host.

As CAP_NET_ADMIN is not present by default in K8S pods, the attacker can’t configure the IPs they want to MitM, they can’t use iptables to NAT or REDIRECT the traffic, and they can’t use IP_TRANSPARENT. The attacker can however still use CAP_NET_RAW and implement a tcp/ip stack in user space.

This report includes a POC based on smoltcp (https://github.com/smoltcp-rs/smoltcp) that sends router advertisements and implements a dummy HTTP server listening on any IPv6 addresses.

This vulnerability can easily be fixed by setting accept_ra = 0 by default on any interface managed by CNI / K8S.

## Kubernetes Version:
Reproduced on:
GKE Cos 1.14.10-gke.17 with native VPC
GKE Cos 1.16.6-gke.12 with/without native VPC
GKE Cos + containerd 1.16.6-gke.12 without native VPC
Kubespray k8s 1.17.3 + containerd


## Component Version:
CNI 0.7.5

## Steps To Reproduce:

Please find attached F748694, a recording of my shell using asciinema (https://github.com/asciinema/asciinema)

The GKE cluster used was created using the following command:
`gcloud beta container --project "copper-frame-263204" clusters create "testipv6" --zone "us-central1-c" --no-enable-basic-auth --release-channel "rapid" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-stackdriver-kubernetes --no-enable-ip-alias --network "projects/copper-frame-263204/global/networks/default" --subnetwork "projects/copper-frame-263204/regions/us-central1/subnetworks/default" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair`

This cluster is created without `--enable-ip-alias` (but the attack also with it)

## Supporting Material/References:
F748693: rust source code for the POC
F748694: asciinema recording

## Impact

An attacker able to run arbitrary code as root inside of a container can MitM part of the host’s traffic. This vulnerability if chained with other vulnerability like last year’s RCE in apt (CVE-2019-3462) could allow to escalate to the host.

## Attachments
- ipv6mitm.tar.xz
- ipv6mitm.cast
