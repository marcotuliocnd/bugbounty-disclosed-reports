# Change project visibility to a restricted option

## Report Details
- **Report ID**: 1086781
- **URL**: https://hackerone.com/reports/1086781
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-25T15:23:00.325Z
- **Disclosed**: 2021-12-30T01:28:59.886Z

## Reporter
- **Username**: s4nderdevelopment
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When a GitLab administrator (on gitlab.com or a private instance) has restricted a project visibility option, the project visibility can still be changed to that option. This can be done using the API route. The same applies to groups. They can also be set to (for example) internal on the public gitlab.com website. 

### Steps to reproduce

(1. A GitLab instance administrator restricts the project visibility option 'internal', 'private' or 'public'. In this example, I will use the 'internal' option)
2. A non-privileged user creates a project (in this example, the id is 27236) and generates an access token for their account
3. The non-privileged user makes a PUT request to: '/api/v4/projects/27236' with the following body: '{"visibility": "internal"}' and their access token set in the 'Authorization' header like this: 'Bearer <access-token>'.
4. The non-privileged user should now have their project visibility set to internal, even though this should not be possible.

(5. The same actions can be applied to groups)

### Impact

When an administrator of a GitLab instance would like to keep all projects private or internal (for example, for universities and schools), students should not be able to modify their project visibility to public. This is also the case for our school. (I got permission to test this on my schools GitLab instance.) I cannot visit any project on my schools GitLab instance without logging in, except for one of my projects, which I have set to 'public'.

### Examples

This bug is project related, but I do not know if settings (including project visibility) get exported with the project. 

Tested GitLab versions: 13.7 and 13.8

Link to my project: https://gitlab.com/s4nderdevelopment/url-shortener

### What is the current *bug* behavior?

When the PUT API request was made, the response code is 200 and the response body shows the project with the updated option.
Also, on the project settings page, the grayed-out visibility option (restricted option) is selected.

### What is the expected *correct* behavior?

The API response should have the status code 403 if a restricted project visibility was selected. Also, the option should not be updated in the project settings.

### Relevant logs and/or screenshots

I added a screenshot as an attachment.

### Output of checks

This bug happens on GitLab.com

#### Results of GitLab environment info

The bug was also present on my test GitLab instance, so i executed `sudo gitlab-rake gitlab:env:info`:

```
System information
System:         Debian 10
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.2p137
Gem Version:    3.1.4
Bundler Version:2.1.4
Rake Version:   13.0.1
Redis Version:  5.0.9
Git Version:    2.29.0
Sidekiq Version:5.2.9
Go Version:     unknown

GitLab information
Version:        13.7.4-ee
Revision:       368b4fb2eee
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.4
URL:            http://DEBIAN-VM-S4NDER.local
HTTP Clone URL: http://DEBIAN-VM-S4NDER.local/some-group/some-project.git
SSH Clone URL:  git@DEBIAN-VM-S4NDER.local:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers: 

GitLab Shell
Version:        13.14.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## Impact

When an administrator of a GitLab instance would like to keep all projects private or internal (for example, for universities and schools), students should not be able to modify their project visibility to public. This is also the case for our school. (I got permission to test this on my schools GitLab instance.) I cannot visit any project on my schools GitLab instance without logging in, except for one of my projects, which I have set to 'public'.

## Attachments
- 2021-01-25_15-03-091_s4nderdevelopment_url-shortene_export.tar.gz
- Internal-grayed-out-project-visibility.png
