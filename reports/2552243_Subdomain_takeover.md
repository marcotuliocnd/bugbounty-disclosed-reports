# Subdomain takeover ██████

## Report Details
- **Report ID**: 2552243
- **URL**: https://hackerone.com/reports/2552243
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-06-14T10:58:46.768Z
- **Disclosed**: 2024-07-26T14:59:11.721Z

## Reporter
- **Username**: martinvw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The subdomain `█████` is pointing to `open-elb-prod-277276106.us-east-1.elb-amazonaws.com.`, the domain `elb-amazonaws.com` was available for registration

## Impact

Using this vulnerability an attacker can:
- host unwanted/malicious content under your domain
- receive email on subdomains mentioned above
- effectively execute cross-site scripting attacks
- in some cases, steal cookie data
- in some cases, trick password managers into filling in passwords

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit http://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt

## Suggested Mitigation/Remediation Actions
Remove CNAME record █████



## Attachments
No attachments
