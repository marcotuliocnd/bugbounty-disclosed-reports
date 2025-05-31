# Information Disclosure in AWS S3 Bucket

## Report Details
- **Report ID**: 163476
- **URL**: https://hackerone.com/reports/163476
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T05:10:19.679Z
- **Disclosed**: 2016-08-26T18:09:58.710Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi,

While this doesn't fall directly under the Program scope, I feel that the subject of this report is directly connected to the primary Legal Robot web properties and would like to inform your team in case this was a misconfiguration concern.

I noticed that **legalrobot.amazonaws.com** is configured to display a publicly readable root directory listing, and believe this AWS S3 bucket may be associated with Legal Robot systems.

It is possible to read data from this bucket; AWS GET requests (from the v2 API) can also be used to retrieve modified data views. Given that buckets with other name permutations are set to `AccessDenied`, this appears to be an **ACL misconfiguration**.

In terms of attack scenario, if Legal Robot engineers upload new sensitive material (e.g. proprietary data) to the bucket, believing that the ACL is correctly configured, there may be a risk to Legal Robot as a result, hence why all other buckets are restricted.

Unfortunately my personal AWS account is inactive, so I have been unable to confirm the ability of an unaffiliated user writing files into the **legalrobot** bucket.

Thanks!

## Attachments
No attachments
