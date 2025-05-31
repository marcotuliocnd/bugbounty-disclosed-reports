# Signed integer overflow in tool_progress_cb()

## Report Details
- **Report ID**: 591770
- **URL**: https://hackerone.com/reports/591770
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-05-28T18:58:13.144Z
- **Disclosed**: 2019-10-04T20:58:05.194Z

## Reporter
- **Username**: geeknik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Good afternoon curl security! I built this curl from commit 8144ba38c383718355d8af2ed8330414edcbbc83. We discovered a signed integer overflow in tool_progress_cb().

## Steps To Reproduce:
Compiled with the Undefined Behavior Sanitizer enabled. Ran with the following command line:
`./curl -q -# -T- -C- file:///dev/null`

## Supporting Material/References:
```
tool_cb_prg.c:129:22: runtime error: signed integer overflow: 9223372036854775807 - -1 cannot be represented in type 'long'
    #0 0x42fc40 in tool_progress_cb /root/curl/src/tool_cb_prg.c:129:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737
    #7 0x47fbb6 in operate_do /root/curl/src/tool_operate.c:1604:20
    #8 0x46a606 in operate /root/curl/src/tool_operate.c:2098:20
    #9 0x469176 in main /root/curl/src/tool_main.c:326:14
    #10 0x7f9199d682e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #11 0x409fe9 in _start (/root/curl/src/curl+0x409fe9)

tool_cb_prg.c:135:22: runtime error: signed integer overflow: 9223372036854775807 - -1 cannot be represented in type 'long'
    #0 0x42fe09 in tool_progress_cb /root/curl/src/tool_cb_prg.c:135:22
    #1 0x562090 in Curl_pgrsUpdate /root/curl/lib/progress.c:484:16
    #2 0x4d3da1 in multi_runsingle /root/curl/lib/multi.c:2009:29
    #3 0x4cce1b in curl_multi_perform /root/curl/lib/multi.c:2066:14
    #4 0x4a7740 in easy_transfer /root/curl/lib/easy.c:624:15
    #5 0x4a7740 in easy_perform /root/curl/lib/easy.c:718
    #6 0x4a7740 in curl_easy_perform /root/curl/lib/easy.c:737
    #7 0x47fbb6 in operate_do /root/curl/src/tool_operate.c:1604:20
    #8 0x46a606 in operate /root/curl/src/tool_operate.c:2098:20
    #9 0x469176 in main /root/curl/src/tool_main.c:326:14
    #10 0x7f9199d682e0 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x202e0)
    #11 0x409fe9 in _start (/root/curl/src/curl+0x409fe9)

######################################################################################################################################################################################################################################################### 100.0%

```

## Impact

An integer overflow or wraparound occurs when an integer value is incremented to a value that is too large to store in the associated representation. When this occurs, the value may wrap to become a very small or negative number. While this may be intended behavior in circumstances that rely on wrapping, it can have security consequences if the wrap is unexpected. This is especially the case if the integer overflow can be triggered using user-supplied inputs. This becomes security-critical when the result is used to control looping, make a security decision, or determine the offset or size in behaviors such as memory allocation, copying, concatenation, etc.

## Attachments
No attachments
