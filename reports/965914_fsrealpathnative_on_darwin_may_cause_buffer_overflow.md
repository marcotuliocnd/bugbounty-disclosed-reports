# `fs.realpath.native` on darwin may cause buffer overflow

## Report Details
- **Report ID**: 965914
- **URL**: https://hackerone.com/reports/965914
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-24T15:18:48.912Z
- **Disclosed**: 2020-10-17T19:17:19.242Z

## Reporter
- **Username**: ashi009
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 

The libuv's implementation of realpath is flawed on darwin and may cause buffer overflow.

**Description:** 

libuv's `realpath` implementation determines the buffer size with `pathconf` and fallback to `_POSIX_PATH_MAX` (256) if that fails for any reason (eg. `ENOENT`). However `realpath` requires a buffer of at least `PATH_MAX` (1024) bytes to be used, hence causes the buffer overflow if the resolved path is longer than 256 bytes.

## Steps To Reproduce:

1. `LONG_PATH='/tmp/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/long/path/254B'`
1. `SHORT_LINK='/tmp/short'`
1. `mkdir -p "${LONG_PATH}"`
1. `ln -s "${LONG_PATH}" "${SHORT_LINK}"`
1. `node -e "fs.realpathSync.native('${SHORT_LINK}/file-not-exist')"`

## Impact: 

Cause node process to crash.

## Supporting Material/References:

- https://github.com/bazelbuild/rules_nodejs/issues/1958
- https://github.com/libuv/libuv/issues/2965
- https://github.com/libuv/libuv/issues/2966

## Impact

Given that nodejs on darwin are mostly desktop applications and used as developer tools, exploit this is very unlikely to cause more damage than an application crash.

## Attachments
No attachments
