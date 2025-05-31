# Ratelimiting can be bypassed using IPv6 subnets

## Report Details
- **Report ID**: 1154003
- **URL**: https://hackerone.com/reports/1154003
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-07T01:26:34.328Z
- **Disclosed**: 2021-07-01T18:02:41.444Z

## Reporter
- **Username**: sjw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Nextcloud hardcodes IPv6 subnets to /128.
End users get at least a /64 subnet (more than the whole IPv4 address space!), most providers assign even larger subnets like /48.
The subnet is used to block bruteforce attempts [3] and rate limiting [4]. An attacker can easily generate random addresses from the assigned /48 subnet to bypass these protections.
Nextcloud should block at least /64 subnets or even better dynamically change the size of the subnet depending on the amount of suspect requests coming from a larger subnet, maybe up to /32.

[1] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/Normalizer/IpAddress.php#L107-L110
[2] https://www.ripe.net/publications/docs/ripe-552#assignment
[3] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/Bruteforce/Throttler.php#L132
[4] https://github.com/nextcloud/server/blob/f12fab23db3529c34f620789f345f5e5e841c06a/lib/private/Security/RateLimiting/Limiter.php#L84

## Impact

bruteforce protection and rate limiting are basically useless for IPv6 targets.

## Attachments
No attachments
