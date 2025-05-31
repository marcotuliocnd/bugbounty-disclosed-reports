# Arbitrary file overwrites in `node-tar`

## Report Details
- **Report ID**: 344595
- **URL**: https://hackerone.com/reports/344595
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-30T12:28:04.938Z
- **Disclosed**: 2019-04-03T20:14:08.789Z

## Reporter
- **Username**: max
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Background

I was looking for vulnerabilities in a different tar library, `tar-fs`, and discovered a bug that allowed me to overwrite arbitrary files on the host system using its default extraction method. After reporting the bug to the maintainer of `tar-fs`, Mathias Buus, he realized that `node-tar` was vulnerable to the same attack. However, he found that the npm client is not vulnerable here since the library it uses, `pacote`, [doesn't allow any hardlinks or symlinks](https://github.com/zkat/pacote/blob/latest/lib/extract-stream.js#L41).

# Vulnerability

If a tar file contains a hardlink to an existing file on the filesystem, and then a subsequent regular file with the same name as this hardlink, the contents of the regular file will overwrite the contents of the original file.

For example, the attached file, `hardlink_exploit.tar.gz`, contains two relevant files. First, a hardlink to `/tmp/overwriteme` called `hardboi/yyy`, and second, a regular file called `hardboi/yyy` containing `oops`.

To demonstrate this vulnerability:

- Make a file called `/tmp/overwriteme` with whatever contents
- Extract the attached tar archive using the following code:

```
tar = require('tar')

tar.x(
  {
    file: 'hardlink_exploit.tar.gz'
  }
).then(_=> { console.log("done") })
```

- Observe the contents of /tmp/overwriteme are now "oops"

I'm not sure what the best way to resolve this vulnerability is. My local copy of GNU Tar isn't vulnerable because by default it doesn't allow hardlinks that point to an absolute file or that try to directory traverse above the parent:

```
$ tar -xvf hardlink_pkg.tar.gz
hardboi/
tar: Removing leading `/' from hard link targets
hardboi/yyy
tar: hardboi/yyy: Cannot hard link to ‘tmp/overwriteme’: No such file or directory
hardboi/yyy
hardboi/package.json
tar: Exiting with failure status due to previous errors
```

## Impact

Applications, of which there are probably many, that rely on `node-tar` to be secure-by-default when extracting a tar file are in fact vulnerable. Unless hardlinks are explicitly disabled as in `pacote`, arbitrary files can be overwritten with the permissions of the user running `node-tar`.

## Attachments
- hardlink_exploit.tar.gz
