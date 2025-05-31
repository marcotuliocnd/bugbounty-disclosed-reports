# Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io

## Report Details
- **Report ID**: 794382
- **URL**: https://hackerone.com/reports/794382
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-12T10:38:37.420Z
- **Disclosed**: 2021-01-16T06:07:13.398Z

## Reporter
- **Username**: rhynorater
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
## Summary:
I discovered that it was possible to takeover ` test-cncf-aws.canary.k8s.io` by assigning a zone to that name with one of the following nameservers in Route53:
```
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-265.awsdns-33.com.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-687.awsdns-21.net.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1458.awsdns-54.org.
test-cncf-aws.canary.k8s.io. 3600 IN    NS      ns-1825.awsdns-36.co.uk.
```
Once the zone was claimed, I was able to create DNS records under this host. Consider the following record:
```
poc.test-cncf-aws.canary.k8s.io
```

##Steps To Reproduce:
1. See above domain

##Remediation Instructions
Remove the NS record delegation NS privs on a subdomain before you delete the zone

## Impact

With this vulnerability, an attacker can host arbitrary content under your domain. This can allow an attacker to host brand-damaging materials, steal sensitive * scoped session cookies, and even escalate other vulnerabilities.

## Attachments
No attachments
