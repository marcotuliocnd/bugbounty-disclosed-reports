# SSRF in proxy.duckduckgo.com via the image_host parameter

## Report Details
- **Report ID**: 358119
- **URL**: https://hackerone.com/reports/358119
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-27T15:39:32.113Z
- **Disclosed**: 2018-08-15T14:46:32.647Z

## Reporter
- **Username**: fpatrik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
# Description

https://proxy.duckduckgo.com/iur/ endpoint is vulnerable to ssrf via image_host
get parameter.

## Vulnerable URL:
https://proxy.duckduckgo.com/iur/?f=1&image_host=https://tudomanyok.hu/

## Some internal URL:
https://proxy.duckduckgo.com/iur/?f=1&image_host=https://127.0.0.1:18091/
http://127.0.0.1:9998/
http://127.0.0.1:8092/
http://127.0.0.1:8091/

The only restriction that is there must be a http:// or https:// before the URL so you can't go with ssh://

# How to reporduce

1. Go to one of the internal urls and you will see that there is something (some url is only visible with view-source)
2. The best example is the  http://127.0.0.1:18091/ one if you will visit: view-source:https://proxy.duckduckgo.com/iur/?f=1&image_host=https://127.0.0.1:18091/ui/ that there is something called couchebase console. (only visible in view-source)

These are I think internal web ports because I wasn't able to go to these ports from the external proxy.duckduckgo.com url.

## Impact

Attacker can scan your internal network, finding internal port, and internal web applications

The hacker selected the **Server-Side Request Forgery (SSRF)** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Can internal services be reached bypassing network access control?**
Yes

**What internal services were accessible?**
http://127.0.0.1:9998/
http://127.0.0.1:8092/
http://127.0.0.1:8091/
https://127.0.0.1:18091/
...

**Security Impact**
I was possible to reach internal services, however I didn't tested that is that important or not (because i didn't want to violate any law)



## Attachments
- ssrf.png
- ssrf3.png
