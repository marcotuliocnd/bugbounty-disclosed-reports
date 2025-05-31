# Subdomain takeover on s3.shopify.com

## Report Details
- **Report ID**: 207576
- **URL**: https://hackerone.com/reports/207576
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-20T00:48:19.644Z
- **Disclosed**: 2017-02-27T23:30:20.507Z

## Reporter
- **Username**: avlidienbrunn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Preword**
I know that this is not explicitly in scope, but I still felt it was serious enough to justify a report and let you decide the potential impact.

**Description**
The subdomain s3.shopify.com was pointed using CNAME to Amazon S3, but no bucket with that name was registered. This meant that anyone could sign up for Amazon S3, claim the bucket as their own and then serve content on s3.shopify.com.

DNS record:
```
s3.shopify.com.		3599	IN	CNAME	shopify-assets.s3.amazonaws.com.
shopify-assets.s3.amazonaws.com. 7518 IN CNAME	s3-directional-w.amazonaws.com.
s3-directional-w.amazonaws.com.	7218 IN	CNAME	s3-1-w.amazonaws.com.
s3-1-w.amazonaws.com.	4	IN	A	52.216.80.56
```


**Impact**
This could be used as stored XSS by uploading a HTML page.

Given that the attacker could control all the content (even at /), it could also make for a pretty convincing phishing page.

Last, if any of your application relies on s3.shopify.com any of the data sent/fetched there could be controlled by an attacker.

**Mitigation/PoC**
I have claimed the bucket on my account and disabled use except for the following URL:
http://s3.shopify.com/xss_unguessable3211231232.html

This means that nobody else can claim the bucket and add content.

**Fix**
Remove the s3.shopify.com DNS entry. Alternatively, if you wish to use s3.shopify.com with S3, tell me in a comment and I will remove the bucket from my Amazon account.

## Attachments
No attachments
