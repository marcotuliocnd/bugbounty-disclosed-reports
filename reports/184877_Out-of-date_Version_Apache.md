#  Out-of-date Version (Apache) 

## Report Details
- **Report ID**: 184877
- **URL**: https://hackerone.com/reports/184877
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-24T15:09:27.537Z
- **Disclosed**: 2019-12-02T17:49:02.429Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
URL  https://████████/  
Identified Version  2.2.15 (contains 4 important and 10 other vulnerabilities)  
Latest Version  2.2.31  
Vulnerability Database  Result is based on 27.10.2016 vulnerability database content.  
Vulnerability Details


Link identified you are using an out-of-date version of Apache.

Impact

Since this is an old version of the software, it may be vulnerable to attacks.

Remedy


Please upgrade your installation of Apache to the latest stable version.

Remedy References

•Downloading the Apache HTTP Server

Known Vulnerabilities in this Version


Medium Apache mod_cache and mod_dav Request Handling Denial of Service Vulnerability 

The mod_cache and mod_dav modules in the Apache HTTP Server allow remote attackers to cause a denial of service (process crash) via a request that lacks a path. 

External References
•CVE-2010-1452 

Low Apache APR-util apr_brigade_split_line() Denial of Service Vulnerability 

Memory leak in the apr_brigade_split_line function in buckets/apr_brigade.c in the Apache Portable Runtime Utility library (aka APR-util), as used in the mod_reqtimeout module in the Apache HTTP Server and other software, allows remote attackers to cause a denial of service (memory consumption) via unspecified vectors related to the destruction of an APR bucket. 

External References
•CVE-2010-1623 

Medium Apache APR apr_fnmatch() Denial of Service Vulnerability

Stack consumption vulnerability in the fnmatch implementation in apr_fnmatch.c in the Apache Portable Runtime (APR) library before 1.4.3 and the Apache HTTP Server before 2.2.18, allows context-dependent attackers to cause a denial of service (CPU and memory consumption) via *? sequences in the first argument, as demonstrated by attacks against mod_autoindex in httpd. 

External References
•CVE-2011-0419

Exploit
•http://www.securityfocus.com/data/vulnerabilities/exploits/47820.txt

Medium Apache HTTP Server CVE-2011-3192 Denial Of Service Vulnerability

The byterange filter in the Apache HTTP Server allows remote attackers to cause a denial of service (memory and CPU consumption) via a Range header that expresses multiple overlapping ranges, as exploited in the wild in August 2011, a different vulnerability than CVE-2007-0086.

External References
•CVE-2011-3192

Exploit
•http://www.securityfocus.com//data/vulnerabilities/exploits/49303.c
• http://www.securityfocus.com/data/vulnerabilities/exploits/49303-2.c

Important Apache HTTP Server 'mod_proxy' Reverse Proxy Information Disclosure Vulnerability

The mod_proxy module in the Apache HTTP Server does not properly interact with use of (1) RewriteRule and (2) ProxyPassMatch pattern matches for configuration of a reverse proxy, which allows remote attackers to send requests to intranet servers via a malformed URI containing an initial @ (at sign) character.

External References
•CVE-2011-3368

Exploit
•http://www.securityfocus.com//data/vulnerabilities/exploits/49957.py

Important Apache HTTP Server Scoreboard Local Security Bypass Vulnerability

scoreboard.c in the Apache HTTP Server 2.2.21 and earlier might allow local users to cause a denial of service (daemon crash during shutdown) or possibly have unspecified other impact by modifying a certain type field within a scoreboard shared memory segment, leading to an invalid call to the free function.

External References
•CVE-2012-0031

Important Apache HTTP Server 'mod_proxy' Reverse Proxy Information Disclosure Vulnerability

The mod_proxy module in the Apache HTTP Server 1.3.x through 1.3.42, 2.0.x through 2.0.64, and 2.2.x through 2.2.21, when the Revision 1179239 patch is in place, does not properly interact with use of (1) RewriteRule and (2) ProxyPassMatch pattern matches for configuration of a reverse proxy, which allows remote attackers to send requests to intranet servers via a malformed URI containing an @ (at sign) character and a : (colon) character in invalid positions. 

External References
•CVE-2011-4317

Important Apache HTTP Server CVE-2011-3348 Denial Of Service Vulnerability

The mod_proxy_ajp module in the Apache HTTP Server before 2.2.21, when used with mod_proxy_balancer in certain configurations, allows remote attackers to cause a denial of service (temporary "error state" in the backend server) via a malformed HTTP request.

External References
•CVE-2011-3348

Medium mod_proxy_ajp DoS Vulnerability

The mod_proxy_ajp module in the Apache HTTP Server 2.2.12 through 2.2.21 places a worker node into an error state upon detection of a long request-processing time, which allows remote attackers to cause a denial of service (worker consumption) via an expensive request.

External References
•CVE-2012-4557

Low Apache Multiple XSS Vulnerability

Multiple cross-site scripting (XSS) vulnerabilities in the balancer_handler function in the manager interface in mod_proxy_balancer.c in the mod_proxy_balancer module in the Apache HTTP Server 2.2.x before 2.2.24-dev and 2.4.x before 2.4.4 allow remote attackers to inject arbitrary web script or HTML via a crafted string.

External References
•CVE-2012-4558

Low Apache Code Execution Vulnerability

mod_rewrite.c in the mod_rewrite module in the Apache HTTP Server 2.2.x before 2.2.25 writes data to a log file without sanitizing non-printable characters, which might allow remote attackers to execute arbitrary commands via an HTTP request containing an escape sequence for a terminal emulator.

External References
•CVE-2013-1862

Low Apache Denial of Service Vulnerabillity

mod_dav.c in the Apache HTTP Server before 2.2.25 does not properly determine whether DAV is enabled for a URI, which allows remote attackers to cause a denial of service (segmentation fault) via a MERGE request in which the URI is configured for handling by the mod_dav_svn module, but a certain href attribute in XML data refers to a non-DAV URI.

External References
•CVE-2013-1896

Low Apache 'main/util.c' Denial of Service Vulnerability

The dav_xml_get_cdata function in main/util.c in the mod_dav module in the Apache HTTP Server before 2.4.8 does not properly remove whitespace characters from CDATA sections, which allows remote attackers to cause a denial of service (daemon crash) via a crafted DAV WRITE request.

External References
•CVE-2013-6438

Low Apache 'mod_log_config.c' Denial of Service Vulnerability

The log_cookie function in mod_log_config.c in the mod_log_config module in the Apache HTTP Server before 2.4.8 allows remote attackers to cause a denial of service (segmentation fault and daemon crash) via a crafted cookie that is not properly handled during truncation.

External References
•CVE-2014-0098


## Attachments
No attachments
