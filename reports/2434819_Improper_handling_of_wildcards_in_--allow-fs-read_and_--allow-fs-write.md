# Improper handling of wildcards in --allow-fs-read and --allow-fs-write

## Report Details
- **Report ID**: 2434819
- **URL**: https://hackerone.com/reports/2434819
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-03-26T14:53:39.108Z
- **Disclosed**: 2024-05-29T14:27:11.947Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
**Summary:** The permission model implementation does not process wildcards in the paths given via `--allow-fs-read` or `--allow-fs-write` correctly and may incorrectly grant access to paths that should be inaccessible.

**Description:** There are two separate issues here:

1. The implementation silently ignores any text after a wildcard character (`*`), which appears to be undocumented and thus at the very least falls under CWE-657:

    ```
    $ node --experimental-permission \
           --allow-fs-read=/home/tniessen/.ssh/*.pub \
           -p "fs.readFileSync('/home/tniessen/.ssh/id_github').length"
    464
    ```

    The user clearly did not intend to grant access to private SSH key files but only to public key files (`.pub`). The permission model silently discards this intended restriction. (Not supporting such wildcard patterns is fine, but silently discarding the extra text is not.)

2. When the wildcard character is at the end of some path, the permission model also grants access to another path, which appears to always be the original path with the wildcard and the last character removed:

    ```
   $ node --experimental-permission \
           --allow-fs-read=/etc/passwd.* \
           -p 'fs.readFileSync("/etc/passwd")'
   <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 6e 6f 62 6f 64 79 3a 78 3a 36 35 35 33 34 3a 36 35 35 33 34 3a 4e ... 2103 more bytes>
    ```

   Note that `/etc/passwd` does not match the pattern `/etc/passwd.*`.

## Impact

These issues have limited security impact in Node.js 20 and Node.js 21. The first issue may lead users to unintentionally grant access to certain parts of the file system. The second issue only appears to grant access to a single resource with a predetermined name, which is likely unhelpful for attackers in practice.

## Attachments
No attachments
