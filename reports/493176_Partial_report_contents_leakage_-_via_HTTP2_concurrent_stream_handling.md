# Partial report contents leakage - via HTTP/2 concurrent stream handling

## Report Details
- **Report ID**: 493176
- **URL**: https://hackerone.com/reports/493176
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-09T01:32:15.116Z
- **Disclosed**: 2021-08-05T20:07:09.752Z

## Reporter
- **Username**: tomvg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

The concurrent handling of HTTP/2 streams allows for a "timeless timing attack": instead of timing, the ordering of responses is used, making the attack resilient to network jitter. As the `/bugs.json` endpoint takes slightly longer to process when a query returns results, it is possible to reliably determine whether this query had one or more results. This can then be used to reveal information about (un)disclosed bug reports in a cross-site search attack, among other things, finding vulnerable endpoints.

**Description:**

A timing attack against `/bugs.json` was reported in #350432 and #350432 (and possibly #4701 - though this one isn't public, so I don't know the details). These prior reports aimed to determine the response size, and from that infer the number of results returned for a particular query. For the two public reports, the timing measurements were not reliably enough for an attack. I tried to replicate and improve these attacks (with the timing techniques we used for [HEIST](https://tom.vg/papers/heist_blackhat2016.pdf#page=5)), and found that indeed noy reliable results could be obtained, presumably due to relatively high (network) jitter. The "timing" attack in this report works quite differently, and in fact it is not really a timing attack in the sense that it doesn't use timing information (which is what makes it a lot more resilient against jitter). Furthermore, it does not attempt to determine the response size, but rather the server processing time.

The concept of the attack is pretty straightforward: the attacker triggers 2 simultaneous requests with `fetch()`, one to a baseline query that returns no results (e.g. `/bugs.json?text_query=NO_RESULT_WILL_BE_FOUND`), and one for a query for something the attacker is interested in (e.g. `/bugs.json?text_query=/bugs.json%20timing`). As `hackerone.com` is using HTTP/2, the two requests will be sent over the same TCP connection, in two TCP packets following right after each other (this makes that they will arrive at almost exactly the same time at the server, since any jitter experienced by the first packet will also be experienced by the second). As the two HTTP/2 streams are concurrent, they will be processed in parallel on the server. As there is a difference in processing time, even when this is minimal (against my own server, I found that an execution time difference of 1-5 µsec is measurable from the browser), one request will generate a response faster than the other. The server will send these responses as soon as they are ready. As soon as the client receives the headers of a response, it will resolve the `Promise` returned by the `fetch()` call. This allows the attacker to determine which response was generated first (and this which took the least/most execution time).

If the target query does not contain any results, the execution time will be the same as the baseline, and the probability that the response is in the same order as the requests were sent, is approximately 50%. In case the target query does yield results, the probability that the response for the target query comes in last, is higher (because the server needed some additional time to process). Because this attack is still subjective to jitter in processing time (typically one or more magnitudes smaller than the network jitter experienced in typical timing attacks), the attacker would have to collect a number of measurements and count the response ordering for them. In my tests, I found that 20 request-pairs suffice to provide a reliable result. In fact, for all the tests I've run, all attacks were successful, even when I tried to run it from the airport WiFi.

Ironically, the only time that the attack was not working, was when the baseline query erroneously returned results. I belief this is probably a bug in HackerOne caused by some sort of race condition (at the time of testing, I was sending quite a lot of requests in parallel until I noticed there's in fact some rate limiting in effect). It might be worth to explore this further; may be just a bug, or may somehow be exploitable. It's hard for me to replicate though... If it's easier for you to track this, I can open a separate report, though I haven't been able to show any security impact for this bug.

### PoC||GTFO

I implemented a basic proof-of-concept, hosted [here](https://poc.tom.vg/hackerone/hackerone-bugs.json-concurrent-requests.html). To use it, just change the `text_query` parameter to something that would have at least one result. Next, simply click start and wait 6-7 seconds. If you find that the value (or values, if you select multiple iterations) of `numCorrectBaseline` is lower than those of `numCorrectTarget`, it means that the attack was successful (as the response for the target URL was slower). These are the results I obtained for 10 iterations, on my home WiFi connection:

```json
{
    "numCorrectBaseline": [11, 10, 9, 8, 6, 9, 10, 6, 10, 11],
    "numCorrectTarget": [15, 18, 14, 16, 15, 16, 14, 13, 16, 20]
}
```

From this it seems clear that the attack is quite robust (would be neat if you could replicate this!).

It appears that `/bugs/count/` (and possibly some other endpoint that I haven't tested) might also be affected by these issues, though the `/bugs/count/` endpoint seems slightly less robust (I assume since it has to retrieve less information from the database).


### Mitigation

I assume that you are well aware on how to mitigate these types of vulnerabilities. But adding it just for the sake of completeness...

1. CSRF token: I noticed that on `/bugs`, the request for `/bugs.json` would already include the `x-csrf-token` header. However, its value is not validate. Such a CSRF token would mitigate the vulnerability
2. In #350432 it was mentioned that this endpoint would be deprecated (and removed?), and replaced with GraphQL requiring a token to query the information; of course this would also work (and hopefully this report might expedite the process)
3. SameSite cookies: if the `__Host-session` cookie was served with e.g. `SameSite=lax`, this attack would not be possible.



### Optional: Your Environment (Browser version, Device, etc)

* Tested on my Macbook Pro, both in Chrome and Firefox (up-to-date version), in a variety of network conditions (ethernet, WiFi, crappy WiFi)


### Optional: Supporting Material/References (Screenshots)

* I've included a screenshot of 5 iterations run over the airport WiFi.


### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

no

## Impact

This vulnerability basically provides the attacker with search capabilities in the victim's reported bugs. The attacker could abuse this to discover vulnerable endpoints or other sensitive data. For instance, the attacker could start with a query for `https://hackerone.com/`, determine that the victim reported a vulnerability there, then cycle through all endpoints, `https://hackerone.com/activities`, `https://hackerone.com/apps`, ... and find which one was probably vulnerable (the vulnerable endpoint will likely be present in the report). Knowing the endpoint, the attacker could further refine the type of vulnerability by using several keywords, perhaps find the query parameters etc.
Since the text search matches any substring (and not just on word-boundaries), the attacker could also brute-force certain secrets, e.g. when they were redacted in a public report.

I hope that the basic PoC I made shows that this type of attack would indeed be feasible, otherwise, I can try to create a more extensive version.

## Attachments
- screenshot-attack-from-airport-wifi.png
