# Undici ProxyAgent vulnerable to MITM 

## Report Details
- **Report ID**: 1599063
- **URL**: https://hackerone.com/reports/1599063
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-06-13T15:07:42.127Z
- **Disclosed**: 2022-07-13T13:20:15.817Z

## Reporter
- **Username**: pimterry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Full GitHub advisory summarizing the issue is here: https://github.com/nodejs/undici/security/advisories/GHSA-pgw7-wx7w-2w33
The original Node.js HackerOne report is here: https://hackerone.com/bugs?report_id=1583680

This was fixed & disclosed in Undici v5.5.1.

This primarily affects Undici, a subproject under the Node.js umbrella, which is experimentally included as part of recent Node.js releases. This issue doesn't immediately affect standalone Node.js usage today due to the limited APIs initially exposed, but it does affect all usage of Node.js's new Fetch API with HTTP proxies (since Undici was required for that) and @mcollina in https://hackerone.com/bugs?report_id=1583680 who processed the Node.js security report said this should be eligible for a Node.js bounty.

## Impact

See https://github.com/nodejs/undici/security/advisories/GHSA-pgw7-wx7w-2w33 for more details but in short: it allows for trivial MitM of all HTTPS traffic sent to a proxy with Undici's ProxyAgent API. In all cases the proxy can invisibly MitM 'secure' traffic, and in most cases everybody else on the network path can do so too.

## Attachments
No attachments
