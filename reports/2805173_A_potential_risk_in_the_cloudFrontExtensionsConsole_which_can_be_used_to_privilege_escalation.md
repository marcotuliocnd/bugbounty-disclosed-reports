# A potential risk in the cloudFrontExtensionsConsole which can be used to privilege escalation.

## Report Details
- **Report ID**: 2805173
- **URL**: https://hackerone.com/reports/2805173
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-26T05:06:41.271Z
- **Disclosed**: 2024-11-19T16:33:00.368Z

## Reporter
- **Username**: zolaer9527
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Summary:**  I found a potential risk in the cloudFrontExtensionsConsole when I deployed it in the awslabs repository on GitHub. The application created functions and the roles of the functions had too many excessive permissions. A  malicious user could leverage these permissions to escalate his/her privilege in multiple ways.

**Description:** First, the cloudFrontExtensionsConsole application created four functions that are cf_config_version_exporter, cf_config_version_manager, cf_config_version_manager_graphql, and cloudFrontExtensionsConso-SingletonLambdaf7d4f7304-ZbLF9YFgQ4eq rLambdaFunction. These functions share the same role which is cloudFrontExtensionsConso-CloudFrontConfigVersionCo-rAgdktzDTPRh. The role has the "iam:CreateRole", "iam:GetRole", "iam:CreatePolicy", and "iam:AttachRolePolicy" for "*" resources.  A  malicious user could leverage these permissions to escalate his/her privilege in multiple ways. For example, he/she can leverage the AttachRolePolicy permission to attach the AWS-managed policy or the policy created by the CreatePolicy to the role that he/she can access. It could allow a user to gain full administrator access to the AWS account.

Second, the cloudFrontExtensionsConsole application also created two functions that are cloudFrontExtensionsConso-RepoConstructSyncExtensi-ydrYwNGQCoFr and cloudFrontExtensionsConso-RepoConstructExtDeployer-1uHGWxrjog9S. These two functions share the same role which is cloudFrontExtensionsConso-RepoConstructExtDeployerR-wBEukYirZfbr. The role has the "iam:*" for "*" resources. These permissions can be exploited in more ways, including but not limited to the attack methods mentioned above.

In a word, the functions created by the cloudFrontExtensionsConsole have too many excessive permissions, which could cause very serious consequences.


## Remediation Instructions
1. Use finer-grained authorization roles to replace the way that many functions share one role. And use the specific resource names to replace the "*".
2. The permissions for IAM resources should be removed if they do not affect normal functionality.
3. Add a permissions boundary to restrict the permission.

## Impact

## Summary:
A  malicious user could leverage these permissions to escalate his/her privilege.

## Attachments
No attachments
