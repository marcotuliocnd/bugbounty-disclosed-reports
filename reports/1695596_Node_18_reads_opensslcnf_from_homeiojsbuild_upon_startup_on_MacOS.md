# Node 18 reads openssl.cnf from /home/iojs/build/... upon startup on MacOS

## Report Details
- **Report ID**: 1695596
- **URL**: https://hackerone.com/reports/1695596
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-08T19:43:15.601Z
- **Disclosed**: 2022-10-26T08:17:58.968Z

## Reporter
- **Username**: mhdawson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:**

Similar to https://hackerone.com/reports/1623175 it looks like in Node 18 and later, when it starts 
 it attempts to read /home/iojs/build/ws/out/Release/obj.target/deps/openssl/openssl.cnf on MacOS which ordinarily doesn't exist. This is even after the fix for linux.

The attack would be an attacker with access to a shared MacOS host with a self-chosen username (iojs) being able to affect the OpenSSF configuration of other users. I believe the iojs home directory is something configured within the Node.js build/CI pipeline, as opposed to something internal to OpenSSL.

**Description:**

## Steps To Reproduce:

From inspection of the code, look at the path specified in: https://github.com/nodejs/node/blob/7f9cd60eef6fad245baed9896ec6376b693e089a/deps/openssl/openssl.gyp#L24

        'openssl_dir': '<(PRODUCT_DIR_ABS)/obj.target/deps/openssl',

and unlike other platforms, this is not overriden on MacOS in "/deps/openssl/openssl_common.gypi"

This is a similar problem to what was fixed for Linux in https://nodejs.org/en/blog/vulnerability/july-2022-security-releases/#attempt-to-read-openssl-cnf-from-home-iojs-build-upon-startup-medium-cve-2022-32222

## Impact:

 openssl.cnf file is being read as part of OpenSSL's initialization; this is used to configure Node.js

## Supporting Material/References:

This is the suggested fix (also includes removing existing compiler warnings about duplicate OPENSSL definitions)

diff --git a/deps/openssl/openssl.gyp b/deps/openssl/openssl.gyp
  2 index 7b1278044e..861bbc5844 100644
  3 --- a/deps/openssl/openssl.gyp
  4 +++ b/deps/openssl/openssl.gyp
  5 @@ -7,21 +7,17 @@
  6      'conditions': [
  7        ['OS == "win"', {
  8          'obj_dir_abs': '<(PRODUCT_DIR_ABS)/obj',
  9 -        'openssl_dir': '<(PRODUCT_DIR_ABS)/obj/lib',
 10        }],
 11        ['GENERATOR == "ninja"', {
 12          'obj_dir_abs': '<(PRODUCT_DIR_ABS)/obj',
 13          'modules_dir': '<(PRODUCT_DIR_ABS)/obj/lib/openssl-modules',
 14 -        'openssl_dir': '<(PRODUCT_DIR_ABS)/obj/lib',
 15        }, {
 16          'obj_dir_abs%': '<(PRODUCT_DIR_ABS)/obj.target',
 17          'modules_dir': '<(PRODUCT_DIR_ABS)/obj.target/deps/openssl/lib/openssl-modules',
 18 -        'openssl_dir': '<(PRODUCT_DIR_ABS)/obj.target/deps/openssl',
 19        }],
 20        ['OS=="mac"', {
 21          'obj_dir_abs%': '<(PRODUCT_DIR_ABS)/obj.target',
 22          'modules_dir': '<(PRODUCT_DIR_ABS)/obj.target/deps/openssl/lib/openssl-modules',
 23 -        'openssl_dir': '<(PRODUCT_DIR_ABS)/obj.target/deps/openssl',
 24        }],
 25      ],
 26    },
 27 @@ -57,7 +53,6 @@
 28          ['node_shared_openssl=="false"', {
 29            'defines': [
 30              'MODULESDIR="<(modules_dir)"',
 31 -            'OPENSSLDIR="<(openssl_dir)"',
 32            ]
 33          }],
 34        ],
 35 diff --git a/deps/openssl/openssl_common.gypi b/deps/openssl/openssl_common.gypi
 36 index d4e39e8416..256eb7d180 100644
 37 --- a/deps/openssl/openssl_common.gypi
 38 +++ b/deps/openssl/openssl_common.gypi
 39 @@ -49,6 +49,7 @@
 40          'WARNING_CFLAGS': ['-Wno-missing-field-initializers']
 41        },
 42        'defines': [
 43 +        'OPENSSLDIR="/System/Library/OpenSSL/"',
 44          'ENGINESDIR="/dev/null"',
 45        ],
 46      }, 'OS=="solaris"', {

## Impact

The openssl.cnf file contains security configuration information for OpenSSL. It's possible that changing things like default ciphers could affect the security of an application using it.

## Attachments
No attachments
