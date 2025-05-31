# Ruby 2.4.1 has "Stack consistency error" and aborts when processing return statement within a case statement

## Report Details
- **Report ID**: 247640
- **URL**: https://hackerone.com/reports/247640
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-10T07:42:38.487Z
- **Disclosed**: 2017-09-24T12:51:58.766Z

## Reporter
- **Username**: haquaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi,

I found the following file causes a ruby bug stating "Stack consistency error" and aborts.

File:
```
0>case
when 0
return end
```

xxd -g1 output of file
```
00000000: 30 3e 63 61 73 65 0a 77 68 65 6e 20 30 0a 72 65  0>case.when 0.re
00000010: 74 75 72 6e 20 65 6e 64 0a                       turn end.
```

ruby output:
```
crash.rb:3: [BUG] Stack consistency error (sp: 7, bp: 6)
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0002 p:0011 s:0007 e:000005 EVAL   crash.rb:3 [FINISH]
c:0001 p:0000 s:0003 E:0005d0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
crash.rb:3:in `<main>'

-- Other runtime information -----------------------------------------------

* Loaded script: crash.rb

* Loaded features:

    0 enumerator.so
    1 thread.rb
    2 rational.so
    3 complex.so
    4 /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/encdb.so
    5 /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/trans/transdb.so
    6 /usr/local/lib/ruby/2.4.0/unicode_normalize.rb
    7 /usr/local/lib/ruby/2.4.0/x86_64-linux/rbconfig.rb
    8 /usr/local/lib/ruby/2.4.0/rubygems/compatibility.rb
    9 /usr/local/lib/ruby/2.4.0/rubygems/defaults.rb
   10 /usr/local/lib/ruby/2.4.0/rubygems/deprecate.rb
   11 /usr/local/lib/ruby/2.4.0/rubygems/errors.rb
   12 /usr/local/lib/ruby/2.4.0/rubygems/version.rb
   13 /usr/local/lib/ruby/2.4.0/rubygems/requirement.rb
   14 /usr/local/lib/ruby/2.4.0/rubygems/platform.rb
   15 /usr/local/lib/ruby/2.4.0/rubygems/basic_specification.rb
   16 /usr/local/lib/ruby/2.4.0/rubygems/stub_specification.rb
   17 /usr/local/lib/ruby/2.4.0/rubygems/util/list.rb
   18 /usr/local/lib/ruby/2.4.0/x86_64-linux/stringio.so
   19 /usr/local/lib/ruby/2.4.0/rubygems/specification.rb
   20 /usr/local/lib/ruby/2.4.0/rubygems/exceptions.rb
   21 /usr/local/lib/ruby/2.4.0/rubygems/dependency.rb
   22 /usr/local/lib/ruby/2.4.0/rubygems/core_ext/kernel_gem.rb
   23 /usr/local/lib/ruby/2.4.0/monitor.rb
   24 /usr/local/lib/ruby/2.4.0/rubygems/core_ext/kernel_require.rb
   25 /usr/local/lib/ruby/2.4.0/rubygems.rb
   26 /usr/local/lib/ruby/2.4.0/rubygems/path_support.rb
   27 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/version.rb
   28 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/core_ext/name_error.rb
   29 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/levenshtein.rb
   30 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/jaro_winkler.rb
   31 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checker.rb
   32 /usr/local/lib/ruby/2.4.0/delegate.rb
   33 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checkers/name_error_checkers/class_name_checker.rb
   34 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checkers/name_error_checkers/variable_name_checker.rb
   35 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checkers/name_error_checkers.rb
   36 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checkers/method_name_checker.rb
   37 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/spell_checkers/null_checker.rb
   38 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean/formatter.rb
   39 /usr/local/lib/ruby/gems/2.4.0/gems/did_you_mean-1.1.0/lib/did_you_mean.rb

* Process memory map:

7fff7000-8fff7000 rw-p 00000000 00:00 0 
8fff7000-2008fff7000 ---p 00000000 00:00 0 
2008fff7000-10007fff8000 rw-p 00000000 00:00 0 
562660459000-562660f58000 r-xp 00000000 fd:01 135                        /usr/local/bin/ruby
562661158000-56266117e000 r--p 00aff000 fd:01 135                        /usr/local/bin/ruby
56266117e000-5626611ed000 rw-p 00b25000 fd:01 135                        /usr/local/bin/ruby
5626611ed000-562661e89000 rw-p 00000000 00:00 0 
600000000000-602000000000 ---p 00000000 00:00 0 
602000000000-602000020000 rw-p 00000000 00:00 0 
602000020000-603000000000 ---p 00000000 00:00 0 
603000000000-603000060000 rw-p 00000000 00:00 0 
603000060000-604000000000 ---p 00000000 00:00 0 
604000000000-604000080000 rw-p 00000000 00:00 0 
604000080000-606000000000 ---p 00000000 00:00 0 
606000000000-606000090000 rw-p 00000000 00:00 0 
606000090000-607000000000 ---p 00000000 00:00 0 
607000000000-607000080000 rw-p 00000000 00:00 0 
607000080000-608000000000 ---p 00000000 00:00 0 
608000000000-608000050000 rw-p 00000000 00:00 0 
608000050000-60b000000000 ---p 00000000 00:00 0 
60b000000000-60b000020000 rw-p 00000000 00:00 0 
60b000020000-60c000000000 ---p 00000000 00:00 0 
60c000000000-60c000040000 rw-p 00000000 00:00 0 
60c000040000-60d000000000 ---p 00000000 00:00 0 
60d000000000-60d000050000 rw-p 00000000 00:00 0 
60d000050000-60e000000000 ---p 00000000 00:00 0 
60e000000000-60e000030000 rw-p 00000000 00:00 0 
60e000030000-60f000000000 ---p 00000000 00:00 0 
60f000000000-60f000010000 rw-p 00000000 00:00 0 
60f000010000-610000000000 ---p 00000000 00:00 0 
610000000000-610000020000 rw-p 00000000 00:00 0 
610000020000-611000000000 ---p 00000000 00:00 0 
611000000000-611000080000 rw-p 00000000 00:00 0 
611000080000-612000000000 ---p 00000000 00:00 0 
612000000000-612000030000 rw-p 00000000 00:00 0 
612000030000-613000000000 ---p 00000000 00:00 0 
613000000000-613000020000 rw-p 00000000 00:00 0 
613000020000-614000000000 ---p 00000000 00:00 0 
614000000000-614000030000 rw-p 00000000 00:00 0 
614000030000-615000000000 ---p 00000000 00:00 0 
615000000000-615000020000 rw-p 00000000 00:00 0 
615000020000-616000000000 ---p 00000000 00:00 0 
616000000000-616000360000 rw-p 00000000 00:00 0 
616000360000-617000000000 ---p 00000000 00:00 0 
617000000000-617000030000 rw-p 00000000 00:00 0 
617000030000-618000000000 ---p 00000000 00:00 0 
618000000000-618000020000 rw-p 00000000 00:00 0 
618000020000-619000000000 ---p 00000000 00:00 0 
619000000000-619000050000 rw-p 00000000 00:00 0 
619000050000-61a000000000 ---p 00000000 00:00 0 
61a000000000-61a000020000 rw-p 00000000 00:00 0 
61a000020000-61b000000000 ---p 00000000 00:00 0 
61b000000000-61b000020000 rw-p 00000000 00:00 0 
61b000020000-61c000000000 ---p 00000000 00:00 0 
61c000000000-61c000020000 rw-p 00000000 00:00 0 
61c000020000-61d000000000 ---p 00000000 00:00 0 
61d000000000-61d000020000 rw-p 00000000 00:00 0 
61d000020000-61e000000000 ---p 00000000 00:00 0 
61e000000000-61e000020000 rw-p 00000000 00:00 0 
61e000020000-61f000000000 ---p 00000000 00:00 0 
61f000000000-61f000030000 rw-p 00000000 00:00 0 
61f000030000-620000000000 ---p 00000000 00:00 0 
620000000000-620000020000 rw-p 00000000 00:00 0 
620000020000-621000000000 ---p 00000000 00:00 0 
621000000000-621000080000 rw-p 00000000 00:00 0 
621000080000-622000000000 ---p 00000000 00:00 0 
622000000000-622000020000 rw-p 00000000 00:00 0 
622000020000-623000000000 ---p 00000000 00:00 0 
623000000000-623000030000 rw-p 00000000 00:00 0 
623000030000-624000000000 ---p 00000000 00:00 0 
624000000000-624000060000 rw-p 00000000 00:00 0 
624000060000-625000000000 ---p 00000000 00:00 0 
625000000000-625000090000 rw-p 00000000 00:00 0 
625000090000-626000000000 ---p 00000000 00:00 0 
626000000000-626000030000 rw-p 00000000 00:00 0 
626000030000-627000000000 ---p 00000000 00:00 0 
627000000000-627000020000 rw-p 00000000 00:00 0 
627000020000-628000000000 ---p 00000000 00:00 0 
628000000000-628000010000 rw-p 00000000 00:00 0 
628000010000-629000000000 ---p 00000000 00:00 0 
629000000000-629000020000 rw-p 00000000 00:00 0 
629000020000-62b000000000 ---p 00000000 00:00 0 
62b000000000-62b000030000 rw-p 00000000 00:00 0 
62b000030000-62c000000000 ---p 00000000 00:00 0 
62c000000000-62c000020000 rw-p 00000000 00:00 0 
62c000020000-62d000000000 ---p 00000000 00:00 0 
62d000000000-62d0002d0000 rw-p 00000000 00:00 0 
62d0002d0000-62f000000000 ---p 00000000 00:00 0 
62f000000000-62f000030000 rw-p 00000000 00:00 0 
62f000030000-632000000000 ---p 00000000 00:00 0 
632000000000-632000030000 rw-p 00000000 00:00 0 
632000030000-633000000000 ---p 00000000 00:00 0 
633000000000-633000060000 rw-p 00000000 00:00 0 
633000060000-640000000000 ---p 00000000 00:00 0 
640000000000-640000003000 rw-p 00000000 00:00 0 
7fb057651000-7fb057683000 rw-p 00000000 00:00 0 
7fb057683000-7fb05769e000 r-xp 00000000 fd:01 513782                     /usr/local/lib/ruby/2.4.0/x86_64-linux/stringio.so
7fb05769e000-7fb05789e000 ---p 0001b000 fd:01 513782                     /usr/local/lib/ruby/2.4.0/x86_64-linux/stringio.so
7fb05789e000-7fb05789f000 r--p 0001b000 fd:01 513782                     /usr/local/lib/ruby/2.4.0/x86_64-linux/stringio.so
7fb05789f000-7fb0578a1000 rw-p 0001c000 fd:01 513782                     /usr/local/lib/ruby/2.4.0/x86_64-linux/stringio.so
7fb0578a1000-7fb0578a9000 r-xp 00000000 fd:01 768982                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/trans/transdb.so
7fb0578a9000-7fb057aa8000 ---p 00008000 fd:01 768982                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/trans/transdb.so
7fb057aa8000-7fb057aa9000 r--p 00007000 fd:01 768982                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/trans/transdb.so
7fb057aa9000-7fb057aab000 rw-p 00008000 fd:01 768982                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/trans/transdb.so
7fb057aab000-7fb057ab5000 r-xp 00000000 fd:01 768950                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/encdb.so
7fb057ab5000-7fb057cb4000 ---p 0000a000 fd:01 768950                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/encdb.so
7fb057cb4000-7fb057cb5000 r--p 00009000 fd:01 768950                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/encdb.so
7fb057cb5000-7fb057cb8000 rw-p 0000a000 fd:01 768950                     /usr/local/lib/ruby/2.4.0/x86_64-linux/enc/encdb.so
7fb057cb8000-7fb057e50000 r--p 00000000 fd:01 5196                       /usr/lib/locale/locale-archive
7fb057e50000-7fb05a1a2000 rw-p 00000000 00:00 0 
7fb05a1a2000-7fb05a362000 r-xp 00000000 fd:01 12855                      /lib/x86_64-linux-gnu/libc-2.23.so
7fb05a362000-7fb05a562000 ---p 001c0000 fd:01 12855                      /lib/x86_64-linux-gnu/libc-2.23.so
7fb05a562000-7fb05a566000 r--p 001c0000 fd:01 12855                      /lib/x86_64-linux-gnu/libc-2.23.so
7fb05a566000-7fb05a568000 rw-p 001c4000 fd:01 12855                      /lib/x86_64-linux-gnu/libc-2.23.so
7fb05a568000-7fb05a56c000 rw-p 00000000 00:00 0 
7fb05a56c000-7fb05a582000 r-xp 00000000 fd:01 2035                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fb05a582000-7fb05a781000 ---p 00016000 fd:01 2035                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fb05a781000-7fb05a782000 rw-p 00015000 fd:01 2035                       /lib/x86_64-linux-gnu/libgcc_s.so.1
7fb05a782000-7fb05a789000 r-xp 00000000 fd:01 12841                      /lib/x86_64-linux-gnu/librt-2.23.so
7fb05a789000-7fb05a988000 ---p 00007000 fd:01 12841                      /lib/x86_64-linux-gnu/librt-2.23.so
7fb05a988000-7fb05a989000 r--p 00006000 fd:01 12841                      /lib/x86_64-linux-gnu/librt-2.23.so
7fb05a989000-7fb05a98a000 rw-p 00007000 fd:01 12841                      /lib/x86_64-linux-gnu/librt-2.23.so
7fb05a98a000-7fb05aa92000 r-xp 00000000 fd:01 12850                      /lib/x86_64-linux-gnu/libm-2.23.so
7fb05aa92000-7fb05ac91000 ---p 00108000 fd:01 12850                      /lib/x86_64-linux-gnu/libm-2.23.so
7fb05ac91000-7fb05ac92000 r--p 00107000 fd:01 12850                      /lib/x86_64-linux-gnu/libm-2.23.so
7fb05ac92000-7fb05ac93000 rw-p 00108000 fd:01 12850                      /lib/x86_64-linux-gnu/libm-2.23.so
7fb05ac93000-7fb05ac9c000 r-xp 00000000 fd:01 12837                      /lib/x86_64-linux-gnu/libcrypt-2.23.so
7fb05ac9c000-7fb05ae9b000 ---p 00009000 fd:01 12837                      /lib/x86_64-linux-gnu/libcrypt-2.23.so
7fb05ae9b000-7fb05ae9c000 r--p 00008000 fd:01 12837                      /lib/x86_64-linux-gnu/libcrypt-2.23.so
7fb05ae9c000-7fb05ae9d000 rw-p 00009000 fd:01 12837                      /lib/x86_64-linux-gnu/libcrypt-2.23.so
7fb05ae9d000-7fb05aecb000 rw-p 00000000 00:00 0 
7fb05aecb000-7fb05aece000 r-xp 00000000 fd:01 12844                      /lib/x86_64-linux-gnu/libdl-2.23.so
7fb05aece000-7fb05b0cd000 ---p 00003000 fd:01 12844                      /lib/x86_64-linux-gnu/libdl-2.23.so
7fb05b0cd000-7fb05b0ce000 r--p 00002000 fd:01 12844                      /lib/x86_64-linux-gnu/libdl-2.23.so
7fb05b0ce000-7fb05b0cf000 rw-p 00003000 fd:01 12844                      /lib/x86_64-linux-gnu/libdl-2.23.so
7fb05b0cf000-7fb05b14e000 r-xp 00000000 fd:01 25776                      /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
7fb05b14e000-7fb05b34d000 ---p 0007f000 fd:01 25776                      /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
7fb05b34d000-7fb05b34e000 r--p 0007e000 fd:01 25776                      /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
7fb05b34e000-7fb05b34f000 rw-p 0007f000 fd:01 25776                      /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.0
7fb05b34f000-7fb05b367000 r-xp 00000000 fd:01 12838                      /lib/x86_64-linux-gnu/libpthread-2.23.so
7fb05b367000-7fb05b566000 ---p 00018000 fd:01 12838                      /lib/x86_64-linux-gnu/libpthread-2.23.so
7fb05b566000-7fb05b567000 r--p 00017000 fd:01 12838                      /lib/x86_64-linux-gnu/libpthread-2.23.so
7fb05b567000-7fb05b568000 rw-p 00018000 fd:01 12838                      /lib/x86_64-linux-gnu/libpthread-2.23.so
7fb05b568000-7fb05b56c000 rw-p 00000000 00:00 0 
7fb05b56c000-7fb05b592000 r-xp 00000000 fd:01 12833                      /lib/x86_64-linux-gnu/ld-2.23.so
7fb05b5a7000-7fb05b5fd000 rw-p 00000000 00:00 0 
7fb05b5fd000-7fb05b5fe000 ---p 00000000 00:00 0 
7fb05b5fe000-7fb05b782000 rw-p 00000000 00:00 0 
7fb05b782000-7fb05b791000 rw-p 00000000 00:00 0 
7fb05b791000-7fb05b792000 r--p 00025000 fd:01 12833                      /lib/x86_64-linux-gnu/ld-2.23.so
7fb05b792000-7fb05b793000 rw-p 00026000 fd:01 12833                      /lib/x86_64-linux-gnu/ld-2.23.so
7fb05b793000-7fb05b794000 rw-p 00000000 00:00 0 
7fff347b5000-7fff34fb4000 rw-p 00000000 00:00 0                          [stack]
7fff34fdf000-7fff34fe1000 r--p 00000000 00:00 0                          [vvar]
7fff34fe1000-7fff34fe3000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]


[NOTE]
You may have encountered a bug in the Ruby interpreter or extension libraries.
Bug reports are welcome.
For details: http://www.ruby-lang.org/bugreport.html

```

Running --dump=insns:
```
== disasm: #<ISeq:<main>@crash.rb>======================================
0000 trace            1                                               (   3)
0002 putobject_OP_INT2FIX_O_0_C_                                      (   1)
0003 putobject_OP_INT2FIX_O_0_C_                                      (   2)
0004 branchif         9
0006 putnil                                                           (   3)
0007 jump             11
0009 putnil
0010 leave
0011 opt_gt           <callinfo!mid:>, argc:1, ARGS_SIMPLE>, <callcache>
0014 leave
```

Ruby version output:
```
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-linux]
```

I've attached the crash.rb file.

The crash does not happen if I remove the "return" from the case statement, and the jump statement in the insns dump shows 10 instead of 11.

Would a bug such as this be valid for this bounty, or should I report them directly to the ruby project?

Cheers,

Hugh

## Attachments
- crash.rb
