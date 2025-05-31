# Buffer overflow in libavi_plugin memmove() call

## Report Details
- **Report ID**: 484398
- **URL**: https://hackerone.com/reports/484398
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-23T03:31:55.215Z
- **Disclosed**: 2019-06-12T14:32:59.767Z

## Reporter
- **Username**: retoor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vlc_h1c

## Vulnerability Information
**Summary:** When parsing an invalid AVI  file, a buffer overflow might occur.

**Description:** The ReadFrame function in the avi.c file uses a variable i_width_bytes, which is obtained directly from the file. It is a signed integer. It does not do a strict check before the memory operation(memmove, memcpy), which may cause a buffer overflow.

## Steps To Reproduce:
1.) Open vlc.exe with windbg
2.) F5 makes the program run
3 ) Drag poc files into vlc
4.) Monitor the crash from WinDBG

vlc version 3.0.6 x64
system version win7 x64

More relevant information and poc in the attachment

## Impact

If successful, a malicious third party could trigger an invalid memory access, leading to a crash of the process of the VLC media player. May cause remote code execution.

## Attachments
No attachments
