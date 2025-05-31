# Path traversal in command line client

## Report Details
- **Report ID**: 637840
- **URL**: https://hackerone.com/reports/637840
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-08T19:17:44.126Z
- **Disclosed**: 2020-05-28T18:59:16.286Z

## Reporter
- **Username**: lixtelnis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mariadb

## Vulnerability Information
The command line client has a directory traversal bug which allows server chosen files to be dlopened when it connects to a malicious server.

The path can also be padded with `/` characters so that `strxnmov` drops the `.so` extension.

The `dlopen` call is performed here: <https://github.com/MariaDB/server/blob/10.5/sql-common/client_plugin.c#L368>

## Impact

In rare situations where the attacker controls a file at a known location on the victim's machine this can lead to code execution using `init/fini` functions. See attached `dlopen.sh`.

Other side effects present in commonly installed software are not to be neglected. The mecanism is far from being uncommon in C files alone according to this search:

<https://codesearch.debian.net/search?q=__attribute__.*constructor+filetype%3Ac&perpkg=1>

Without abusing the path traversal bug the dialog plugin might also be used to fool a user into sending its password unhashed. See attached `dialog.sh`.

## Attachments
- disc.zip
