# Installing a crafted gem package may create or overwrite files

## Report Details
- **Report ID**: 243156
- **URL**: https://hackerone.com/reports/243156
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-26T09:14:48.920Z
- **Disclosed**: 2017-08-31T23:18:39.368Z

## Reporter
- **Username**: mame
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rubygems

## Vulnerability Information
There is no check for `name` field in `metadata.gz`.  By assigning a maliciously crafted string like `../../../../../any/where` to the field, an attacker can create an arbitrary file out of the directory of the gem, or even replace an existing file with a malicious file.

## Proof of Concept 1: Create a file anywhere

This PoC attempts to create a file `/tmp/malicious-0/BOOOOM`.

1) Download the attached file `malicious.gem`.
2) Run `gem install malicious.gem --no-doc`.
3) `/tmp/malicious-0/BOOOOM` should be created.

`malicious.gem` assigns `../../../../../../../../../../tmp/malicious` as `name` field.  This attack is relatively weak since the path must include a directory named `<name>-<version>`, such as `malicious-0`.  Still, there are many chances that cause a catastrophe.  For example, think of replacing a file in `/etc/dbus-1/`.

## Proof of Concept 2: Replace `rackup` command

This PoC attempts to replace `gems/rack-2.0.3/bin/rackup` with a malicious file.

1) Download the attached file `replace-rackup.gem`.
2) Run `gem install rack -v 2.0.3`.
3) Run `gem install replace-rackup.gem --no-doc`.
4) Run `rackup`.  It will emit just `BOOOOM!`.

`replace-rackup.gem` assigns `../gems/rack` as `name` field, and contains a malicious file `bin/rackup`.  This is really exploitable for attackers.

## Note

For how to create the malicious gems, see the attached file `src.tar.gz`.

In my opinion, **this attack is much more dangerous** than the issues I reported recently.  I hope you could fix this issue ASAP.

## Attachments
- src.tar.gz
- create-file.gem
- replace-rackup.gem
