# null pointer dereference and segfault in tile-count-merge

## Report Details
- **Report ID**: 245221
- **URL**: https://hackerone.com/reports/245221
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-02T00:41:36.403Z
- **Disclosed**: 2017-07-11T15:36:07.317Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mapbox

## Vulnerability Information
This crash was triggered with `642f773 ` while fuzzing `tile-count-merge` with AFL on Debian 8 x64.

`./tile-count-merge -o /dev/null test000`

```
ASAN:SIGSEGV
=================================================================
==10201==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000048d0af bp 0x7ffd8644b6a0 sp 0x7ffd8644ae30 T0)
    #0 0x48d0ae in __interceptor_memcmp (/root/tile-count/tile-count-merge+0x48d0ae)
    #1 0x4dc6c9 in finder::operator<(finder const&) const /root/tile-count/merge.cpp:115:10
    #2 0x4dc6c9 in bool __gnu_cxx::__ops::_Iter_less_val::operator()<finder*, finder const>(finder*, finder const&) const /usr/bin/../lib/gcc/x86_64-linux-gnu/4.9/../../../../include/c++/4.9/bits/predefined_ops.h:54
    #3 0x4dc6c9 in finder* std::__lower_bound<finder*, finder, __gnu_cxx::__ops::_Iter_less_val>(finder*, finder*, finder const&, __gnu_cxx::__ops::_Iter_less_val) /usr/bin/../lib/gcc/x86_64-linux-gnu/4.9/../../../../include/c++/4.9/bits/stl_algobase.h:965
    #4 0x4ca6e0 in finder* std::lower_bound<finder*, finder>(finder*, finder*, finder const&) /usr/bin/../lib/gcc/x86_64-linux-gnu/4.9/../../../../include/c++/4.9/bits/stl_algobase.h:999:14
    #5 0x4ca6e0 in do_merge(merge*, unsigned long, int, int, long long, int, bool, unsigned long) /root/tile-count/merge.cpp:213
    #6 0x4c38e4 in main /root/tile-count/mergetool.cpp:105:2
    #7 0x7fba250bcb44 in __libc_start_main /build/glibc-qK83Be/glibc-2.19/csu/libc-start.c:287
    #8 0x4c248c in _start (/root/tile-count/tile-count-merge+0x4c248c)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV ??:0 __interceptor_memcmp
==10201==ABORTING
```

## Attachments
- test000.gz
