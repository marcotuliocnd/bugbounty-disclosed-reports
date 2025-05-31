# potential memory corruption in or/buffers.c (particularly on 32 bit)

## Report Details
- **Report ID**: 163459
- **URL**: https://hackerone.com/reports/163459
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T01:06:27.016Z
- **Disclosed**: 2017-10-19T10:15:23.431Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
In ```or/buffer.s.c```:
```c
/** Return the allocation size we'd like to use to hold <b>target</b>
 * bytes. */
static inline size_t
preferred_chunk_size(size_t target)
{
  size_t sz = MIN_CHUNK_ALLOC;
  while (CHUNK_SIZE_WITH_ALLOC(sz) < target) {
    sz <<= 1;
  }
  return sz;
}
```

```c
#define MIN_CHUNK_ALLOC 256
#define CHUNK_SIZE_WITH_ALLOC(memlen) ((memlen) - CHUNK_HEADER_LEN)
```

CHUNK_HEADER_LEN is usually around 30 bytes or so.

The problem with ```preferred_chunk_size``` is that for a large ```size_t target```, the function will return 0.

If you compile this program with ```-m32```:

```c
#include <stdio.h>
#include <stdint.h>
#define FLEXIBLE_ARRAY_MEMBER /**/
#define DEBUG_CHUNK_ALLOC
/** A single chunk on a buffer. */
typedef struct chunk_t {
  struct chunk_t *next; /**< The next chunk on the buffer. */
  size_t datalen; /**< The number of bytes stored in this chunk */
  size_t memlen; /**< The number of usable bytes of storage in <b>mem</b>. */
#ifdef DEBUG_CHUNK_ALLOC
  size_t DBG_alloc;
#endif
  char *data; /**< A pointer to the first byte of data stored in <b>mem</b>. */
  uint32_t inserted_time; /**< Timestamp in truncated ms since epoch
                           * when this chunk was inserted. */
  char mem[FLEXIBLE_ARRAY_MEMBER]; /**< The actual memory used for storage in
                * this chunk. */
} chunk_t;
#if defined(__GNUC__) && __GNUC__ > 3
#define STRUCT_OFFSET(tp, member) __builtin_offsetof(tp, member)
#else
 #define STRUCT_OFFSET(tp, member) \
   ((off_t) (((char*)&((tp*)0)->member)-(char*)0))
#endif
#define MIN_CHUNK_ALLOC 256
#define CHUNK_HEADER_LEN STRUCT_OFFSET(chunk_t, mem[0])
#define CHUNK_SIZE_WITH_ALLOC(memlen) ((memlen) - CHUNK_HEADER_LEN)
static inline size_t
preferred_chunk_size(size_t target)
{
  size_t sz = MIN_CHUNK_ALLOC;
  while (CHUNK_SIZE_WITH_ALLOC(sz) < target) {
    sz <<= 1;
  }
  return sz;
}

int main(void)
{
    size_t i = 1024;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    printf("i is %08X, preferred_chunk_size is %08X\n", i, preferred_chunk_size(i)); i <<= 1;
    return 0;
}
```

the output is:

```
i is 00000400, preferred_chunk_size is 00000800
i is 00000800, preferred_chunk_size is 00001000
i is 00001000, preferred_chunk_size is 00002000
i is 00002000, preferred_chunk_size is 00004000
i is 00004000, preferred_chunk_size is 00008000
i is 00008000, preferred_chunk_size is 00010000
i is 00010000, preferred_chunk_size is 00020000
i is 00020000, preferred_chunk_size is 00040000
i is 00040000, preferred_chunk_size is 00080000
i is 00080000, preferred_chunk_size is 00100000
i is 00100000, preferred_chunk_size is 00200000
i is 00200000, preferred_chunk_size is 00400000
i is 00400000, preferred_chunk_size is 00800000
i is 00800000, preferred_chunk_size is 01000000
i is 01000000, preferred_chunk_size is 02000000
i is 02000000, preferred_chunk_size is 04000000
i is 04000000, preferred_chunk_size is 08000000
i is 08000000, preferred_chunk_size is 10000000
i is 10000000, preferred_chunk_size is 20000000
i is 20000000, preferred_chunk_size is 40000000
i is 40000000, preferred_chunk_size is 80000000
i is 80000000, preferred_chunk_size is 00000000
```

The danger is that the return value of ```preferred_chunk_size``` is always used as a parameter to ```tor_malloc``` or ```tor_realloc```. It is called at these places:

In ```buf_pullup```:
```c
 210     newsize = CHUNK_SIZE_WITH_ALLOC(preferred_chunk_size(capacity));
 211     newhead = chunk_grow(buf->head, newsize);
```

In ```buf_new_with_capacity```:
```c
 283 /** Create and return a new buf with default chunk capacity <b>size</b>.
 284  */
 285 buf_t *
 286 buf_new_with_capacity(size_t size)
 287 {
 288   buf_t *b = buf_new();
 289   b->default_chunk_size = preferred_chunk_size(size);
 290   return b;
 291 }
```

In ```buf_add_chunk_with_capacity```:
```c
 401 /** Append a new chunk with enough capacity to hold <b>capacity</b> bytes to
 402  * the tail of <b>buf</b>.  If <b>capped</b>, don't allocate a chunk bigger
 403  * than MAX_CHUNK_ALLOC. */
 404 static chunk_t *
 405 buf_add_chunk_with_capacity(buf_t *buf, size_t capacity, int capped)
 406 {
 407   chunk_t *chunk;
 408 
 409   if (CHUNK_ALLOC_SIZE(capacity) < buf->default_chunk_size) {
 410     chunk = chunk_new_with_alloc_size(buf->default_chunk_size);
 411   } else if (capped && CHUNK_ALLOC_SIZE(capacity) > MAX_CHUNK_ALLOC) {
 412     chunk = chunk_new_with_alloc_size(MAX_CHUNK_ALLOC);
 413   } else {
 414     chunk = chunk_new_with_alloc_size(preferred_chunk_size(capacity));
 415   }
```

```buf_new_with_capacity``` is currently called nowhere except for tests.
```buf_add_chunk_with_capacity``` is called at various places but currently not with the ```capped``` parameter set to 0.

However, ```buf_pullup``` is called at various places and the call to ```preferred_chunk_size``` is reachable. Whether it is reachable with a parameter large enough that it will return 0 I'm not sure about.

```c
int
tor_main(int argc, char *argv[])
{
    buf_t* buf;
    char* string;
    size_t string_len;
    size_t i;

    buf = buf_new();
    string_len = 0x00001000;
    string = tor_malloc(string_len);
    for (i = 0; i < 507904; i++)
    {
        write_to_buf(string, string_len, buf);
    }
    write_to_buf(string, 0x3FFFFFA, buf);
    free(string);
    buf_pullup(buf, 0x90000000); 
}
```

What will happen is that ```buf_pullup``` will call ```chunk_grow```
```c
 140 static inline chunk_t *
 141 chunk_grow(chunk_t *chunk, size_t sz)
 142 {
 143   off_t offset;
 144   size_t memlen_orig = chunk->memlen;
 145   tor_assert(sz > chunk->memlen);
 146   offset = chunk->data - chunk->mem;
 147   chunk = tor_realloc(chunk, CHUNK_ALLOC_SIZE(sz));
 148   chunk->memlen = sz;
 149   chunk->data = chunk->mem + offset;
```

```tor_realloc``` will in effect be called with a size parameter of 0. Whether and how much legitimate heap memory ```realloc``` will allocate might be implementation-dependent. The point is that the following lines might overwrite heap memory:

```c
 148   chunk->memlen = sz;
 149   chunk->data = chunk->mem + offset;
```

since ```chunk``` is a memory area that has just been allocated to 0 (or 1, after correction) bytes.

The whole scenario is not very likely considering Tor's frugal memory consumption but it is nonetheless a programming fault in the buffers "API" that could lead to stability issues. Especially if you ever expand the use of ```buf_pullup```, ```buf_new_with_capacity```, and/or uncapped ```buf_add_chunk_with_capacity```, it'll be wise to hard-limit the amounts of right-shifts in ```preferred_chunk_size``` (a single unintended negative integer -> size_t can be conducive in establishing an exploitation path).

## Attachments
No attachments
