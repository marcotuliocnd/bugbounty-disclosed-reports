# A deactivated user can access data through GraphQL

## Report Details
- **Report ID**: 1192460
- **URL**: https://hackerone.com/reports/1192460
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-11T19:38:13.496Z
- **Disclosed**: 2021-08-30T13:25:12.844Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

A deactivated user should not be able to access information through the API. This rule is not enforced when making requests through the GraphQL endpoint. 

When reading through the changelog for 13.11.2 i noticed that the rule for a deactivated user allows for :log_in (as it should) but it is restricted from :access_api(as it should) [link](https://gitlab.com/gitlab-org/gitlab/-/blob/e568b72493328ad271ddb38f0b22109bc91d8447/app/policies/global_policy.rb#L64). The GraphQL endpoint does not seam to use this rules when authorizing a user. I guess GraphQL only checks for api scope on the user.

This opens for three potential problems:

* A user using its account through the GraphQL API (through some script or similar) would not get a warning that the account is deactivated. This could lead to the account being removed if the entities controlling the GitLab instance has any automatic procedures deleting accounts. When reading about the deactivation feature I got the impression that most admins requesting the feature would use it in automated "cleanings" of their user base. I could see how an admin could implement a "deactivate after 90 days inactivity" and "delete after 180 days inactivity" rule or similar. This could lead to an account being "in use" through GraphQL could get deleted without proper warnings.
* An admin could use deactivated accounts as "bots" or "service accounts" bypassing the billing of these accounts. (an admin can create users and deactivate them directly, before ever using the account)
* The fact that the account should not be able to do this. An admin reading the docs are under the assumption that a deactivated account is blocked from using the API. An inactive user could have left some form of scripts running that would keep on using resources on the GitLab instance, which I guess the admin would like to remediate by deactivating the account.

__as of 13.10.4:__ A deactivated user can (without activating its account) use read queries on the GraphQL endpoint. The latest security patch removes the ability to use mutations due to the fact that 
 ```
   rule { deactivated }.policy do
    prevent :access_git
    prevent :access_api
    prevent :receive_notifications
    prevent :use_slash_commands
  end
```
prevents :access_api, and
```
rule { ~can?(:access_api) }.prevent :execute_graphql_mutation
```
prevents from using mutations if I understand the code correctly.

__tested on 13.11.1:__  (Prior to latest security patch 13.11.2) A deactivated user can (without activating its account) use queries and mutations on the GraphQL endpoint.

### Steps to reproduce

__Unlimited service accounts__
1. Login as admin
2. Create a user
3. Deactivate the user
4. Create an api token for the deactivated user
5. Use the token in GraphQL requests such as (replacing url and token)
```
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n  currentUser{id}\n}"}'d
```

__User with deactivated account__
1. Use any old token from your deactivated account in requests such as
```
curl 'https://gitlab.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer <<TOKEN>>' --data '{"query":"{\n  currentUser{id}\n}"}'d
```

__or on servers prior to 13.11.2 (tested on 13.11.1)__
1. Login as admin
2. Create a user
3. Deactivate the user
4. Create an api token for the deactivated user
5. Add the user to a project with (use admin token, and a real project id)
```
curl --header "Authorization: Bearer <<ADMIN TOKEN>>" "https://gitlab.domain.com/api/v4/projects//members" --data "user_id=2&access_level=40"
```
6. Then perform a mutation with the disabled account:
```
curl 'https://gitlab.domain.com/api/graphql' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer <<DEACTIVATEDTOKEN>>' --data '{"query":"mutation {\n  labelCreate(input:{title:\"deactivated\", projectPath:\"test1/test1\"}){\n    errors\n    label{\n      id\n    }\n  }\n}"}'
```
to create a label in the project.

### Impact

For GitLab it could lead to loss of revenue due to the ability to create accounts that are not billabel but "usable". At the moment the GraphQL API is a bit limited but will probably grow in scope.

For users. Running the risk of missing warnings about disabled accounts. Could lead to deletion of account if admins does not notice that the account is being used.

### Examples

I would guess that this is affecting GitLab.com but can not create a disabled account there.

### What is the current *bug* behavior?

With a token from a disabled account the REST API gives:
```
curl --header "Authorization: Bearer jKSvxhuDN-Noag6N-w7R" "http://gitlab.joaxcar.com/api/v4/user"

{"message":"403 Forbidden - Your account has been deactivated by your administrator. Please log back in from a web browser to reactivate your account at http://gitlab.joaxcar.com"}
```
with GraphQL
```
curl 'http://gitlab.joaxcar.com/api/graphql' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Authorization: Bearer jKSvxhuDN-Noag6N-w7R' --data '{"query":"{\n  currentUser{id}\n}"}'

{"data":{"currentUser":{"id":"gid://gitlab/User/15"}}}
```

### What is the expected *correct* behavior?

GraphQL should give a warning as the REST API and block disabled users from accessing data.


#### Results of GitLab environment info

```
System information
System:		
Current User:	gitlab
Using RVM:	no
Ruby Version:	3.0.1p64
Gem Version:	/usr/lib/ruby/2.7.0/bundler/spec_set.rb:86:in `block in materialize': Could not find rake-13.0.3 in any of the sources (Bundler::GemNotFound)
	from /usr/lib/ruby/2.7.0/bundler/spec_set.rb:80:in `map!'
	from /usr/lib/ruby/2.7.0/bundler/spec_set.rb:80:in `materialize'
	from /usr/lib/ruby/2.7.0/bundler/definition.rb:170:in `specs'
	from /usr/lib/ruby/2.7.0/bundler/definition.rb:237:in `specs_for'
	from /usr/lib/ruby/2.7.0/bundler/definition.rb:226:in `requested_specs'
	from /usr/lib/ruby/2.7.0/bundler/runtime.rb:101:in `block in definition_method'
	from /usr/lib/ruby/2.7.0/bundler/runtime.rb:20:in `setup'
	from /usr/lib/ruby/2.7.0/bundler.rb:149:in `setup'
	from /usr/lib/ruby/2.7.0/bundler/setup.rb:20:in `block in <top (required)>'
	from /usr/lib/ruby/2.7.0/bundler/ui/shell.rb:136:in `with_level'
	from /usr/lib/ruby/2.7.0/bundler/ui/shell.rb:88:in `silence'
	from /usr/lib/ruby/2.7.0/bundler/setup.rb:20:in `<top (required)>'
	from <internal:/usr/lib/ruby/3.0.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
	from <internal:/usr/lib/ruby/3.0.0/rubygems/core_ext/kernel_require.rb>:85:in `require'
Bundler Version:unknown
Rake Version:	13.0.3
Redis Version:	6.2.3
Git Version:	2.31.1
Sidekiq Version:5.2.9
Go Version:	go1.16.4 linux/amd64

GitLab information
Version:	13.10.4
Revision:	e11cc45d59e
Directory:	/usr/share/webapps/gitlab
DB Adapter:	PostgreSQL
DB Version:	13.2
URL:		http://gitlab.joaxcar.com
HTTP Clone URL:	http://gitlab.joaxcar.com/some-group/some-project.git
SSH Clone URL:	gitlab@gitlab.joaxcar.com:some-group/some-project.git
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	13.17.0
Repository storage paths:
- default: 	/var/lib/gitlab/repositories
GitLab Shell path:		/usr/share/webapps/gitlab-shell
Git:		/usr/bin/git
```

## Impact

A user with a disabled account can access the GraphQL API without activating the account. Running the risk of missing warnings about disabled accounts. Could lead to deletion of account if admins does not notice that the account is being used. Or accessing data without admins knowing the account is in use.

An admin could create accounts that are not billable but "usable". By creating disables accounts and use them through GraphQL.

I put it at medium due to the risk of data loss if not getting proper warnings and the fact that it has access to the API even if explicitly told that it should not in the documentation.  But feel free to lower the severity if you disagree.

## Attachments
No attachments
