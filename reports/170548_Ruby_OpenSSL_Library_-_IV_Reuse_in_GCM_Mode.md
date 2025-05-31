# Ruby OpenSSL Library - IV Reuse in GCM Mode

## Report Details
- **Report ID**: 170548
- **URL**: https://hackerone.com/reports/170548
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-19T21:05:58.161Z
- **Disclosed**: 2021-03-07T11:46:51.786Z

## Reporter
- **Username**: offftherecord
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hello,

An IV reuse bug was discovered in Ruby's OpenSSL library when using
aes-gcm. When encrypting data with aes-*-gcm, if the IV is set before
setting the key, the cipher will default to using a static IV. This creates
a static nonce and since aes-gcm is a stream cipher, this can lead to known
cryptographic issues.

The documentation does not appear to specify the order of operations when
setting the key and IV [1]. As an example, see the following insecure code
snippet below:

Vulnerable Code:
```
def encrypt(plaintext)
    cipher = OpenSSL::Cipher.new('aes-256-gcm')
    iv = cipher.random_iv # Notice here the IV is set before the key
    cipher.key = '11111111111111111111111111111111'
    cipher.auth_data = ""
    ciphertext = cipher.update(plaintext) + cipher.final
    tag = cipher.auth_tag

    puts "[+] Encrypting: #{plaintext}"
    puts "[+] CipherMessage (IV | Tag | Ciphertext): #{bin2hex(iv)} |
#{bin2hex(tag)} | #{bin2hex(ciphertext)}"
end
```
A developer that uses the code above may incorrectly assume that their code
is secure from the pitfalls associated with IV reuse in aes-*-gcm, since
the ‘cipher.random_iv’ method is used. According to the documentation, this
should generate a random IV each time the encryption method is called.

When the code above is run with the same key and same plaintext message,
the following results are obtained:

Output:
```
# Run 1
./gcm_encrypt.rb 'This is some secret message.'
[+] Encrypting: This is some secret message.
[+] CipherMessage (IV | Tag | Ciphertext): e32594080cca2b37f7d7e968 |
8c676db7551cf046266252ee776ecaa9 | 81092d16b62902d9985656253891dc
800a5bb48fb1c4ad0b7bdf6054
```
```
# Run 2
./gcm_encrypt.rb 'This is some secret message.'
[+] Encrypting: This is some secret message.
[+] CipherMessage (IV | Tag | Ciphertext): 431d70714f5e5f876d1c7830 |
8c676db7551cf046266252ee776ecaa9 | 81092d16b62902d9985656253891dc
800a5bb48fb1c4ad0b7bdf6054
```
Notice that in the output above a unique IV is returned for both runs, but
with the same ciphertext. This proves that even though the random_iv method
is called, the code is defaulting to a static IV. If an attacker can
retrieve multiple ciphertext messages, it is possible to decrypt the
ciphertexts by applying the same attack one would use in a two-time pad
(XOR ciphertexts and crib drag).

Next review the following code snippet and output, which depicts a secure
implementation of the code:

Valid Code:
```
def encrypt(plaintext)
    cipher = OpenSSL::Cipher.new('aes-256-gcm')
    cipher.key = '11111111111111111111111111111111'
    iv = cipher.random_iv # Notice here the IV is set after the key
    cipher.auth_data = ""
    ciphertext = cipher.update(plaintext) + cipher.final
    tag = cipher.auth_tag

    puts "[+] Encrypting: #{plaintext}"
    puts "[+] CipherMessage (IV | Tag | Ciphertext): #{bin2hex(iv)} |
#{bin2hex(tag)} | #{bin2hex(ciphertext)}"
end
```
Output:
```
# Run 1
./gcm_encrypt.rb 'This is some secret message.'
[+] Encrypting: This is some secret message.
[+] CipherMessage (IV | Tag | Ciphertext): 8beb4aa05533e90f4f4eddd3 |
ea1b015958a9b8bd2aafa61887309caf | 19574a9c9869b92140a57a5fd43a14
9a5eaa7e5beefdff5d56cc4136
```
```
# Run 2
./gcm_encrypt.rb 'This is some secret message.'
[+] Encrypting: This is some secret message.
[+] CipherMessage (IV | Tag | Ciphertext): 87361b3f1e32291602ac7b40 |
bce7093daa10cc9d2fad0f2b91e077f2 | 47f9a5ba55631204233ace70f169e6
65846e877dca11a6e13a659540
```
Notice that this time both the IV and ciphertexts are both different for
the same plaintext. This is the intended result a developer would expect to
happen when using this library.

Reference:
[1] https://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/Cipher.html#class-OpenSSL::Cipher-label-Authenticated+Encryption+and+Associated+Data+-28AEAD-29

## Attachments
No attachments
