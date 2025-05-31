# Subdomain takeover at http://test.www.midigator.com

## Report Details
- **Report ID**: 1718371
- **URL**: https://hackerone.com/reports/1718371
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-30T16:15:02.344Z
- **Disclosed**: 2022-11-12T16:05:05.413Z

## Reporter
- **Username**: valluvarsploit_h1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
## Vulnerability
Subdomain test.www.midigator.com points to an AWS S3 bucket that no longer exists. I was able to take control of this bucket and serve my own content on it.

## Proof Of Concept
```code
$ dig test.www.midigator.com
[snipped]
;; ANSWER SECTION:
test.www.midigator.com.	60	IN	CNAME	test.www.midigator.com.s3-website-us-west-1.amazonaws.com.
test.www.midigator.com.s3-website-us-west-1.amazonaws.com. 59 IN CNAME s3-website-us-west-1.amazonaws.com.
s3-website-us-west-1.amazonaws.com. 4 IN A	52.219.193.3
```

{F1963195}

## Remediation
Remove the CNAME entry for the `test.www.midigator.com`

## Impact

Subdomain Takeover

## Attachments
- image.png
