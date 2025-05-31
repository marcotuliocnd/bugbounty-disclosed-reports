#  Cargo not respecting umask when extracting crate archives

## Report Details
- **Report ID**: 2094785
- **URL**: https://hackerone.com/reports/2094785
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-08-03T15:30:18.564Z
- **Disclosed**: 2023-08-15T18:15:38.372Z

## Reporter
- **Username**: addisoncrump
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Cargo did not properly protect files in the cargo registry. When an archive contained files which were marked as globally writeable, they would be unpacked as-is and retain their global writeability. This is CWE-278 (not available in HackerOne).

This was discovered as part of a (personal) routine file permissions check:

```sh
find / ! -type l -perm -002 -exec ls -alhd {} \;
```

## Impact

A local attacker may inject arbitrary code into the cached files present in the cargo registry. This, in turn, allows for a local attacker to act as the targeted user (when the user compiles the modified code) or to poison prebuilt binaries built by that user and thus have arbitrary code execution against downstream users (supply chain attack).

## Attachments
No attachments
