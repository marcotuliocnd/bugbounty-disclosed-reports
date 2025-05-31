# A crash when an exception is caught in a caller and the receiver returned from `ensure`

## Report Details
- **Report ID**: 204774
- **URL**: https://hackerone.com/reports/204774
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-08T22:04:47.881Z
- **Disclosed**: 2017-02-28T09:44:48.161Z

## Reporter
- **Username**: ahmadsherif
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
This snippet crashes when ran by `./bin/sandbox`:
```ruby
class A
  def foo
    pr = proc { return 1 }

    begin
      does_not_exist
    ensure
      pr[]
    end
  end
end

begin
  A.new.foo
rescue
end
```

Crash details:
```
./bin/sandbox:20: [BUG] Segmentation fault at 0x0000000000000e
ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-linux]

-- Control frame information -----------------------------------------------
c:0003 p:---- s:0010 e:000009 CFUNC  :sandbox_eval
c:0002 p:0201 s:0005 E:0015d8 EVAL   ./bin/sandbox:20 [FINISH]
c:0001 p:0000 s:0002 E:0017a0 (none) [FINISH]

-- Ruby level backtrace information ----------------------------------------
./bin/sandbox:20:in `<main>'
./bin/sandbox:20:in `sandbox_eval'

-- Machine register context ------------------------------------------------
 RIP: 0x00007efdc0f073b4 RBP: 0x00007efdbfa7a4e0 RSP: 0x00007efdbfa78678
 RAX: 0x0000000000000091 RBX: 0x0000000000000006 RCX: 0x00007efdc0f80a73
 RDX: 0x0000000000000091 RDI: 0x00007efdbfa7a4e0 RSI: 0x0000000000000006
  R8: 0x00007efdc0f7ecf5  R9: 0x0000000000000000 R10: 0x00007efdbfadb0d0
 R11: 0x0000000000000006 R12: 0x0000000000000010 R13: 0x0000000000000091
 R14: 0x00007efdbfa811d0 R15: 0x00007efdbfa810b0 EFL: 0x0000000000010246

-- C level backtrace information -------------------------------------------
.rvm/rubies/ruby-2.3.1/lib/libruby.so.2.3(rb_vm_bugreport+0x4e8) [0x7efdc5046138] vm_dump.c:688
.rvm/rubies/ruby-2.3.1/lib/libruby.so.2.3(rb_bug_context+0xd4) [0x7efdc4ed9204] error.c:435
.rvm/rubies/ruby-2.3.1/lib/libruby.so.2.3(sigsegv+0x3e) [0x7efdc4fb4dde] signal.c:890
/usr/lib/libpthread.so.0 [0x7efdc4c4f080]
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_respond_to+0x14) [0x7efdc0f073b4] mruby-engine/ext/mruby_engine/mruby/include/mruby/boxing_word.h:75
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_check_convert_type+0x54) [0x7efdc0f2cdd4] mruby-engine/ext/mruby_engine/mruby/src/object.c:314
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_check_string_type+0x1c) [0x7efdc0f1cefc] mruby-engine/ext/mruby_engine/mruby/src/string.c:1750
mruby-engine/lib/mruby_engine/mruby_engine.so(join_ary+0xad) [0x7efdc0f228ed] mruby-engine/ext/mruby_engine/mruby/src/array.c:1051
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_ary_join+0x2e) [0x7efdc0f22bde] mruby-engine/ext/mruby_engine/mruby/src/array.c:1075
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vformat+0x14b) [0x7efdc0f0faeb] mruby-engine/ext/mruby_engine/mruby/src/error.c:363
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_name_error+0x9a) [0x7efdc0f0fd0a] mruby-engine/ext/mruby_engine/mruby/src/error.c:400
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_mod_const_missing+0x54) [0x7efdc0f07a24] mruby-engine/ext/mruby_engine/mruby/src/class.c:2185
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_with_block+0x2b5) [0x7efdc0ef98b5] mruby-engine/ext/mruby_engine/mruby/src/vm.c:430
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_funcall_argv+0xc) [0x7efdc0efa00c] mruby-engine/ext/mruby_engine/mruby/src/vm.c:447
mruby-engine/lib/mruby_engine/mruby_engine.so(const_get+0x140) [0x7efdc0ef6ae0] mruby-engine/ext/mruby_engine/mruby/src/variable.c:913
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_const_get+0xcb) [0x7efdc0ef813b] mruby-engine/ext/mruby_engine/mruby/src/variable.c:953
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_exec+0x236f) [0x7efdc0efd35f] mruby-engine/ext/mruby_engine/mruby/src/vm.c:966
mruby-engine/lib/mruby_engine/mruby_engine.so(mrb_vm_run+0x57) [0x7efdc0f01717] mruby-engine/ext/mruby_engine/mruby/src/vm.c:801
mruby-engine/lib/mruby_engine/mruby_engine.so(mruby_engine_monitored_eval+0x103) [0x7efdc0eef253] ../../../../ext/mruby_engine/eval_monitored.c:68
/usr/lib/libpthread.so.0 [0x7efdc4c45454]
/usr/lib/libc.so.6(clone+0x5f) [0x7efdc3fb57df]
```

My environment is as follows:
* mruby-engine version is 09be20e67888b20bebf9b0588bc3cbec7f55325f
* MRuby version is d0ecf862d9d2e7aed461bc9360686449f56c5d25
* I have mruby-print added to my gem box
* GCC version is "gcc (GCC) 6.3.1 20170109"
* I'm running ArchLinux (uname -r => "4.8.13-1-ARCH")

## Attachments
No attachments
