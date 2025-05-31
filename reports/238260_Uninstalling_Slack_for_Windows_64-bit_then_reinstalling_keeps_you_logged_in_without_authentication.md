# Uninstalling Slack for Windows (64-bit), then reinstalling keeps you logged in without authentication

## Report Details
- **Report ID**: 238260
- **URL**: https://hackerone.com/reports/238260
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-08T21:04:47.641Z
- **Disclosed**: 2020-11-10T20:11:55.675Z

## Reporter
- **Username**: pclinger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
I understand that you are unlikely to consider bugs that require physical machine access, however this issue affected me directly and I was very surprised by it, so I felt it was important to report it in case it was not known.

Steps to reproduce:

1) Install the desktop Slack app for Windows (64-bit).
2) Login to Slack
3) Uninstall Slack
4) Reinstall Slack

Result: You will automatically be logged back in to your account, even though you uninstalled Slack from your computer and did not enter a username/password to login to the fresh Slack installation.

The Slack uninstall process is fully automatic, there is no prompt or indication that there is data left behind. I believe it is reasonable to expect that when uninstalling Slack my session data should have been removed. If I am a user on a shared user account (for example, if I borrowed a computer and I installed Slack, but uninstalled it later), they can take full control of my account after the fact.

When testing this, I could access all of my messages and data, and even access the Slack admin panel for my team that I am an administrator of.

## Attachments
- 1-uninstall.png
- 2-download-slack.png
- 3-slack-installed.png
- 4-logged-in-without-password.png
