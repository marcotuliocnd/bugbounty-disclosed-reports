# [CRITICAL]-Taking over entire subdomain of romit.io

## Report Details
- **Report ID**: 173681
- **URL**: https://hackerone.com/reports/173681
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-03T16:17:52.265Z
- **Disclosed**: 2016-10-03T17:24:46.821Z

## Reporter
- **Username**: ehsahil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: enter

## Vulnerability Information
Hi, 

During recon, I found out that `blog.romit.io` was not mapped with `wordpress.com` and the domain was   returning back error like `this domain has not been mapped with wordpress.com, to map it please login into wordpres.com`. 

So, I quickly created an account on `wordpress.com` and mapped `blog.romit.io` by paying **13USD** from my credit card. 

So, **I become the admin of blog.romit.io** for just 13USD.

**Proof of concept:**

Just visit `https://blog.romit.io`. 

**Impact**: This issue can have really huge impact on the companies reputation someone can post malicious content on the blog and then romit.io users will think its official but its **NOT**. 

**FIX?**

1. You can delete the **CNAME** entry for `blog.romit.io`

or.. 

2. You can have my wordpress.com credentials. 

Please see attached screenshots.

Thanks 
-@gone

## Attachments
- Screen_Shot_2016-10-03_at_9.38.30_PM.png
- Screen_Shot_2016-10-03_at_9.38.10_PM.png
