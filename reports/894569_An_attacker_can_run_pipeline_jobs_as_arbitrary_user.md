# An attacker can run pipeline jobs as arbitrary user

## Report Details
- **Report ID**: 894569
- **URL**: https://hackerone.com/reports/894569
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-09T15:53:22.000Z
- **Disclosed**: 2020-08-26T14:11:44.351Z

## Reporter
- **Username**: u3mur4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

An attacker can run arbitrary pipeline jobs as a `victim` user. This means the attacker can access the user private repositories, member only repositories, registry, etc... by using the victim `CI_JOB_TOKEN` token.

> This is only my recent research and I wanted to report it as soon as possible. I will update the report with more information later on.

### Steps to reproduce

VICTIM:

- Sign in to a GitLab instance as a *Victim user*
- Create an arbitrary private repository with some private files. (We will steal this repo as a poc.)

ATTACKER ACCOUNT 1: 

- Sign in to a GitLab instance as a *Attacker1 user*
- Create a new project using the following settings:
    - Project Name: `poc`
    - Visibility Level : `public`
    - Check the `Initialize repository with a README` checkbox
- Add a new `.gitlab-ci.yml` file to the project

```
image: "ruby:2.6"

before_script:
  - echo Hello

rspec:
  script:
    - echo Hello
```

> We will mirror this repository and update the `.gitlab-ci.yml` file later on to trigger the CI/CD job.

ATTACKER ACCOUNT 2: 
- Sign in / Register to a GitLab instance as a *Attacker2 user*
- Create a new public group called as `test`
- Create a new project inside the `test` group using the following settings:
    - Project Name: `poc`
    - Visibility Level : `public`
- Go to `Project settings` => `Repository` => `Mirroring repositories`
    - Set `Git repository URL` to the previously created repository by the *Attacker1 user*
    - Set `Mirror direction` to `Pull`
    - Check the `Trigger pipelines for mirror updates` checkbox
    - Click the `Mirror repository` button
- Go to the `test` group `Members` option and invite the *Victim user*
- Set the *Victim user* `Choose a role permission` to `Owner`
- Go to the `Account Setting` => `Account` and delete this account.

ATTACKER ACCOUNT 1: 

- Sign in back to the GitLab instance as a *Attacker1 user*
- Go to the `attacker1/poc` project and update the `.gitlab-ci.yml` file using the following content:

```
image: "ruby:2.6"

rspec:
  script:
    - git clone https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.com/victim/private_repo_name.git
    - cd private_repo_name
    - ls -lah .
    - cat README.md
```
- Wait half an hour to automatically trigger a mirror update in the `test/poc` project which owner is the *Victim user*.

The `test/poc` project will trigger a mirror update which also triggers a pipeline run. The triggerer of the pipeline will be the *Victim user*. 
The *Attacker1 user* controls the `attacker/poc/gitlab-ci.yml` file which is mirrored to the `test/poc` project.


### What is the current *bug* behavior?

- If there is a mirrored project with `Trigger pipelines for mirror updates` enabled inside a group and the group owner delete its account (need another owner role inside the group) then the trigger of the pipeline will be to other owner account. (I think this only works when the account deleted without removing the account from the group members but I still need to confirm this.)

### What is the expected *correct* behavior?

- refuse pipeline run in the previously mentioned case

### Output of checks

This bug happens on GitLab.com.

#### Results of GitLab environment info
```
bundle exec rake gitlab:env:info RAILS_ENV=development
System information
System:		
Proxy:		no
Current User:	u3mur4
Using RVM:	no
Ruby Version:	2.6.6p146
Gem Version:	3.0.3
Bundler Version:1.17.3
Rake Version:	12.3.3
Redis Version:	6.0.4
Git Version:	2.27.0
Sidekiq Version:5.2.7
Go Version:	go1.14.4 linux/amd64

GitLab information
Version:	13.1.0-pre
Revision:	4bd9f8164e0
Directory:	/home/u3mur4/Hack/gitlab/gitlab-development-kit/gitlab
DB Adapter:	PostgreSQL
DB Version:	12.3
URL:		http://gdk.yoyo.pw:3000
HTTP Clone URL:	http://gdk.yoyo.pw:3000/some-group/some-project.git
SSH Clone URL:	ssh://u3mur4@gdk.yoyo.pw:2222/some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: google_oauth2

GitLab Shell
Version:	13.3.0
Repository storage paths:
- default: 	/home/u3mur4/Hack/gitlab/gitlab-development-kit/repositories
GitLab Shell path:		/home/u3mur4/Hack/gitlab/gitlab-development-kit/gitlab-shell
Git:		/usr/bin/git
```

## Impact

stealing the CI_JOB_TOKEN of any user (access the user private repositories, member only repositories and registry, etc...)

## Attachments
No attachments
