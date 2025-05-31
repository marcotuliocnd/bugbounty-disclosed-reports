# Group search leaks private MRs, code, commits

## Report Details
- **Report ID**: 692252
- **URL**: https://hackerone.com/reports/692252
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-11T10:22:51.911Z
- **Disclosed**: 2019-12-14T11:25:59.717Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Using the group search you can access MRs and code set as "not public" in a project

### Steps to reproduce

Create a public group, create a public project inside the group, but with private code.
Push some code, search in the **group search** the code while logged out, you will find it also if it should be private.

I provide some working links in the example section.

### Impact

An attacker can extract all the private code, private MRs, private commits from a project

### Examples

I am going to use customers.gitlab.com examples because it is how I actually found the problem - the search I have done are about a Hackerone report I first published. I haven't saved any data, nor screenshot of what I have found, apart from the one attached

1. Go to https://gitlab.com/gitlab-org in a private window
2. In the top right bar, insert `Resolve "Account takeover due to IDOR on customers.gitlab.com [applicable for gitlab users only]"`
3. Select "Merge requests"
4. You see in the search result a MR that should be private, since the `customer-gitlab-com` project has no public code/MR
5. Link: https://gitlab.com/search?group_id=9970&project_id=&repository_ref=&scope=merge_requests&search=Resolve+%22Account+takeover+due+to+IDOR+on+customers.gitlab.com+%5Bapplicable+for+gitlab+users+only%5D%22

You can do the same thing for the code:
1. Go to https://gitlab.com/gitlab-org in a private window
2. In the top right bar, insert `In order to create an account for the [admin panel]`
3. Select "Code"
4. You see a piece of the README of customers.gitlab.com, which has a private code
5. Link:  https://gitlab.com/search?group_id=9970&repository_ref=&scope=blobs&search=In+order+to+create+an+account+for+the+%5Badmin+panel%5D&snippets=#

In the case of MRs, you can use also the wildcard symbol and filter by project, to extract all the private MRs:

https://gitlab.com/search?utf8=%E2%9C%93&snippets=&scope=merge_requests&repository_ref=&search=*&group_id=9970&project_id=2670515

When you filter by project, the code search stops to work, so if you want to extract all the code you have to apply custom search, but it is still feasible.

You got the point, we have also commits:
- https://gitlab.com/search?utf8=%E2%9C%93&snippets=&scope=commits&repository_ref=&search=Merge+branch+%27433-idor-fix%27+into+%27staging%27&group_id=9970

Issues are not affected by this bug

### What is the current *bug* behavior?

Leak of MRs overview, code, commits, and I suspect also wiki, but for some reason group search of wiki didn't work on my personal group, and I didn't want to look over other gitlab-org data

### What is the expected *correct* behavior?

No search result

### Relevant logs and/or screenshots

A MR of customers.gitlab.com I shouldn't have access to. Notice how I am not logged in in this screenshot

### Output of checks

This bug happens on GitLab.com

## Impact

An attacker can extract all the private code, private MRs, private commits from a project

## Attachments
- Screenshot_2019-09-11_Resolve_Account_takeover_due_to_IDOR_on_customers_gitlab_com__applicable_for_gitlab_users_only____Sea_..._.png
