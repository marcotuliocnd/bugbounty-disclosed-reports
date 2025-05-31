# Cache poisoning DoS to various TTS assets

## Report Details
- **Report ID**: 728664
- **URL**: https://hackerone.com/reports/728664
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-04T07:36:48.616Z
- **Disclosed**: 2020-03-12T16:02:40.277Z

## Reporter
- **Username**: nathand
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
I have recently come across a technique to force a Cloudfoundry app to return a HTTP 404 error when requesting any resource, which contains cache friendly headers. What this means is, if the Cloudfoundry app in question is behind a web cache like Cloudfront or Cloudflare etc, it will possibly store a copy of the 404 error response as the cache for the resource being requested, which is served to other users. This describes a cache poisoning Denial of Service, and the concept for this is detailed at https://cpdos.org.

The technique to achieve CPDoS against a Cloudfoundry and hence TTS app is to send a request with the following header:

```
X-CF-APP-INSTANCE
```

This header is designed to allow admins to debug CF apps, by choosing which app instance they want serving their request. However, if we supply this header with a bad value, it will force the gorouter in the Cloudfoundry stack to issue a HTTP 404, e.g.:

```
X-CF-APP-INSTANCE: xxx:1
```

**Please note: I have already reported this to Pivotal/Cloudfoundry by contacting their security email address directly.** They have not yet confirmed the vulnerability, although I'm fairly confident the issue exists in gorouter. However, I thought it relevant to report this to you regardless, as you should be able to mitigate this vulnerability without waiting for Pivotal to release an update for gorouter, by configuring your web caches/WAFs appropriately (don't cache 404's, strip out this header etc). With that said, I understand if this report is not valid due to this - if this is the case, a heads up so I can close it from my end would be appreciated.

The following assets appear to be vulnerable:

```
analytics.usa.gov
federation.data.gov
18f.gsa.gov
code.gov
```

Please note that this is not an exhaustive list as I did not test against every asset in scope, however I did attempt the poisoning against `login.gov` and did not succeed, which I suspect might be because `login.gov` is specifically configured not to cache 404 errors. With that said, the config for `login.gov` may provide a means to protect the above listed assets and others that may be vulnerable.

## Proof of concept

To poison the cache for a resource, the following script can be used - in this case, `https://federation.data.gov/?cb=xxx` is being poisoned to serve a 404 error to other users. Please note the presence of the `?cb=xxx` query string - this is designed to be a "cache buster", to prevent poisoning the real home page. You may need to change the cache buster value to avoid hitting a previous successful cached copy.

```
#!/bin/bash

while true
do
    printf 'GET /?cb=xxx HTTP/1.1\r\n'\
'Host: federation.data.gov\r\n'\
'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0\r\n'\
'Accept: */*\r\n'\
'Accept-Language: en-US,en;q=0.5\r\n'\
'Accept-Encoding: gzip, deflate\r\n'\
'X-CF-APP-INSTANCE: xxx:1\r\n'\
'Connection: close\r\n'\
'\r\n'\
    | openssl s_client -ign_eof -connect federation.data.gov:443
    sleep 1
done
```

(FYI the poisoning script can probably sleep longer than 1 second - this is just to make sure the poisoning takes effect)

You should see 404 errors being returned in this script's output. Because the web cache appears to key on `Cookie` header values, this will only poison the cache for users without a pre-existing cookie for the domain (i.e. new users). This can be demonstrated by the following curl command (or by accessing the resource in a private browser window session without pre-existing cookies):

```
curl -i -s -k -X $'GET' \
    -H $'Host: federation.data.gov' -H $'Accept-Encoding: gzip, deflate' -H $'Connection: close' \
    $'https://federation.data.gov/?cb=xxx'
```

If there are specific resources and assets which don't key cache on cookie headers, then these will probably be easier to exploit against more users. 

In this asset's case, the error will be:

```
404 Not Found: Requested route ('cg-06ab120d-836f-49a2-bc22-9dfb1585c3c6.app.cloud.gov') does not exist.
```

A bonus here is this error reveals an "internal" hostname otherwise not accessible to an attacker.

Given the assets all appear to use Cloudfront for caching, it is true that the poisoning will be regional - however, it is fairly trivial to acquire VPS' around the world (or perhaps just around the US in this case) to poison specific regions, and using a tool like https://www.nexcess.net/web-tools/dns-checker/, an attacker may be able to determine regional IPs for the asset, and poison regions by directly targeting them (not confirmed - I was aware of a technique to do this but was unable to confirm this).

One thing I did notice is these poisoning attacker requests may not hit the app logs in Cloudfoundry, e.g. the `cf logs APP_NAME` output, since it errors at the gorouter. If you have app logging dependent on displaying what is visible in the CF app logs, it may not detect these attacks.

## Impact

By exploiting this vulnerability, an attacker may be able to achieve denial of service for various TTS assets, particularly to new users.

## Attachments
No attachments
