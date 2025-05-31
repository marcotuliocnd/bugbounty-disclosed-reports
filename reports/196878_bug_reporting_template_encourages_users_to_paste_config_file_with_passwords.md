# bug reporting template encourages users to paste config file with passwords

## Report Details
- **Report ID**: 196878
- **URL**: https://hackerone.com/reports/196878
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-09T12:40:38.155Z
- **Disclosed**: 2017-04-19T08:10:18.555Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The dangerous bug reporting template
=============================

The github bug reporting template for nextcloud's server and some apps contains this:

**The content of config/config.php:**

```
If you have access to your command line run e.g.:
sudo -u www-data php occ config:list system
from within your instance's installation folder

or 

Insert your config.php content here
(Without the database password, passwordsalt and secret)
```

This is obviously very problematic. From the wording and instructions it is very likely that users will do the wrong thing: Paste the config.php without removing all passwords, for various reasons:
* It's likely to assume that many users won't read the detailed instructions and will just do the first thing they're told: Insert the content of config/config.php.
* The instruction with sudo and www-data is specific to certain server configurations and may not work everywhere, thus it will fail for some users who will try the next option, namely inserting config.php directly.
* The instruction "Without the database password, passwordsalt and secret" is incomplete. There can be more sensitive fields in the config file, e.g. "mail_smtppassword".

Not surprisingly users misread these instructions and paste sensitive passwords. See e.g.:
https://github.com/nextcloud/calendar/issues/151
https://github.com/nextcloud/calendar/issues/155

Proposed remediation
=================

I think it's necessary that you search all existing bug reports that have been created with this template for sensitive passwords and remove them. It is probably also appropriate to inform the affected users.

I also believe encouraging users to paste a config file with passwords is inherently dangerous and no amount of warnings will prevent all users from making mistakes. In general I think it should always be a guiding principle of software design to make it hard for users to make security mistakes.

There are various ways the situation could be improved, this is what I could think of:
* Provide a way in the webinterface to let users view a version of the config file where all sensitive values are removed (like the command line instruction, but more accessible).
* Change the instruction and avoid all references to pasting the raw config file content. If there's a need to get the config file in rare circumstances a developer could ask a bug reporter for it, ideally via private channels and only post a manually vetted version to the bug report.

Leakage of instanceid
=================

One additional observation: The "occ config:list" command removes dbpassword, secret and mail_smtppassword, but it leaves instanceid intact. I'm not familiar enough to judge how sensitive this value is, but it seems to be an unique identifier for each owncloud installation. It would probably be wise to remove that, too.

Affects owncloud and nextcloud
========================

This issue affects the development of both owncloud and nextcloud in the same way. Thus I will report it to both projects.

## Attachments
No attachments
