# Sauce Labs API key unencrypted in an old commit

## Report Details
- **Report ID**: 1302395
- **URL**: https://hackerone.com/reports/1302395
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-13T00:41:13.928Z
- **Disclosed**: 2024-10-08T20:25:20.091Z

## Reporter
- **Username**: trufflesecurity
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
Hey there,

I found an API key in an old copy of the Travis.yaml file which is encoded, not encrypted. It's available here https://github.com/rails/rails/blob/a9cb1968b6a01572a472a3df3aa750ebc022e076/.travis.yml#L32

This decodes to a key you can test as seen below:
```
curl https://rubyonrails:a035343f-e922-40b3-aa3c-06b3ea635c48@saucelabs.com/rest/v1/users/rubyonrails
```

which returns:
```
{"username": "rubyonrails", "vm_lockdown": false, "new_email": null, "last_name": null, "tunnels_lockdown": false, "parent": null, "team_management": true, "creation_time": 1462825877, "user_type": "floss (medium)", "monthly_minutes": {"manual": "infinite", "automated": "infinite"}, "prevent_emails": ["marketing"], "to_plan": null, "performance_enabled": false, "domain": null, "manual_minutes": "infinite", "can_run_manual": true, "concurrency_limit": {"mac": 15, "scout": 10, "overall": 10, "real_device": 0}, "is_public": true, "to_username": null, "id": "rubyonrails", "access_key": "a035343f-e922-40b3-aa3c-06b3ea635c48", "first_name": "Ruby on Rails", "verified": true, "name": null, "subscribed": false, "title": null, "ancestor_user_type": "floss (medium)", "terminating_subscription": false, "is_sso": false, "allow_integrations_page": true, "to_migration_status": null, "last_login": null, "ancestor_concurrency_limit": {"mac": 15, "scout": 10, "overall": 10, "real_device": 0}, "allowed_regions": ["us-west-1"], "require_full_name": false, "sso_alias": null, "ancestor": "rubyonrails", "minutes": "infinite", "email": "██████████", "to_migration_date": null}%
```

Indicating the key the key is still active.

## Impact

At a glance I don't see any access controls on sauce labs, so I think this key might give an attacker full control of ████'s account.

I found the key using [TruffleHog](https://github.com/trufflesecurity/truffleHog), which is an open source tool I wrote that finds secrets in source code

## Attachments
No attachments
