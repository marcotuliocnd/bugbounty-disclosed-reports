# GIT Detected

## Report Details
- **Report ID**: 221298
- **URL**: https://hackerone.com/reports/221298
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-15T21:22:26.114Z
- **Disclosed**: 2017-04-20T09:58:38.332Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello team,
While i was testing nextcloud.com, I've detected GIT repository files. GIT repository files can disclose GIT repository usernames and file lists. While disclosures of this type do not provide direct attack vectors, they can be useful for an attacker when combined with other vulnerabilities discovered within the application. 

URL:  https://nextcloud.com/wp-content/themes/next/.git/config

Page is showing:
[core] repositoryformatversion = 0 filemode = true bare = false logallrefupdates = true [remote "origin"] url = https://github.com/nextcloud/nextcloud.com.git fetch = +refs/heads/*:refs/remotes/origin/* [branch "master"] remote = origin merge = refs/heads/master [branch "pricing"] remote = origin merge = refs/heads/pricing [branch "orderform"] remote = origin merge = refs/heads/orderform 

## Attachments
No attachments
