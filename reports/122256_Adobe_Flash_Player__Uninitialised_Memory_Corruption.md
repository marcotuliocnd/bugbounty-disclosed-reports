# Adobe Flash Player  Uninitialised Memory Corruption

## Report Details
- **Report ID**: 122256
- **URL**: https://hackerone.com/reports/122256
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-11T04:19:30.194Z
- **Disclosed**: 2019-11-12T09:42:53.153Z

## Reporter
- **Username**: riusksk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
##Description
---------------
A Uninitialised Memory Corruption exist in Adobe Flash Player SA for Mac (test in v20.0.0.228 sa version)，successful exploitation could cause a crash and potentially allow an attacker to take control of the affected system. 

##Environment
---------------
1、Mac OSX 10.11.2
2、flashplayer20_0d0_228_mac_sa

##Details
---------------

valgrind --tool=memcheck /Users/riusksk/Downloads/Flash\ Player.app/Contents/MacOS/Flash\ Player poc.swf    

==3453== Memcheck, a memory error detector

==3453== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.

==3453== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info

==3453== Command: /Users/riusksk/Downloads/Flash\ Player.app/Contents/MacOS/Flash\ Player poc.swf

==3453== 

==3453== Conditional jump or move depends on uninitialised value(s)

==3453==    at 0x7FFF5FC24A27: bcmp (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC11914: ImageLoaderMachO::validateFirstPages(linkedit_data_command const*, int, unsigned char const*, unsigned long, long long, ImageLoader::LinkContext const&) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC16B8A: ImageLoaderMachOCompressed::instantiateFromFile(char const*, int, unsigned char const*, unsigned long, unsigned long long, unsigned long long, stat const&, unsigned int, unsigned int, linkedit_data_command const*, encryption_info_command const*, ImageLoader::LinkContext const&) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC10A7E: ImageLoaderMachO::instantiateFromFile(char const*, int, unsigned char const*, unsigned long long, unsigned long long, stat const&, ImageLoader::LinkContext const&) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC038C2: dyld::loadPhase6(int, stat const&, char const*, dyld::LoadContext const&) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC0846D: dyld::loadPhase5(char const*, char const*, dyld::LoadContext const&, std::__1::vector<char const*, std::__1::allocator<char const*> >*) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC0818D: dyld::loadPhase4(char const*, char const*, dyld::LoadContext const&, std::__1::vector<char const*, std::__1::allocator<char const*> >*) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC07EF2: dyld::loadPhase3(char const*, char const*, dyld::LoadContext const&, std::__1::vector<char const*, std::__1::allocator<char const*> >*) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC07647: dyld::loadPhase1(char const*, char const*, dyld::LoadContext const&, std::__1::vector<char const*, std::__1::allocator<char const*> >*) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC0347A: dyld::loadPhase0(char const*, char const*, dyld::LoadContext const&, std::__1::vector<char const*, std::__1::allocator<char const*> >*) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC0315E: dyld::load(char const*, dyld::LoadContext const&) (in /usr/lib/dyld)

==3453==    by 0x7FFF5FC0870A: dyld::libraryLocator(char const*, bool, char const*, ImageLoader::RPathChain const*) (in /usr/lib/dyld)

==3453== 

==3453== Use of uninitialised value of size 8


lldb Flash\ Player

(lldb) target create "Flash Player"

warning: (x86_64) /Users/riusksk/Downloads/Flash Player.app/Contents/MacOS/Flash Player empty dSYM file detected, dSYM was created with an executable with no debug info.

Current executable set to 'Flash Player' (x86_64).

(lldb) run ~/Downloads/poc.swf

Process 96650 launched: '/Users/riusksk/Downloads/Flash Player.app/Contents/MacOS/Flash Player' (x86_64)

Vector smash protection is enabled.

Process 96650 stopped

* thread #1: tid = 0xbbffa, 0x00007fff82cc0b4f CoreFoundation`CFStringGetLength + 15, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)

frame #0: 0x00007fff82cc0b4f CoreFoundation`CFStringGetLength + 15

CoreFoundation`CFStringGetLength:

->  0x7fff82cc0b4f <+15>: movq   (%rbx), %rax

0x7fff82cc0b52 <+18>: testq  %rax, %rax

0x7fff82cc0b55 <+21>: je     0x7fff82cc0b97            ; <+87>

0x7fff82cc0b57 <+23>: leaq   -0xff65e76(%rip), %rcx    ; __CFConstantStringClassReferencePtr

(lldb) bt

* thread #1: tid = 0xbbffa, 0x00007fff82cc0b4f CoreFoundation`CFStringGetLength + 15, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x0)

* frame #0: 0x00007fff82cc0b4f CoreFoundation`CFStringGetLength + 15

frame #1: 0x00007fff82df89cc CoreFoundation`_CFURLCreateWithFileSystemPath + 60

frame #2: 0x000000010040d204 Flash Player`main + 165412

frame #3: 0x0000000100394bb4 Flash Player`___lldb_unnamed_function14212$$Flash Player + 356

frame #4: 0x00000001004053e8 Flash Player`main + 133128

frame #5: 0x000000010040563e Flash Player`main + 133726

frame #6: 0x000000010039630a Flash Player`___lldb_unnamed_function14228$$Flash Player + 10

frame #7: 0x00000001001032fd Flash Player`___lldb_unnamed_function2712$$Flash Player + 13

frame #8: 0x000000010034863c Flash Player`___lldb_unnamed_function12938$$Flash Player + 844

frame #9: 0x000000010034824c Flash Player`___lldb_unnamed_function12937$$Flash Player + 764

frame #10: 0x0000000100342843 Flash Player`___lldb_unnamed_function12890$$Flash Player + 1203

frame #11: 0x00000001003421ef Flash Player`___lldb_unnamed_function12888$$Flash Player + 559

frame #12: 0x00000001002fd32c Flash Player`___lldb_unnamed_function12368$$Flash Player + 540

frame #13: 0x0000000100301438 Flash Player`___lldb_unnamed_function12395$$Flash Player + 968

frame #14: 0x0000000100302447 Flash Player`___lldb_unnamed_function12397$$Flash Player + 1527

frame #15: 0x0000000100309957 Flash Player`___lldb_unnamed_function12454$$Flash Player + 535

frame #16: 0x0000000100308e12 Flash Player`___lldb_unnamed_function12453$$Flash Player + 770

frame #17: 0x0000000100350dc3 Flash Player`___lldb_unnamed_function12977$$Flash Player + 371

frame #18: 0x000000010039702a Flash Player`___lldb_unnamed_function14247$$Flash Player + 138

frame #19: 0x0000000100405546 Flash Player`main + 133478

frame #20: 0x000000010040563e Flash Player`main + 133726

frame #21: 0x000000010039630a Flash Player`___lldb_unnamed_function14228$$Flash Player + 10

frame #22: 0x00000001001032fd Flash Player`___lldb_unnamed_function2712$$Flash Player + 13

frame #23: 0x000000010034863c Flash Player`___lldb_unnamed_function12938$$Flash Player + 844

frame #24: 0x00000001003489b4 Flash Player`___lldb_unnamed_function12939$$Flash Player + 436

frame #25: 0x00000001003e2499 Flash Player`___lldb_unnamed_function15719$$Flash Player + 1145

frame #26: 0x00000001003e29ee Flash Player`___lldb_unnamed_function15722$$Flash Player + 46

frame #27: 0x00007fff8c0fb2c4 AppKit`-[NSApplication _doOpenFile:ok:tryTemp:] + 315

frame #28: 0x00007fff8bd26775 AppKit`-[NSApplication finishLaunching] + 1557

frame #29: 0x00007fff8bd25e05 AppKit`-[NSApplication run] + 231

frame #30: 0x00007fff8bca8520 AppKit`NSApplicationMain + 1176

frame #31: 0x0000000100001784 Flash Player`___lldb_unnamed_function1$$Flash Player + 52

##Reference
riusksk of Tencent Security Platform Department (CVE-2016-0992):
https://helpx.adobe.com/security/products/flash-player/apsb16-08.html





## Attachments
- poc.swf
