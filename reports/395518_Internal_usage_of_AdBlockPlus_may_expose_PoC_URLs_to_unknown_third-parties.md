# Internal usage of AdBlockPlus may expose PoC URLs to unknown third-parties

## Report Details
- **Report ID**: 395518
- **URL**: https://hackerone.com/reports/395518
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-15T15:17:54.897Z
- **Disclosed**: 2018-08-17T17:53:13.301Z

## Reporter
- **Username**: dudez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello HackerOne team,

this is probably going to be a *different* kind of report than what you are used to: it looks to me this is more of an internal, operational security best-practice that you may choose to follow.

This is something that's bugging me from January now, but it took me some time and thinking before reporting that because i wasn't completely sure of my initial intuition.

Anyway, since i keep getting supporting evidence, i decided it's finally time to reach out.

## Summary
Internal usage of AdBlockPlus by the HackerOne staff may inadvertently exposes PoC URLs or other sensitive information to unknown third-parties.

The problem is obviously broader than this and can easily encompass every single researcher who installed more or less exotic extensions in their browser (me as well), but ensuring that is a lot more difficult.

## Description

Back in January i reported a vulnerability to the ████ team via their managed program running on HackerOne at ██████████.

The associated PoC was meant to be a private webpage hosted by me that demonstrated the information leak i was reporting and the possibility to escalate that to an higher level.

During the triage process the status was changed to *Needs more info* by the H1 staff because the PoC wasn't running as expected and left a note that there was no way to confirm it: within the message, a screenshot of the error has been attached, showing the usage of the **AdBlock/AdBlockPlus** software.

Since the vulnerable endpoint was blocked due to being an ad-serving endpoint (!) i promptly replied to disable it and have the PoC running as expected, and not long after that i got a reply from the H1 staff stating they were able to reproduce it fine.

While waiting for reproduction i was monitoring my server's log for accesses to see if it got served fine, and this is where i noticed some *strange behavior kicking in*: the **Yandex search engine** was now accessing the PoC page from an IP belonging to the `5.*.*.*` range!

Unfortunately i don't have the January logs illustrating that endpoint being visited, but since i suspected AdBlock wasn't playing it right, i immediately renamed the page for one whole month or so, and the PoC has never been accessed anymore.

*I'm attaching a redacted screenshot from the original report that shows the page has been visited with ABP enabled.*

To ensure my suspicions were well founded i thought to setup some subdomains as *honey pots* for testing and decided to give it a go: 

- created `z.dudez.ninja` and `r34lz.dudez.ninja` subdomains
- installed AdBlockPlus in Chromium/Firefox
- browsed to both subdomains
- uninstalled AdBlockPlus
- (reinstalled my good old uBlock Origin)

Sure enough, just hours later i got the first hit asking for the `r34lz.dudez.ninja` subdomain, followed by the `z` one as well and to this day i still got hit by the crawlers there:
```
37.9.113.122 - - - "r34lz.dudez.ninja" [27/Jul/2018:21:24:26 +0000] -/- "GET /robots.txt HTTP/1.1" 404 178 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
37.9.113.122 - - - "r34lz.dudez.ninja" [27/Jul/2018:21:24:30 +0000] -/- "GET / HTTP/1.1" 502 182 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
..
5.255.253.8 - - - "r34lz.dudez.ninja" [15/Aug/2018:13:18:57 +0000] -/- "GET /robots.txt HTTP/1.1" 404 178 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
95.108.181.100 - - - "r34lz.dudez.ninja" [15/Aug/2018:13:19:02 +0000] -/- "GET / HTTP/1.1" 502 182 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
..
37.9.113.122 - - - "z.dudez.ninja" [15/Aug/2018:13:54:55 +0000] TLSv1.2/ECDHE-RSA-AES128-GCM-SHA256 "GET /robots.txt HTTP/1.1" 404 178 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
37.9.113.122 - - - "z.dudez.ninja" [15/Aug/2018:13:54:59 +0000] TLSv1.2/ECDHE-RSA-AES128-GCM-SHA256 "GET / HTTP/1.1" 200 53 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
```

I also read some articles in the past, hinting that ABP being a business will take advantage of its position (e.g. https://www.wired.com/2016/03/heres-how-that-adblocker-youre-using-makes-money/), in some way it looks like the browsing history is not that private after all.

As you noticed, although that was a managed program, i didn't disclose anything related to the report: if you need more information, such as the original report ID to ███ or whatever is missing feel free to ask, i'll be glad and more than willing to collaborate.

## Browsers Verified In
- n/a

## IP Address
- n/a

## Mitigation
If still in use and/or installed, i would encourage the H1 staff to stop using the AdBlock software and use [uBlock Origin](https://github.com/gorhill/uBlock) as a replacement.

## Impact

As we don't really know what kind of use AdBlock/AdBlockPlus is doing with the harvested data, hacker-submitted PoC and other sensitive information may be at risk of being indexed in some way.

## Attachments
No attachments
