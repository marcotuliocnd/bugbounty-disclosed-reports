# Permission model improperly protects against path traversal in Node.js 20

## Report Details
- **Report ID**: 2225660
- **URL**: https://hackerone.com/reports/2225660
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-10-25T13:58:08.992Z
- **Disclosed**: 2023-11-30T15:43:45.568Z

## Reporter
- **Username**: tniessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
**Summary:** A previously disclosed vulnerability (CVE-2023-30584) was patched insufficiently in commit [205f1e6](https://github.com/nodejs/node/commit/205f1e643e25648173239b2de885fec430268492). The new path traversal vulnerability arises because the implementation does not protect itself against the application overwriting built-in utility functions with user-defined implementations.

**Description:** The function `possiblyTransformPath` calls `pathModule.resolve(path)`, where `pathModule` is the result of `require('path')`. Application code may replace the value of the `require('path').resolve`property with a user-defined function that does not resolve `/../` within any given path. Because `possiblyTransformPath` retrieves the value of the `pathModule.resolve` property dynamically, it will use the user-defined function instead of the built-in function and will thus fail to fully resolve the path given by the application. The vulnerability can be prevented by maintaining a reference to the original value of `pathModule.resolve` for use in `possiblyTransformPath`, assuming that the original implementation of the `resolve()` function is not subject to any such vulnerabilities itself.

## Steps To Reproduce:

Temporarily assigning `path.resolve = (s) => s` disables the resolution of `/../` within the permission model implementation.

```console
$ node --experimental-permission --allow-fs-read=/tmp/ -p "path.resolve = (s) => s; fs.readFileSync('/tmp/../etc/passwd')"
<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a 64 61 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f ... 3174 more bytes>
```

## Supporting Material/References:

* [Original HackerOne report 2092852 of this vulnerability](https://hackerone.com/reports/2092852)
* [HackerOne report 1952978](https://hackerone.com/reports/1952978) for the previous path traversal vulnerability (CVE-2023-30584)
* [Vulnerable implementation of `possiblyTransformPath`](https://github.com/nodejs/node/blob/af4cdcde154be58fc47b389670efbe10da489923/lib/internal/fs/utils.js#L711-L718)

## Suggested patch

```patch
diff --git a/lib/internal/fs/utils.js b/lib/internal/fs/utils.js
index b7354e30e9..4971656d0a 100644
--- a/lib/internal/fs/utils.js
+++ b/lib/internal/fs/utils.js
@@ -710,2 +710,3 @@ const validatePath = hideStackFrames((path, propName = 'path') => {
 // The permission model needs the absolute path for the fs_permission
+const resolvePath = pathModule.resolve;
 function possiblyTransformPath(path) {
@@ -713,3 +714,3 @@ function possiblyTransformPath(path) {
     if (typeof path === 'string') {
-      return pathModule.resolve(path);
+      return resolvePath(path);
     }
```

This patch assumes that `pathModule.resolve()` itself is not susceptible to having its behavior altered in a security-critical way through user-defined properties.

This patch was merged into the main branch of Node.js as [commit 32bcf4ca](https://github.com/nodejs/node/commit/32bcf4ca27bba9d4e48418f12dc6d7c2252e71ec) and into the Node.js 20 release line as [commit cd352751](https://github.com/nodejs/node/commit/cd352751118eccab625573092bf47d9b0d84b792).

## Impact

The impact is almost identical with that of CVE-2023-30584. Applications may use this vulnerability to read and write files and directories that the user has not granted access to.

## Attachments
No attachments
