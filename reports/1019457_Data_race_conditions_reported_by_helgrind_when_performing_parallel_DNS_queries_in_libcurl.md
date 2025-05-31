# Data race conditions reported by helgrind when performing parallel DNS queries in libcurl

## Report Details
- **Report ID**: 1019457
- **URL**: https://hackerone.com/reports/1019457
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-27T00:52:50.673Z
- **Disclosed**: 2020-11-04T21:44:37.603Z

## Reporter
- **Username**: brumbrum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
While running binary built from curl git repo file "docs/examples/10-at-a-time.c" under valgrind specifically with the helgrind tool, reports race condition in getaddrinfo() calls.   Using the latest curl/libcurl from github repo.

From the valgrind documentation "Helgrind is a Valgrind tool for detecting synchronisation errors in C, C++ and Fortran programs that use the POSIX pthreads threading primitives."


Command used for testing:

valgrind --tool=helgrind --log-file=helgrind_%p.log ./10-at-a-time


See helgrind log files attached to this report.


Here is one example of the helgrind reports:
Note: libcurl was rebuilt in debug to provide complete stack traces. Problem occurs in both debug and non-debug builds.

==43481== Possible data race during read of size 1 at 0x8325DE8 by thread #7
==43481== Locks held: none
==43481==    at 0x8325DE8: ns_name_pton (ns_name.c:160)
==43481==    by 0x831D8DF: __res_hnok (res_comp.c:202)
==43481==    by 0x833906B: check_name (dns-host.c:284)
==43481==    by 0x833906B: _nss_dns_gethostbyname4_r (dns-host.c:335)
==43481==    by 0x4A5B58E: gaih_inet.constprop.0 (getaddrinfo.c:765)
==43481==    by 0x4A5D0D8: getaddrinfo (getaddrinfo.c:2256)
==43481==    by 0x486D6AB: curl_dbg_getaddrinfo (curl_addrinfo.c:554)
==43481==    by 0x486CD6D: Curl_getaddrinfo_ex (curl_addrinfo.c:124)
==43481==    by 0x4861FE0: getaddrinfo_thread (asyn-thread.c:307)
==43481==    by 0x4872148: curl_thread_create_thunk (curl_threads.c:57)
==43481==    by 0x4842B1A: ??? (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_helgrind-amd64-linux.so)
==43481==    by 0x4ED6608: start_thread (pthread_create.c:477)
==43481==    by 0x4A76292: clone (clone.S:95)
==43481==  Address 0x8325de8 is in the Text segment of /usr/lib/x86_64-linux-gnu/libresolv-2.31.so
==43481==    at 0x8325DE8: ns_name_pton (ns_name.c:160)



Will also see some of the calls falling, sometimes.  Not every time though.  Issues might vary based on number of cores/threads present or allocated to the test system. For this testing using a VirtualBox VM with 3 vCPUs running up to date Ubuntu 20.04.


I received the following errors over various runs with the helgrind tool.  Usually the initial few logged output lines will report some failure, rarely do the later output logged lines show failures.  Some examples of errors received over various runs:

R: 16 - Error in the HTTP2 framing layer <https://www.microsoft.com>
R: 16 - Error in the HTTP2 framing layer <https://www.google.com>
R: 35 - SSL connect error <https://www.mysql.com>

R: 52 - Server returned nothing (no headers, no data) <https://www.bbc.co.uk>

R: 55 - Failed sending data to the peer <https://www.google.com>


$ valgrind --version
valgrind-3.15.0


When not running under helgrind the 10-at-a-time binary usually runs without issues, but sometimes one will randomly fail, which might be normal sometimes, but appears to validate that this is a real problem and not only revealed with libcurl used under helgrind.

R: 35 - SSL connect error <https://www.hp.com>


Have not tried c-ares library.  Would you find it useful if I did?


Not clear if the problem is with libcurl or with the libc library implementing getaddrinfo().

## Impact

- Failure to connect to target system.
- Connecting to wrong IP if DNS data corrupted, potentially disclosing sensitive data to wrong site.


Mitigation:
- Limit parallel DNS usage.
- Potentially c-ares library may not have this issue, but this is not verified.

## Attachments
- helgrind_43280.log
- helgrind_43481.log
- helgrind_43338.log
- helgrind_43432.log
