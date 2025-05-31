# DiffieHellman doesn't generate keys after setting a key

## Report Details
- **Report ID**: 1927480
- **URL**: https://hackerone.com/reports/1927480
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-31T13:33:06.125Z
- **Disclosed**: 2023-07-20T20:59:27.162Z

## Reporter
- **Username**: bensmyth
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
DiffieHellman doesn't generate keys after setting a key

## Steps To Reproduce:

  1. Instantiate: `const dh = crypto.createDiffieHellman(1024);`
  2. Set private key: 
```
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));  
```
  3. Generate random private key:
```
//generate random private key
dh.generateKeys();                                 
//outputs 02: zero day.
console.log(dh.getPrivateKey().toString('hex'));   
```

## Underlying issue:

OpenSSL (https://github.com/majek/openssl/blob/master/crypto/dh/dh_key.c) doesn't generate keys when they're already instantiated: 

```
if (dh->priv_key == NULL)
  {
  priv_key=BN_new();
  if (priv_key == NULL) goto err;
  generate_new_key=1;
  }
else
  priv_key=dh->priv_key;

if (dh->pub_key == NULL)
  {
  pub_key=BN_new();
  if (pub_key == NULL) goto err;
  }
else
  pub_key=dh->pub_key;
```

node:crypto should use OpenSSL correctly. Method `generateKeys()` should re-instantiate OpenSSL before requesting a key, thereby avoiding the above.

## Impact

DiffieHellman may be used as the basis for application level security, implications are consequently broad. E.g., key reuse can cause major problems, cryptanalysis may break confidentiality, integrity, ...

## Attachments
No attachments
