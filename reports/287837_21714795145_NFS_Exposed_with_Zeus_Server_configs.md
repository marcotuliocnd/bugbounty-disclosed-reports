# 217.147.95.145 NFS Exposed with Zeus Server configs

## Report Details
- **Report ID**: 287837
- **URL**: https://hackerone.com/reports/287837
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-06T19:54:27.012Z
- **Disclosed**: 2018-09-17T15:32:53.340Z

## Reporter
- **Username**: meals
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!


**Description:** 217.147.95.145 has nfs exposed to the internet which is remotely mountable that has some Zeus server configuration stuff on it. Idk what Zeus is, however NFS should not be remotely mountable from the internet.

## Application & Version:
217.147.95.145 NFS Service

## Steps To Reproduce:
  1. edit your /etc/fstab to include the remote mount:
217.147.95.145:/zeus0	/mnt/bohemia nfs rw,soft,intr,noatime,rsize=4096,wsize=4096
2. $ mount -a
3.root@kali:/mnt/bohemia/app_zeus1.8/logs# ls -la
total 1446449
drwxr-xr-x 2 1001 1001        232 Nov  3  2016 .
drwxr-xr-x 3 root root       4096 Jan 13  2016 ..
-rw-r--r-- 1 1001 1001 1443350354 Nov  6 14:29 Zeus_Log_2016Y11M3D_23H25M53S_889MS.txt
-rw-r--r-- 1 1001 1001    4023959 Feb 19  2016 Zeus_Log_2016Y1M13D_9H46M20S_728MS.txt
-rw-r--r-- 1 1001 1001   21315749 May 25  2016 Zeus_Log_2016Y2M20D_11H48M19S_171MS.txt
-rw-r--r-- 1 1001 1001        416 May 25  2016 Zeus_Log_2016Y5M26D_1H44M12S_439MS.txt
-rw-r--r-- 1 1001 1001   12498587 Nov  3  2016 Zeus_Log_2016Y5M26D_2H0M10S_390MS.txt


## Supporting Material/References:

Nmap scan report for 217.147.95.145
Host is up (0.073s latency).
Not shown: 27 closed ports
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 6.0p1 Debian 4+deb7u3 (protocol 2.0)
| ssh-hostkey:
|   1024 9d:bc:9a:1e:2b:87:b6:92:5f:ea:06:24:9c:36:7f:48 (DSA)
|   2048 47:4b:b1:a9:d4:4f:b3:3b:6b:75:41:94:19:47:7d:66 (RSA)
|_  256 bb:22:09:05:68:67:b9:2f:cc:fd:69:66:50:4c:da:e0 (ECDSA)
111/tcp   open  rpcbind    2-4 (RPC #100000)
| nfs-showmount:
|_  /zeus0 *
| nfs-statfs:
|   Filesystem  1K-blocks   Used       Available  Use%  Maxfilesize  Maxlink
|_  /zeus0      10474496.0  2223696.0  8250800.0  22%   1024.0T      256
| rpcinfo:
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100003  3           2049/tcp  nfs
|   100005  1,3        38466/tcp  mountd
|   100021  1            660/udp  nlockmgr
|   100021  1,4          662/tcp  nlockmgr
|   100024  1          43538/tcp  status
|   100024  1          44527/udp  status
|_  100227  3           2049/tcp  nfs_acl
662/tcp   open  nlockmgr   1-4 (RPC #100021)
2049/tcp  open  nfs_acl    3 (RPC #100227)
9102/tcp  open  jetdirect?
24007/tcp open  rpcbind
| nfs-showmount:
|_  /zeus0 *
| nfs-statfs:
|   Filesystem  1K-blocks   Used       Available  Use%  Maxfilesize  Maxlink
|_  /zeus0      10474496.0  2223696.0  8250800.0  22%   1024.0T      256
38465/tcp open  nfs        0 (RPC #100003)
38466/tcp open  mountd     1-3 (RPC #100005)
| nfs-showmount:
|_  /zeus0 *
38468/tcp open  nfs        0 (RPC #100003)
38469/tcp open  nfs        0 (RPC #100003)
43538/tcp open  status     1 (RPC #100024)
49152/tcp open  rpcbind
| nfs-showmount:
|_  /zeus0 *
| nfs-statfs:
|   Filesystem  1K-blocks   Used       Available  Use%  Maxfilesize  Maxlink
|_  /zeus0      10474496.0  2223696.0  8250800.0  22%   1024.0T      256
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel




ls -la app_zeus1.8
total 4483
drwxr-xr-x 3 root root    4096 Jan 13  2016 .
drwxr-xr-x 7 root root      75 Nov  4  2015 ..
-rw-r--r-- 1 1001 1001     368 Jan 13  2016 Config.xml
-rw-r--r-- 1 root root     389 Jan 13  2016 Config.xml2
-rw-r--r-- 1 root root     311 Dec  4  2015 Config.xml_bck
-rw-r--r-- 1 root root     368 Dec 16  2015 Config.xml_bck2
-rw-r--r-- 1 root root     332 Dec  4  2015 Config.xml_test
-rw-r--r-- 1 1001 1001 1394864 Oct  4  2013 FSharp.Core.dll
-rw-r--r-- 1 1001 1001 1070080 Feb  6  2015 FSharp.Data.dll
-rw-r--r-- 1 1001 1001 1084928 Feb  6  2015 FSharp.Data.pdb
-rw-r--r-- 1 1001 1001  691712 Feb  6  2015 FSharp.PowerPack.dll
drwxr-xr-x 2 1001 1001     232 Nov  3  2016 logs
-rw-r--r-- 1 1001 1001   25600 Feb 27  2015 udpkit.common.dll
-rw-r--r-- 1 1001 1001  114176 Feb 27  2015 udpkit.common.pdb
-rw-r--r-- 1 1001 1001   65024 Feb 27  2015 udpkit.master.dll
-rw-r--r-- 1 1001 1001   77312 Feb 27  2015 udpkit.master.pdb
-rw-r--r-- 1 1001 1001   26112 Feb 27  2015 zeus.exe
-rw-r--r-- 1 1001 1001     527 Feb 27  2015 zeus.exe.config
-rw-r--r-- 1 root root       0 Jan 13  2016 Zeus_Log_2015Y12M4D_20H15M6S_636MS.txt
-rw-r--r-- 1 root root       0 Jan 13  2016 Zeus_Log_2015Y12M4D_20H3M35S_264MS.txt
-rw-r--r-- 1 1001 1001   32256 Feb 27  2015 zeus.pdb
{F237149}
{F237150}
{F237151}

## Attachments
- Screen_Shot_2017-11-06_at_2.52.43_PM.png
- Screen_Shot_2017-11-06_at_2.52.28_PM.png
- Screen_Shot_2017-11-06_at_2.53.28_PM.png
