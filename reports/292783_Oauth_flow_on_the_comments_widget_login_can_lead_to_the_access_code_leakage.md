# Oauth flow on the comments widget login can lead to the access code leakage

## Report Details
- **Report ID**: 292783
- **URL**: https://hackerone.com/reports/292783
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-24T13:49:34.571Z
- **Disclosed**: 2017-11-24T13:52:31.378Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
##Description
Hello. Here is a keyword: `frog`
I discovered an little Oauth flow in the comments widget authentication process using redirect_uri manipulations.
The widget located on the all blogposts, which have URL
```
https://edoverflow.com/2017/[post-title]/
```
Upon authentication, it appeared that `code` parameter gets stripped from the URL after successful authentication, so there was no visible way to do the leakage thorugh, for example, Referer header upon clicking some external link in the blogpost.
At this time, i noticed the only one code leakage to the 
```
https://fonts.googleapis.com/css?family=Inconsolata
```
upon `code` verification (since it returned 200 OK) but it appeared not very serious issue for me, and i digged deeper.
I discovered, that it was possible to manipulate the `redirect_uri` parameter, using the arbitrary directories, since it looked like whole `https://edoverflow.com` URL was whitelisted.
So, i tried next URL, to non-existent path /1:
```
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252F1%26scope%3Dpublic_repo
```
{F242032}
and... code was not stripped. So it became clear for me, that the code strips only on pages with a comment widget.
Next, i tried to find some place, where i can post arbitrary content (like images), with controlled src, to leak the code through Referer. Unfortunately (or fortunately) site used content proxying through GitHub - so my dream about `High` impact had not came true:)
So my last hope was at least leak the code to the some external sites, and i came across this link:
```
https://edoverflow.com/about/
```
and
```
https://edoverflow.com/metadata
```
Using 
```
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252Fabout%252f%26scope%3Dpublic_repo
```
and same link with `/metadata` path,
i was able to leak the access code with user interaction to the several sites in the Referer header, like `keybase.io`, `liberapay.com`, `hackerone.com`, `crypto101.io`, `twitter.com`, `youtube.com` and several Press sites like Bloomberg.

##Suggested Fix
I suggest to restrict the `redirect_uri` only to the blogposts path, to prevent `code` leakage in the other parts of the site, and secure external links from possible Referer leakage, just in case.

## Impact

The severity was set as low, because attacker can't directly conduct the authentication bypass against victim, in case attacker is not an admin of the one of the external sites=). 
Still, there was some risks, so issue was reported in several minutes after discovery

## Attachments
- 12.JPG
