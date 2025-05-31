# 1-byte heap buffer overflow in DNS resolver

## Report Details
- **Report ID**: 1210450
- **URL**: https://hackerone.com/reports/1210450
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-27T10:32:41.665Z
- **Disclosed**: 2021-08-27T00:07:05.588Z

## Reporter
- **Username**: luismerino
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Official announcement: http://mailman.nginx.org/pipermail/nginx-announce/2021/000300.html

A security issue in nginx resolver was identified, which might allow an
attacker to cause 1-byte memory overwrite by using a specially crafted
DNS response, resulting in worker process crash or, potentially, in
arbitrary code execution (CVE-2021-23017).

The issue only affects nginx if the "resolver" directive is used in
the configuration file.  Further, the attack is only possible if an
attacker is able to forge UDP packets from the DNS server.

The issue affects nginx 0.6.18 - 1.20.0.
The issue is fixed in nginx 1.21.0, 1.20.1.

Patch for the issue can be found here:

http://nginx.org/download/patch.2021.resolver.txt

Thanks to Luis Merino, Markus Vervier, Eric Sesterhenn, X41 D-Sec GmbH.

## Impact

Crash or, potentially,  arbitrary code execution.

## Attachments
No attachments
