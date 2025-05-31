# **minor issue ** -Nextcloud 10.0 session issue with desktop client and android client

## Report Details
- **Report ID**: 165353
- **URL**: https://hackerone.com/reports/165353
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-09-02T18:16:30.152Z
- **Disclosed**: 2020-03-01T15:01:20.331Z

## Reporter
- **Username**: egrep
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Scenario:
***********
--> Installed nextcloud 10.0 locally and created "admin" account
--> Installed nextcloud desktop client and andoid client

I found session related vulnerability in nextcloud 10.0 where killing session in User(admin) --> Personal --> Sessions not actually killing sessions in desktop client

Steps:
1) Logged into admin account in browser
2) Logged into admin account in desktop client and android client. Currently admin account is having 3 sessions : browser, desktop, andoid
3) Goto User(admin) --> Personal --> Sessions --> kill desktop client session --> upload new file using browser --> Still dekstop client is syncing files without asking any password prompt (issue1)
4) Though android client is still  active, sessions are not capturing in personal --> sessions tab

Hope these are minor issues

## Attachments
No attachments
