# Buffer write overflow when forming dns over http request

## Report Details
- **Report ID**: 694449
- **URL**: https://hackerone.com/reports/694449
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-13T14:09:24.170Z
- **Disclosed**: 2021-02-08T07:55:02.375Z

## Reporter
- **Username**: pauldreik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
If dns over http is used, the hostname to look up is packed into a buffer to send to the dns server using the doh_encode function from the doh.c source file. By default, curl uses a 512 byte buffer. For that length,  the buffer may be overflowed with one byte, which is set to 1.

Note that this happens even with the fix in https://github.com/curl/curl/pull/4345 which Daniel made after I emailed about a similar bug in the curl/doh repository.

## Steps To Reproduce:

Build curl with address sanitizer, and/or add an assert
assert(*olen <=len) ;
right before returning from doh_encode() in doh.c https://github.com/curl/curl/blob/65f5b958c95d538a9b205e2753a476d1a7c89179/lib/doh.c#L135

Then issue a curl request:
 `src/curl --doh-url https://irrelevant/ x....xxxxxxxxxxxxxxxxxxxxx.x....x.xxxxxxxxxx.xxxxxxxxx.xxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxx...xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.x.x.......xxxxxxxxxxxxxxxxxxxxxx...xxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx...xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx......xxxxxx.....xx..........xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxxxx..x......xxxxxxxx..xxxxxxxxxxxxxxxxxxx.x...xxxx.x.x.x...xxxxx`



## Supporting Material/References:
When adding the assert above, this is the output of the above command:

    curl: ../../../lib/doh.c:144: DOHcode doh_encode(const char *, DNStype, unsigned char *, size_t, size_t *): Assertion `*olen <=len' failed.

## Impact

If the attacker somehow can control the hostname eventually used by curl, and DOH is in use, the buffer overflow can happen.

For the common case where dnsprobe.dohbuffer is used, the overwrite may be immediately remedied by assignment to the length (see https://github.com/curl/curl/blob/65f5b958c95d538a9b205e2753a476d1a7c89179/lib/doh.c#L195 )
This relies on the compiler not rearranging the writes.

## Attachments
No attachments
