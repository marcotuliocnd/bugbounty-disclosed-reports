# Amazon Kendra Intelligent Ranking Service Reporting "AWS Internal" for CloudTrail Events Generated from FIPS Endpoints

## Report Details
- **Report ID**: 3044471
- **URL**: https://hackerone.com/reports/3044471
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-03-18T15:27:46.002Z
- **Disclosed**: 2025-05-28T00:24:53.437Z

## Reporter
- **Username**: nick_frichette_dd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aws_vdp

## Vulnerability Information
**Description:** When performing calls to the AWS API, [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) is responsible for logging that API activity for customers. These CloudTrail event logs contain information about the API call, when it was performed, by whom, etc. 

**We have found 4 API endpoints for the Kendra Intelligent Ranking service that incorrectly report the user-agent and network information as "AWS Internal"**. As a result of this, an adversary can perform API calls using these endpoints and evade the logging of their IP address/operating system information. 

As a coincidence, these 4 API endpoints are all FIPS endpoints. This is similar to a previous bug we submitted for the [Comprehend Medical Service](██████████) leading me to believe this may be a wider issue across a small number of services.

## Steps To Reproduce:

First, as a base line, perform the following AWS CLI command:

```
aws kendra-ranking list-rescore-execution-████ans
```

Wait 5-10 minutes for this event to appear in CloudTrail. From here, inspect the CloudTrail log and see that the UserAgent field is populated, as well as the source IP address. 

Next, run the following command:

```
aws kendra-ranking list-rescore-execution-███ans --endpoint-url ████████
```

Wait 5-10 minutes for this event to appear in CloudTrail. From here, inspect the CloudTrail log and see that the UserAgent field and network information is "AWS Internal". Because of this endpoint we used, we cannot see the request information which may degrade a defenders ability to track down an adversary.

## List of endpoints exhibiting this behavior
* █████████
* ███████
* ███
███████:
An adversary can use these endpoints to avoid disclosing their source IP address or user agent information to the victim.

## Attachments
No attachments
