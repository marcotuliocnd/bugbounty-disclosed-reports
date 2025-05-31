# 16 instances where return value of OpenSSL i2d_RSAPublicKey is discarded -- might lead to use of uninitialized memory

## Report Details
- **Report ID**: 142773
- **URL**: https://hackerone.com/reports/142773
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-02T23:53:52.293Z
- **Disclosed**: 2017-11-26T13:13:02.150Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
The following functions rely on OpenSSL i2d_RSAPublicKey and do not heed its return value.

```
int crypto_pk_get_all_digests()
    tor-0.2.7.6/src/common/tortls.c:775
        if i2d_RSAPublicKey fails, cert->pkey_digests is all zeroes (cert was allocated with tor_malloc_zero)
int crypto_pk_get_digest()
    tor-0.2.7.6/src/or/connection_or.c:1686
        if i2d_RSAPublicKey fails, digest_rcvd_out is left uninitialized XXX
        (digest_rcvd_out is a stack-based buffer in connection_tls_finish_handshake and is never initialized)
    tor-0.2.7.6/src/or/hibernate.c:552
        if i2d_RSAPublicKey fails, digest is left uninitialized XXX
    tor-0.2.7.6/src/or/rendcommon.c:482
        if i2d_RSAPublicKey fails, service_id is left uninitialized XXX
    tor-0.2.7.6/src/or/rendservice.c:2318
        if i2d_RSAPublicKey fails, key_digest is left uninitialized XXX
    tor-0.2.7.6/src/or/router.c:201
        if i2d_RSAPublicKey fails, server_identitykey_digest is left uninitialized XXX
    tor-0.2.7.6/src/or/router.c:859
        if i2d_RSAPublicKey fails, v3_digest is all zeroes (it was initialized with memset) XXX
    tor-0.2.7.6/src/or/router.c:1019
        if i2d_RSAPublicKey fails, digest is left uninitialized XXX
    tor-0.2.7.6/src/or/routerkeys.c:1070
        if i2d_RSAPublicKey fails, signed_data is left uninitialized XXX
    tor-0.2.7.6/src/or/routerparse.c:5075
        if i2d_RSAPublicKey fails, public_key_hash is left uninitialized XXX
int crypto_pk_get_fingerprint()
    tor-0.2.7.6/src/or/control.c:1737
        if i2d_RSAPublicKey fails, answer is left uninitialized XXX
    tor-0.2.7.6/src/or/dirvote.c:1922
        if i2d_RSAPublicKey fails, fingerprint is left uninitialized XXX
    tor-0.2.7.6/src/or/dirvote.c:1923
        if i2d_RSAPublicKey fails, signing_key_fingerprint is left uninitialized XXX
    tor-0.2.7.6/src/or/dirvote.c:1946
        if i2d_RSAPublicKey fails, signing_key_fingerprint is left uninitialized (or retains its previous data) XXX
int rend_get_service_id()
    tor-0.2.7.6/src/or/directory.c:2138
        if i2d_RSAPublicKey fails, service_id is left uninitialized XXX
    tor-0.2.7.6/src/or/rendservice.c:3250
        if i2d_RSAPublicKey fails, service_id is left uninitialized XXX
```

i2d_RSA_PublicKey does a memory allocation internally and a shortage of allocatable memory will cause it to fail. Like I said in the other report, a repeatedly triggered memory leak by the attacker, or utilizing some way to allocate a large amount of memory, or a "natural" memory shortage on the system caused by another process using large amounts of memory could trigger this.

Here is a proof of concept:

```c
#include <openssl/sha.h>
#include <stdio.h>
#include <stdlib.h>
#include <openssl/rsa.h>

#define tor_assert(x) {if (!(x)) { abort(); }}

struct crypto_pk_t
{
  int refs; /**< reference count, so we don't have to copy keys */
  RSA *key; /**< The key itself */
};
typedef struct crypto_pk_t crypto_pk_t;
int
crypto_digest(char *digest, const char *m, size_t len)
{
  tor_assert(m);
  tor_assert(digest);
  return (SHA1((const unsigned char*)m,len,(unsigned char*)digest) == NULL);
}
int
crypto_pk_get_digest(const crypto_pk_t *pk, char *digest_out)
{
  unsigned char *buf = NULL;
  int len;

  len = i2d_RSAPublicKey((RSA*)pk->key, &buf);
  if (len < 0 || buf == NULL)
    return -1;
  if (crypto_digest(digest_out, (char*)buf, len) < 0) {
    OPENSSL_free(buf);
    return -1;
  }
  OPENSSL_free(buf);
  return 0;
}

#define DIGEST_LEN 20
int main(void)
{
    char _digest[DIGEST_LEN];
    char digest[] = "uninitialized mem..";

    if ( sizeof(_digest) != sizeof(digest) )
    {
        return 0;
    }
    void* ptr = (void*)1;
    int count = 0;
    crypto_pk_t* pk = malloc(sizeof(crypto_pk_t));

    pk->key = RSA_generate_key(1024, 3, 0, 0);

    while ( ptr != 0 )
    {
        ptr = malloc(100);
        count ++;
    }

    printf("allocated 100 * %d bytes\n", count);
    printf("crypto_pk_digest returns: %d\n", crypto_pk_get_digest(pk, digest));

    printf("digest is: %s\n", digest);
    return 0;
}
```

Before you run this, you might want to run this command:

```
ulimit -Sv 500000
```

so that process memory is limited to 500MB (so your whole system doesn't start lagging).

It should output something like this:

```
allocated 100 * 4477420 bytes
crypto_pk_digest returns: -1
digest is: uninitialized mem..
```

In other words, ```digest``` is not touched by ```crypto_pk_digest()``` and retains it original value.

Guido

## Attachments
No attachments
