# Users can download old project exports due to unclaimed namespace

## Report Details
- **Report ID**: 195058
- **URL**: https://hackerone.com/reports/195058
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-01T15:58:28.420Z
- **Disclosed**: 2017-01-23T23:10:00.394Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
TL;DR: Happy new year and happy birthday, @douwem!

# Vulnerability details
When a user renames its namespace, another user can claim the namespace and download old export files from the victim. The attack scenario here is that someone would scrape existing GitLab namespaces (users and groups, which are public) and see if they're renamed (freeing up the old namespace). The attacker can then claim the namespace the victim's old export files.

# Impact
This may expose confidential project information, including the repository code, merge requests, issues, and snippets.

# Proof of concept
Follow the steps below to reproduce the vulnerability.

**As the victim**
1. Create a group called `test`
2. Create a new private project in the `test` group called `test`
3. Click the `Generate export` button in the project's settings page
4. Now rename the group to `new-test`

**As the attacker**
1. Create a group called `test` (this is possible because the old group was renamed to `new-test`)
2. Create a new private project in the `test` group called `test`
3. Go to http://gitlab-instance/test/test/download_export
4. Profit! The attacker will download the export file generated by the victim 

# Remediation
Expire download links when the namespace OR project URL changes. This vulnerability also applies when changing the project URL, although that is less severe. This might grant users access to private repositories, although far less likely than the PoC outlined in this report.

## Attachments
No attachments
