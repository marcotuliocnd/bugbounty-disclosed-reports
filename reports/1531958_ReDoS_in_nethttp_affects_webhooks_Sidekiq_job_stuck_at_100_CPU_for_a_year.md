# ReDoS in net/http affects webhooks: Sidekiq job stuck at 100% CPU for a year

## Report Details
- **Report ID**: 1531958
- **URL**: https://hackerone.com/reports/1531958
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-06T05:09:58.763Z
- **Disclosed**: 2022-09-13T04:42:18.678Z

## Reporter
- **Username**: afewgoats
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

A Gitlab webhook may be pointed at a malicious webhook receiver.
The webhook receiver can respond with a specially crafted long header.
Gitlab processes the header with Ruby's net/http where there is a regular expression operation with quadratic complexity (ReDoS).
This causes the `web_hook` Sidekiq job to get stuck at 100% CPU utilisation until the regular expression processing is complete (weeks later).
The long headers are also kept in memory and the connection can be kept open.

#### Comparison to 1252116

In report #1252116, the impact was that the network connection was kept open indefinitely, potentially causing connection pool and memory exhaustion. This new report is instead about CPU exhaustion for a more serious and more powerful DoS. It also bypasses the timeout added to fix #1252116 (https://gitlab.com/gitlab-org/gitlab/-/commit/a8807ee52d0b22b68beb31f0cad6ad5b77b4caf6) (deployed in 14.9.2) as the timeout only gets hit once the regular expression has finished processing (timeout is checked between header lines).

#### The root cause

A Regular Expression Denial of Service (ReDoS) vulnerability in Ruby's net/http affects Gitlab webhooks.

The bug is in [net/http/response.rb#57](https://github.com/ruby/net-http/blob/7b852b1feb7c1c0bc3019687d6ee5c385ce26eb9/lib/net/http/response.rb#L57) when reading headers line by line:

```rb
line = sock.readuntil("\n", true).sub(/\s+\z/, '')
```

The `sub` regex is the issue. While it looks safe and linear, the `sub` operation will actually have quadratic complexity as there is no starting anchor.

A header line which contains many consecutive spaces but *does not end in a space*, such as

```rb
( "a" + " " * 950000 + "b" ).sub(/\s+\z/, '')
```

will exhibit extreme backtracking.

The time complexity is quadratic with respect to the number of spaces in the string (doubling the number of spaces quadruples the processing time). Approximate timings from my laptop (I measured until 10,000 and then extrapolated):

```
|  Spaces  |  Seconds   |  Hours   |  Days  |
|----------|------------|----------|--------|
|     2000 |        1.8 |          |        |
|     4000 |        7.2 |          |        |
|     8000 |       28.6 |          |        |
|    10000 |       44.7 |          |        |
|   100000 |     4473.0 |     1.24 |   0.05 |
|  1000000 |   447300.0 |   124.25 |   5.18 |
| 10000000 | 44730000.0 | 12425.00 | 517.71 |
```

### Steps to reproduce

1. Run the attached malicious node server on port 3000: `node ./net-http-response.js`
2. Create a project and add webhooks for issue events to http://maliciousserver:3000/xyz.
3. (If you hosted the malicious server on your local network, you will need to "Allow requests to the local network from web hooks and services" in /admin/application_settings/network.)
4. Create an issue (or close or reopen one) to trigger the webhook. Gitlab will make a webhook request.
5. The malicious server will respond with `HTTP/1.1 200 OK` and then a header line with 9,500,000 consecutive spaces in the middle.
6. The `web_hook` Sidekiq job will be stuck processing at 100% CPU and will not complete for **over a year**. This can be seen in the Background Jobs panel (/admin/background_jobs) and `top`:

{F1681377}

{F1681378}

The ReDoS triggers on web requests made to Gitlab which trigger an external request e.g. validating the URL before repository import. However, in these cases a `RequestTimeoutException` triggers after 60 seconds of 100% CPU.

The regex runs without a timeout on project webhooks. It's not just project webhooks though. Any use of `Gitlab::HTTP.post` such as system webhooks and integrations (e.g. Mattermost) are affected.

To demonstrate the net/http bug:

```rb
require 'net/http'
uri = URI('http://maliciousserver:3000/x')
Net::HTTP.get(uri)
```

### What is the current *bug* behavior?

Gitlab webhooks and system hooks get stuck for years in a CPU intensive regular expression operation when receiving a malicious header from an external service.

### What is the expected *correct* behavior?

Processing a webhook response should never take longer than a year. More strictly, it should obey the webhook read timeout and also not run at 100% CPU.

Ruby should simply use `sock.readuntil("\n", true).rstrip` instead of a regex as I think it does the same thing. I can make a PR / issue for ruby unless you want to do it yourselves - let me know if and how you want me to proceed.

Potentially drop responses with very long header lines.

### Relevant logs and/or screenshots

net/http is called by httparty which is called by
```
"lib/gitlab/http.rb:57:in `perform_request'","app/services/web_hook_service.rb:125:in `make_request'"
```

### Output of checks

The bug happens locally. I did not test this on Gitlab.com because I'm sure it will affect it.

#### Results of GitLab environment info

(For installations with omnibus-gitlab package run and paste the output of:
`sudo gitlab-rake gitlab:env:info`)

Running in docker

```
System information
System:
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.5p203
Gem Version:    3.1.4
Bundler Version:2.2.33
Rake Version:   13.0.6
Redis Version:  6.2.6
Sidekiq Version:6.4.0
Go Version:     unknown

GitLab information
Version:        14.9.2-ee
Revision:       3034418fb31
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.7
URL:            https://gitlab.example.com
HTTP Clone URL: https://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers: 

GitLab Shell
Version:        13.24.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
```

## Impact

CPU exhaustion DoS.
Memory exhaustion DoS.
CPU intensive Sidekiq job runs forever (ok, not forever, but over a year) wasting energy and slowing down the system.
Also possible to get connection pool exhaustion by sending data slowly and keeping the socket open until the regex completes (bypassing fix for #1252116) for multiple webhook connections.

## Attachments
- gitlab-high-cpu-header-regex-dos.png
- gitlab-header-regex-dos-sidekiq-background_jobs.png
- net-http-response.js
