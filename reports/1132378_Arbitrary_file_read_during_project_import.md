# Arbitrary file read during project import

## Report Details
- **Report ID**: 1132378
- **URL**: https://hackerone.com/reports/1132378
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-22T15:23:30.056Z
- **Disclosed**: 2021-05-24T08:51:03.967Z

## Reporter
- **Username**: saltyyolk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary
A mis-usage of json schema validator could be used by an attacker to read any file in GitLab server. The issue allows the attacker to leak ~250 bytes of data of any file.
At the same time, as the root cause of the issue here is 'open-uri'. It's an SSRF issue at the same time.

### Steps to reproduce
1. Use the import feature of gitlab.com to import the attached import.tar.gz as 'GitLab export' ███████
2. Wait the import process to finish
3. Access URL: https://gitlab.com/api/v4/projects/PROJECT_ID/import where PROJECT_ID is the id of the imported project, which could be found in the home page of the project.
4. The connection information of gitlab's production database is in the output, as attached.

### Impact
For GitLab.com, this issue could be used to leak some critical credentials. I went through the charts in `https://gitlab.com/gitlab-org/charts/gitlab/-/tree/master/charts/gitlab/charts/sidekiq/templates`. It seems that there're a bunch of  juicy credentials could be leaked with this method, including Rails secret_key_base, database credentials and GitLab's smtp credentials. The object storage service account credential is limitedly accessed because of the 250 bytes limitation.

For self-hosted GitLab instances, this issue could cause more severe problems since most of self-hosted GitLab instances has sidekiq running with gitlab-rails & gitlab-shell. So .gitlab_shell_token could be easily downloaded and be used to access internal APIs such as '/api/v4/internal/personal_access_token', which could issue an private access token of an admin of someone else.

### Relevant logs and/or screenshots
███
███████

### Output of checks
This bug happens on GitLab.com

## Impact

For GitLab.com, this issue could be used to leak some critical credentials. I went through the charts in `https://gitlab.com/gitlab-org/charts/gitlab/-/tree/master/charts/gitlab/charts/sidekiq/templates`. It seems that there're a bunch of  juicy credentials could be leaked with this method, including Rails secret_key_base, database credentials and GitLab's smtp credentials. The object storage service account credential is limitedly accessed because of the 250 bytes limitation.

For self-hosted GitLab instances, this issue could cause more severe problems since most of self-hosted GitLab instances has sidekiq running with gitlab-rails & gitlab-shell. So .gitlab_shell_token could be easily downloaded and be used to access internal APIs such as '/api/v4/internal/personal_access_token', which could issue an private access token of an admin of someone else.

## Attachments
No attachments
