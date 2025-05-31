# Access Violation Reading in libfaad_plugin

## Report Details
- **Report ID**: 502816
- **URL**: https://hackerone.com/reports/502816
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-27T14:45:14.362Z
- **Disclosed**: 2019-07-24T00:20:01.699Z

## Reporter
- **Username**: biewuxz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vlc_h1c

## Vulnerability Information
1	Basic info of application
1.1	Info of application
Application Name	VLC media player for Windows
Application Version	4.0.0-dev Otto Chriek
Download Address	http://nightlies.videolan.org/
Testing OS	Windows 8

2	Info of test file
2.1	Test file info
Normal file name	normal.mkv
Normal file type	MKV(Matroska file)
Normal file MD5	A24F0AE656C72CA4E6FBFC0DAC4E59B8
Crash file name	crash.mkv
Crash file type	MKV(Matroska file)
Crash file MD5	E509565096CEB61B9D5088FA80CD7775

2.2	Crash file info
Replace a piece of data padding, from offset 0x14c5 to offset 0x1528, the comparison of two files: 
diff.png.
Description of crash file:
Using MKVToolNix tool to parse the crash file, the mutation data triggering crash is located at:
Segment->Cluster->Simple Block->Frame section.
The Track Number equal to 2, indicating that this SimpleBlock is audio. And matroska does not have a detailed description of the mutated Frame data. (https://www.matroska.org/technical/specs/index.html#simpleblock_structure)。
 See the file: block.png, block_data.png.

3	Info of test
3.1	Description of test
Run VLC media player, try to play crash.mkv file, program crash and an error pop-up. 
3.2	Description of debug
Loading VLC debugging with WinDbg, below is the debug info and stack backtrace.
The key point to crash may be: libfaad_plugin!vlc_entry_license__4_0_3+0xd4f4. Total debug log:  x64dug_info.txt.

main input debug: `file:///C:/softs/crash.mkv' successfully opened
lua art finder debug: Trying Lua playlist script C:\Program Files\VideoLAN\VLC\lua\meta\art\02_frenchtv.luac
(290.b60): Access violation - code c0000005 (first chance)
First chance exceptions are reported before any exception handling.
This exception may be expected and handled.
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Program Files\VideoLAN\VLC\plugins\codec\libfaad_plugin.dll - 
libfaad_plugin!vlc_entry_license__4_0_3+0xd4f4:
000007ff`46780604 440fb64803      movzx   r9d,byte ptr [rax+3] ds:00000000`51551003=??
0:029> kP
Child-SP          RetAddr           Call Site
00000000`5da995b0 000007ff`4677743d libfaad_plugin!vlc_entry_license__4_0_3+0xd4f4
00000000`5da995d0 000007ff`46779301 libfaad_plugin!vlc_entry_license__4_0_3+0x432d
00000000`5da99620 000007ff`467797dc libfaad_plugin!vlc_entry_license__4_0_3+0x61f1
00000000`5da996e0 000007ff`46779b06 libfaad_plugin!vlc_entry_license__4_0_3+0x66cc
00000000`5da9f930 000007ff`46779f27 libfaad_plugin!vlc_entry_license__4_0_3+0x69f6
00000000`5da9f990 000007ff`467733a5 libfaad_plugin!vlc_entry_license__4_0_3+0x6e17
00000000`5da9fa10 000007ff`4677437a libfaad_plugin!vlc_entry_license__4_0_3+0x295
00000000`5da9faf0 000007ff`46771b62 libfaad_plugin!vlc_entry_license__4_0_3+0x126a
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Program Files\VideoLAN\VLC\libvlccore.dll - 
00000000`5da9fb30 000007ff`4da3ca94 libfaad_plugin+0x1b62
00000000`5da9fcc0 000007ff`4da3c888 libvlccore!input_Control+0x34a4
00000000`5da9fd10 000007ff`4da3cc94 libvlccore!input_Control+0x3298
00000000`5da9fdd0 000007ff`4daaacf6 libvlccore!input_Control+0x36a4
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Windows\system32\msvcrt.dll - 
00000000`5da9fec0 000007ff`59d8707b libvlccore!vlc_rand_bytes+0xa46
00000000`5da9ff00 000007ff`59da5e6d msvcrt!isspace+0x5b
*** ERROR: Symbol file could not be found.  Defaulted to export symbols for C:\Windows\system32\KERNEL32.DLL - 
00000000`5da9ff30 000007ff`58e9167e msvcrt!beginthreadex+0x13d
00000000`5da9ff60 000007ff`5ba3c3f1 KERNEL32!BaseThreadInitThunk+0x1a
00000000`5da9ff90 00000000`00000000 ntdll!RtlUserThreadStart+0x21

4	File list
4.1	File list
Normal file:  normal.mkv
Crash file: crash.mkv
comparison of two files: diff.png
MKVToolNix:  block.png, block_data.png
Whole Windbg log:  x64dug_info.txt


All the files, logs and pictures are in the attchment, and the decompression password is：vL(@Vr#Bwx2&

## Impact

This is not just a simple crash, it's possible to read memory data.

## Attachments
- Access_Violation_Reading.rar
