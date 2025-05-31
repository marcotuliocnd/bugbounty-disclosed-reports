# GitHub import allows user to create child group under existing namespace

## Report Details
- **Report ID**: 301137
- **URL**: https://hackerone.com/reports/301137
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-29T01:13:46.612Z
- **Disclosed**: 2018-05-24T18:27:39.151Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
When importing a GitHub repository on GitLab, a request is made to `/import/github`. The user is allowed to pass along a target namespace where they want to add the repository. In this process, the code will create the namespace if it doesn't exist already. However, this can be used to create a sub-group of an existing group and give you "owner" level access to the sub-group. This has a couple benefits, including being able to use the plan of the owner group, see who is part of the group (helpful in case the group is private), and, perhaps most importantly, being able to create new projects under a group you're unauthorized to.

To reproduce, make sure there's a GitLab instance that has a group a user is unauthorized to create projects / groups for. Then, sign in to the normal user account and authorize GitLab to view your GitHub projects. Intercept your network traffic, then click the "Import" button. Observe a request similar to the one below being submitted:

**Request**
```
POST /import/github HTTP/1.1
Host: gitlab-instance
...

repo_id=115670444&target_namespace=jobertabma&new_name=test
```

In this request, change the `target_namespace` to `secret-group/test`. This will create a sub-group called `test` to the group `secret-group`.████ To exploit this, an attacker could set a GitLab logo as their group avatar and start spreading gitlab-ce and gitlab-ee projects under the gitlab-org namespace.

**The sub-group as shown on the gitlab-org group page**
{F250077}

**Automatic billing due to the relationship with gitlab-org**
{F250076}

This has been tested against the latest version of GitLab.

## Impact

N/A

## Attachments
- Screen_Shot_2017-12-28_at_5.11.46_PM.png
- Screen_Shot_2017-12-28_at_5.12.07_PM.png
