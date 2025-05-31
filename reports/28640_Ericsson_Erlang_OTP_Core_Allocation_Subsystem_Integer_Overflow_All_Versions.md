# Ericsson Erlang OTP Core Allocation Subsystem Integer Overflow (All Versions)

## Report Details
- **Report ID**: 28640
- **URL**: https://hackerone.com/reports/28640
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-09-19T20:01:50.377Z
- **Disclosed**: 2019-11-12T23:47:42.687Z

## Reporter
- **Username**: donb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
#############################################################################
#
# Lab Mouse Security Report 
# LMS-2014-06-23-7
#

Report ID: LMS-2014-06-23-7
Report Code Name: EARLGREY.1

Researcher Name: Don A. Bailey
Researcher Organization: Lab Mouse Security
Researcher Email: donb@securitymouse.com
Researcher Website: www.securitymouse.com

Vulnerability Status: Patched
Vulnerability Embargo: Successful

Vulnerability Class: Integer Overflow
Vulnerability Effect: Memory Corruption
Vulnerability Impact: DoS, OOW, RCE
Vulnerability DoS Practicality: Practical
Vulnerability OOW Practicality: Practical
Vulnerability RCE Practicality: Impractical
Vulnerability Criticality: Moderate

Vulnerability Scope:
---------------------
All versions of Erlang OTP are vulnerable. 

Criticality Reasoning
---------------------
While Erlang OTP is vulnerable to an integer overflow condition in several
object allocation functions, triggering the vulnerability remotely is 
difficult. A software engineer would need to build an application that
exposes certain aspects of the Erlang OTP through an API, or a protocol that
triggers these issues. 

Because triggering these issues remotely will largely result in Denial of
Service, it is unlikely that RCE can occur without significant effort on
behalf of an attacker. 

Therefore, while RCE is possible, and probable on certain architectures,
it is impractical from the context of the average attacker. This vulnerability 
must be exploited by highly skilled individuals with extensive memory 
management and software architecture backgrounds. 

However, older versions of Erlang will be more subject to exploitation due
to the widespread use of Erlang in telecommunications environments on
widespread 32bit embedded systems. Where these systems are concerned,
remote attacks will not be subject to ASLR, NX, or other security enhancements
that would normally make exploitation improbable. Therefore, systems that fit 
this classification must be evaluated for their potential security impact. 

This decreases the priority of this vulnerability from High to Moderate. 

It is also notable that this subtle vulnerability would need to be exploited
in very specialized scenarios, primarily in circumstances where
 - a driver/NIF poorly uses the allocation API (see the Erlang LZ4 NIF)
 - a 32bit architecture is used
 - memory pressure results in small adjacent heap chunks 

Vulnerability Description
-------------------------
An integer overflow occurs in all alloc and realloc functions in the file
erts/emulator/beam/erl_binary.h
	- erts_bin_drv_alloc_fnf
	- erts_bin_drv_alloc
	- erts_bin_nrml_alloc
	- erts_bin_realloc_fnf
	- erts_bin_realloc

The vulnerability occurs whenever the CHICKEN_PAD is used:
erts_bin_drv_alloc_fnf(Uint size)
{
    Uint bsize = ERTS_SIZEOF_Binary(size) + CHICKEN_PAD;

The macro ERTS_SIZEOF_Binary adds 'size' to the size of the internal structure
'Binary'. Then, CHICKEN_PAD is added to this value. Integer overflow can occur
in either the macro or the addition of the CHICKEN_PAD if 'size' is a large
integer. 

When erts_alloc() is called in subsequent code, the memory chunk requested will
be too small to store an entire ErtsBinary structure. 

In certain cases it is possible to corrupt memory in interesting ways. For
example, with crypto:rand_bytes() the user can specify a mask to be set in
the first and last byte of the generated array. 

On 32bit systems, we can pass a sufficiently large size to rand_bytes_3. If we
make the value large enough to trigger the integer overflow, the mask 
functionality can be used to overwrite the 'flags' field in the 'Binary' 
structure. If this field is set to BIN_FLAG_MAGIC, the Binary will be 
interpreted as an ErtsMagicBinary. 

When this object is freed by the garbage collector, the ErtsMagicBinary's
'destructor' function will be called. Since an ErtsBinary is a C union of
the 'Binary' structure and the 'ErtsMagicBinary' structure, the first four
bytes (or eight, on 64bit platforms) of the random data will be interpreted
as the destructor. 

The garbage collector will unwittingly call the destructor when freeing up
memory. This results in code execution on platforms where memory can be
allocated at very low addresses. It is notable that on modern systems, this
attack can rarely succeed.

In the example below, an integer overflow is used to force a '1' to be 
written to the 'flags' variable of the Binary structure. The value '27' is
written to the random data array, but is later interpreted as a function
address, causing Erlang to crash.

donb@debian:~$ erl
Erlang R15B01 (erts-5.9.1) [source] [async-threads:0] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1> crypto:rand_bytes(16#FFFFFFF1, 1, 27).
Segmentation fault (core dumped)
donb@debian:~$ gdb -q /usr/lib/erlang/erts-5.9.1/bin/beam core
Reading symbols from /usr/lib/erlang/erts-5.9.1/bin/beam...(no debugging 
symbols found)...done.
[New LWP 22034]

warning: Can't read pathname for load map: Input/output error.
[Thread debugging using libthread_db enabled]
Using host libthread_db library 
"/lib/i386-linux-gnu/i686/cmov/libthread_db.so.1".
Core was generated by `/usr/lib/erlang/erts-5.9.1/bin/beam -- -root 
/usr/lib/erlang -progname erl -- -'.
Program terminated with signal 11, Segmentation fault.
#0  0x0000001b in ?? ()
(gdb) i r eip
eip            0x1b     0x1b
(gdb) 


Vulnerability Resolution
------------------------
To resolve this issue, simply check for integer overflow in the 
ERTS_SIZEOF_Binary macro and after adding the CHICKEN_PAD macro. This will
disable attackers from abusing this functions throughout the distribution.

Update - September 18th, 2014
----------------------------------------------
Ericsson has released an updated version of Erlang OTP (17.3) that addresses this issue. Please update to the latest OTP as soon as possible. 

## Attachments
No attachments
