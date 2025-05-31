# Inadequate Cryptographic Key Size and Insecure Cryptographic Mode.  File Name :- curl_ntlm_core.c

## Report Details
- **Report ID**: 1113663
- **URL**: https://hackerone.com/reports/1113663
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-03-01T09:37:07.101Z
- **Disclosed**: 2021-03-08T08:24:10.065Z

## Reporter
- **Username**: sanchitcfc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
The application is generating cryptographic keys or key pairs using a short and inadequate length.
This application is using the ECB (Electronic Codebook) mode of operation to perform encryption, which is considered semantically insecure.

Vulnerable File name :- curl_ntlm_core.c
Vulnerable line no. 274 :- err = CCCrypt(kCCEncrypt, kCCAlgorithmDES, kCCOptionECBMode, key,

## Impact

If a message with identical blocks is encrypted, an attacker get a certain advantage to have information on plaintext, by only observing CipherText.

## Attachments
No attachments
