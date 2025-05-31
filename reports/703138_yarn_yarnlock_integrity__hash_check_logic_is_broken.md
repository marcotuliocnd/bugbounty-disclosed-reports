# [yarn] yarn.lock integrity & hash check logic is broken

## Report Details
- **Report ID**: 703138
- **URL**: https://hackerone.com/reports/703138
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-27T19:51:27.138Z
- **Disclosed**: 2020-02-26T13:46:41.721Z

## Reporter
- **Username**: chalker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a vulnerability in `yarn`.

It allows to pollute yarn cache via a crafted `yarn.lock` file and place a malicious package into cache under any name/version, bypassing both integrity and hash checks in `yarn.lock` so that any future installs of that package will install the fake version (regardless of integrity and hashes).

# Module

**module name:** `yarn`
**version:** 1.7.3 (`latest` tag)
**npm page:** `https://www.npmjs.com/package/yarn`

## Module Description

> Fast, reliable, and secure dependency management.

## Module Stats

`187 702` downloads in the last day
`998 482` downloads in the last week
`4 214 949` downloads in the last month

# Vulnerability

## Vulnerability Description

In short: integrity check logic _and_ hash check logic seems broken.

* Integrity/hash checks seem to be performed when placing a package to cache, not when a package is taken out of the cache. It’s a bit tricky though.

* It is easy to get installs pass with both hash and integrity simultaneously mismatching in yarn.lock, without any manual intervention apart from calling yarn on crafted lockfiles (to pollute cache).

So, more details on what is happening:

1. When the package is downloaded, only integrity is checked.
   The package is saved into cache with its sha1 hash. sha1 hash is not checked.

2. When the package is taken out of cache, it’s taken by name + version + sha1 hash.
   Integrity is not checked (completely ignored).

3. When one pollutes a cache by specifying incorrect hash in yarn.lock
   (but correct integrity), that hash is trusted and goes into cache.

4. After that, installing yarn.lock files with both that specific incorrect hash
   and any integrity just pass, until yarn cache is cleared.

5. Removing node_modules does not help, only clearing yarn cache helps.

While that might seem just moderately dangerous at the first glance (integrity needs to match once), there is a larger problem with that:

It is very simple to trick yarn into putting an *completely unrelated package* into cache, including a different package or even a tgz file that is not even coming from npm registry. And integrity is not checked afterwards.

## Steps To Reproduce:

Code to reproduce is shared with Yarn maintainers via https://github.com/ChALkeR/yarnbug2.

It used the following logic:

(1). Create a `yarn.lock` file by installing the _payload_ package or tgz file, e.g.:
```
  "dependencies": {
   "ponyhooves": "^1.0.1"
  }
```
```
ponyhooves@^1.0.1:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/ponyhooves/-/ponyhooves-1.0.1.tgz#e57c9c3e976d570f97f229356ca5d6ee13efd358"
  integrity sha1-5XycPpdtVw+X8ik1bKXW7hPv01g=
```

(2). Replace the package name, version, and hash with _target_ package. Leave integrity intact.
  
```
  "dependencies": {
    "express": "4.11.1"
  }
```
```
express@4.11.1:
  version "4.11.1"
  resolved "https://registry.yarnpkg.com/ponyhooves/-/ponyhooves-1.0.1.tgz#36d04dd27aa1667634e987529767f9c99de7903f"
  integrity sha1-5XycPpdtVw+X8ik1bKXW7hPv01g=
```
  
(3). Installing this yarn.lock will pollute `express@4.1.11` package in yarn cache (if it is not already present there). Any future installs of `express@4.1.11` will resolve to this payload package -- hashes match with express, and integrity check is ignored.

## Workaround

`yarn cache clean` before installs.

## Patch

* Cache should check both hash and integrity on initial install (not just integrity). That is not a sufficient fix though (sha1 is weak).
* Cache should take integrity into account, so that if integrity in`yarn.lock` mismatches integrity of the archive that was placed in cache, install should error or ignore the cached version.

## Supporting Material/References:

- Node.js v12.11.0
- npm v6.11.3

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

I am sponsored by [Exodus](https://exodus.io) to perform security research.

## Impact

Pollute local yarn cache with malicious packages and bypass hash/integrity checks.

It is even possible to execute `postinstall` this way even if the original malicious package has been installed with `yarn --ignore-scripts`.

## Attachments
No attachments
