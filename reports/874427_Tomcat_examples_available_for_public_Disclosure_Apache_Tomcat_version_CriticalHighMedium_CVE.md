# Tomcat examples available for public, Disclosure Apache Tomcat version, Critical/High/Medium CVE

## Report Details
- **Report ID**: 874427
- **URL**: https://hackerone.com/reports/874427
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-14T19:38:44.178Z
- **Disclosed**: 2020-06-11T18:17:21.287Z

## Reporter
- **Username**: pvm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
There are multiple issues found on ███:
1. ███████/examples/ - Apache Tomcat examples are available for public. Multiple issues -  session and cookies manipulation, internals IP disclosure.
2. Error page contains information about Apache Tomcat version
3. Reported Tomcat version is vulnerable. Multiple CVEs - critical, high and medium

**Description:**
1. Examples are available by link: ███████/examples/

2. Information disclosure about Apache Tomcat version

3. Vulnerable version Apache Tomcat/8.5.33

https://nvd.nist.gov/vuln/detail/CVE-2020-1938
Base Score: 9.8 CRITICALVector:  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-0232
Base Score: 8.1 HIGH Vector:  CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-17563
Base Score: 7.5 HIGH Vector:  CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-10072
Base Score: 7.5 HIGH Vector:  CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-0199
Base Score: 7.5 HIGH Vector:  CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H

https://nvd.nist.gov/vuln/detail/CVE-2020-1967
Base Score: 7.5 HIGH Vector:  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-12418
Base Score: 7.0 HIGH Vector:  CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H

https://nvd.nist.gov/vuln/detail/CVE-2019-0221
Base Score: 6.1 MEDIUM Vector:  CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N

https://nvd.nist.gov/vuln/detail/CVE-2019-2684
Base Score: 5.9 MEDIUM Vector:  CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N

https://nvd.nist.gov/vuln/detail/CVE-2020-1935
Base Score: 4.8 MEDIUM Vector:  CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N

https://nvd.nist.gov/vuln/detail/CVE-2018-11784
Base Score: 4.3 MEDIUM Vector:  CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N

## Impact
More than Critical. The system is vulnerable. Exploits are available.

## Step-by-step Reproduction Instructions

1. Navigate to █████████/examples/
You will see the standard examples page. Servlets allow to modify cookies and sessions.
2. Navigate to any non exists address to get the Apache Tomcat version
E.g. ███/examples/Readme

## Product, Version, and Configuration (If applicable)
Apache Tomcat/8.5.33

## Suggested Mitigation/Remediation Actions
1. Upgrade Tomcat
2. Remove /examples
3. Change the configuration - display a custom 404 page

## Impact

More than Critical. The system is vulnerable. Exploits are available.
In the An attacker can change session and cookies. Potential sessions interception.
CVEs: Critical -1, High - 6, Medium - 4

## Attachments
No attachments
