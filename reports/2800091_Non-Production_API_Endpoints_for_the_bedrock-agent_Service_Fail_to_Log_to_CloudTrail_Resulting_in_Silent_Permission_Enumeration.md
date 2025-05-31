# Non-Production API Endpoints for the bedrock-agent Service Fail to Log to CloudTrail Resulting in Silent Permission Enumeration

## Report Details
- **Report ID**: 2800091
- **URL**: https://hackerone.com/reports/2800091
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-23T18:23:22.077Z
- **Disclosed**: 2025-05-28T00:39:38.568Z

## Reporter
- **Username**: nick_frichette_dd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Summary:** Typically, when an adversary gains access to stolen AWS IAM credentials they will [frequently](https://sysdig.com/blog/scarleteel-2-0/) test those credentials to see what access they have. They do this by performing API calls and seeing which succeed and which fail. There are even automated [tools](█████) to make this process easier. For defenders and security professionals, this behavior serves as a golden opportunity for detection as it likely involves generating a large number of failed API call attempts. If an adversary could enumerate permissions without logging to CloudTrail, they could perform this activity invisibly.

There are many categories of CloudTrail bypass. The specific variant we will be focussed on in this report has been referred to as “non-production endpoint permission enumeration CloudTrail bypass”. If you would like to learn more about it, you can find more details [here](https://securitylabs.datadoghq.com/articles/non-production-endpoints-as-an-attack-surface-in-aws/#silent-permission-enumeration). 

**We have found 26 non-production endpoints for the bedrock-agent service which can be used with standard IAM credentials, and do not log to CloudTrail.** While it is good that they don’t appear to have access to customer partition data, they can still be used for permission enumeration without logging to CloudTrail. 

AWS has previously [stated](https://securitylabs.datadoghq.com/articles/non-production-endpoints-as-an-attack-surface-in-aws/#the-response-from-aws) that this type of vulnerability should be reported. Specifically, “For isolated non-production endpoints that do not log to CloudTrail but are otherwise callable with normal credentials and exhibit normal IAM permission behavior, AWS considers the CloudTrail logging bypass of such endpoints also to be a security issue. If you find an API or APIs on an endpoint with these characteristics, please contact the AWS Security Team at aws-security@amazon.com”. 

As an aside, these endpoints appear to include AWS employee names or aliases in them. Presumably these are for test environments or something similar.

**Description:** 

## Steps To Reproduce:

To see an example of what should appear in CloudTrail when using normal production endpoints, perform the following AWS CLI operation with a sufficiently privileged IAM user or role:

```
aws bedrock-agent list-agents --region us-west-2
```

Wait approximately 5-10 minutes and a log will appear in CloudTrail. Next, perform the following AWS CLI operation:

```
aws bedrock-agent list-agents --region us-west-2 --endpoint-url ████████
```

After waiting 5-10 minutes (or longer), notice that it does not generate a log in CloudTrail. An adversary can perform this operation and depending on the response of the API make a determination if an Identity they have compromised does, or does not have permission to perform the operation. 

## Supporting Material/References:

* Indicate the Amazon service or product that this vulnerability occurs on:  

bedrock-agent  

* What type of Amazon AWS account(s) is needed to verify or reproduce this vulnerability?: 

Standard commercial partition account

* Estimated CVSS score and vector string: 

4.3 CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N/CR:X/IR:X/AR:X

* Estimated CWEs (comma separated): 

CWE-778: Insufficient Logging

* Have you already publicly disclosed any information on this issue? If so, when and where?: 

This specific example? No. This general technique? Yes, a lot actually. I’ve blogged about it [here](https://securitylabs.datadoghq.com/articles/non-production-endpoints-as-an-attack-surface-in-aws/#silent-permission-enumeration) and spoke about it at Black Hat USA 2023 (██████████) and fwd:cloudsec 2023 (█████████) [I have broken these links because HackerOne appeared to complain about them?] 

The following is a list of endpoints we found that exhibited this behavior.

* ████████
* ████
* █████
* ███████
* ████
* ██████████
* ███████
* ██████████
* ██████████
* ████
* ████
* ████████
* ████████
* █████████
* ██████████
* ████████
* ████████
* ████
* ██████████
* █████████
* ███████
* ████
* ████████
* ███████
* ████
* ██████

## Impact

## Summary: An adversary can enumerate permissions of compromised credentials for the bedrock-agent service without logging to CloudTrail.

## Attachments
No attachments
