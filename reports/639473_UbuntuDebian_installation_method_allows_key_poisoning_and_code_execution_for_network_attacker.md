# Ubuntu/Debian installation method allows key poisoning and code execution for network attacker

## Report Details
- **Report ID**: 639473
- **URL**: https://hackerone.com/reports/639473
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-10T14:22:15.304Z
- **Disclosed**: 2020-01-21T14:18:00.363Z

## Reporter
- **Username**: hanno
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mariadb

## Vulnerability Information
The MariaDB installation instructions for apt-based distributions (Debian/Ubuntu) look like this:
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
sudo add-apt-repository 'deb [arch=amd64] http://mirror.wtnet.de/mariadb/repo/10.4/ubuntu disco main'

The apt-key command is problematic and vulnerable to two different kinds of attacks.

Attack 1: Key poisoning
==================

keyserver.ubuntu.com is part of the SKS keyserver network and gets synced with other keyservers.

Recently there have been attacks "poisoning" PGP keys on the keyservers. The principle is actually extremely simple: The keyservers operate on an "append only" principle, and everyone can add new signatures to an existing key. So one can make a key practically unusable by adding lots of signatures.

More background:
https://dkg.fifthhorseman.net/blog/openpgp-certificate-flooding.html
https://gist.github.com/rjhansen/67ab921ffb4084c865b3618d6955275f

An "expoit" has also been published, but this is more or less trivial:
https://gist.github.com/yegortimoshenko/8d57c7892d4bcd50d11e69f71b1f80bf

An attacker can poison the release key . This will likely either lead to the key becoming unimportable or gpg becoming unusable or extremely slow.

Attack 2: Key ID collission
====================

The above command fetches the key via its 64 bit key id over an unauthenticated connection.
The shortened 64 bit key ids aren't safe from collisions, an attacker can create a different key with the same 64 bit key id (though this requires a large amount of computing power, but it's feasible). Only the full 160 bit key ids are safe.

Therefore a network/mitm attacker can serve a user a bad key with the same key id and then a signed repository with rogue packages.


Solution
======

To avoid both scenarios I recommend fetching the key from a secure (HTTPS) place under your control. This is also what Debian recommends:
https://wiki.debian.org/DebianRepository/UseThirdParty

## Impact

Make installation instructions unusable due to poisoned key or execute malicious code as a network attacker during installation.

## Attachments
No attachments
