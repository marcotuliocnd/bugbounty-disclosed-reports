# Improper confidentiality protection of server-side encryption keys

## Report Details
- **Report ID**: 743505
- **URL**: https://hackerone.com/reports/743505
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-21T16:27:21.803Z
- **Disclosed**: 2020-11-13T14:40:12.778Z

## Reporter
- **Username**: yahe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
This vulnerability is related to the [Improper integrity protection of server-side encryption keys](https://hackerone.com/bugs?subject=user&report_id=732431) vulnerability but leverages a different attack vector. While the previous attack broke the confidentiality of encrypted files because the public keys are not integrity-protected, this new attack breaks the integrity of encrypted files because the confidentiality of the public keys is not properly protected. As before, this attack also works with per-user key encryption.

**Optional** prerequisite: If you want to generate authenticated files that are AES-256-CTR encrypted, you have to know how many versions of a file there have been. Oftentimes it will just be `1` or you can denote the number of previous versions thanks to the default versioning plugin that stores old versions on disk as well. An external storage provider will have the possibility to know the version of a certain file by counting the write accesses to encrypted files. **But** you can also just use the previously supported AES-256-CFB encryption which allows you to just skip the "signing" of the file. 

How to do this:
* Generate a fresh file key (e.g. with `openssl rand -hex 32`)
* Generate a fresh envelope key (e.g. with `openssl rand -hex 16`)
* Encrypt the file key with the envelope key (e.g. with `encrypt-filekey.php` [1]) and replace the original `fileKey` file of the file you want to attack with the newly generated file
* Encrypt the envelope key with all public keys (they're stored as plain PEM-encoded keys on disk) that have currently access to the file (e.g. with `encrypt-envelopekey.php` [2]) and replace the corresponding `<username>.shareKey` files with the newly generated files
* Take the file that you want to modify and calculate its unencrypted file size (e.g. with `calculate-filesize.php` [3])
* Prepare a file with the same size and encrypt it for the newly generated file key (e.g. with `encrypt-file.php` [4]). If you use the AES-256-CTR encryption, then you have to know the version number of the file  or you can just use the AES-256-CFB encryption which doesn't require you to know the version number of the file (see **optional** prerequisite).

The Nextcloud server-side encryption currently is not able to distinguish between a file that has been encrypted by the server itself and a file that has been encrypted by a malicious attacker who has access to the Nextcloud data directory. This also holds true for setups where the administrator moved the whole data directory to a remote storage provider (through davfs2, s3fs, sshfs or similar) as this provider will then also be able to access the required key material.

[1] https://github.com/syseleven/nextcloud-tools/blob/master/encrypt-filekey.php
[2] https://github.com/syseleven/nextcloud-tools/blob/master/encrypt-envelopekey.php
[3] https://github.com/syseleven/nextcloud-tools/blob/master/calculate-filesize.php
[4] https://github.com/syseleven/nextcloud-tools/blob/master/encrypt-file.php

## Impact

An attacker who has access to the encrypted files and the public keys of the users is able to replace encrypted files with properly encrypted (and **optionally** properly authenticated/"signed") files as long as the length of the new file contents matches the length of the old file contents.

## Attachments
- nextcloud_poc5.mp4
