# Incorrect GC behavior in xxlimited could lead to use-after-free

## Report Details
- **Report ID**: 203002
- **URL**: https://hackerone.com/reports/203002
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-02T19:33:06.151Z
- **Disclosed**: 2019-11-12T09:01:08.444Z

## Reporter
- **Username**: zeroinside
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Issue submitted: http://bugs.python.org/issue29398
xxlimited module exist only in Python3.6 compiled on Linux.


Starting program: /usr/bin/python3.6 xlimited.py
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff73d73f5 in PyArena_Malloc () from /usr/lib/libpython3.6m.so.1.0
(gdb) info reg
rax            0x2000000000000000       2305843009213693952
rbx            0x4141414141414141       4702111234474983745
rcx            0xe      14
rdx            0x0      0
rsi            0x10     16
rdi            0x7ffff7f812a0   140737353618080
rbp            0x7ffff7f812a0   0x7ffff7f812a0
rsp            0x7fffffffd8d0   0x7fffffffd8d0
r8             0x10e    270
r9             0x2      2
r10            0x2      2
r11            0x122a0  74400
r12            0x1      1
r13            0x7ffff7f812a0   140737353618080
r14            0x7fffffffda40   140737488345664
r15            0x7ffff7f28558   140737353254232
rip            0x7ffff73d73f5   0x7ffff73d73f5 <PyArena_Malloc+21>
eflags         0x10202  [ IF RF ]
cs             0x33     51
ss             0x2b     43
ds             0x0      0
es             0x0      0
fs             0x0      0
gs             0x0      0
(gdb) 

As presented above, PoC gives good control on RBX passed in PyArena_Malloc() function. Payload is limited to ASCII characters, because of exec() origin. In other variants, PoC leads to double-free. 




## Attachments
- xlimited.py
