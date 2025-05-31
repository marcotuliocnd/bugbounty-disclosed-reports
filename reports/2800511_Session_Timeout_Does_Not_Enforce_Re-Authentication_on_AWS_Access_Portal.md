# Session Timeout Does Not Enforce Re-Authentication on AWS Access Portal

## Report Details
- **Report ID**: 2800511
- **URL**: https://hackerone.com/reports/2800511
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-24T05:16:13.742Z
- **Disclosed**: 2025-03-05T19:56:29.925Z

## Reporter
- **Username**: xendaviour
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
> NOTE! Thanks for submitting a report to Amazon Web Services! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** [AWS SSO allows re-access to the AWS Access Portal without re-authentication after a session timeout, potentially bypassing expected security controls..]

**Description:** [After the session timeout period is reached, users are correctly logged out of the AWS Management Console. However, they are still able to access the AWS Access Portal and re-login without needing to re-authenticate. This behavior circumvents the expected session management security, where users should be required to fully re-authenticate (via AWS SSO) after a session has expired. This could lead to unauthorized access if the session is left unattended.]

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. [Log into the AWS Management Console using AWS SSO.]
  2. [Wait for the session timeout period to elapse.]
  3. [Attempt to access the AWS Access Portal via [████████]]
4.[Observe that despite the session timeout, you can access the portal and login without re-authenticating.]

## For IAM AuthZ issues
* [Raw JSON policy used for testing]
* [web console]

## Remediation Instructions
The session expiration should be consistently enforced across the AWS Management Console and AWS Access Portal. After session timeout, users should be required to fully re-authenticate via AWS SSO before gaining access again.) 

## Supporting Material/References:

* Indicate the Amazon service or product that this vulnerability occurs on: (AWS S3, Amazon Lambda, etc): Amazon service or product affected: AWS IAM Identity Center (formerly AWS SSO), AWS Access Portal

* What type of Amazon AWS account(s) is needed to verify or reproduce this vulnerability?:  Amazon AWS account(s) needed to reproduce: An AWS account using AWS SSO with a session timeout policy in place.

* Estimated CVSS score and vector string. (We currently use CVSS :3.1 for scoring)
CVSS 3.1 Score: 6.3 (Medium)

* Estimated CWEs (comma separated)
CWE-613: Insufficient Session Expiration, CWE-288: Authentication Bypass
* Have you already publicly disclosed any information on this issue? If so, when and where?
no
* Would you like to blog or present on the submission? if so, would you like your content reviewed by AWS subject matter experts and feedback provided?
yes
* Any documentation links or other relevant links
URL where the issue was observed: [██████████]

## Impact

## Summary:
1. Data Breaches

    Unauthorized Access to Sensitive Data: Attackers could exploit this vulnerability to gain access to confidential information, including customer data, financial information, and proprietary business processes, leading to data breaches.

2. Compliance Violations

    Regulatory Non-Compliance: If sensitive data is accessed without proper authentication, it may violate compliance regulations such as GDPR, HIPAA, or PCI-DSS, resulting in legal repercussions and financial penalties for the organization.

3. Loss of Trust

    Reputational Damage: If customers or stakeholders become aware of unauthorized access to sensitive information, it could lead to a loss of trust in the organization, damaging its reputation and customer relationships.

4. Account Takeover

    Unauthorized Actions: An attacker gaining access could perform actions on behalf of the legitimate user, such as modifying configurations, accessing billing information, or launching unauthorized resources, potentially leading to further security incidents.

5. Increased Attack Surface

    Expanded Vulnerability Exposure: The ability to access services without proper authentication can be leveraged by attackers to further exploit vulnerabilities within the AWS environment, leading to a cascading effect of security risks.

6. Potential Financial Loss

    Cost of Incident Response: Organizations may incur significant costs in investigating the breach, rectifying security vulnerabilities, and implementing additional security measures to prevent future incidents.

7. Operational Disruption

    Interference with Business Operations: Unauthorized actions taken by an attacker can disrupt business operations, leading to downtime or degraded service performance.

Summary

The overall impact of this vulnerability poses a high risk to the organization, primarily affecting data confidentiality, compliance standing, and organizational reputation. Addressing the vulnerability is crucial to maintaining trust, security, and operational integrity in cloud services.

## Attachments
No attachments
