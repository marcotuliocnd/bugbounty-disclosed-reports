# fetch with integrity option is too lax when algorithm is specified but hash value is in incorrect

## Report Details
- **Report ID**: 2377760
- **URL**: https://hackerone.com/reports/2377760
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-02-18T12:17:24.035Z
- **Disclosed**: 2024-05-03T17:41:15.961Z

## Reporter
- **Username**: uzlopak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
__A potential solution is attached as 0001-improve-bytesMatch.patch__

**Summary:** 
I was investigating for some low hanging fruits regarding performance bottlenecks in undici, when I found this potential security issue in undici, and thus in nodejs. First I wrote a benchmark for bytesMatch and saw the following result:

```sh
aras@aras-Lenovo-Legion-5-17ARH05H:~/workspace/undici$ node benchmarks/bytesMatch.mjs 
cpu: AMD Ryzen 7 4800H with Radeon Graphics
runtime: node v21.6.2 (x64-linux)

benchmark                                    time (avg)             (min … max)       p75       p99      p999
------------------------------------------------------------------------------- -----------------------------
bytesMatch valid sha256 and base64        2'292 ns/iter   (2'009 ns … 9'452 ns)  2'209 ns  7'709 ns  9'452 ns
bytesMatch invalid sha256 and base64      2'153 ns/iter   (2'013 ns … 2'306 ns)  2'209 ns  2'275 ns  2'306 ns
bytesMatch valid sha256 and base64url       243 ns/iter       (205 ns … 318 ns)    261 ns    286 ns    301 ns
bytesMatch invalid sha256 and base64url     245 ns/iter       (203 ns … 400 ns)    264 ns    320 ns    390 ns
```

See attached 0001-add-benchmark.patch

So for some reason base64url was significantly faster than base64, even in the invalid case. So further investigations resulted in the finding that parseHashWithOptions in the underlying undici library is not matching base64url encoded hashes. Worse it is not matching any algorithms provided with invalid hashes. E.g. `sha256--` wont result in detecting that a sha256 hash was provided, thus skipping totally the whole SRI check.

https://github.com/nodejs/undici/blob/e1195cbf32cb5f10f25e820d580264f24c7edc71/lib/fetch/util.js#L591


## Steps To Reproduce:

See attached 0001-add-test.patch. It contains unit tests, which you can run against main branch.

## Impact: 

Resources which should be checked via SRI Logic are loaded nonetheless. 

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, references, commits, code examples, etc.).

## Impact

Resources which should be checked via SRI Logic are loaded nonetheless.

## Attachments
- 0001-add-test.patch
- 0001-add-benchmark.patch
- 0001-improve-bytesMatch.patch
