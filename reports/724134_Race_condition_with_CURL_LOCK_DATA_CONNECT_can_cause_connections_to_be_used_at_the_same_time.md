# Race condition with CURL_LOCK_DATA_CONNECT can cause connections to be used at the same time

## Report Details
- **Report ID**: 724134
- **URL**: https://hackerone.com/reports/724134
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-10-28T18:37:12.913Z
- **Disclosed**: 2021-01-08T18:07:22.964Z

## Reporter
- **Username**: creid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
We've seen race conditions when using CURL_LOCK_DATA_CONNECT in libcurl where sometimes two different threads using two different easy handles ends up sharing the same connection pointer at the same time.
This causes UAFs and double frees when both threads are freeing items on the same connection pointer.

## Steps To Reproduce:
I added curl.cpp which stresses CURL_LOCK_DATA_CONNECT and should eventually trigger an ASAN error with curl compiled using clang's address sanitizers.
It's not consistent how it fails since it's a threading issue. I've found that it's more consistent after adding a random sleep after the unlock here https://github.com/curl/curl/blob/master/lib/url.c#L1372.

A colleague suggested that a potential fix could be to remove the CONN_INUSE check from [this condition ](https://github.com/curl/curl/blob/master/lib/url.c#L1194) because the connection isn't actually marked as inuse until a different set of lock and unlocks. It does appear to stop the crashes but we're unsure on how ideal that fix is.

## Supporting Material/References:

curl.cpp - Repro code
asan-output.txt - Asan results with some added logging
Notably three threads with different easy handles decide to reuse the 0x61b000fbd688 connection at the same time.
```
[thread: 7bdde700] multi_done(data = 0x623000206108,  conn = 0x61b000fbd688)
[thread: 825eb700] url.c:1370 chosen connection=0x61b000fbd688
[thread: 825eb700] reuse_conn(old_conn=0x61b000979188, conn=0x61b000fbd688)
[thread: 7bdde700] url.c:1370 chosen connection=0x61b000fbd688
[thread: 7bdde700][thread: 8a7ff700] Cur reuse_conn(old_conn=0x61b0012e1888, conn=0x61b000fbl.c:1370 chosen connecd688)
[thread: 877f9700] url_attach_connnection(data = 0x6230002c4d08,  conn = 0x61b000f1a388)
tion=0x61b000fbd688
[thread: 877f9700] reuse_conn(old_conn=0x61b000a94988, conn=0x61b000fbd688)
[thread: 825eb700] Curl_attach_connnection(data = 0x62300030e508,  conn = 0x61b000fbd688)
[thread: 7bdde700] Curl_attach_connnection(data = 0x6230000e3908,  conn = 0x61b000fbd688)
[thread: 877f9700] Curl_attach_connnection(data = 0x62300021cd08,  conn = 0x61b000fbd688)
```

## Impact

Not sure how much of a security impact or exploitable this is in practice since it's pretty inconsistent on when it's hit.

## Attachments
- curl.cpp
- asan-output.txt
