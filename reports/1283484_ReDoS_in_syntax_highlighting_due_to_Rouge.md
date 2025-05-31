# ReDoS in syntax highlighting due to Rouge

## Report Details
- **Report ID**: 1283484
- **URL**: https://hackerone.com/reports/1283484
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-29T16:40:15.658Z
- **Disclosed**: 2021-11-15T14:53:39.705Z

## Reporter
- **Username**: doyensec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Gitlab is using the ruby gem "rouge" which has a ReDoS vulnerability. In rouge, the lexers used to parse programming languages rely heavily on regular expressions. Some of the regular expressions have cubic worst-case complexity and are vulnerable to Regular Expression Denial of Service (ReDoS). By crafting malicious input, an attacker can cause Denial of Service.

In Gitlab, rouge is used for syntax highlighting when viewing source code files and when rendering markdown (issues, comments, wiki pages, etc.).

We first reported the vulnerability to rouge on 9 March 2021. As it remains unfixed and Gitlab is vulnerable, we are reporting here for your information.

### Rouge bug in detail

The vulnerable lexer regular expressions are below. Line numbers refer to the latest rouge version (3.26.0).

**Factor**
lib/rouge/lexers/factor.rb line 246
Pattern: `"""\s+.*?\s+"""`
As the two `\s+` groups and the `.*` group match spaces, a long string of spaces with no final `"""` will cause catastrophic backtracking.

**GHC Core**
lib/rouge/lexers/ghc_core.rb line 20
Pattern: `^Result size of .+\s*.*}`
Again, .+ \s* and .* all match spaces, so by not ending in a }, the regex will backtrack.

**Ceylon**
lib/rouge/lexers/ceylon.rb line 54
Pattern: `.*``.*``.*"`
The three .* groups match backticks as well, so if a long string of backticks doesn't end in a ", backtracking will occur. To cause ReDoS, an initial double quote is required.

The Factor and Ceylon regexes have been fixed on master (https://github.com/rouge-ruby/rouge/commit/78af25c2dd69be8ce0a83eb368ddcafe7cc294c4) but a new version has not been released. GHC Core has not been fixed.

__Recipes for creating source code files which cause ReDoS:__

GHC Core (.dump-cse): `'Result size of ' + ' ' * 3456`
Factor (.factor): `'"""' + ' ' * 3456`
Ceylon (.ceylon): ``'"' + '`' * 3456``

As the worst-case complexity is cubic, doubling the length of the repeating part (spaces or backticks) makes processing take 8 times as long.

### Steps to reproduce

#### To test the rouge gem itself outside Gitlab

Using the attached files, run `rougify redos.factor`, `rougify redos.dump-cse`, `rougify redos.ceylon` and see that processing takes a while. Doubling the length of the repeating section of the file will make the processing time take about 8 times as long.

#### Gitlab wiki (Stored ReDoS)

Edit the main wiki page by adding a fenced code block of factor, ceylon or ghc-core:

``````
```ghc-core
Result size of                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
```
``````

Attempt to view the wiki and get a 500 after ~60 seconds of 100% CPU.

#### Affect the Gitlab file viewer (Stored ReDoS)

Upload the redos.factor and redos.ceylon payloads to a repository and then view them. Increase the length of the repeating part to increase the time taken to process. If it takes >60 seconds, there will be a 502 error.

Upload README.md (containing a fenced code block) so that the ReDoS occurs every time the project page is visited.

#### Gitlab issues and comments

Create an issue containing a fenced code block of factor, ceylon or ghc-core. Rendering only occurs when creating or editing the issue or comment, not each time it's viewed.

### Impact

__Server DoS__ - The request causes Rouge to run at 100% CPU until killed e.g. by a 60 second timeout. Making multiple concurrent requests to the affected resources will overwhelm the server and make it unavailable.

Viewing a crafted .ceylon or .factor file will fail with 502 timeouts. As will viewing a Markdown page containing a fenced code block.

Visiting a wiki page with crafted factor, ceylon or ghc-core fenced code blocks will fail with a 500. If done on the home page, this blocks all access to the Wiki, unless you have a link to a particular wiki page or append `/edit` to the wiki page and fix it.

### What is the current *bug* behavior?

Rouge is vulnerable to ReDoS, so some Gitlab requests result in high CPU usage until timeout.

### What is the expected *correct* behavior?

Rouge regexes avoid overlapping / ambiguous regex patterns, avoiding cubic worst-case complexity.

### Relevant logs and/or screenshots

#### Viewing wiki

{F1386878}

```
Rack::Timeout::RequestTimeoutException (Request ran for longer than 60000ms):
  
lib/rouge/formatters/html_gitlab.rb:19:in `stream'
lib/gitlab/metrics/instrumentation.rb:160:in `block in stream'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `stream'
lib/banzai/filter/syntax_highlight_filter.rb:42:in `highlight_node'
lib/banzai/filter/syntax_highlight_filter.rb:22:in `block in call'
lib/banzai/filter/syntax_highlight_filter.rb:21:in `call'
lib/banzai/pipeline/base_pipeline.rb:23:in `block (2 levels) in singleton class'
lib/banzai/renderer.rb:130:in `render_result'
lib/gitlab/metrics/instrumentation.rb:160:in `block in render_result'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `render_result'
lib/banzai/renderer.rb:164:in `block in cacheless_render'
lib/gitlab/metrics.rb:79:in `measure'
lib/banzai/renderer.rb:163:in `cacheless_render'
lib/gitlab/metrics/instrumentation.rb:160:in `block in cacheless_render'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `cacheless_render'
lib/banzai/renderer.rb:30:in `render'
lib/gitlab/metrics/instrumentation.rb:160:in `block in render'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `render'
lib/banzai.rb:16:in `render'
app/helpers/markup_helper.rb:262:in `markdown_unsafe'
app/helpers/markup_helper.rb:140:in `markup_unsafe'
app/helpers/markup_helper.rb:131:in `render_wiki_content'
app/views/shared/wikis/show.html.haml:30
app/controllers/application_controller.rb:128:in `render'
app/controllers/concerns/wiki_actions.rb:81:in `show'
ee/lib/gitlab/ip_address_state.rb:10:in `with'
ee/app/controllers/ee/application_controller.rb:40:in `set_current_ip_address'
app/controllers/application_controller.rb:487:in `set_current_admin'
lib/gitlab/session.rb:11:in `with_session'
app/controllers/application_controller.rb:478:in `set_session_storage'
lib/gitlab/i18n.rb:99:in `with_locale'
lib/gitlab/i18n.rb:105:in `with_user_locale'
app/controllers/application_controller.rb:472:in `set_locale'
app/controllers/application_controller.rb:466:in `set_current_context'
lib/gitlab/metrics/elasticsearch_rack_middleware.rb:16:in `call'
lib/gitlab/middleware/rails_queue_duration.rb:33:in `call'
lib/gitlab/metrics/rack_middleware.rb:16:in `block in call'
lib/gitlab/metrics/web_transaction.rb:21:in `run'
lib/gitlab/metrics/rack_middleware.rb:16:in `call'
lib/gitlab/middleware/speedscope.rb:13:in `call'
lib/gitlab/request_profiler/middleware.rb:17:in `call'
lib/gitlab/jira/middleware.rb:19:in `call'
lib/gitlab/middleware/go.rb:20:in `call'
lib/gitlab/etag_caching/middleware.rb:21:in `call'
lib/gitlab/middleware/multipart.rb:172:in `call'
lib/gitlab/middleware/read_only/controller.rb:50:in `call'
lib/gitlab/middleware/read_only.rb:18:in `call'
lib/gitlab/middleware/same_site_cookies.rb:27:in `call'
lib/gitlab/middleware/handle_malformed_strings.rb:21:in `call'
lib/gitlab/middleware/basic_health_check.rb:25:in `call'
lib/gitlab/middleware/handle_ip_spoof_attack_error.rb:25:in `call'
lib/gitlab/middleware/request_context.rb:21:in `call'
config/initializers/fix_local_cache_middleware.rb:11:in `call'
lib/gitlab/middleware/rack_multipart_tempfile_factory.rb:19:in `call'
lib/gitlab/metrics/requests_rack_middleware.rb:74:in `call'
lib/gitlab/middleware/release_env.rb:12:in `call'
```

#### Viewing redos.ceylon

{F1386876}

{F1386877}

#### Editing an issue

{F1386899}

```
Completed 500 Internal Server Error in 60084ms (ActiveRecord: 44.0ms | Elasticsearch: 0.0ms | Allocations: 32909)
  
Rack::Timeout::RequestTimeoutException (Request ran for longer than 60000ms):
  
lib/rouge/formatters/html_gitlab.rb:19:in `stream'
lib/gitlab/metrics/instrumentation.rb:160:in `block in stream'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `stream'
lib/banzai/filter/syntax_highlight_filter.rb:42:in `highlight_node'
lib/banzai/filter/syntax_highlight_filter.rb:22:in `block in call'
lib/banzai/filter/syntax_highlight_filter.rb:21:in `call'
lib/banzai/pipeline/base_pipeline.rb:23:in `block (2 levels) in singleton class'
lib/banzai/renderer.rb:130:in `render_result'
lib/gitlab/metrics/instrumentation.rb:160:in `block in render_result'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `render_result'
lib/banzai/renderer.rb:164:in `block in cacheless_render'
lib/gitlab/metrics.rb:79:in `measure'
lib/banzai/renderer.rb:163:in `cacheless_render'
lib/gitlab/metrics/instrumentation.rb:160:in `block in cacheless_render'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `cacheless_render'
lib/banzai/renderer.rb:52:in `cacheless_render_field'
lib/gitlab/metrics/instrumentation.rb:160:in `block in cacheless_render_field'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `cacheless_render_field'
app/models/concerns/cache_markdown_field.rb:53:in `rendered_field_content'
app/models/concerns/cache_markdown_field.rb:62:in `block in refresh_markdown_cache'
app/models/concerns/cache_markdown_field.rb:59:in `to_h'
app/models/concerns/cache_markdown_field.rb:59:in `refresh_markdown_cache'
app/services/issuable_base_service.rb:263:in `block in update'
app/services/issuable_base_service.rb:262:in `update'
app/services/issues/update_service.rb:20:in `update'
lib/gitlab/metrics/instrumentation.rb:160:in `block in update'
lib/gitlab/metrics/method_call.rb:27:in `measure'
lib/gitlab/metrics/instrumentation.rb:160:in `update'
app/services/issues/update_service.rb:14:in `execute'
ee/app/services/ee/issues/update_service.rb:23:in `execute'
app/controllers/concerns/issuable_actions.rb:27:in `update'
ee/lib/gitlab/ip_address_state.rb:10:in `with'
ee/app/controllers/ee/application_controller.rb:40:in `set_current_ip_address'
app/controllers/application_controller.rb:487:in `set_current_admin'
lib/gitlab/session.rb:11:in `with_session'
app/controllers/application_controller.rb:478:in `set_session_storage'
lib/gitlab/i18n.rb:99:in `with_locale'
lib/gitlab/i18n.rb:105:in `with_user_locale'
app/controllers/application_controller.rb:472:in `set_locale'
app/controllers/application_controller.rb:466:in `set_current_context'
lib/gitlab/metrics/elasticsearch_rack_middleware.rb:16:in `call'
lib/gitlab/middleware/rails_queue_duration.rb:33:in `call'
lib/gitlab/metrics/rack_middleware.rb:16:in `block in call'
lib/gitlab/metrics/web_transaction.rb:21:in `run'
lib/gitlab/metrics/rack_middleware.rb:16:in `call'
lib/gitlab/middleware/speedscope.rb:13:in `call'
lib/gitlab/request_profiler/middleware.rb:17:in `call'
lib/gitlab/jira/middleware.rb:19:in `call'
lib/gitlab/middleware/go.rb:20:in `call'
lib/gitlab/etag_caching/middleware.rb:21:in `call'
lib/gitlab/middleware/multipart.rb:172:in `call'
lib/gitlab/middleware/read_only/controller.rb:50:in `call'
lib/gitlab/middleware/read_only.rb:18:in `call'
lib/gitlab/middleware/same_site_cookies.rb:27:in `call'
lib/gitlab/middleware/handle_malformed_strings.rb:21:in `call'
lib/gitlab/middleware/basic_health_check.rb:25:in `call'
lib/gitlab/middleware/handle_ip_spoof_attack_error.rb:25:in `call'
lib/gitlab/middleware/request_context.rb:21:in `call'
config/initializers/fix_local_cache_middleware.rb:11:in `call'
lib/gitlab/middleware/rack_multipart_tempfile_factory.rb:19:in `call'
lib/gitlab/metrics/requests_rack_middleware.rb:74:in `call'
lib/gitlab/middleware/release_env.rb:12:in `call'
```

### Output of checks

Not tested on GitLab.com, but it is almost certainly vulnerable. Tested in docker.

#### Results of GitLab environment info

```
System information
System:
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.2p137
Gem Version:    3.1.4
Bundler Version:2.1.4
Rake Version:   13.0.3
Redis Version:  6.0.14
Git Version:    2.32.0
Sidekiq Version:5.2.9
Go Version:     unknown

GitLab information
Version:        14.0.2-ee
Revision:       2504e045362
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.6
URL:            https://gitlab.example.com
HTTP Clone URL: https://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        13.19.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## Impact

CPU exhaustion DoS

## Attachments
- gitlab-viewer-error.png
- gitlab-rouge-ceylon.png
- gitlab-wiki-500.png
- redos.factor
- redos.ceylon
- redos.dump-cse
- README.md
- gitlab-issue.png
