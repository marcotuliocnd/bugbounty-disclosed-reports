# XSS by clicking Jira's link

## Report Details
- **Report ID**: 1194254
- **URL**: https://hackerone.com/reports/1194254
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-12T16:10:03.660Z
- **Disclosed**: 2022-06-08T14:07:40.490Z

## Reporter
- **Username**: ooooooo_q
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Since the value of `/-/jira_connect/users?return_to=xxx` of `xxx` is used as a link as it is, it becomes XSS in some browsers.

### Steps to reproduce

1. Prepare a gitlab environment with no CSP configured (e.g. `localhost`)
2. Logged in with safari browser
3. Go to the `https://localhost/-/jira_connect/users?return_to=javascript:alert(location)` URL
4. click `Return to GitLab for Jira` button

### Impact

XSS

### Examples

Affects logged-in users regardless of project.

### What is the current *bug* behavior?

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.11.3-ee/app/controllers/jira_connect/users_controller.rb

```ruby
class JiraConnect::UsersController < ApplicationController
  feature_category :integrations

  layout 'signup_onboarding'

  def show
    @jira_app_link = params.delete(:return_to)
  end
end
```

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.11.3-ee/app/views/jira_connect/users/show.html.haml

```haml
  - if @jira_app_link
    %p= external_link s_('Integrations|Return to GitLab for Jira'), @jira_app_link, class: 'gl-button btn btn-confirm'
```

https://gitlab.com/gitlab-org/gitlab/-/blob/v13.11.3-ee/app/helpers/external_link_helper.rb

```haml
module ExternalLinkHelper
  def external_link(body, url, options = {})
    link_to url, { target: '_blank', rel: 'noopener noreferrer' }.merge(options) do
      "#{body}#{sprite_icon('external-link', css_class: 'gl-ml-1')}".html_safe
    end
  end
end
```
`external_link` has not verified the validity of the url.

### What is the expected *correct* behavior?

If it is a link other than http and https, it will not work.

### Relevant logs and/or screenshots

{F1298918}

### Output of checks

Blocked by CSP at GitLab.com

#### Results of GitLab environment info

```
# gitlab-rake gitlab:env:info

System information
System:
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	6.0.12
Git Version:	2.31.1
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.11.3
Revision:	b321336e443
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.6
URL:		https://gitlab.example.com
HTTP Clone URL:	https://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	13.17.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

It becomes XSS when the user is directed to the user who is logged in with the Safari browser to the instance where CSP is not set.

Chrome and Firefox showed other tabs and javascript was not executed.

## Attachments
- jira_safari_xss.png
