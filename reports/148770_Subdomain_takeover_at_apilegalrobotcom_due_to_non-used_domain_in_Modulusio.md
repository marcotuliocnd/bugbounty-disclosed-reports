# Subdomain takeover at api.legalrobot.com due to non-used domain in Modulus.io.

## Report Details
- **Report ID**: 148770
- **URL**: https://hackerone.com/reports/148770
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-01T23:47:27.250Z
- **Disclosed**: 2016-08-26T22:37:13.422Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi,

I noticed that the following domain: api.legalrobot.com was returning the following information:

```
NO APPLICATION WAS FOUND FOR
api.legalrobot.com
```
{F102881}

from Modulus.io. The problem with this is that this tends to be pretty bad depending on the service you use.

In this case, what I did was to create a new account on Modulus, and saw the following setup when I created my own application:
{F102879}

I tried adding the specific domain, but it said it was already added somewhere. The problem was that I then tried with the wildcard: `*.legalrobot.com`, and that actually worked:
{F102878}

Which also made the page resolve my app:
{F102877}

You should not point subdomains to services you do not use (yet). Since I have claimed the wildcard `*.legalrobot.com` now (just for PoC of course), let me know if I should remove this, so you could claim the wildcard yourself, which would probably prevent you completely from risking that subdomains will be taken over.

PoC-link:
https://api.legalrobot.com/
I've just made a simple `Hello World!` but look in the HTML-source for a reference to me:
```
$ curl https://api.legalrobot.com
Hello World!<!--FRANS ROSEN-->
```

Also, please note that Modulus will actually resolve the domain serving SSL, which is a really bad thing.
 
You should remove the DNS post, or let me know if I should remove the wildcard-domain so you could claim it in this service. Let me know if you need additional information.

Also, we'll add this into the scanner during next week since we've seen a couple of clients being affected by this. You do not need to reward me anything as you could see this as a form of premium service or whatnot.. :)

Regards,
Frans

## Attachments
- Screen_Shot_2016-07-02_at_01.39.04.png
- Screen_Shot_2016-07-02_at_01.42.30.png
- Screen_Shot_2016-07-02_at_01.43.06.png
- Screen_Shot_2016-07-02_at_01.41.35.png
