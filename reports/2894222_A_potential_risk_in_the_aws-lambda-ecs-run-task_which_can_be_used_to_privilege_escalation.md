# A potential risk in the aws-lambda-ecs-run-task which can be used to privilege escalation.

## Report Details
- **Report ID**: 2894222
- **URL**: https://hackerone.com/reports/2894222
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-12-11T06:19:16.702Z
- **Disclosed**: 2024-12-27T14:40:27.234Z

## Reporter
- **Username**: zolaer9527
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Summary:** I found a potential risk in the aws-lambda-ecs-run-task when I deployed it in the awslabs repository on GitHub. The application created a function with a role that has too many excessive permissions. A  malicious user could leverage these permissions to escalate his/her privilege in multiple ways.


**Description:** The aws-lambda-ecs-run-task application creates a function named rLambdaFunction, which has a role named rLambdaFunctionRole with the arn:aws:iam::aws:policy/AdministratorAccess policy. The policy allows for any action on all resources. That means the attacker can leverage these permissions to escalate privileges. If a malicious controlled this function, he/she can directly do what he/she wants to do as a root.

## Impact

## Summary:
A malicious user could leverage these permissions to escalate his/her privilege.

## Attachments
No attachments
