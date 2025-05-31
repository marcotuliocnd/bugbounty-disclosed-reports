# [bower] Arbitrary File Write through improper validation of symlinks while package extraction

## Report Details
- **Report ID**: 473811
- **URL**: https://hackerone.com/reports/473811
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-01T17:17:27.369Z
- **Disclosed**: 2019-01-26T07:38:40.345Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report file write in arbitrary locations via install command in `bower`
It allows attackers to write arbitrary files when a malicious package is extracted.

# Module

**module name:** bower
**version:** 1.8.4
**npm page:** `https://www.npmjs.com/package/bower`

## Module Description

Bower offers a generic, unopinionated solution to the problem of front-end package management, while exposing the package dependency model via an API that can be consumed by a more opinionated build stack. There are no system wide dependencies, no dependencies are shared between different apps, and the dependency tree is flat.

## Module Stats

weekly downloads
175,693

# Vulnerability

## Vulnerability Description

Quoting from #362118

>The vulnerability is a form of directory traversal that can be exploited by extracting files from an archive. The premise of the directory traversal vulnerability is that an attacker can gain access to parts of the file system outside of the target folder in which they should reside. The attacker can then overwrite executable files and either invoke them remotely or wait for the system or user to call them, thus achieving remote command execution on the victim’s machine. The vulnerability can also cause damage by overwriting configuration files or other sensitive resources, and can be exploited on both client (user) machines and servers.

When we install a package that is in the tar archive format using `bower`, it tries to extract the package first. Bower installer attempts to prevent a package from writing any files outside the install directory; however it is possible to bypass the check with a symbolic link in a crafted npm package.

### Example structure of malicious npm package:

```
$ tar -xvf hello.tar.gz
hello/
hello/README.md
hello/link
hello/link/PWNED
hello/package.json

$ tar -tvf hello.tar.gz
drwxr-xr-x 0/0               0 2019-01-01 21:27 hello/
-rw-r--r-- 0/0              12 2019-01-01 21:27 hello/README.md
lrw-r--r-- 0/0               0 2019-01-01 21:27 hello/link -> /tmp
-rw-r--r-- 0/0              15 2019-01-01 21:27 hello/link/PWNED
-rw-r--r-- 0/0             102 2019-01-01 21:27 hello/package.json
```


## Steps To Reproduce:

Using attached file `hello.tar.gz`

```
$ bower install ./hello.tar.gz
bower hello.tar#*                 copy /home/path/hello.tar.gz
bower hello.tar#*              extract hello.tar.gz
bower hello.tar#*             resolved /home/path/hello.tar.gz
bower hello.tar#*              install hello.tar
```

This creates a file `/tmp/PWNED` which is a sufficient PoC

## Patch

I'm fully aware that `bower` has been deprecated and using `yarn` is advised. Therefore, I would recommend releasing an advisory if a patch might not be possible.

The vulnerability lies in [`extract.js`](https://github.com/bower/bower/blob/e8b94ecbd07376996eb0bea6cb30c20deb7e89b6/lib/util/extract.js#L133)

```JavaScript
function isSymlink(entry) {
    return entry.type === 'SymbolicLink';
}
```

According to the docs of [`tar-fs`](https://www.npmjs.com/package/tar-fs) making following changes will work in order to properly ignore symlinks

```diff
- function isSymlink(entry) {
+ function isSymlink(_, entry) {
-     return entry.type === 'SymbolicLink';
+    return entry.type === 'symlink';
}
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Ubuntu 16.04
- Node v11.3.0
- Bower 1.8.4

# Wrap up


- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

> Hunter's comments and funny memes goes here


{F399574}

## Impact

Writing arbitrary files on the system

## Attachments
- hello.tar.gz
- HAPPY_NEW_YEAR.png
