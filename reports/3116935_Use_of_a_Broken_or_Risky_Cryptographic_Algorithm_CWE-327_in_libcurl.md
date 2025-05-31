# Use of a Broken or Risky Cryptographic Algorithm (CWE-327) in libcurl

## Report Details
- **Report ID**: 3116935
- **URL**: https://hackerone.com/reports/3116935
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2025-04-29T07:42:35.722Z
- **Disclosed**: 2025-04-29T21:16:05.238Z

## Reporter
- **Username**: tannicarcher
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
The DES cipher (Data Encryption Standard) is used in the `curl_ntlm_core.c` file of libcurl. DES is considered insecure due to its short key length (56 bits) and its susceptibility to brute-force attacks. Modern cryptographic standards recommend replacing DES with AES (Advanced Encryption Standard), which is more robust and secure.

## Affected version
[Which curl/libcurl version are you using to reproduce? On which platform? `curl -V` typically generates good output to include]

## Steps To Reproduce:
1. Inspect the `lib/curl_ntlm_core.c` file of the libcurl source code.
2. Locate the use of the `kCCAlgorithmDES` constant, which corresponds to the DES cipher.
3. Verify that DES is being used for cryptographic operations in NTLM authentication (NTLMv1).
## Supporting Material/References:
- File: `lib/curl_ntlm_core.c`
- Line Reference: 228:29
- CWE Reference: [CWE-327](https://cwe.mitre.org/data/definitions/327.html)

  * [attachment / reference]

## Impact

## Summary:
Using DES compromises the security of the application due to the following points:
- **Brute-force attacks**: The short key length makes it possible to brute-force DES keys in a reasonable amount of time with modern hardware.
- **Cryptographic weaknesses**: DES is vulnerable to various cryptanalysis techniques, such as differential and linear cryptanalysis.
- **Compliance risks**: DES does not meet modern cryptographic standards and could lead to non-compliance with security regulations.

An attacker exploiting this vulnerability could:
- Intercept and decrypt sensitive data during NTLM authentication.
- Execute man-in-the-middle (MITM) attacks to impersonate a user or server.
- Gain unauthorized access to systems relying on NTLM authentication.

---

## Recommended Fix:
Replace the use of `kCCAlgorithmDES` with `kCCAlgorithmAES`, which supports stronger encryption standards (e.g., AES-128, AES-256). This change will significantly enhance the security of NTLM authentication in libcurl.

## Attachments
No attachments
