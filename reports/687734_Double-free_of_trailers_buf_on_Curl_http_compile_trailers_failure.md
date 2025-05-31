# Double-free of `trailers_buf' on `Curl_http_compile_trailers()` failure

## Report Details
- **Report ID**: 687734
- **URL**: https://hackerone.com/reports/687734
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-04T12:49:57.663Z
- **Disclosed**: 2021-01-12T13:12:04.613Z

## Reporter
- **Username**: thomas_v
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
When `Curl_http_compile_trailers()` fails, `trailers_buf` is freed twice, because we don't pass to this function the pointer value by reference.

## Steps To Reproduce:
Did not actually reproduce, please double check patch attached and analysis.

## Impact

Some memory corruption due to the double-free.

## Attachments
- patch.txt
