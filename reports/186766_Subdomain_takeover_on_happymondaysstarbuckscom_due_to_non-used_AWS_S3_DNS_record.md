# Subdomain takeover on happymondays.starbucks.com due to non-used AWS S3 DNS record

## Report Details
- **Report ID**: 186766
- **URL**: https://hackerone.com/reports/186766
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-30T06:19:05.330Z
- **Disclosed**: 2016-12-19T22:59:42.194Z

## Reporter
- **Username**: dpgribkov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

I discovered that happymondays.starbucks.com DNS CNAME record is pointing to S3 AWS bucket which doesn't exist. Here's the screenshot of vulnerable domain: {F138556}

As happymondays.starbucks.com was free to register on AWS S3 service and DNS-setup is already correct set-up: {F138557} 
I was able to claim the domain for PoC using the following set-up:  {F138558}
Also I have placed a two files located under root directory for validation: {F138559}
For mitigation you should immediately remove the DNS-entry for this domain. 

As you might consider, the impact of this are pretty significant. I now can publish whatever I want on this domain, even fetching httpOnly cookies. I would also be able to register SSL certificate for this domain through Let's Encrypt (it is only need meta/file verification to issue the certificate) That would end up with the ability to read secure cookies as well.

In addition, there's no way at all for a visitor of this page to validate that the content on this domain is not served by Starbucks, making it extremely easy to utilize this for targeting the organization by fake login forms / spear phishing using your own domain to plant the attack.

Cheers,
Danil





## Attachments
- Screenshot_from_2016-11-30_00-50-20.png
- Screenshot_from_2016-11-30_00-58-45.png
- Screenshot_from_2016-11-30_01-02-09.png
- Screenshot_from_2016-11-30_01-08-17.png
