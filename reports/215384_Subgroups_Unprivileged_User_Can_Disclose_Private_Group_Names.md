# [Subgroups] Unprivileged User Can Disclose Private Group Names

## Report Details
- **Report ID**: 215384
- **URL**: https://hackerone.com/reports/215384
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-22T16:14:59.742Z
- **Disclosed**: 2017-03-30T06:18:52.225Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi @briann and team,

Congratulations on the launch of GitLab 9.0! While exploring Subgroup functionality, I noticed that an unprivileged user can disclose private group names by incrementing the `parent_id` parameter. 

## Proof of Concept
To reproduce this issue, I set up a fresh GitLab 9.0 CE server and created a Private Group using the `root` account. Afterwards, I created an unprivileged user (no group or project assignments) and visited the below URL, disclosing the name of `PrivateGroup`.

Attempting to access the `PrivateGroup` via the standard routes (e.g. Group Page) presents the unprivileged user with the expected 404 page.

```
http://<instance>/groups/new?parent_id=2
```

### Screenshot
{F170581}

Thanks!

## Attachments
- ExposedGroupName.png
