# GitHub API Key for BrewTestBot is publicly exposed

## Report Details
- **Report ID**: 388740
- **URL**: https://hackerone.com/reports/388740
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-07-31T05:47:18.646Z
- **Disclosed**: 2018-08-11T13:57:57.996Z

## Reporter
- **Username**: ejholmes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
Hello!

While browsing through some old reports, I found that https://jenkins.brew.sh was publicly accessible. I got curious when I saw one of the [brew bottle builds](https://jenkins.brew.sh/job/Homebrew%20Bottles/33255/console) doing a `git push` to BrewTestBot/homebrew-core, and wondered if the credentials to make authenticated pushes were accessible.

Sure enough, you can view environment variables for the build on [this page](https://jenkins.brew.sh/job/Homebrew%20Bottles/33255/injectedEnvVars/), which includes a `HOMEBREW_GITHUB_API_TOKEN` environment variable.

This API token belongs to the [BrewTestBot](https://github.com/BrewTestBot) user on GitHub, and this API key allows me to commit to the `BrewTestBot/homebrew-core` repository:

```
$ export GITHUB_API_TOKEN=<github token from above>
$ curl https://api.github.com/repos/BrewTestBot/homebrew-core/git/blobs -u $GITHUB_API_TOKEN:x-oauth-basic -d '{"content":"test"}' -H "Content-Type: application/json"
{
  "sha": "30d74d258442c7c65512eafab474568dd706c430",
  "url": "https://api.github.com/repos/BrewTestBot/homebrew-core/git/blobs/30d74d258442c7c65512eafab474568dd706c430"
}
```

## Impact

Based on the purpose of `BrewTestBot`, this might be entirely intended, but if the GitHub access token has overly permissive scopes, it might be usable to perform other actions, aside from a `git push`. In that case, an SSH deploy key may be better, and less permissive.

If exposing this API key publicly is intended behavior, please feel free to close this.

## Attachments
No attachments
