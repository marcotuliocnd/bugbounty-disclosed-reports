# Use of uninitialized value in ftp_getrc_msg method of mod_proxy_ftp.c

## Report Details
- **Report ID**: 838685
- **URL**: https://hackerone.com/reports/838685
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-04T07:29:16.387Z
- **Disclosed**: 2020-10-10T13:20:51.892Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This is a Security Bug Report for mod_proxy_ftp. This bug is present in ftp_getrc_msg method of modules/proxy/mod_proxy_ftp.c file.
This is the line which causes this bug.

```c
...
  mb = apr_cpystrn(mb, response + 4, me - mb);
...
```
If ftp server returns a response like "\r\n", which has 3 characters with terminating NULL byte, apr_cpystrn method will copy uninitialized values.
Because that line uses "response + 4" as the source of data for apr_cpystrn method.

Apache Http Server version: 2.4.41
CVE-ID: [CVE-2020-1934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1934)
Apache Http server fixed security bugs: (https://httpd.apache.org/security/vulnerabilities_24.html)

Steps to reproduce
---------------------
Python 3 and Ubuntu OS 18.04 are required.


* Download attached ftpserver.py file.
* Enable proxy_module and proxy_ftp_module on Apache Http server.
* Add these lines to httpd.conf file of Apache http server.

```apache
   ProxyRequests On

   <Proxy *>
     Order deny,allow
     Deny from all
     Allow from 127.0.0.1
   </Proxy>
```

* Enter proxy settings
   * Open Setting on your Ubuntu OS.
   * Select Network
   * Click settings icon next to "Network Proxy" option.
   * Tick "Manual" option.
   * Enter Apache servers IP and port next to "FTP Proxy"
* Run Apache http server with Valgrind.
 ` sudo valgrind --leak-check=yes bin/httpd -X`
* Run attached ftpserver.py
   `sudo python3 ftpserver.py`
   * This python program will start a server on port 21.
* Open a new terminal window and run this command.
   `curl ftp://127.0.0.1`

Valgrind Output
------------------
Memcheck, a memory error detector
Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
Command: bin/httpd -X

Thread 4:
Conditional jump or move depends on uninitialised value(s)
at 0x52E6FFE: apr_cpystrn (in /usr/lib/x86_64-linux-gnu/libapr-1.so.0.6.3)
by 0x8A0A46A: ftp_getrc_msg (mod_proxy_ftp.c:403)
by 0x8A0C6CF: proxy_ftp_command (mod_proxy_ftp.c:828)
by 0x8A0EAF1: proxy_ftp_handler (mod_proxy_ftp.c:1212)
by 0x87F0259: proxy_run_scheme_handler (mod_proxy.c:3082)
by 0x87E9F08: proxy_handler (mod_proxy.c:1251)
by 0x17462C: ap_run_handler (config.c:170)
by 0x17516E: ap_invoke_handler (config.c:444)
by 0x195E74: ap_process_async_request (http_request.c:453)
by 0x1915BD: ap_process_http_async_connection (http_core.c:158)
by 0x1917EB: ap_process_http_connection (http_core.c:252)
by 0x183D4A: ap_run_process_connection (connection.c:42)

Conditional jump or move depends on uninitialised value(s)
at 0x52E700F: apr_cpystrn (in /usr/lib/x86_64-linux-gnu/libapr-1.so.0.6.3)
by 0x8A0A46A: ftp_getrc_msg (mod_proxy_ftp.c:403)
by 0x8A0C6CF: proxy_ftp_command (mod_proxy_ftp.c:828)
by 0x8A0EAF1: proxy_ftp_handler (mod_proxy_ftp.c:1212)
by 0x87F0259: proxy_run_scheme_handler (mod_proxy.c:3082)
by 0x87E9F08: proxy_handler (mod_proxy.c:1251)
by 0x17462C: ap_run_handler (config.c:170)
by 0x17516E: ap_invoke_handler (config.c:444)
by 0x195E74: ap_process_async_request (http_request.c:453)
by 0x1915BD: ap_process_http_async_connection (http_core.c:158)
by 0x1917EB: ap_process_http_connection (http_core.c:252)
by 0x183D4A: ap_run_process_connection (connection.c:42)

Conditional jump or move depends on uninitialised value(s)
at 0x8A0A475: ftp_getrc_msg (mod_proxy_ftp.c:405)
by 0x8A0C6CF: proxy_ftp_command (mod_proxy_ftp.c:828)
by 0x8A0EAF1: proxy_ftp_handler (mod_proxy_ftp.c:1212)
by 0x87F0259: proxy_run_scheme_handler (mod_proxy.c:3082)
by 0x87E9F08: proxy_handler (mod_proxy.c:1251)
by 0x17462C: ap_run_handler (config.c:170)
by 0x17516E: ap_invoke_handler (config.c:444)
by 0x195E74: ap_process_async_request (http_request.c:453)
by 0x1915BD: ap_process_http_async_connection (http_core.c:158)
by 0x1917EB: ap_process_http_connection (http_core.c:252)
by 0x183D4A: ap_run_process_connection (connection.c:42)
by 0x1A189C: process_socket (event.c:1050)
...

* Complete valgrind output is attached.

## Impact

Uninitialized data may leak data from memory.

## Attachments
- ftpserver.py
- valgring_output.txt
