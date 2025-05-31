# PHP mbstring / Oniguruma multiple remote heap/stack corruptions

## Report Details
- **Report ID**: 237915
- **URL**: https://hackerone.com/reports/237915
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-06-08T06:55:30.297Z
- **Disclosed**: 2019-10-14T04:40:04.200Z

## Reporter
- **Username**: xixabangm4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Oniguruma [1] by K. Kosako is a BSD licensed regular expression library that supports a variety of character encodings. The Ruby programming language, in version 1.9, as well as PHP's multi-byte string module (since PHP5), use Oniguruma as their regular expression engine. It is also used in products such as Atom, Take Command Console, Tera Term, TextMate, Sublime Text and SubEthaEdit.

We've identified six remote memory corruption issues in Oniguruma that affect the latest stable release v6.2.0 and the develop branch, they have received upstream patch in the latest stable version v6.3.0; PHP upstream has now included 5 of the patches (CVE-2017-9224, CVE-2017-9226, CVE-2017-9227, CVE-2017-9228, CVE-2017-9229) that are applicable to the mbstring module [2, 3]. The regular expression APIs may be exposed to regular expressions from the network, potentially allow remote exploitation or denial of service in products that use Oniguruma, such as when used in PHP5/7 and Ruby.

[1] https://github.com/kkos/oniguruma
[2] https://github.com/php/php-src/commit/20eacb787f4543604f3c657e191baf274bb943c2
[3] https://github.com/php/php-src/commit/bee52f352f00d86593bef43ed4cec4dbfd9edfcf

CVE-2017-9226: Heap Out-of-bounds Write
An issue was discovered in Oniguruma 6.2.0, as used in Oniguruma-mod in Ruby through 2.4.1 and mbstring in PHP through 7.1.5. A heap out-of-bounds write or read occurs in next_state_val() during regular expression compilation. Octal numbers larger than 0xff are not handled correctly in fetch_token() and fetch_token_in_cc(). A malformed regular expression containing an octal number in the form of '\700' would produce an invalid code point value larger than 0xff in next_state_val(), resulting in an out-of-bounds write memory corruption. Upstream issue report, fix and PHP commits as below:

https://github.com/kkos/oniguruma/issues/55
https://github.com/kkos/oniguruma/commit/f015fbdd95f76438cd86366467bb2b39870dd7c6
https://github.com/kkos/oniguruma/commit/b4bf968ad52afe14e60a2dc8a95d3555c543353a
https://github.com/php/php-src/commit/1e0c4386ab87c6f6392933450130470cbd1a2b19

CVE-2017-9224: Stack Out-of-bounds Read
An issue was discovered in Oniguruma 6.2.0, as used in Oniguruma-mod in Ruby through 2.4.1 and mbstring in PHP through 7.1.5. A stack out-of-bounds read occurs in match_at() during regular expression searching. A logical error involving order of validation and access in match_at() could result in an out-of-bounds read from a stack buffer. Upstream issue report, fix and PHP commits as below:

https://github.com/kkos/oniguruma/issues/57
https://github.com/kkos/oniguruma/commit/690313a061f7a4fa614ec5cc8368b4f2284e059b
https://github.com/php/php-src/commit/60b1829e1cd18facc696264fd830c4bbd593cfa9

CVE-2017-9227: Invalid Dereference, Denial-of-Service
An issue was discovered in Oniguruma 6.2.0, as used in Oniguruma-mod in Ruby through 2.4.1 and mbstring in PHP through 7.1.5. A stack out-of-bounds read occurs in mbc_enc_len() during regular expression searching. Invalid handling of reg->dmin in forward_search_range() could result in an invalid pointer dereference, as an out-of-bounds read from a stack buffer. Upstream issue report, fix and PHP commits as below:

https://github.com/kkos/oniguruma/issues/58
https://github.com/kkos/oniguruma/commit/9690d3ab1f9bcd2db8cbe1fe3ee4a5da606b8814
https://github.com/php/php-src/commit/6a8ae7cf8db3ec8dabfd027e01cdbcbb52654c90

CVE-2017-9228: Uninitialized Variable, Out-of-bounds Write
An issue was discovered in Oniguruma 6.2.0, as used in Oniguruma-mod in Ruby through 2.4.1 and mbstring in PHP through 7.1.5. A heap out-of-bounds write occurs in bitset_set_range() during regular expression compilation due to an uninitialized variable from an incorrect state transition. An incorrect state transition in parse_char_class() could create an execution path that leaves a critical local variable uninitialized until it's used as an index, resulting in an out-of-bounds write memory corruption. Upstream issue report, fix and PHP commits as below:

https://github.com/kkos/oniguruma/issues/60
https://github.com/kkos/oniguruma/commit/3b63d12038c8d8fc278e81c942fa9bec7c704c8b
https://github.com/php/php-src/commit/1c845d295037702d63097e2216b3c5db53f79273

CVE-2017-9229: Denial-of-Service
An issue was discovered in Oniguruma 6.2.0, as used in Oniguruma-mod in Ruby through 2.4.1 and mbstring in PHP through 7.1.5. A SIGSEGV occurs in left_adjust_char_head() during regular expression compilation. Invalid handling of reg->dmax in forward_search_range() could result in an invalid pointer dereference, normally as an immediate denial-of-service condition. Upstream issue report, fix and PHP commits as below:

https://github.com/kkos/oniguruma/issues/59
https://github.com/kkos/oniguruma/commit/b690371bbf97794b4a1d3f295d4fb9a8b05d402d
https://github.com/php/php-src/commit/5416deec665db293ae25548828791453d776a6bf






## Attachments
No attachments
