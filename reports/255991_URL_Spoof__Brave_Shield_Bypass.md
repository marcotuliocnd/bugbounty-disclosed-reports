# URL Spoof / Brave Shield Bypass

## Report Details
- **Report ID**: 255991
- **URL**: https://hackerone.com/reports/255991
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-03T03:33:55.679Z
- **Disclosed**: 2017-08-31T21:48:19.844Z

## Reporter
- **Username**: mattaustin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Improper URL parsing in Brave allows an attacker to spoof the hostname shield settings are applied to.

## POC:
https://youtu.be/yz99T_Trfuc

## Products affected: 

 * Brave (browser-laptop) 0.18.14 rev ad92d02

## Steps To Reproduce:

 1. Browse to http://brave.com
 2. Click on the Shield icon and toggle the shield from "up" to "down"
 3. Browse to http://brave.com%60x.code-fu.org/ and notice the shield is down for this domain as well. 

I believe this could be used enable flash by spoofing one of the "whitelisted" domains. 

The renderer will load the code-fu.org domain, however I believe when the  URL is later parsed in node it uses (non standards compliant?) url.parse. This leads to some confusion: 

``` javascript
> url.parse('http://brave.com%60x.code-fu.org/')
Url {
  href: 'http://brave.com/%60x.code-fu.org/'
  protocol: 'http:',
  host: 'brave.com',
  hostname: 'brave.com',
  pathname: '%60x.code-fu.org/',
  path: '%60x.code-fu.org/',
}
```

vs

``` javascript
> new url.URL('http://brave.com%60x.code-fu.org/')
URL {
  href: 'http://brave.com`x.code-fu.org/',
  protocol: 'http:',
  host: 'brave.com`x.code-fu.org',
  hostname: 'brave.com`x.code-fu.org',
  pathname: '/',
}
```

Node now (7+) supports the the WHATWG through the [url.URL](https://nodejs.org/api/url.html#url_the_whatwg_url_api) . This seems to be the same / compatible with the way the render / chrome parses the URL. 


## Attachments
- Screenshot_2017-08-02_20.32.28.png
