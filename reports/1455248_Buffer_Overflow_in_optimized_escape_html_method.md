# Buffer Overflow in optimized_escape_html method

## Report Details
- **Report ID**: 1455248
- **URL**: https://hackerone.com/reports/1455248
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-20T13:37:51.348Z
- **Disclosed**: 2022-01-22T14:03:33.908Z

## Reporter
- **Username**: chamal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
* This report is a copy of bug report (https://hackerone.com/reports/1328463).
     I was asked to submit this bug here, because Ruby bug bounty program is moved to this new Internet Bug Bounty program.

Operating System
================
Windows 10
*This should reproduce in any other operating system where `long` data type takes 4 bytes.*

Description
==========

This bug is present in `optimized_escape_html` method of [ext\cgi\escape\escape.c](https://github.com/ruby/ruby/blob/master/ext/cgi/escape/escape.c) file.
Below mentioned line causes this bug.
```cpp
char *buf = ALLOCV_N(char, vbuf, RSTRING_LEN(str) * HTML_ESCAPE_MAX_LEN);
```

`RSTRING_LEN` is a preprocessor directive. It expands to below code.
```cpp
static inline long
RSTRING_LEN(VALUE str)
{
    return rbimpl_rstring_getmem(str).as.heap.len;
}
```
`HTML_ESCAPE_MAX_LEN` is defined as this.
``` cpp
#define HTML_ESCAPE_MAX_LEN 6
```
 

Note that `RSTRING_LEN` returns a `long` data type value.
`Long` data type takes 4 bytes on Windows operating system.
So maximum value for a unsigned `long` data type is 4,294,967,295.

Attached test case passes a string, which has 715828054 characters to `CGI.escapeHTML` method.
Length of the buffer is calculated as -> `RSTRING_LEN(str) * HTML_ESCAPE_MAX_LEN`
                                                                                            715828054 * 6 = 4,294,968,324
This value is too large for `long` data type. 
So 4,294,968,324 becomes 1028, when stored in a `long` variable.
So `ALLOCV_N` method creates a buffer of 1028 bytes.

`optimized_escape_html` method contains a loop, which writes to this buffer.
```cpp
    const char *cstr = RSTRING_PTR(str);
    const char *end = cstr + RSTRING_LEN(str);
    char *dest = buf;
    while (cstr < end) {
        const unsigned char c = *cstr++;
        uint8_t len = html_escape_table[c].len;
        if (len) {
            memcpy(dest, html_escape_table[c].str, len);
            dest += len;
        }
        else {
            *dest++ = c;
        }
    }
```
	
This loops expects a buffer of size 4,294,968,324. But it receives a buffer with 1028 bytes.
So this loop writes data, beyond provided buffer.

Reproduction Steps
================
1. Download attached F1585929 file.
2. Run
     `ruby escape.rb`. 
    *Please attach to a debugger to notice the crash.*

## Impact

Attacker may be able to write unintended data to memory.

## Attachments
- escape.rb
- escapeStack.rb
