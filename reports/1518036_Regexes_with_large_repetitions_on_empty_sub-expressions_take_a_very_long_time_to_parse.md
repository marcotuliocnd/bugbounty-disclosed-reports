# Regexes with large repetitions on empty sub-expressions take a very long time to parse

## Report Details
- **Report ID**: 1518036
- **URL**: https://hackerone.com/reports/1518036
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-03-21T20:57:04.184Z
- **Disclosed**: 2022-03-22T22:24:15.254Z

## Reporter
- **Username**: addisoncrump
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Rust's regex crate guarantees a linear time complexity with regex length for compilation of untrusted regexes. However, existing mitigations for known malicious regexes are based on memory usage and, as such, do not mitigate repetitions of empty sub-expressions. For example, the following payload triggers such an issue:

```re
(?:){4294967295}
```

This will cause the regex compiler to attempt to create 4294967295 instances of an empty sub-expression, which will ultimately allocate zero bytes and therefore bypass existing memory-based mitigations. This can be further weaponised to create an exponential time complexity with regex length by using repetitions of repetitions, e.g.:

```re
(?:){64}{64}{64}{64}{64}{64}
```

This payload would cause the regex compiler to attempt to create 64^6 instances of an empty sub-expression.

## Impact

An attacker can induce a CPU time-based denial of service with effectively infinite CPU time, which would cause the service to become entirely unavailable.

## Attachments
No attachments
