# Uninstalling Mattermost Launcher for Windows (64-bit), then reinstalling keeps you logged in without authentication

## Report Details
- **Report ID**: 1797661
- **URL**: https://hackerone.com/reports/1797661
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-12-08T18:07:15.494Z
- **Disclosed**: 2023-01-14T13:00:53.647Z

## Reporter
- **Username**: annonmous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hello Team,

Hope you are doing great and enjoying a lot. 
This issue affected me directly and I was very amazed by it, so I felt it was important to report it in case it was not known. It is resulting unintended behavior:

In addition to this report is very similar to both of already been Resolved hackerone reports
https://hackerone.com/reports/238260
https://hackerone.com/reports/1278261

Steps to reproduce:
1) Install The Mattermost Desktop App for Windows (64-bit).
2) Enter the Display name with Server URL
3) Login to Mattermost Desktop App
4) Uninstall Mattermost Desktop App
5) Reinstall Mattermost Desktop App

Conclusion: You will automatically be logged back in to your account, even though you uninstalled Mattermost Desktop App from your computer and did not enter a username/password to login to the fresh Mattermost Desktop App installation.

Thanks and have a good day ;)
Regards
@annonmous

## Impact

The Mattermost Desktop App uninstall process is fully automatic, there is no prompt or indication that there is data left behind. I believe it is reasonable to expect that when uninstalling Mattermost Desktop App users session data should have been removed. If I am a user on a shared user account (for example, if I borrowed a computer and I installed Mattermost Desktop App, but uninstalled it later), they can take full control of my account after the fact.

When testing this, I could access all of my messages and data, and even access the Mattermost Desktop App admin panel for my team that I am an administrator of.

## Attachments
No attachments
