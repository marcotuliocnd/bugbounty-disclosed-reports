# A HackerOne employee's GitHub personal access token exposed in Travis CI build logs

## Report Details
- **Report ID**: 215625
- **URL**: https://hackerone.com/reports/215625
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-23T16:47:49.041Z
- **Disclosed**: 2017-05-23T07:15:00.708Z

## Reporter
- **Username**: sainaen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary**
A HackerOne employee Reed Loden ([GitHub:reedloden](https://github.com/reedloden)) exposed their personal access token twice in build logs of the [rubysec/rubysec.github.io](https://github.com/rubysec/rubysec.github.io) project:
1. [2015-12-10](https://travis-ci.org/rubysec/rubysec.github.io/jobs/95954424#L258)
2. [2016-03-01](https://travis-ci.org/rubysec/rubysec.github.io/jobs/112766749#L319)

**Description**
The token has `public_repo` [scope](https://developer.github.com/v3/oauth/#scopes), which means that it allows access to any *public* repos the owner account has access to, with the same permissions. This includes all public repositories under [Hacker0x01](https://github.com/Hacker0x01), for which Reed has full access: pull, push, as well as admin permissions.

**Cause**
The cause of this as far as I can tell is incorrect  use of `git push` command in [the script](https://github.com/rubysec/ruby-advisory-db/blob/master/scripts/post-advisories.sh#L18):  passing a`-q`/`--quiet` option is not enough, as according to help it *“Suppresses all output <…> unless an error occurs”*, which happened in those two cases, in turn because of missing `--force` option.

**Other**
In addition to revoking the token, you might want to review *any* commits to your repositories since the first exposure. The token allows to push from the Reeds account, but commit's author/committer can be set to anything. As far as I know, there's no UI on GitHUb to see what commits were *pushed* from the particular account.

Also, please, make sure not to disclose this issue publicly (including by accident, with a commit message, for example) at least for some time. Revoking/rotating token with a generic “updating the token” commit should be fine though, as generally nobody pays attention to them.

Note, that I've contacted GitHub to perform mass revocation of credentials that I found, but they aren't as fast as I hoped, so meanwhile I'm trying to notify affected parties individually.

## Attachments
No attachments
