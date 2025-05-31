# Heap corruption via memarea.c

## Report Details
- **Report ID**: 138025
- **URL**: https://hackerone.com/reports/138025
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-11T20:00:34.272Z
- **Disclosed**: 2017-10-19T10:16:01.417Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hello again,

There is a potential vulnerability in memarea.c.

common/memarea.c:

```c
230 void *
231 memarea_alloc(memarea_t *area, size_t sz)
232 {
233   memarea_chunk_t *chunk = area->first;
234   char *result;
235   tor_assert(chunk);
236   CHECK_SENTINEL(chunk);
237   tor_assert(sz < SIZE_T_CEILING);
238   if (sz == 0)
239     sz = 1;
240   if (chunk->next_mem+sz > chunk->U_MEM+chunk->mem_size) {
```

The vulnerability lies in the addition of a pointer and an integer on line 240:

```c
240   if (chunk->next_mem+sz ...
```
To which address ```chunk->next_mem``` points is not within the application's (tor) purview, since it originates from within malloc() (which is accessed via tor_malloc()) and to some extent the system's kernel memory management), and malloc() is implemented in the libc with which tor was linked.
My point is that no or few assumptions can be made about the virtual address to which chunk->next_mem points.

```sz``` is variable and may be influenced by an external party on the network.

Furthermore, it is guaranteed that ```sz``` is smaller than SIZE_T_CEILING, which is 0x80000000 on 32 bit:

```c
tor_assert(sz < SIZE_T_CEILING);
```

The above predicates imply that 1) given a 32 bit system, where 2) chunk->next_mem happens to point to a virtual address of 0x80000000 or higher and 3) ```sz``` >= ```0x100000000 - chunk->mem_next``` an overflow will occur in the addition of the pointer ```chunk->next_mem+sz```, thus unduly evading this check, which was meant to assert whether is sufficient memory in the current block.

In other words, if chunk->next_mem is 0xA0000000, and memarea_alloc is called to request ```0x60000000``` bytes, then the following will happen:

```c
230 void *
231 memarea_alloc(memarea_t *area, size_t sz)
232 {     
233   memarea_chunk_t *chunk = area->first;
234   char *result;
235   tor_assert(chunk);
236   CHECK_SENTINEL(chunk);
237   tor_assert(sz < SIZE_T_CEILING);
238   if (sz == 0)
239     sz = 1;
240   if (chunk->next_mem+sz > chunk->U_MEM+chunk->mem_size) {
...
...   This code is not executed
...
254   } 
255   result = chunk->next_mem;
256   chunk->next_mem = chunk->next_mem + sz;
```

In this case, line 256 translate to:

```
256   chunk->next_mem = 0xA0000000 + 0x60000000;
```

Eg. ```chunk->next_mem``` now equals 0.

The higher the value of ```chunk->next_mem```, and the higher the maximum value of ```sz``` that a potential attacker can enforce to be allocated, the higher the odds of yielding a ```chunk->next_mem``` value that points to real data (eg. a block of heap memory allocated by tor).

I've used 32 bit in this example. 64 bit is theoretically possible too (SIZE_T_CEILING is larger on 64 bit as well), but less likely.

An easy way to test this is by changing this line in memarea.c alloc_chunk():

```c
res = tor_malloc(chunk_size);
```

to

```c
res = mmap((void*)0xF0000000, chunk_size, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0);
```

(also include ```#include <sys/mman.h>```)

then this code will trigger a segmentation fault

```
  memarea_t *area;
  area = memarea_new();
  char *mem = memarea_alloc(area, 0x10000000);
  memset(mem, 0, 0x10000000);
```

(be aware that this example applies to 32 bit, so compile with ```CFLAGS="-m32"```)

Guido

## Attachments
No attachments
