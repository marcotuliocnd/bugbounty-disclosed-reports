# Code Injection in Slack's Windows Desktop Client leads to Privilege Escalation

## Report Details
- **Report ID**: 162955
- **URL**: https://hackerone.com/reports/162955
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-24T08:27:34.777Z
- **Disclosed**: 2017-07-14T19:01:03.937Z

## Reporter
- **Username**: fbogner
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi,

This report is about a Code Injection vulnerability in Slack's Windows Desktop Client (slack.exe) that allows any local user to inject code into other user's Slack client.

It has been verified on a fully patched english Windows 7 64bit running the latest available Slack Desktop Client (2.1.1 32-Bit Direct Download). 

The issue is that slack.exe tries to load its OpenSSL configuration from the non-existing file
C:\usr\local\ssl\openssl.cnf (See Procmon screenshot). As any authenticated Windows user is allowed to
create new folders at the system drive's root, the expected folder structure can be created by anyone. 

This enables any local user to create the expected OpenSSL config file. Using this config file it is then possible to instruct OpenSSL to load additional libraries. This finally leads to arbitrary code execution in other user's slack.exe process. This is especially a problem as Slack is automatically started after logging in.

Here's a video illustrating the attack: https://owncloud.bogner.sh/s/MRXZSp0YyfK9ycf
Additionally you can download the source code and the binary version of the used payloads here: https://owncloud.bogner.sh/s/z7kbZr9STr08R73

To fix this vulnerability the OpenSSL config file should only be loaded from secure locations (like somewhere from within the application's root folder)

If you have any questions just let me know.
Florian

## Attachments
- Screen_Shot_2016-08-24_at_09.48.52.png
