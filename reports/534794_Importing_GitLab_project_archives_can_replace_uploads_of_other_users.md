# Importing GitLab project archives can replace uploads of other users

## Report Details
- **Report ID**: 534794
- **URL**: https://hackerone.com/reports/534794
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-11T00:14:26.525Z
- **Disclosed**: 2019-12-11T10:39:45.788Z

## Reporter
- **Username**: ajxchapman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
Importing a modified exported GitLab project archive can overwrite uploads for other users.  If the `secret` and `file name` of an upload are known (these can be easily identified for any uploads to public repositories), any user can import a new project which overwrites the served content of the upload with arbitrary content.

This issue could be abused to backdoor project compiled binaries, allowing the spread of malware.

I have not performed a full risk assessment or root cause analysis of this issue at this time. I wanted to get the issue reported to GitLab asap after discovery. If you require any further details or information please let me know.

### Steps to reproduce
See the video below for an example of this issue:
{F466353}

The video shows the following steps:
1. As user `root` (on the left hand side of the video), create a new project
1. Upload a file to the project (e.g. by creating a new issue)
1. Take note of the file `secret` and `file name` of the original upload
1. Craft a GitLab project export tar.gz with the replacement upload file with a path equal to the original upload `secret` and `file name`, e.g. `./uploads/ed5ab56bc85699117ba230eb799fd3bf/indi.jpg` (See {F466355} attached)
1. As user `test` (on the right hand side of the video) create a new project, importing the crafted tar.gz from the above step
1. As the user `root` refresh your view of the upload file, and note that it has been modified

This example was demonstrated against the official GitLab docker image from https://hub.docker.com/r/gitlab/gitlab-ce/.

### Impact
Any upload type can be replaced using this method, if the `secret` and `file name` are known (these can be easily identified for any uploads to public repositories). An attacker could abuse this to backdoor project compiled binaries, allowing the spread of malware.



### Examples
See the attached project files:
1. Origin project export {F466356}
1. Modified project export used to change the upload file {F466355}

### What is the current *bug* behavior?
Importing a project as any user can modify the served upload files of other users.

### What is the expected *correct* behavior?
Importing a project should not be able to modify the served upload files of other users.

### Relevant logs and/or screenshots
See the following `/var/log/gitlab/gitlab-rails/production.log` entry:
```log
Started GET "/root/new_project/uploads/ed5ab56bc85699117ba230eb799fd3bf/indi.jpg" for 127.0.0.1 at 2019-04-10 23:07:12 +0000
Processing by Projects::UploadsController#show as HTML
  Parameters: {"namespace_id"=>"root", "project_id"=>"new_project", "secret"=>"[FILTERED]", "filename"=>"indi.jpg"}
Sent file /opt/gitlab/embedded/service/gitlab-rails/public/uploads/test/modified_project/ed5ab56bc85699117ba230eb799fd3bf/indi.jpg (0.2ms)
```
Note that the request was for the `/root/new_project/uploads/ed5ab56bc85699117ba230eb799fd3bf/indi.jpg` file, however the file from the `test/modified_project` was  served.

### Output of checks
#### Results of GitLab environment info
GitLab docker environment:
```sh
 docker images gitlab/gitlab-ce
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gitlab/gitlab-ce    latest              7a65562fb501        6 days ago          1.78GB
```

gitlab-rake gitlab:env:info
```sh
System information
System:
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
Version:        11.9.6
Revision:       14bac95
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     postgresql
URL:            http://gitlab.example.com
HTTP Clone URL: http://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
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

## Impact

Any upload type can be replaced using this method, if the `secret` and `file name` are known (these can be easily identified for any uploads to public repositories). An attacker could abuse this to backdoor project compiled binaries, allowing the spread of malware.

I have not performed a full risk assessment or root cause analysis of this issue at this time. I wanted to get the issue reported to GitLab asap after discovery.

## Attachments
- gitlab_uploads.mp4
- modified.tar.gz
- 2019-04-10_23-56-482_root_new_project_export.tar.gz
