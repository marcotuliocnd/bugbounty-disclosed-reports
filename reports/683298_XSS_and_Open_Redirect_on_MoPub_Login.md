# XSS and Open Redirect on MoPub Login

## Report Details
- **Report ID**: 683298
- **URL**: https://hackerone.com/reports/683298
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-08-27T23:07:07.662Z
- **Disclosed**: 2019-09-24T23:18:02.369Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** I found open redirect at the MoPub login page, https://app.mopub.com/login?next=https://google.com. It also allows javascript URIs, leading to XSS.


**Description:** You can modify the "next" URL parameter to redirect to any website upon logging in on MoPub. 

## Steps To Reproduce:

1. Take this URL: https://app.mopub.com/login?next=https://google.com
2. Change "https://google.com" to whatever URL you want to redirect to.
3. Visit the URL and login
4. You will be redirected to that site

## Impact: Outlined in Impact section below

## Supporting Material/References:

Here's a proof of concept using the URL javascript:alert("proof of concept"):
{F568245}

## Impact

An attacker could use this for phishing, cookie jacking, etc. since it allows javascript URIs and therefore XSS vectors. Additionally, they could use URL encoding to hide the URL that the victim is being redirected to.

## Attachments
- d075ed6487c103b8c497250d385fe75f.mp4
