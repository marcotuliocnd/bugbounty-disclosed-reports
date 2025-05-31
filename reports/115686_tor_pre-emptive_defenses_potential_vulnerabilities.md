# [tor] pre-emptive defenses, potential vulnerabilities

## Report Details
- **Report ID**: 115686
- **URL**: https://hackerone.com/reports/115686
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-10T12:02:55.218Z
- **Disclosed**: 2017-11-26T13:14:04.234Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Replacing all ```tor_malloc``` calls with tor_calloc and ```tor_malloc_zero```
==============================================================

Zeroing memory upon allocating it will prevent vulnerabilities that consist of transmitting data buffers which are not wholly initialized with the intended data (or contain remnants of previous contents).

Pseudocode:
```c
char* outbuffer = tor_malloc(100);
memcpy(outbuffer, inbuffer, i);
send(outbuffer);
```

If ```i``` is the result of a calculation whose outcome is _presumed_ to align with the outbuffer's size (100), but in practice is prone to a corner-case where the result is in fact less than 100, then whatever uninitialized memory is present in the allocated heap memory will be transmitted to the other party.

But if you're using ```tor_malloc_zero``` instead, then the uninitialized memory would simply consist of zeroes, and thus useless for a malicious recipient of the buffer.

```tor_calloc``` is like ```tor_malloc_zero``` in that it zeroes the allocated memory before disclosing it to the invoking function, and moreover has the property of accepting two size_t parameters and verifying whether the product (result of multiplication) is prone to an overflow, and fails if it is. Therefore, it is ideal to use as a substitute for manual multiplication in preparation for a ```tor_malloc``` or ```tor_malloc_zero```:

```c
tor_malloc(n * sizeof(some_struct_t));
```

In instances such as this, it is again _presumed_ that the product of ```n``` and the ```sizeof``` cannot result in an overflow. Even when this is fairly obvious, I'd say there is no reason to delegate the multiplication to ```tor_calloc``` that offers a hard guarantee that the multiplication is safe. As your code grows, and the value of ```n``` starts hinging on factors that may not be immediately obvious, or if fields are added to some_struct_t in order to cater to future requirements, overflows may become a reality without the protection that ```tor_calloc``` offers.

Potential heap corruption via ```write_escaped_data``` in control.c
==============================================================
/** Given a <b>len</b>-character string in <b>data</b>, made of lines
 * terminated by CRLF, allocate a new string in *<b>out</b>, and copy the
 * contents of <b>data</b> into *<b>out</b>, adding a period before any period
 * that appears at the start of a line, and adding a period-CRLF line at
 * the end. Replace all LF characters sequences with CRLF.  Return the number
 * of bytes in *<b>out</b>.
 */
STATIC size_t
write_escaped_data(const char *data, size_t len, char **out)
{
  size_t sz_out = len+8;
  char *outp;
  const char *start = data, *end;
  int i;
  int start_of_line;
  for (i=0; i<(int)len; ++i) {
    if (data[i]== '\n')
      sz_out += 2; /* Maybe add a CR; maybe add a dot. */
  }
  *out = outp = tor_malloc(sz_out+1);
  end = data+len;
  start_of_line = 1;
  while (data < end) {
    if (*data == '\n') {
      if (data > start && data[-1] != '\r')
        *outp++ = '\r';
      start_of_line = 1;
    } else if (*data == '.') {
      if (start_of_line) {
        start_of_line = 0;
        *outp++ = '.';
      }
    } else {
      start_of_line = 0;
    }
    *outp++ = *data++;
  }
  if (outp < *out+2 || fast_memcmp(outp-2, "\r\n", 2)) {
    *outp++ = '\r';
    *outp++ = '\n';
  }
  *outp++ = '.';
  *outp++ = '\r';
  *outp++ = '\n';
  *outp = '\0'; /* NUL-terminate just in case. */
  tor_assert((outp - *out) <= (int)sz_out);
  return outp - *out;
}

There are two potential vulnerabilities lurking here:

1. If the input size (```len```) >= 0x80000000, then this loop will not execute at all:
        
```c
  for (i=0; i<(int)len; ++i) {
    if (data[i]== '\n')
      sz_out += 2; /* Maybe add a CR; maybe add a dot. */
  }
```

Because the condition ```i<(int)len``` is effectively ```i<(negative number)``` and ```i``` is intialized to 0, this can never be true. As a result of this, the output buffer (whose size is based on sz_out) is too small to hold the result for an input buffer containing '\n' characters.
Triggering this is typically only feasible on a 64-bit system, because if the input buffer is >= 0x80000000 bytes, then sz_out is set to 0x80000008 bytes, and allocating such an amount twice (one for the input buffer, and one for the output buffer) is not possible on a 32-bit system.

2. If the equation (number of '\n' characters in input buffer * 2 + size of input buffer) exceeds 0xFFFFFFFF, then this will cause heap corruption on a 32-bit system, because sz_out overflows.

See my attached proof of concept. Compile and execute like this:

```c
gcc -fsanitize=address -fomit-frame-pointer write_escaped_data.c; ./a.out 1
gcc -m32 -fsanitize=address -fomit-frame-pointer write_escaped_data.c; ./a.out 2
```

As for real exploitability, I spent some effort on creating a real, remote proof of concept for this, but because the data that write_escaped_data may process is the result a multitude of (to me) intricate processes it is hard to come up with a reliable attack.

```write_escaped_data``` draws data from all the getinfo_helper_* functions (via ```handle_control_getinfo``` and ```handle_getinfo_helper```) as well as the amalgate of many potentially many, reasonably large strings in ```control_event_networkstatus_changed_helper```: 

```c
  SMARTLIST_FOREACH(statuses, const routerstatus_t *, rs,
    {
      s = networkstatus_getinfo_helper_single(rs);
      if (!s) continue;
      smartlist_add(strs, s);
    });

  s = smartlist_join_strings(strs, "", 0, NULL);
  write_escaped_data(s, strlen(s), &esc);
```

base64_decode potential heap corruption on 32-bit systems
==============================================================
```c
int
base64_decode(char *dest, size_t destlen, const char *src, size_t srclen)
{
...
...
  if (destlen < (srclen*3)/4)
    return -1;
  if (destlen > SIZE_T_CEILING)
    return -1;
```

The problem here is that the multiplication (by 3) occurs before the division (by 4).

For source strings larger than 0xFFFFFFFF / 3 == 0x55555555, an overflow will occur within this calculation. If the result of the overflow-affected calculation is smaller than what ```destlen``` is, then this check will be passed and memory will be corrupted.

See my proof of concept:

```
$ gcc -m32 -fsanitize=address -fomit-frame-pointer base64_decode.c; ./a.out 
=================================================================
==32449== ERROR: AddressSanitizer: stack-buffer-overflow on address 0xfff6fe04 at pc 0x804898b bp 0xfff6fcf8 sp 0xfff6fcec
...
...
```

Potential heap corruption in do_getpass in routerkeys.c
==============================================================
At present this cannot be triggered, but, unless this code was designed like this on purpose and you're aware of the weakness, you might want to revisit it.

```do_getpass``` contains this code:
```c
  if (twice) {
    const char msg[] = "One more time:";
    size_t p2len = strlen(prompt) + 1;
    if (p2len < sizeof(msg))
      p2len = sizeof(msg);
    prompt2 = tor_malloc(strlen(prompt)+1);
    memset(prompt2, ' ', p2len);
    memcpy(prompt2 + p2len - sizeof(msg), msg, sizeof(msg));

    buf2 = tor_malloc_zero(buflen);
  }
```

There is only one call to this function in the code for which twice == 1:

```code
  if (do_getpass("Enter new passphrase:", pwbuf0, sizeof(pwbuf0), 1,
                 get_options()) < 0) {
    log_warn(LD_OR, "NO/failed passphrase");
    return -1;
  }
```

This will not trigger a memory corruption, but if the first parameter had been shorter, it would:

Compile and run like this:

```
$ gcc -fomit-frame-pointer -fsanitize=address do_getpass.c 
$ ./a.out "Enter new passphrase:"
$ ./a.out "Enter new passphrase"
$ ./a.out "Enter new passphras"
$ ./a.out "Enter new passphra"
$ ./a.out "Enter new passphr"
$ ./a.out "Enter new passph"
$ ./a.out "Enter new passp"
$ ./a.out "Enter new pass"
$ ./a.out "Enter new pas"

==7883== ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60040000dffe at pc 0x400c0a bp 0x7fff8d9c22e0 sp 0x7fff8d9c22d8
...
...
```

So it's not really a vulnerability at present, but I thought I'd mention it to you since it struck me as odd and it could become a problem if you pass a dynamic, potentially short string (for ex. created with snprintf) to do_getpass.

## Attachments
- do_getpass.c
- base64_decode.c
- write_escaped_data.c
