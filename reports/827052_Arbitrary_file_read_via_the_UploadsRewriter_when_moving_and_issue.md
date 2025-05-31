# Arbitrary file read via the UploadsRewriter when moving and issue

## Report Details
- **Report ID**: 827052
- **URL**: https://hackerone.com/reports/827052
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-03-23T10:54:31.839Z
- **Disclosed**: 2020-04-27T16:15:59.072Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
The `UploadsRewriter` does not validate the file name, allowing arbitrary files to be copied via directory traversal when moving an issue to a new project.

The pattern used to look for references is :
```
  MARKDOWN_PATTERN = %r{\!?\[.*?\]\(/uploads/(?<secret>[0-9a-f]{32})/(?<file>.*?)\)}.freeze
```

This is used by the `UploadsRewriter` when copying an issue to also copy across the files:

```ruby
   @text.gsub(@pattern) do |markdown|
          file = find_file(@source_project, $~[:secret], $~[:file])
          break markdown unless file.try(:exists?)

          klass = target_parent.is_a?(Namespace) ? NamespaceFileUploader : FileUploader
          moved = klass.copy_to(file, target_parent)
...
   def find_file(project, secret, file)
        uploader = FileUploader.new(project, secret: secret)
        uploader.retrieve_from_store!(file)
        uploader
      end
```

As there is no restriction on what `file` can be, path traversal can be used to copy any file.

Demo
{F757226}

### Steps to reproduce

1. Create two projects
1. Add an issue with the following description:

  ```markdown
![a](/uploads/11111111111111111111111111111111/../../../../../../../../../../../../../../etc/passwd)
```
1. Move the issue to  the second project
1. The file will have been copied to the project

### Impact

Allows an attacker to read arbitrary files on the server, including tokens, private data, configs, etc

### What is the current *bug* behavior?

The file name and path are not checked when copying an issue between projects

### What is the expected *correct* behavior?

The file or path should be validated before copying files.

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
Git Version:	2.24.1
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	12.8.7-ee
Revision:	2643fd87200
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
Version:	11.0.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

Allows an attacker to read arbitrary files on the server, including tokens, private data, configs, etc

## Attachments
- file-read.mp4
