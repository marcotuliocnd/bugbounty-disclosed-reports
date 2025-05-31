# Potential use-after-free due to struct array_entry_t lacking an explicit copy constructor

## Report Details
- **Report ID**: 511317
- **URL**: https://hackerone.com/reports/511317
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-17T16:55:25.401Z
- **Disclosed**: 2019-05-10T20:02:23.754Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
```struct array_entry_t``` in ```contrib/epee/include/storages/portable_storage_base.h``` does not implement a copy constructor.

Wherever there is code that attempts to copy-construct ```array_entry_t```, the compiler inserts a copy constructor for ```array_entry_t``` that merely copies over the values.

The struct possesses an iterator (```mutable typename entry_container<t_entry_type>::type::const_iterator m_it```) which is copied over by the implicit copy constructor (inserted ad-hoc by the compiler).

This leads to a situation where ```m_it``` points to a different ```m_array_entry```. If that ```m_array_entry``` is deleted, then dereferencing ```m_it``` constitutes a use-after-free bug.

```cpp
#include <storages/portable_storage_base.h>

int main(void)
{
    /* Construct the first array_entry_t */
    auto ae = new epee::serialization::array_entry_t<uint64_t>;

    /* Insert two values */
    ae->insert_first_val(111);
    ae->insert_next_value(999);

    /* Moves the iterator from the first element to the second element. */
    ae->get_first_val();
    /* The iterator is now at the value 999 */

    /* Construct a new array_entry_t using the one already created.
     * Invokes the copy constructor.
     */
    auto ae2 = new epee::serialization::array_entry_t<uint64_t>(*ae);

    /* Delete the first array_entry_t */
    delete ae;

    /* ae2.m_it now still points to the array of the first array_entry_t,
     * but that array was deleted in the statement above, so dereferencing it
     * will be a use after free.
     *
     * Let's try:
     */

    auto res = ae2->get_next_val();
    if ( res != nullptr ) {
        /* Dereferencing freed pointer (use after free) */
        printf("%zu\n", *res);
    }

    delete ae2;

    return 0;
}
```

Compile (from the monero source root path):

```
clang++ -g -I contrib/epee/include/ poc.cpp -fsanitize=address
```

Note that the implicit copy constructor is in fact called when serialization is performed using ```epee::serialization::portable_storage::load_from_binary```.
However, I haven't observed an actual use-after-free, hence 'low' severity for this report.
In my opinion it is nonetheless something that ought to be addressed because future code dealing with ```array_entry_t``` and its methods could inadvertently lead to use-after-free.

Patch:
```
From da7c7fe3766777eadd058a4682de5527bc5f5904 Mon Sep 17 00:00:00 2001
From: Guido Vranken <guidovranken@gmail.com>
Date: Sun, 17 Mar 2019 17:39:37 +0100
Subject: [PATCH] Implement array_entry_t copy constructor

Manually initialize the array_entry_t iterator to ensure it points
to the correct m_array, thereby preventing a potential use-after-free
situation.

Signed-off-by: Guido Vranken <guidovranken@gmail.com>
---
 contrib/epee/include/storages/portable_storage_base.h | 1 +
 1 file changed, 1 insertion(+)

diff --git a/contrib/epee/include/storages/portable_storage_base.h b/contrib/epee/include/storages/portable_storage_base.h
index da84fd8e..ca7c81dd 100644
--- a/contrib/epee/include/storages/portable_storage_base.h
+++ b/contrib/epee/include/storages/portable_storage_base.h
@@ -82,6 +82,7 @@ namespace epee
     struct array_entry_t
     {
       array_entry_t():m_it(m_array.end()){}        
+      array_entry_t(const array_entry_t& other):m_array(other.m_array), m_it(m_array.end()){}
 
       const t_entry_type* get_first_val() const 
       {
-- 
2.17.1


```

## Impact

Use-after-free; information disclosure, RCE

## Attachments
No attachments
