# Amazon Comprehend Medical Service Reporting "AWS Internal" for CloudTrail Events Generated from FIPS Endpoints

## Report Details
- **Report ID**: 2979238
- **URL**: https://hackerone.com/reports/2979238
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-02-06T20:29:40.147Z
- **Disclosed**: 2025-02-25T20:52:51.220Z

## Reporter
- **Username**: nick_frichette_dd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Description:** When performing calls to the AWS API, [AWS CloudTrail](██████) is responsible for logging that API activity for customers. These CloudTrail event logs contain information about the API call, when it was performed, by whom, etc. 

**We have found 8 API endpoints for the Comprehend Medical service that incorrectly report the user-agent and network information as "AWS Internal"**. As a result of this, an adversary can perform API calls using these endpoints and evade the logging of their IP address/operating system information. 

As a coincidence, these 8 API endpoints are all FIPS endpoints. It's entirely possible that this was an intentional decision, however I haven't run into it before and therefore wanted to report it in case that was not the case.

## Steps To Reproduce:

First, as a base line, perform the following AWS CLI command:

```
aws comprehendmedical list-phi-detection-jobs
```

Wait 5-10 minutes for this event to appear in CloudTrail. From here, inspect the CloudTrail log and see that the UserAgent field is populated, as well as the source IP address. 

Next, run the following command:

```
aws comprehendmedical list-phi-detection-jobs --endpoint-url █████████
```

Wait 5-10 minutes for this event to appear in CloudTrail. From here, inspect the CloudTrail log and see that the UserAgent field and network information is "AWS Internal". Because of this endpoint we used, we cannot see the request information which may degrade a defenders ability to track down an adversary.

## List of endpoints exhibiting this behavior
* ████████
* comprehendmedical-fips.us-east-1.api.aws
* ████
* ███████
* ███
* █████
* ████████
* ██████

## Impact

## Summary:
An adversary can use these endpoints to avoid disclosing their source IP address or user agent information to the victim.

## Attachments
No attachments
