# Take over subdomains of r2.dev using R2 custom domains

## Report Details
- **Report ID**: 1700276
- **URL**: https://hackerone.com/reports/1700276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-14T16:05:12.886Z
- **Disclosed**: 2022-09-28T12:49:46.895Z

## Reporter
- **Username**: albertspedersen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cloudflare

## Vulnerability Information
> **███████** ████ [████ █████████]██████████████████ ███ ██████████

It is possible to take over any subdomain of `r2.dev` (possible also the base domain) and have it serve the contents of an R2 bucket in your account.

### Requirements

Access to R2 public buckets in the dashboard is currently behind a flag. The server-side check for access to R2 public buckets was recently removed, so you can just use an mitmproxy script to toggle the flag client-side.

```py
import json
import mitmproxy
import re


class R2PublicBuckets:
	async def response(self, flow: mitmproxy.http.HTTPFlow):
		if re.match(r'https?://dash\.cloudflare\.com/api/v4/accounts/[0-9a-f]{32}/flags', flow.request.url):
			data = json.loads(flow.response.text)
			data['result']['workers']['r2_publicbuckets'] = True
			flow.response.text = json.dumps(data, separators=(',', ':'))

addons = [
	R2PublicBuckets()
]
```

### Steps

1. Add `r2.dev` to your Cloudflare account and follow the steps until you're asked to complete zone ownership verification.

2. Create an R2 bucket if you don't already have one and add e.g. `albert.r2.dev` as a custom domain in the "Domain Access" section.

{F1926348}

3. Wait a few seconds and then refresh the page. The custom domain should now show "Status: Active". In case "Access to Bucket" is "Not allowed", click the three dots besides the domain and then "Enable domain".

{F1926346}

4. Visit the custom domain and notice how it serves content from your R2 bucket.

{F1926347}

Additionally, this vulnerability can also be used to *block* another domain from being used as an R2 custom domain. Simply repeat step one and two for the target zone/domain. If the user tries to add the domain as a custom domain for their R2 bucket, the API will throw an error and the custom domain will be activated in your account. The target domain will then serve the contents of your bucket until the user deletes the custom domain (which will show "Status: Error") on their end. An example of this is https://r2.walshy.dev/.

### Cause

This vulnerability exists because the API does not check if the zone is active before adding the specified domain as an SSL for SaaS custom hostname. I presume taking over subdomains of `r2.dev` is only possible because they're in the same zone as the fallback origin, and/or there's already a CNAME record on `*.r2.dev` pointing to the fallback origin (`public.r2.dev`).

## Impact

Every R2 bucket has a `pub-<public_id>.r2.dev` subdomain which, when public bucket access is enabled, will serve the contents of the bucket. This vulnerability can be used to take over those subdomains and instead have them serve content from your bucket.

## Attachments
- custom-domain-active.png
- visit-custom-domain.png
- add-custom-domain.png
