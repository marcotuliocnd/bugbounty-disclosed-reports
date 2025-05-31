# Array Index Underflow--http rpc

## Report Details
- **Report ID**: 825091
- **URL**: https://hackerone.com/reports/825091
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-20T07:40:45.783Z
- **Disclosed**: 2021-10-11T20:35:12.885Z

## Reporter
- **Username**: minerscan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
## Summary:
parserse_base_utils.h:197
const unsigned char tmp = isx[(int)*++it];
Int type will cause the array subscript to appear negative and read wrong data, 
Solution:
const unsigned char tmp = isx[(unsigned char)*++it];

## Releases Affected:

  * up to date version on github
## Steps To Reproduce:
[add details for how we can reproduce the issue]

\#include <iostream>
\#include "serialization/keyvalue_serialization.h"
\#include "storages/portable_storage_template_helper.h"
\#include "storages/portable_storage_base.h"

\#ifdef __cplusplus
extern "C"
\#endif
int LLVMFuzzerTestOneInput(const char *data, size_t size) {
  std::string s(data,size);
  try
  {
    epee::serialization::portable_storage ps;
    ps.load_from_json(s);
  }
  catch (const std::exception &e)
  {
    std::cerr << "Failed to load from binary: " << e.what() << std::endl;
    return 1;
  }
  return 0;
}

## Supporting Material/References:

  * seed file attached

## Impact

1.crash
2.leaking of sensitive info

## Attachments
- fuzz_seed
