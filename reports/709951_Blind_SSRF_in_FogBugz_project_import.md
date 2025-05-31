# Blind SSRF in FogBugz project import

## Report Details
- **Report ID**: 709951
- **URL**: https://hackerone.com/reports/709951
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-08T19:27:07.400Z
- **Disclosed**: 2023-05-30T06:53:04.576Z

## Reporter
- **Username**: mike12
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Steps to reproduce

1. Run GitLab `docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest`
2. Connect to the GitLab Docker container: `docker exec -it gitlab /bin/bash`
3. Install netcat: `apt update && apt install -y netcat`
4. Run server in container: `nc -llvp 12345`
5. Use http://localhost:12345 as FogBugz URL  (see screenshot) 
{F602736}

#### Results of GitLab environment info

```
root@gitlab:/# gitlab-rake gitlab:env:info

System information
System:    
Current User:  git
Using RVM:  no
Ruby Version:  2.6.3p62
Gem Version:  2.7.9
Bundler Version:1.17.3
Rake Version:  12.3.2
Redis Version:  3.2.12
Git Version:  2.22.0
Sidekiq Version:5.2.7
Go Version:  unknown

GitLab information
Version:  12.3.5
Revision:  2417d5becc7
Directory:  /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:  PostgreSQL
DB Version:  10.9
URL:    http://gitlab.example.com
HTTP Clone URL:  http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
Using LDAP:  no
Using Omniauth:  yes
Omniauth Providers: 

GitLab Shell
Version:  10.0.0
Repository storage paths:
- default:   /var/opt/gitlab/git-data/repositories
GitLab Shell path:    /opt/gitlab/embedded/service/gitlab-shell
Git:    /opt/gitlab/embedded/bin/git
```

## Impact

The vulnerability allows an attacker to make arbitrary requests inside a GitLab instance's network.

## Attachments
- Screenshot_from_2019-10-08_21-04-34.png
