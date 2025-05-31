# Subdomain takeover in Gitlab pages

## Report Details
- **Report ID**: 2523654
- **URL**: https://hackerone.com/reports/2523654
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-05-28T21:00:46.022Z
- **Disclosed**: 2024-10-09T16:07:19.493Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

It's possible for an attacker to take over a dangling custom domain pointing to GitLabPages using `instanceX.gitlab.io'

The problems arises when adding a custom domain to Gitlab Pages, without the domain being verified it still servers content (allowing 7 days before disabling it)

### Steps to reproduce

I did some tests with gitlab.com domains, `docs-dev.gitlab.com` worked correctly. 
The domain has the following fingerprints:

Dig  
```
docs-dev.gitlab.com.    300     IN      CNAME   gitlab-com.gitlab.io.
gitlab-com.gitlab.io.   300     IN      A       35.185.44.232
```
And going to the URL shows:

```
HTTP/1.1 302 Found
content-type: text/html; charset=utf-8
location: https://projects.staging.gitlab.io/auth?domain=http://docs-dev.gitlab.com&state=giZFQTsOOFXvR_0po68zrg==
permissions-policy: interest-cohort=()
set-cookie: gitlab-pages=..._; Path=/auth; Expires=Tue, 28 May 2024 21:07:33 GMT; Max-Age=600; HttpOnly
vary: Origin
date: Tue, 28 May 2024 20:57:33 GMT
gitlab-lb: haproxy-pages-01-lb-gstg
gitlab-sv: pages-us-east1-c

HTTP/2 401 
content-type: text/html; charset=utf-8
permissions-policy: interest-cohort=()
vary: Origin
x-content-type-options: nosniff
content-length: 2872
date: Tue, 28 May 2024 20:57:34 GMT

```

1. Create a GitLab pages using this project (https://gitlab.com/g15391522/pn1)
2. Go to  **Deploy** ->  ** Pages ** 
3. Disable `Force HTTPS (requires valid certificates)` 
4. Add the target custom domain and click in Save

Go to http://docs-dev.gitlab.com/

Now the content of the site will be :

{F3307313}

## Impact

They could perform several attacks like:

   -  Cookie Stealing
   - Phishing campaigns.
   - Bypass Content-Security Policies and CORS.

## Attachments
- image.png
