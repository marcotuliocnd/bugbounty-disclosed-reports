# Subdomain Takeover on  delivey.yelp.com 

## Report Details
- **Report ID**: 1715538
- **URL**: https://hackerone.com/reports/1715538
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-28T14:45:13.380Z
- **Disclosed**: 2022-11-12T15:49:34.354Z

## Reporter
- **Username**: racersaravanaa05
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
[Subdomain takeover vulnerabilities occur when a subdomain (delivery.yelp.com) is pointing to a service]
Vulnerable url : delivery.yelp.com
This is an [verify Link](http://delivery.yelp.com.s3-website-us-east-1.amazonaws.com/).
{F1959331}

## Platform(s) Affected:
[website  ]


## Steps To Reproduce

  1. [Create the Amazon S3 Bucket on this Name : delivery.yelp.com]
{F1959320}
  1. [then Upload the Attacker HTML web page]
  1. [then using Static Web hosting ]

## Supporting Material/References:
{F1959332}

Remediation
Remove the cname entry or claim the subdomain delivey.yelp.com on amazon aws

## Impact

Risk
fake website
malicious code injection
users tricking
company impersonation
This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

Best Regards, 
Racer Saravanaa 05

## Attachments
- Screenshot_(104).png
- Screenshot_(105).png
- 2022-09-28_20-02-52.mp4
