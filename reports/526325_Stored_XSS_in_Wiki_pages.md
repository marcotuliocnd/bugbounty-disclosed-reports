# Stored XSS in Wiki pages

## Report Details
- **Report ID**: 526325
- **URL**: https://hackerone.com/reports/526325
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-04T12:14:14.275Z
- **Disclosed**: 2019-09-02T11:30:07.764Z

## Reporter
- **Username**: ryhmnlfj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

I found Stored XSS using Wiki-specific Hierarchical link Markdown in Wiki pages.

### Steps to reproduce

1. Sign in to GitLab.
2. Open a Project page that you have permission to edit Wiki pages.
3. Open Wiki page.
4. Click "New page" button.
5. Fill out "Page slug" form with `javascript:`.
6. Click "Create page" button.
7. Fill out the each form as follows:    
Title: `javascript:`    
Format: Markdown    
Content: `[XSS](.alert(1);)`    
(Please see "CreatePage.png")    
{F462086}    
8. Click "Create page" button.
9. Click "XSS" link in created page.

### What is the current *bug* behavior?

The alert dialog appears after clicking "XSS" link in created page.
Please see "Result_Firefox.png".
{F462087}

#### Description In Detail:

GitLab application converts the Markdown string `.alert(1);` to the href attribute `javascript:alert(1);`.
Furthermore, Wiki-specific Markdown string `.` is converted to `javascript:` in this case.

### What is the expected *correct* behavior?

The dangerous href attribute `javascript:alert(1);` should be filtered.
A safe HTTP/HTTPS link should be rendered instead.

### Additional Informations:

1. In the above case, another Wiki-specific Markdown string `..` is also converted to `javascript:`.

2. Using Title string such as `javascript:STRING_EXPECTED_REMOVING` also reproduces this vulnerability.
For example, if a wiki page is created with a disguised Title string `JavaScript::SubClassName.function_name`, GitLab application converts Wiki-specific Markdown string `.` to `JavaScript:` in such page.
It seems that GitLab application recognizes scheme-like string `JavaScript:` and removes the rest of Title string `:SubClassName.function_name`.

3. An attacker can use various schemes by replacing Title string `javascript:` to other scheme. (e.g. `data:`, `vbscript:`, and so on.)

### Output of checks

This bug happens on the official Docker installation of GitLab Enterprise Edition 11.9.4-ee.

#### Results of GitLab environment info

Output of `sudo gitlab-rake gitlab:env:info`:

```
System information
System:		
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.5.3p105
Gem Version:	2.7.6
Bundler Version:1.16.6
Rake Version:	12.3.2
Redis Version:	3.2.12
Git Version:	2.18.1
Sidekiq Version:5.2.5
Go Version:	unknown

GitLab information
Version:	11.9.4-ee
Revision:	55be7f0
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	postgresql
DB Version:	9.6.11
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	8.7.1
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

If wiki pages created by using this vulnerability are visible to everyone (Wiki Visibility setting is set to "Everyone With Access") in "Public" project, there is a possibility that a considerable number of GitLab users and visitors click a malicious link.

## Attachments
- CreatePage.png
- Result_Firefox.png
