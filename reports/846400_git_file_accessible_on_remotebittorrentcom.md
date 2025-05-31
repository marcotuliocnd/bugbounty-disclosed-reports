# .git file accessible on remote.bittorrent.com

## Report Details
- **Report ID**: 846400
- **URL**: https://hackerone.com/reports/846400
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-10T12:04:52.839Z
- **Disclosed**: 2020-05-11T23:12:54.468Z

## Reporter
- **Username**: aslanemre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: btfs

## Vulnerability Information
Hi team,
i detected your .git file accessible for any unauthorized user.

url : https://remote.bittorrent.com/static/webui/.git/config

HTTP/1.1 200 OK
Set-Cookie: BTURT=talon-i-0837bbfadd509c546-2; path=/; domain=.utorrent.com
Server: TornadoServer/2.1.1git
Connection: keep-alive
Content-Length: 260
Last-Modified: Wed, 18 Mar 2015 19:18:46 GMT
Accept-Ranges: bytes
Content-Type: text/html; charset=UTF-8
Cache-Control: public
Cache-Control: private

[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:bittorrent/webui.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master

## Impact

change perm for this

## Attachments
No attachments
