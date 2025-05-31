# HTTP 401 response injection on "amp.twimg.com/amplify-web-player/prod/source.html" through "image_src" parameter

## Report Details
- **Report ID**: 221328
- **URL**: https://hackerone.com/reports/221328
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-16T05:28:10.070Z
- **Disclosed**: 2017-05-08T17:57:25.706Z

## Reporter
- **Username**: zlz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
# Overview
> The `image_src` parameter on `amp.twimg.com` accepts images from any arbitrary host, therefore, enabling attackers to supply image destinations that respond with a "HTTP 401 Unauthorized" response.

# Description
> HTTP 401 attacks occur when there is no whitelisting or proxying images and/or pages that are autoloaded into the page. The issue with these attacks is that (1) users are prompted to enter credentials that are sent to a potentially attacker owned host, and (2) information disclosure concerning the IP address/browser details of the user.

> {F176242}
> * Here is an example prompt displayed when a user runs this with internet explorer. The website could be changed to something more succeptible, e.x. "twitler.com".

# Proof of concept
> The full URL with the payload included is located here:
https://amp.twimg.com/amplify-web-player/prod/source.html?url=n/a&image_src=https://897theriver.com/admin&player_swf_url=https://897theriver.com/admin&page=amplify_card

### Below are the steps to follow
> 1. Load the following page on the current Firefox, internet explorer, or Safari version.
> 1. Modify the "image_src" parameter to a page ran by yourself with a 401 response (e.x. http://897theriver.com/admin).
> 1. Load the page

# Impact
> Since the victim is not expecting the "401 Unauthorized" prompt that forwards credentials to an attacker, he/she will most likely enter their credentials expecting the panel to be owned by Twitter (kind of like iframing a login panel on an XSS). If this were any less severe it would be most likely categorized as "having too much user interaction", but since it is very in your face, *enter credentials* I decided to report it.

> This attack could easily be used to gather data and steal accounts.

# Remediation
> Proxy/whitelist images included on the page. An example script would only allow images from a certain host and/or load the images into twimg (twimg.com/proxy.php?image=remote), then display them to the user.

## Attachments
- prompt.PNG
