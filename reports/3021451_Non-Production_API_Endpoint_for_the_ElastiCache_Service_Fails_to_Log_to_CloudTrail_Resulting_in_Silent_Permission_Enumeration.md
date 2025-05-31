# Non-Production API Endpoint for the ElastiCache Service Fails to Log to CloudTrail Resulting in Silent Permission Enumeration

## Report Details
- **Report ID**: 3021451
- **URL**: https://hackerone.com/reports/3021451
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-03-03T15:55:33.528Z
- **Disclosed**: 2025-04-25T16:23:03.008Z

## Reporter
- **Username**: nick_frichette_dd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Summary:** Typically, when an adversary gains access to stolen AWS IAM credentials they will [frequently](█████) test those credentials to see what access they have. They do this by performing API calls and seeing which succeed and which fail. There are even automated [tools](████) to make this process easier. For defenders and security professionals, this behavior serves as a golden opportunity for detection as it likely involves generating a large number of failed API call attempts. If an adversary could enumerate permissions without logging to CloudTrail, they could perform this activity invisibly.

There are many categories of CloudTrail bypass. The specific variant we will be focussed on in this report has been referred to as “non-production endpoint permission enumeration CloudTrail bypass”. If you would like to learn more about it, you can find more details [here](███████). 

**We have found 1 non-production endpoint for the ElastiCache service which can be used with standard IAM credentials, and does not log to CloudTrail.** While it is good that it doesn’t appear to have access to customer partition data, it can still be used for permission enumeration without logging to CloudTrail. 

AWS has previously [stated](███████) that this type of vulnerability should be reported. Specifically, “For isolated non-production endpoints that do not log to CloudTrail but are otherwise callable with normal credentials and exhibit normal IAM permission behavior, AWS considers the CloudTrail logging bypass of such endpoints also to be a security issue. If you find an API or APIs on an endpoint with these characteristics, please contact the AWS Security Team at aws-security@amazon.com”. 

**Description:** 

## Steps To Reproduce:

To see an example of what should appear in CloudTrail when using normal production endpoints, perform the following AWS CLI operation with a sufficiently privileged IAM user or role:

```
aws elasticache describe-users
```

Wait approximately 5-10 minutes and a log will appear in CloudTrail. Next, perform the following AWS CLI operation:

```
aws elasticache describe-users --endpoint-url ███████
```

After waiting 5-10 minutes (or longer), notice that it does not generate a log in CloudTrail. An adversary can perform this operation and depending on the response of the API make a determination if an Identity they have compromised does, or does not have permission to perform the operation. 

## Supporting Material/References:

* Indicate the Amazon service or product that this vulnerability occurs on:  

elasticache

* What type of Amazon AWS account(s) is needed to verify or reproduce this vulnerability?: 

Standard commercial partition account

* Estimated CVSS score and vector string: 

4.3 CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N/CR:X/IR:X/AR:X

* Estimated CWEs (comma separated): 

CWE-778: Insufficient Logging

* Have you already publicly disclosed any information on this issue? If so, when and where?: 

This specific example? No. This general technique? Yes, a lot actually. I’ve blogged about it [here](███████) and spoke about it at Black Hat USA 2023 (████████) and fwd:cloudsec 2023 (██████████) [I have broken these links because HackerOne appeared to complain about them?] 

Additionally, we have reported similar findings for different services:
* [datazone part 2](███)
* [docdb-elastic](█████)
* [devicefarm](█████████)
* [datazone](█████)
* [cloudwatch](█████)
* [bedrock](█████████)
* [bedrock-agent](████████)
* [ssm](████████)

The following is the endpoint we found that exhibited this behavior.

- ████: 
An adversary can enumerate permissions of compromised credentials for the elasticache service without logging to CloudTrail.

## Attachments
No attachments
