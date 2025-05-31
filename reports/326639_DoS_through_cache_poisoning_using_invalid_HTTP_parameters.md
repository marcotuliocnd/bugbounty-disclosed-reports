# DoS through cache poisoning using invalid HTTP parameters

## Report Details
- **Report ID**: 326639
- **URL**: https://hackerone.com/reports/326639
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-16T13:26:10.119Z
- **Disclosed**: 2018-05-02T17:29:01.968Z

## Reporter
- **Username**: irvinlim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: greenhouse

## Vulnerability Information
I was taking a look into a related report (https://hackerone.com/reports/298265) and I discovered that the https://boards.greenhouse.io/embed/job_board/js?for= endpoint doesn't throw errors when I try to pass in an array of `for` parameters like this:

```
https://boards.greenhouse.io/embed/job_board/js?for[]=twitter&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=&for[]=
```

Instead, in the resultant JS, we can see that the HTTP parameters are escaped and injected into the `Grnhse.Settings` object:

```js
Grnhse.Settings = {
  targetDomain:   'https://boards.greenhouse.io',
  scrollOnLoad:   true,
  autoLoad:       true,
  boardURI:       'https://boards.greenhouse.io/embed/job_board?for%5B%5D=twitter&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=',
  applicationURI: 'https://boards.greenhouse.io/embed/job_app?for%5B%5D=twitter&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=&amp;for%5B%5D=',
  baseURI:        '',
  iFrameWidth:    650
};
```

When fetching the actual correct endpoint (https://boards.greenhouse.io/embed/job_board/js?for=twitter), we see that the result for `twitter` is cached, returning the same corrupted URIs in the JS file. From my tests, it seems that these endpoints are cached for an unknown amount of time, with some staying in the cache for only a few minutes while others may be an hour or longer.

I also found out that the particular endpoint is on CloudFront by observing one of the IP addresses which served the file (35.164.91.227) and corroborating it with the IP range list published by AWS (https://ip-ranges.amazonaws.com/ip-ranges.json). However, fetching from different edge servers seems to result in the same mutated file being fetched at the correct endpoint (https://boards.greenhouse.io/embed/job_board/js?for=twitter). I conclude that there is a second layer of caching somewhere on the application layer.

The impact of corrupting the `boardURI` and `applicationURI` values is that the `job_app` or `job_board` iframes would fail to load in the client's website since the URI is incorrect, resulting in a denial of service for the client. One example is that Airbnb's job application page shows a Greenhouse.io error page (see attached images), which I managed to replicate it twice and lasted for about 20 minutes and less than 5 minutes respectively.

I tried to investigate if I could reliably replicate this PoC by waiting for cache to expire, as well as across several domains, but failed to find anything conclusive without knowledge of the underlying network architecture. Additionally, I am not sure if what is going on at play is due to a cache, and seeing that some IDs take quite a while to recover back to its normal state, I will stop trying to replicate the attack for now.

P.S. This is my first report, so do let me know if I could be of more help!

## Impact

If the attacker has more patience and knowledge about the underlying architecture, the attacker could attempt to poison the cache reliably, resulting in an extended denial of service of Greenhouse job boards/application iframes in client sites.

## Attachments
- airbnb_error-1.png
- airbnb_error-2.png
