# SSRF in webhooks leads to AWS private keys disclosure

## Report Details
- **Report ID**: 508459
- **URL**: https://hackerone.com/reports/508459
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-12T14:32:57.330Z
- **Disclosed**: 2019-06-28T06:49:12.422Z

## Reporter
- **Username**: honoki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Vulnerability Summary

Omise makes use of Amazon AWS as their application environment. Due to a vulnerability in the way webhooks are implemented, an attacker can make arbitrary HTTP/HTTPS requests from the application server and read their responses. This is known as a server-side request forgery (SSRF) vulnerability.

This vulnerability leads to access to Omise's Amazon EC2 instance with the user role `aws-opsworks-ec2-role`, including AWS private keys.

## Description

The vulnerability exists in the way webhooks follow redirects. In general, it appears that redirects are not followed, but a HTTP 303 See Other status code allows an attacker to bypass this restriction.

By pointing my webhook URL to a server that issues a 303 redirect, I am able to redirect and read the responses of arbitrary HTTP/HTTPS requests from the application server. E.g. the following PHP script results in a successful request that is followed by the server:

`<?php header('Location: http://<arbitrary-location>', TRUE, 303); ?>`

As a result, it is possible to request a number of things, including AWS credentials on the metadata server located at `http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-opsworks-ec2-role`

## Steps to reproduce

* Host the following payload on `https://<your-attacker-server>/redir.php`:

````
<?php header('Location: http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-opsworks-ec2-role', TRUE, 303); ?>
````
* Point your webhook endpoint on https://dashboard.omise.co/test/webhooks/edit to `https://<your-attacker-server>/redir.php`
* Make a random call to the API, e.g. adding a user;
* View the "Recent Deliveries" of the webhook calls on https://dashboard.omise.co/test/webhooks
* Note the `200 OK` status code indicating a successful redirect
* Click the event to view the response body of the AWS metadata

## Recommendation

I recommend to ensure all input provided to the endpoint is validated. In this case, ensure that 303 redirects are not followed either.

I also recommend resetting all AWS access tokens. In addition, I recommend reviewing the Amazon access logs to investigate if this vulnerbility has been exploited in the past.

## Attachments

* **20190312_AWS-SSRF-303-redirect-2.png** - Screenshot showing the output of the AWS credentials obtained through the SSRF vulnerability.
* **20190312_AWS-SSRF-303-redirect.png** - Screenshot showing the output of the AWS index of metadata.

## Impact

By exploiting this vulnerability, an unauthorized attacker could gain access to the AWS environment of Omise. Note that the SSRF vulnerability could be abused in a variety of ways, not just limited to obtaining AWS credentials. For example, to enumerate and access services and web applications running on the internal network.

## Attachments
- 20190312_AWS-SSRF-303-redirect-2.png
- 20190312_AWS-SSRF-303-redirect.png
