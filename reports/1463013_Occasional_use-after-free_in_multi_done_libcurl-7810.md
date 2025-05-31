# Occasional use-after-free in multi_done() libcurl-7.81.0

## Report Details
- **Report ID**: 1463013
- **URL**: https://hackerone.com/reports/1463013
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-28T18:22:33.099Z
- **Disclosed**: 2022-03-09T21:46:52.194Z

## Reporter
- **Username**: luminixaaron
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
We are seeing the use of a `struct connectdata *` on a thread after it was returned to the connection cache (and thus available for use on other threads including potential deallocation) in `multi_done()` in libcurl-7.81.0.  This could occasionally result in an actual use-after-free, witnessed on Windows 10 platform.

## Steps To Reproduce:
- [`multi_done()` line 717](https://github.com/curl/curl/blob/curl-7_81_0/lib/multi.c#L717) a call is made to `Curl_conncache_return_conn()`
- `Curl_conncache_return_conn()` returns `TRUE` (conn was returned to the cache and available for use in other threads) and execution continues on [line 719](https://github.com/curl/curl/blob/curl-7_81_0/lib/multi.c#L719) where the code derefs the now unowned `conn` to get the `connection_id`
- We have a fork with a [commit](https://github.com/luminixinc/curl/commit/e8560cb3a2aa0c104d1afcc77490b70bad1ce9cd) that both tests (inline, not formally) and offers a potential fix for this issue.
- See attached screenshot showing assert firing in debug build

## Impact

Unsure.

I'm not a hacker, and would have been happy to submit this as a GitHub issue instead, but _discretion being the better part of valor_, decided to post this issue here instead :)

Tangentially, I do not care to get credit or receive a bounty for this issue.  Would be great to get this fixed as I suggested or in some other manner, thanks!

## Attachments
- assert.png
