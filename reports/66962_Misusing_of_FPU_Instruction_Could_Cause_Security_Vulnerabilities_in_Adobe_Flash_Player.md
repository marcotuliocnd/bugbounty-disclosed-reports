# Misusing of FPU Instruction Could Cause Security Vulnerabilities in Adobe Flash Player

## Report Details
- **Report ID**: 66962
- **URL**: https://hackerone.com/reports/66962
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-06-09T19:20:55.951Z
- **Disclosed**: 2019-11-12T09:43:36.415Z

## Reporter
- **Username**: yopwn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Misusing of FPU Instruction Could Cause Security Vulnerabilities in Adobe Flash Player

This vulnerability (CVE-2015-3100) was reported to Adobe on March 10, 2015 and has been patched today via APSB15-11 (https://helpx.adobe.com/security/products/flash-player/apsb15-11.html).

Following is the original vulnerability report, sharing privately for your assessment of the impact.

Summary:
========
There is a security vulnerability in Adobe Flash Player when using FPU instructions. Successfully exploiting this vulnerability allows the attacker run arbitrary code with the same right of the current user.


Details:
========
According to http://en.wikibooks.org/wiki/X86_Assembly/Floating_Point#FPU_Register_Stack,

"the FPU has 8 registers, st0 to st7, formed into a stack. Numbers are pushed onto the stack from memory, and are popped off the stack back to memory".

Programs are responsible to maintain the stack when using FPU instructions. If not, for example, all the 8 registers are in-use, future FPU instruction may fail and cause a "stack overflow" problem while the failed instruction doesn't have a chance to know. 


Under some certain situation, Adobe Flash Player may use FPU instructions to handle floating numbers. When playing the attached "PoC.swf", it will run the following function/code.

.text:009CE380 sub_9CE380      proc near               
.text:009CE380
.text:009CE380 arg_0           = dword ptr  4
.text:009CE380
.text:009CE380                 mov     eax, [esp+arg_0]
.text:009CE384                 mov     ecx, eax
.text:009CE386                 and     ecx, 7
.text:009CE389                 cmp     cl, 6
.text:009CE38C                 jnz     short loc_9CE39A		;jmp to 009CE39A
.text:009CE38E                 sar     eax, 3
.text:009CE391                 mov     [esp+arg_0], eax
.text:009CE395                 fild    [esp+arg_0]
.text:009CE399                 retn
.text:009CE39A ; ---------------------------------------------------------------------------
.text:009CE39A
.text:009CE39A loc_9CE39A:					
.text:009CE39A                 and     eax, 0FFFFFFF8h
.text:009CE39D                 fld     qword ptr [eax]		;this will cause one more FPU register in use
.text:009CE39F                 retn
.text:009CE39F sub_9CE380      endp

(We are using the Flash Player projector for test, version is 16.0.0.305.)

However, the main function which calls the sub_9CE380 doesn't "restore" the FPU register's status correctly. Instead of "clean" the registers, it simply return to its main function, and there is no place to "clean" the FPU registers at all. Let's see what the main function does.

03ED5C89    83C4 10         add     esp, 10
03ED5C8C    83EC 0C         sub     esp, 0C
03ED5C8F    50              push    eax
03ED5C90    E8 EB86AFFC     call    flashpla.009CE380		; call to use one FPU register
03ED5C95    83C4 10         add     esp, 10			; no instruction to "clean" the FPU register 
03ED5C98    8BE5            mov     esp, ebp
03ED5C9A    5D              pop     ebp
03ED5C9B    C3              retn				; return

This is a JITed function from our bytecode in one of the "method_bodies" in the SWF file. In the main function of this function, it also doesn't have any FPU instruction to clean the register. Here is what it may look like:

00A10E86    2BE1            sub     esp, ecx
00A10E88    51              push    ecx
00A10E89    8B4D 10         mov     ecx, dword ptr [ebp+10]
00A10E8C    8B55 0C         mov     edx, dword ptr [ebp+C]
00A10E8F    8B46 08         mov     eax, dword ptr [esi+8]
00A10E92    8B40 04         mov     eax, dword ptr [eax+4]
00A10E95    51              push    ecx
00A10E96    52              push    edx
00A10E97    56              push    esi
00A10E98    FFD0            call    eax				; call to our previously-discussed function
00A10E9A    83C4 0C         add     esp, 0C
00A10E9D    59              pop     ecx
00A10E9E    03E1            add     esp, ecx
00A10EA0    59              pop     ecx
00A10EA1    5E              pop     esi
00A10EA2    5D              pop     ebp
00A10EA3    C3              retn				; return


Anyway, when running the 1st time of sub_9CE380, st(0) will become "in-use", when running the 2nd time, the st(0) and st(1) will become "in-use". After we run it 6 times, which will cause st(0) to st(5) "in-use" - this is exactly what we see when playing our PoC.swf.

A failure of maintaining the FPU register stack may cause many problems. For example, if all the 8 registers are all in-use, future FPU instruction which related to FPU register may fail, and the program usually don't have a way to detect such instruction-level failure.

The attached "PoC.swf" will cause the program run to the sub_009EB440 function. There will be some FPU instructions involved and some will fail. Since it's probably a good example to explain this situation, let's see what the sub_009EB440 does. We use Hex-Rays Decomplier and got the following piece of code.

  if ( r_value >= 1.0 )
  {
    v7 = floor(r_value);
    if ( 0.0 != v7 )
    {
      v15 = (double)radix;
      v16 = 1.0 / v15;
      do			//starting point of the loop
      {
        v14 = v7;
        v7 = floor(v7 * v16);
        v8 = v14 - v15 * v7;
        if ( v8 >= 10.0 )
          v9 = (signed int)v8 + 87;
        else
          v9 = (signed int)v8 + 48;
        *v4-- = v9;		/******note: writing 1 byte to stack memory, and the pointer is decreased by 1******/
      }
      while ( 0.0 != v7 );	//the loop
    }
    if ( !negative )
      goto LABEL_16;
    *v4 = 45;
  }
  else
  {
    LOBYTE(v13) = 48;
  }

It's probably the "MathUtils::convertDoubleToStringRadix()" function in Adobe's open-sourced "avmplus" code.

Usually the above code run well, but if there is a FPU register stack overflow, some instruction will fail and it will cause that the execution in the loop will not have a chance to get out - which will cause all the stack memory be overwritten.

We have observed the following "WRITE" exception in the following address:

eax=80000057 ebx=03774000 ecx=00000000 edx=00000000 esi=00032fff edi=0012e650
eip=009eb50d esp=0012e250 ebp=0012e690 iopl=0         nv up ei ng nz na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00240282
flashplayer_16_sa!IAEModule_IAEKernel_UnloadModule+0xff91d:
009eb50d 8806            mov     byte ptr [esi],al          ds:0023:00032fff=00
0:000> db esi
00032fff  00 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  .WWWWWWWWWWWWWWW
0003300f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003301f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003302f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003303f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003304f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003305f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW
0003306f  57 57 57 57 57 57 57 57-57 57 57 57 57 57 57 57  WWWWWWWWWWWWWWWW

The following instruction "fld1" will fail due to that all the registers are in-use.

.text:009EB4C1                 fild    [ebp+arg_C]
.text:009EB4C4                 fst     [ebp+var_1C]
.text:009EB4C7                 fld1				;all the 8 registers are in-use
.text:009EB4C9                 fdivrp  st(1), st
.text:009EB4CB                 fstp    [ebp+var_14]

Readers should note that the above crash we discussed is essentially caused by the wrong use of FPU instructions, such a wrong use may bring many future problems, the above crash - even it looks not quite possible to develop a working exploit - was just one scenario.

Reproduce:
==========
Open the attached "PoC.swf" (the password for the PoC.zip is "adobe_mcafee") you will see the crash. Use your debugger to see what's going on.

## Attachments
No attachments
