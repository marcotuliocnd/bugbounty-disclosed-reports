# smartlist_add, smartlist_insert (may) cause heap corruption as a result of inadequate checks in smartlist_ensure_capacity

## Report Details
- **Report ID**: 112386
- **URL**: https://hackerone.com/reports/112386
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-01-23T03:33:29.620Z
- **Disclosed**: 2017-10-19T10:16:15.572Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
#Walkthrough of the vulnerability

```smartlist_add``` and ```smartlist_insert``` both invoke ```smartlist_ensure_capacity``` prior adding an element to the list in order to ensure that sufficient memory is available, to ```exit()``` if not enough memory is available and to detect requests for an invalid size:

```c
static INLINE void
smartlist_ensure_capacity(smartlist_t *sl, int size)
{
#if SIZEOF_SIZE_T > SIZEOF_INT
#define MAX_CAPACITY (INT_MAX)
#else
#define MAX_CAPACITY (int)((SIZE_MAX / (sizeof(void*))))
#define ASSERT_CAPACITY
#endif
  if (size > sl->capacity) {
    int higher = sl->capacity;
    if (PREDICT_UNLIKELY(size > MAX_CAPACITY/2)) {
#ifdef ASSERT_CAPACITY
      /* We don't include this assertion when MAX_CAPACITY == INT_MAX,
       * since int size; (size <= INT_MAX) makes analysis tools think we're
       * doing something stupid. */
      tor_assert(size <= MAX_CAPACITY);
#endif
      higher = MAX_CAPACITY;
    } else {
      while (size > higher)
        higher *= 2;
    }
    sl->capacity = higher;
    sl->list = tor_reallocarray(sl->list, sizeof(void*),
                                ((size_t)sl->capacity));
  }
#undef ASSERT_CAPACITY
#undef MAX_CAPACITY
}
```

On a typical 64-bit system, ```SIZEOF_INT``` is 4 and ```SIZEOF_SIZE_T``` is 8. Consequently, ```MAX_CAPACITY``` is ```INT_MAX```, which is 0x7FFFFFFF as can be seen in torint.h:

```c
#ifndef INT_MAX
#if (SIZEOF_INT == 4)
#define INT_MAX 0x7fffffffL
#elif (SIZEOF_INT == 8)
#define INT_MAX 0x7fffffffffffffffL
#else
#error "Can't define INT_MAX"
#endif
#endif
```

So ```MAX_CAPACITY``` is 0x7FFFFFFF. Now assume that that many (0x7FFFFFFF) items have already been added to a smartlist via smartlist_add(sl, value).

smartlist_add() is:

```c
void
smartlist_add(smartlist_t *sl, void *element)
{
  smartlist_ensure_capacity(sl, sl->num_used+1);
  sl->list[sl->num_used++] = element;
}
```

If ```sl->num_used``` is 0x7FFFFFFF prior to invoking ```smartlist_add```, then the next ```smartlist_add``` is effectively:

```c
void
smartlist_add(smartlist_t *sl, void *element)
{
  smartlist_ensure_capacity(sl, -2147483648);
  sl->list[2147483647] = element;
  sl->num_used = -2147483648
}
```

This is the case since we are dealing with a signed 32 bit integer, and 2147483647 + 1 equals -2147483647.

All of the code in ```smartlist_ensure_capacity``` is wrapped inside the following ```if``` block:

```c
  if (size > sl->capacity) {
  }
```

The expression -2147483648 > 2147483647 equals false, thus the code inside the block is not executed.

What actually causes the segmentation fault is that a negative 32 bit integer is used to compute a the location of array index on a 64 bit memory layout, ie., the next call to smartlist_add is effectively:

```c
void
smartlist_add(smartlist_t *sl, void *element)
{
  smartlist_ensure_capacity(sl, -2147483647); // Note that this is effective do-nothing code, as explained above
  sl->list[-2147483648] = element;
  sl->num_used = -2147483647
}
```

#Proof of concept

I've prepared a proof of concept which consists of smartlist_new, smartlist_add, smartlist_ensure_capacity taken from the Tor source code version 0.2.7.6 and their dependencies (tor_*alloc functions etc).

I have made one change to it and that is the size of one element can be configured. In the Tor source code this is void*, which is 8 bytes on a 64 bit system.

I've defined:

```c
#define ELEMENT unsigned char
```

because 2147483647 * 8 bytes = 17179869176 bytes = 16 gigabyte, which I couldn't allocate on my system. ```unsigned int``` works since it only requires 8 gigabytes of memory.

#Discussion

The requirement for 16 gigabytes of memory is considerable.

Triggering the vulnerability obviously also requires some code path which will invoke ```smartlist_add``` or ```smartlist_insert``` upon the same smartlist at the attacker's behest. Moreover, such a code path may have the side effect that it requires a separate allocation for each object that is added to the list; ```smartlist_add``` takes a pointer argument after all -- usually, but not always, this pointer refers to freshly allocated memory. Exceptions to this rule are static strings and pointers to a place in a large string or buffer that was already extant.
Once a vulnerable code path has been discovered, then it ultimately boils down to how much memory a user's machine is able to allocate in order to corrupt the heap.

Despite these constraints, smartlists form a considerable portion of the infrastructure of your code (I count some 380+ occurrences of ```smartlist_add```/```smartlist_insert``` in the .c files using grep, that is excluding the test/ directory) and as such it's probably wise to revise the checks in ```smartlist_ensure_capacity```.



## Attachments
- poc.tar
