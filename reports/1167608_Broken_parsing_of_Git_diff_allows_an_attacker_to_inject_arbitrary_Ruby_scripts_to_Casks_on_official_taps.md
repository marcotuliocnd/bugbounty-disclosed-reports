# Broken parsing of Git diff allows an attacker to inject arbitrary Ruby scripts to Casks on official taps

## Report Details
- **Report ID**: 1167608
- **URL**: https://hackerone.com/reports/1167608
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-18T08:08:14.730Z
- **Disclosed**: 2021-04-21T11:24:49.165Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
## Description
Due to improper parsing of Git diff in [Homebrew/actions/review-cask-pr](https://github.com/Homebrew/actions/tree/336bd2aae5314f8c17c66a8319adeba99f13c093/review-cask-pr), it's possible to confuse parser to ignore additional lines.
Which leads injection of malicious Ruby scripts.

## Root cause
`review-cask-pr` uses the git diff file to check if the pull request is "simple" enough to automatically merge it.
To parse the git diff file, it uses [`git_diff`](https://github.com/anolson/git_diff/) gem with some modifications.
https://github.com/Homebrew/actions/blob/master/review-cask-pr/git_diff_extension.rb
Since `git_diff` has a small bug that allows a crafted diff file to confuse additions as a `a_path`, it's possible to confuse `review-cask-pr`.
https://github.com/anolson/git_diff/blob/21913c2a51661449a7250cc3a5ba5f5f4f128959/lib/git_diff/file.rb#L61-L62

## Steps to reproduce
1. Fork [Homebrew/homebrew-cask](https://github.com/Homebrew/homebrew-cask).
2. Modify a cask file to add following lines:
```ruby
++ "b/#{puts 'Going to report it - RyotaK (https://hackeorne.com/ryotak)';b = 1;Casks = 1;iterm2 = {};iterm2.define_singleton_method(:rb) do 1 end}"
++ b/Casks/iterm2.rb
```
3. Open a pull request on [Homebrew/homebrew-cask](https://github.com/Homebrew/homebrew-cask).
4. BrewTestBot will approve these changes.

https://github.com/Homebrew/homebrew-cask/pull/104191

## Impact

Injected script will be evaluated once someone installed the cask, which may allows remote code execution.

## Attachments
No attachments
