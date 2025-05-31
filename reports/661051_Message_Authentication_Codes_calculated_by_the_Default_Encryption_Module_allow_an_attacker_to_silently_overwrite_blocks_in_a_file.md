# Message Authentication Codes calculated by the Default Encryption Module allow an attacker to silently overwrite blocks in a file

## Report Details
- **Report ID**: 661051
- **URL**: https://hackerone.com/reports/661051
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-26T11:03:14.045Z
- **Disclosed**: 2020-11-05T07:59:48.349Z

## Reporter
- **Username**: yahe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**First:** The default encryption module bundled with the Nextcloud Server creates SHA256-HMAC based message authentication codes for each individual 6072 byte-sized block of data. These are the steps to calculate the MAC:

* Take the user password and harden it with SHA256-PBKDF2 (denoted as `$passPhrase` in \[1\]).
* Concatenate `$passPhrase`, `$version` (which is the value `encrypted` from the `oc_filecache` table), `$position` (which is the zero-based index of the encrypted block within the file) and `"a"` and create a SHA512 hash of it (denoted as `$passPhrase` in \[2\]).
* Most MACs of file blocks are created under the salt `hash('sha512', $passPhrase.$version.$position."a", true)` with the exception of the last file block which uses the salt `hash('sha512', $passPhrase.$version.$position."end"."a", true)`,
* Finally create a SHA256-HMAC of the data under the salt `$passPhrase` (as seen in \[3\]).

**Second:** An encrypted file uses the same file key (stored in the corresponding `fileKey` file) and envelope keys (stored in the corresponding `shareKey` files) as its stored file versions.

**Third:** To prevent a file from being  truncated the last block uses a different salt (containing `"end"`). To prevent file blocks from being moved within a file each message authentication key contains the `$position` of the block within the file. To prevent file blocks from being moved between different versions of the same file each message authentication key contains the `$version` of the file.

**Fourth:** However, the concatenation that is used to create message authentication key is ambiguous. It is e.g. not possible to differentiate between the block with `$position` 10 in `$version` 1 of a file (being `$passPhrase."1"."10"."a"`) and the block with `$position` 0 in `$version` 11 of a file (being `$passPhrase."11"."0"."a"`). This way the contents of a properly encrypted and signed file can be modified without breaking the signature check.

**Fifth:** The following steps describe a simple proof of concept:

Create a file consisting of 6072 * 10 "A" + 6072 "B" + 1 "1":

```
php -r 'print(str_repeat("A", 6072*10).str_repeat("B", 6072)."1");' >./collision.txt
```

Upload the file to Nextcloud and visit the folder in which Nextcloud stored the encrypted and signed version of the file `./collision.txt`. Create a backup of the encrypted version 1:

```
cp ./collision.txt ./collision.txt.1
```

Open the file in Nextcloud text editor and create 11 versions. The easiest way to do this is to scroll to the end of the file, add a character, press CTRL+S twice to make sure that the version has been created and proceed until the file has reached version 11. This can be checked in the database by issuing the following query:

```
select encrypted from oc_filecache where path = 'files/collision.txt';
```

Download the file to have a sample of the currently valid version of the file. Then overwrite the file block with `$position` 0 of `./collision.txt` with the file block with `$position` 11 of `./collision.txt.1`.

```
dd if=./collision.txt.1 of=./collision.txt bs=8192 conv=notrunc skip=11 seek=1 count=1
```

Download the file again. When comparing the first download of the file with the second download of the file you should see that the first block of the file has been modified without breaking the signature check.

1) [apps/encryption/lib/Crypto/Crypt.php#L194](https://github.com/nextcloud/server/blob/a374d8837d6de459500e619cf608e0721ea14574/apps/encryption/lib/Crypto/Crypt.php#L194)
2) [apps/encryption/lib/Crypto/Crypt.php#L505](https://github.com/nextcloud/server/blob/a374d8837d6de459500e619cf608e0721ea14574/apps/encryption/lib/Crypto/Crypt.php#L505)
3) [apps/encryption/lib/Crypto/Crypt.php#L506](https://github.com/nextcloud/server/blob/a374d8837d6de459500e619cf608e0721ea14574/apps/encryption/lib/Crypto/Crypt.php#L506)

## Impact

An attacker that has permanent access to the file storage like an administrator or external storage provider can learn how many versions of which files exist without needing access to the database by monitoring the created version files over time.

Such an attacker is able to modify the contents of files by overwriting certain file blocks with specific file blocks from earlier versions of the same files. This file modification is possible **without** having access to any encryption secrets like passwords or keys.

This attack works against master-key encrypted files as well as against user-key encrypted files.

## Attachments
- nextcloud_poc.mp4
