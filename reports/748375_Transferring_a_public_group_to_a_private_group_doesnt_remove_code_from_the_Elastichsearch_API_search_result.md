# Transferring a public group to a private group doesn't remove code from the Elastichsearch API search result

## Report Details
- **Report ID**: 748375
- **URL**: https://hackerone.com/reports/748375
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-29T11:18:45.773Z
- **Disclosed**: 2020-10-06T21:57:06.733Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When a public group with public projects is transferred to a private group, the code and the wiki of the public project, although now should be private, it is still reachable through search APIs.

I set the severity as "medium" and not "high", because any new action over the project issues a re indexing (or some actions, not sure), so if the transfer is for "archiving" purposes it is a problem, but if after the transfer other activities happen, then it is not a problem, cause the project will be removed from the index.

### Steps to reproduce

Alice creates the public group "Example", and a public project named "Example-project" inside the group. In the readme of the project, Alice writes "Example".

Now, Alice creates a private group called "private", and transfer all the "Example" group to the "private" group.

If Bob (totally unrelated to Alice), search for "Example" instance-wide, will not find anything on the interface, but the count of the results will be "1" (see screenshot).

If he uses the APIs (e.g. http://localhost/api/v4/search?search=password&scope=blobs), he will receive the results back with the information that should be private.

This happens also with wiki_blobs.

This doesn't happen transferring single projects, but only transferring entire groups

### Output of checks

#### Results of GitLab environment info

``` 
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
Version:	12.5.2-ee
Revision:	c1b3929bc67
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.9
URL:		http://aldebaran
HTTP Clone URL:	http://aldebaran/some-group/some-project.git
SSH Clone URL:	git@aldebaran:some-group/some-project.git
Elasticsearch:	yes
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

## Impact

Alice thinks her code is now private, but it is not, unless she continues working on the project

## Attachments
No attachments
