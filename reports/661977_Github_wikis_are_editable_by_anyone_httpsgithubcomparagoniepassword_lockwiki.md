# Github wikis are editable by anyone https://github.com/paragonie/password_lock/wiki

## Report Details
- **Report ID**: 661977
- **URL**: https://hackerone.com/reports/661977
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-27T19:14:43.261Z
- **Disclosed**: 2019-07-29T07:15:09.928Z

## Reporter
- **Username**: nitish_mathur
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
submitted a misconfiguration in some of our GitHub repositories to us. Wikis are inherently editable for all users, but for some repositories an organization may want to restrict this access. In some cases it was possible for GitHub users .
Github wikis on the following project
https://github.com/paragonie/password_lock
can be edited by any logged in user in the system. This poses security and reputation risk for the company.
Steps To Reproduce:
1. Go to https://github.com/paragonie/password_lock/wiki and follow the wiki.
2. I can created a simple page in the wiki without be a collaborator of the repo, or and without any permission
3. Going on https://github.com/paragonie/password_lock/wiki you can add a new fake or phishing page clicking on the New page or edit buttons.

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.

attachment / reference
https://hackerone.com/reports/457032
https://hackerone.com/reports/459634

## Impact

The user would surely trust the code (of course if he trusts the company itself), so he will extrapolate this trust to the wiki and consider it being safe enough to follow the instructions and downloading himself a malware.
As wikis listed above can be edited by any person on the internet, a malicious actor can accurately craft a message or a note which would lead a user to download a malicious component in a natural way.

## Attachments
No attachments
