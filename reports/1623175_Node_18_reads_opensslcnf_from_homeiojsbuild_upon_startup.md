# Node 18 reads openssl.cnf from /home/iojs/build/... upon startup.

## Report Details
- **Report ID**: 1623175
- **URL**: https://hackerone.com/reports/1623175
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-03T04:17:48.774Z
- **Disclosed**: 2023-08-11T15:34:47.980Z

## Reporter
- **Username**: msvrmiscovet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:**
I noticed that when Node 18 (18.4.0 on Ubuntu, 64-bit via Docker) starts, it attempts to read `/home/iojs/build/ws/out/Release/obj.target/deps/openssl/openssl.cnf`, which ordinarily doesn't exist. I haven't proven this out, but I suspect that if one were to create this file, it would be read and processed as a normal OpenSSF configuration file. The attack would be an attacker on a shared Linux host with a self-chosen username (`iojs`) being able to affect the OpenSSF configuration of other users. I believe the `iojs` home directory is something configured within the Node.js build/CI pipeline, as opposed to something internal to OpenSSL.

**Description:**

## Steps To Reproduce:

  1. Install Node.js 18.4.0 on Ubuntu (`wget 'https://nodejs.org/dist/v18.4.0/node-v18.4.0-linux-x64.tar.xz' && tar Jxvf ./node-v18.4.0-linux-x64.tar.xz && cd node-v18.4.0-linux-x64/bin` and strace (`sudo apt-get install strace`).
  2. Run node (no parameters) under strace, and watch for `open` syscalls pointing to the openssf.cnf file (`strace -f -ff -e trace=network,file,process -s 128 -D ./node 2>&1 | grep openssl`)
  3. See the read attempt:

```
root@bd9a1157008b:/usr/src/app/node-v18.4.0-linux-x64/bin# strace -f -ff -e trace=network,file,process -s 128 -D ./node 2>&1 | grep openssl
[pid  1536] openat(AT_FDCWD, "/home/iojs/build/ws/out/Release/obj.target/deps/openssl/openssl.cnf", O_RDONLY) = -1 ENOENT (No such file or directory)
```

I did *not* see this occur when testing 16.15.1 (also Ubuntu, 64-bit), but I *do* see this in 17.0.0, which suggests it came in with the move to OpenSSL 3.0 ([change log](https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_V17.md#17.0.0)).

## Impact:
I'm presuming that the openssl.cnf file is being read as part of OpenSSL's initialization; this is likely used to configure Node.js, though admittedly, it might be overwritten afterwards with a "correct" configuration.

## Supporting Material/References:

N/A

## Impact

The openssl.cnf file contains security configuration information for OpenSSL. It's possible that changing things like default ciphers could affect the security of an application using it. (Admittedly, I'm not super familiar with this -- I'm definitely making some assumptions.)

## Attachments
No attachments
