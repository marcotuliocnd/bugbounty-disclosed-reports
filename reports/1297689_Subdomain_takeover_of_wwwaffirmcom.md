# Subdomain takeover of www█████████.affirm.com

## Report Details
- **Report ID**: 1297689
- **URL**: https://hackerone.com/reports/1297689
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-10T05:53:37.861Z
- **Disclosed**: 2021-08-18T18:25:23.162Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: affirm

## Vulnerability Information
## Summary
Hi there, assuming you want this report as your policy mentions Affirm resources with third-parties, but the scope was a little unclear. Regardless, www█████.affirm.com points to an AWS S3 bucket `affirm-prod-www-cms█████████` that no longer exists. I was able to take control of this bucket and put my own content onto it. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.

If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.

**Note:** S3 has a weird quirk where the bucket's region may cause errors if a request to a bucket is addressed to the wrong region. I assume your CDN points to `████-2`, but my bucket is in `us-east-1`. When you make a request to this domain, S3 shows a redirect error because of this. If I wanted to move the bucket to the correct region (for the PoC to fully work), it would put it at risk of being claimed by attackers/others. Hopefully, this is enough for you.

### PoC
To see that the domain points to the `affirm-prod-www-cms█████` bucket:

```
% curl https://www██████████.affirm.com
[...]
<Code>PermanentRedirect</Code>
<Message>The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.</Message>
<Endpoint>s3.amazonaws.com</Endpoint>
<Bucket>affirm-prod-www-cms████</Bucket>
[...]
```

Following this redirect, to see the PoC:
```
% curl https://s3.amazonaws.com/affirm-prod-www-cms████████/index.html
<!-- taken over by hackerone.com/ian bugcrowd.com/iangcarroll ian@lhost.sh -->
```

## Impact

Subdomain takeover

## Attachments
No attachments
