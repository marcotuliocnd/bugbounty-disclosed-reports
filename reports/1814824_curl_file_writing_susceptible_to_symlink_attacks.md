# curl file writing susceptible to symlink attacks

## Report Details
- **Report ID**: 1814824
- **URL**: https://hackerone.com/reports/1814824
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-12-22T09:28:45.195Z
- **Disclosed**: 2023-01-07T22:18:56.986Z

## Reporter
- **Username**: nyymi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
If curl command is used to download a file with predictable file name to a world writable directory (such as `/tmp`), a local attacker is able to mount a symlink attack to either A) redirect the target file writing to another file writable by the user or B) replace the downloaded file contents with arbitrary other data. libcurl `file://` upload is similarly affected.

However, this really isn't a vulnerability in curl or libcurl itself, but use of curl or libcurl.

## Steps To Reproduce:

### Scenario A example:
- attacker does:
  `ln -s /home/victim/.bashrc /tmp/target.sh`
- victim does:
  `curl  --output-dir /tmp -O https://example.com/target.sh` or
  `curl -o /tmp/target.sh https://example.com/whatever` or similar

=> Instead of downloading the file to `/tmp/target.sh` it will be written to `/home/victim/.bashrc`. This attack works the best when the attacker can control which file is downloaded (granted, this is often not possible).

### Scenario B example:
- attacker does:
 `install -m 606 /dev/null /tmp/target.sh`
- attacker waits for the file to be closed (inotify), and  immediately replaces the file contents with malicious content once closed
- victim does:
  `curl  --output-dir /tmp -O https://example.com/target.sh` or
  `curl -o /tmp/target.sh https://example.com/whatever` or similar

=> The victim downloaded content is replaced by malicious content before it's used (copied, executed etc) by the victim.

## Remediation

- Documentation should be amended to warn users against this threat. If temporary files are used, they should be put to secure temporary directory (created by `mktemp -d` or similar).
- While not a vulnerability in curl/libcurl a mode that uses `O_NOFOLLOW` when opening output files could be added. Similarly in this secure mode `--create-dirs` would need to be amended to refuse to create entry in any location owned by another user (but making this check bulletproof is tricky),  This mode could not be the default behaviour, since it would likely break too many things.

## Vulnerability discussion

The obvious argument against this being a vulnerability in curl/libcurl is that the user is responsible for the permissions of the directory they download to.  That is: the insecure use of curl/libcurl is actually where the vulnerability lies.

Interwebs has quite many examples of vulnerable use or examples, including: https://daniel.haxx.se/blog/2020/09/10/store-the-curl-output-over-there/

## Impact

A) Overwriting files owned by the user downloading the files.
B) Replacing downloaded data with malicious content

## Attachments
No attachments
