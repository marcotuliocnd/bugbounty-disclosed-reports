# Disclosure of github access token in config file via nignx off-by-slash

## Report Details
- **Report ID**: 1386547
- **URL**: https://hackerone.com/reports/1386547
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-10-30T15:35:05.260Z
- **Disclosed**: 2022-01-13T18:16:19.419Z

## Reporter
- **Username**: letm3through
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: adobe

## Vulnerability Information
## Summary:
`██████████` is vulnerable to Nginx off-by-slash vulnerability that exposes Git configuration.

## Steps To Reproduce:
1. Visit `https://█████████████` to download git config containing username and token.
2. Use it to pull entire source code via `git clone ████████`

Leaked:
```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = ████
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[branch "vespa-2021-Q4"]
	remote = origin
	merge = refs/heads/vespa-2021-Q4
```

## Impact

Malicious attacker can mess around using the leaked github token to access and modify or even try to delete github repos that the token has permission to.

## Attachments
No attachments
