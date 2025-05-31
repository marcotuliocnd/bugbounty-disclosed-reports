# Uncontrolled Resource Consumption in any Markdown field using Mermaid

## Report Details
- **Report ID**: 670572
- **URL**: https://hackerone.com/reports/670572
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-09T13:54:02.818Z
- **Disclosed**: 2019-12-20T07:15:12.672Z

## Reporter
- **Username**: ryhmnlfj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

I found a bypass for the mitigation of [DoS via Mermaid (CVE-2019-9220)](https://hackerone.com/reports/470067).
As the mitigation for [CVE-2019-9220](https://hackerone.com/reports/470067), the input limit of 5000 characters is currently applied to a Mermaid code block, but it can be bypassed by simply splitting the longer payload to **many** code blocks.

### Steps to reproduce

1. Sign in to GitLab.
2. Open any page where you can input Markdown text using Mermaid into the form.
3. Copy and paste the contents of the attached file (**"payload-5Kchars-x-100blocks.txt"**) to the input form.
4. Save the Markdown text on the page you opened. (For example, click "Comment" on "Issue" page. Please see "Example_on_Issue_page_Firefox.png")
5. Wait a few seconds for **many** Mermaid graphs to begin rendering.

{F551168}

### What is the current *bug* behavior?

When rendering of the Mermaid graphs starts, the browser tab displaying the page freezes.
This behavior prevents browsing and editing the page that have been added the Mermaid graphs.
Also, the resources used by the browser tab will increase as rendering continues. In the worst case, the entire browser also freezes or crashes.

### What is the expected *correct* behavior?

We need a mechanism to stop rendering in advance by detecting if the user's input contains a large number of Mermaid code blocks.

### Relevant logs and/or screenshots

* "payload-5Kchars-x-100blocks.txt" : This text contains 100 sets of Mermaid code blocks. Each code block contains approximately 5000 characters.
* "Example_on_Issue_page_Firefox.png" : Screenshot when pasting the payload on "Issue" page.

### Output of checks

This bug happens on the official Docker installation of GitLab Enterprise Edition `12.1.4-ee`.
The browsers used for testing are `Firefox 68` and `Chromium 76` on Ubuntu.

#### Results of GitLab environment info

Output of `sudo gitlab-rake gitlab:env:info`:
```
System information
System:		
Proxy:		no
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
Version:	12.1.4-ee
Revision:	4ea82400e72
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.7
URL:		http://gitlab.example.com
HTTP Clone URL:	http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.example.com:some-group/some-project.git
Elasticsearch:	no
Geo:		no
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

This vulnerability is effective not only on Issue pages but also on **all pages using Markdown with Mermaid**.

The following impacts exist on the attacked page:

* All users can not view the attacked page. (In some situations, the users may see incomplete rendering of the attacked page, but the user's viewing is still significantly blocked.)
* All users can not take any action on the attacked page.
* Depending on the user's environment, crashing or freezing the entire browser may cause user data being edited to be lost.

These impacts are almost the same as [CVE-2019-9220](https://hackerone.com/reports/470067).
These are more malicious than other issues that can be handled with 500 errors.

## Attachments
- payload-5Kchars-x-100blocks.txt
- Example_on_Issue_page_Firefox.png
