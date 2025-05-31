# Permission model improperly processes UNC paths

## Report Details
- **Report ID**: 2079103
- **URL**: https://hackerone.com/reports/2079103
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-21T16:34:43.134Z
- **Disclosed**: 2024-07-15T09:12:44.019Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
The `is_tree_granted` function in `fs_permission.cc` assumes that any path starting with two backslashes `\\` has a four-character prefix that can be ignored, which is not always true. This subtle bug leads to vulnerable edge cases.

## Steps To Reproduce:

With a recent version of Node.js 20, run a command such as:

```
node --experimental-permission --allow-fs-read=C:\* -p "fs.readdirSync(Buffer.from('\\\\A\\C:\\Users'))"
```

The expected behavior is an `ERR_ACCESS_DENIED` error, but it does not occur. Instead, Node.js calls `scandir` on `\\A\C:\Users`.

## Supporting Material/References:

* [Implementation of `is_tree_granted`](https://github.com/nodejs/node/blob/b68fa599607f69f2ce3b1a3104e0d5984f6bc0d8/src/permission/fs_permission.cc#L53-L68)
* [File path formats on Windows systems: UNC paths](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths)

## Impact

An attacker can potentially gain unintended access to UNC resources. In the above example, an attacker gains file system access to the UNC path `\\A\C:\`, even though no access beyond the local `C:\` drive has been granted.

It is difficult to fully and accurately comprehend the impact. The bug is subtle, and Windows uses notoriously complex file path formats. Overall, I consider the severity of the issue to be low.

## Attachments
No attachments
