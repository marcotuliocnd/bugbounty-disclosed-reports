# Exposed, outdated nginx server (v1.4.6) potentially vulnerable to heap-based buffer overflow & RCE

## Report Details
- **Report ID**: 168485
- **URL**: https://hackerone.com/reports/168485
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-15T04:08:05.986Z
- **Disclosed**: 2016-10-15T10:41:25.332Z

## Reporter
- **Username**: cha5m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: irccloud

## Vulnerability Information
Summary
========
During my reconnaissance for your bug bounty program, I discovered an instance of nginx version 1.4.6 running at the IP address https://54.153.101.52. To locate it, I search for IRCCloud-related certificated and found the self-signed certificate for this server (https://censys.io/ipv4/54.153.101.52). This version is in the range of nginx versions affected by the CVE, [CVE-2014-0133](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0133). There is a known exploit for this CVE. According to MITRE, this "heap-based buffer overflow in the SPDY implementation in nginx 1.3.15 before 1.4.7 and 1.5.x before 1.5.12 allows remote attackers to execute arbitrary code via a crafted request."

{F120380}

However, to succeed, I believe that the exploit requires the ngx_http_spdy_module module (which is not compiled by default) and it requires no --with-debug configure option, if the "spdy" option of the "listen" directive is used in a configuration file. Because I am unable to check the configuration of your server, I wanted to inform you of this outdated version.

Checking for Vulnerability Steps
========
1. Log into server located at 54.153.101.52
2. Check the nginx configuration file. This should provide you with information as to whether or not it is vulnerable.

Mitigation
========
Regardless, this is a very outdated version of nginx that should likely be updated to the most recent version if you intend to keep if publicly-exposed. This would correct the vulnerability (if it is vulnerable). Alternatively, if you only want to correct the vulnerability, you can use the patch below:

```
--- src/http/ngx_http_spdy.c
+++ src/http/ngx_http_spdy.c
@@ -1849,7 +1849,7 @@ static u_char *
 ngx_http_spdy_state_save(ngx_http_spdy_connection_t *sc,
     u_char *pos, u_char *end, ngx_http_spdy_handler_pt handler)
 {
-#if (NGX_DEBUG)
+#if 1
     if (end - pos > NGX_SPDY_STATE_BUFFER_SIZE) {
         ngx_log_error(NGX_LOG_ALERT, sc->connection->log, 0,
                       "spdy state buffer overflow: "
```
Source: https://nginx.org/download/patch.2014.spdy2.txt

Best,
@n0rb3r7


## Attachments
- Screenshot_2016-09-15_00.01.28.png
