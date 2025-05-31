# Pull Request #12949 - Security Implications without CVE assignment

## Report Details
- **Report ID**: 415329
- **URL**: https://hackerone.com/reports/415329
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-27T15:54:41.922Z
- **Disclosed**: 2020-02-13T23:55:08.234Z

## Reporter
- **Username**: jzebor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
**Summary:** Pull Request #12949 has security implications but it was not assigned a CVE by the Node team. It is being reported by Qualys as a 6.8 severity issue without a CVE. 

**Description:**
Here is the commit and pull request -
https://github.com/nodejs/node/commit/010f864426
https://github.com/nodejs/node/pull/12949

I'm reporting this as an employee of F5 Networks and don't expect to receive any bounty for this report. We currently make use of NodeJS in our product and request that the Node team assign a CVE to this issue. It is security relevant, being picked up by popular scanners, and does not have a CVE assigned. CVE assignment for the issue seems relevant and will make it easier for our group and others to track this issue.

## Steps To Reproduce: Launch the inspector or debug mode for a vulnerable node instance. It's clear from that. Here is what Qualys scanner will report for *some* versions of BIG-IP that include a vulnerable instance of NodeJS.

-------
Severity 4 NodeJS Debugger Command Injection
QID: 11869 CVSS Base: 6.8 [1]
Category: CGI CVSS Temporal: 5
CVE ID: -
Vendor Reference: NodeJS v8
Bugtraq ID: -
Service Modified: 02/26/2018 CVSS3 Base: -
User Modified: - CVSS3 Temporal: -
Scan Results page 3
Edited: No
PCI Vuln: Yes
THREAT:
NodeJS includes an out-of-process debugging utility accessible via a V8 Inspector and built-in debugging client.
The NodeJS debugger; releases available since April 2014, when enabled or misconfigured is accessible on TCP port 5858 and accepts connection
from any address. This behaviour can be exploited to execute arbitrary code on the targeted system.
Affected Versions:
Node JS versions prior to 8.0.0
QID Detection Logic: This unauthenticated QID uses the "evaluate" request type to evaluate arbitrary JS and call out to other system commands.
IMPACT: Successful exploitation allows remote, unauthenticated attackers to execute arbitrary code on the targeted system.
SOLUTION: Customers are advised to upgrade to the NodeJS 8.0.0 (https://nodejs.org/en/download/) or latest versions and disable unauthenticated debugger
access to remediate this vulnerability.
Patch:
Following are links for downloading patches to fix the vulnerabilities:
NodeJS latest (https://nodejs.org/en/download/)
COMPLIANCE: Not Applicable
EXPLOITABILITY: There is no exploitability information for this vulnerability.
ASSOCIATED MALWARE: There is no malware information for this vulnerability.
RESULTS: Vulnerable version of Node JS detected: v6.9.1
------

## Impact: Security implications are that an unauthenticated attack can control and/or steal data from a process. 

## Supporting Material/References:
https://github.com/nodejs/node/commit/010f864426
https://github.com/nodejs/node/pull/12949

## Impact

Unauthenticated users can control and/or steal data from a process. 

I'm asking that the NodeJS team assign a CVE to this issue. Doing so will make it easier for external entities to track this issue. It has security relevance and is clearly a way for attackers to achieve process control and it's unclear as to why a CVE was not assigned in the first place.

## Attachments
No attachments
