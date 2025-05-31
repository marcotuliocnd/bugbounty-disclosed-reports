#  Assertion `len == 1' failed, process aborted while streaming ouput from remote server

## Report Details
- **Report ID**: 495508
- **URL**: https://hackerone.com/reports/495508
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-13T19:43:04.061Z
- **Disclosed**: 2019-11-03T16:39:11.399Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: putty_h1c

## Vulnerability Information
**Summary:** 
During the course of testing putty-0.70-2019-02-12.75dda5e on Fedora 29 compiled with clang version 7.0.1 (Fedora 7.0.1-1.fc29), we discovered it was possible to abort a remote client by streaming data at it in such a way as to trigger an assertion failure. 

```
putty: unix/gtkwin.c:3801: void do_text_internal(GtkFrontend *, int, int, wchar_t *, int, unsigned long, int, truecolour): Assertion `len == 1' failed.
Aborted (core dumped)
```

**Description:** 
An assertion is a statement that a predicate (Boolean-valued function, i.e. a true–false expression) is always true at that point in code execution. It can help a programmer read the code, help a compiler compile it, or help the program detect its own defects.   

## Steps To Reproduce:
1. Download PuTTY snapshot
2. Compile with Clang
3. Launch PuTTY with your favorite debugger.
4. Connection to remote host
5. On remote host:
`mkdir corpus && git clone https://gitlab.com/akihe/radamsa.git && cd radamsa && make && sudo make install && cd ~`
6. On remote host, upload the attached files to the corpus directory we created in step 4.
7. On remote host type `while true; radamsa -s 420 -o - -n inf corpus/*; done` and let run until crashes.

## Supporting Material/References:

A sample screenshot taken while fuzzing PuTTY:
{F423359}

I've also attached the core dump that happened at the time of the crash.

## Impact

Denial of service, crash, loss of data contained in scroll back

## Attachments
- Screenshot_2019-02-13_13-27-15.png
- core.putty.9952.gz
