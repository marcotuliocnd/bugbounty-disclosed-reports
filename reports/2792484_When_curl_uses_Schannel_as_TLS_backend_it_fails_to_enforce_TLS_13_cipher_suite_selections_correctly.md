# When curl uses Schannel as TLS backend, it fails to enforce TLS 1.3 cipher suite selections correctly

## Report Details
- **Report ID**: 2792484
- **URL**: https://hackerone.com/reports/2792484
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-18T21:29:32.159Z
- **Disclosed**: 2024-11-04T22:11:58.739Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:

The curl doc page "SSL Ciphers" (https://curl.se/docs/ssl-ciphers.html) says: "Setting TLS 1.3 cipher suites is supported by curl with [...] Schannel (curl 7.85.0+)." But I find that when curl uses Schannel as its TLS backend, it incorrectly enforces the TLS 1.3 cipher suites selection. For example, if I run `curl.exe --tlsv1.3 --tls13-ciphers TLS_AES_128_GCM_SHA256 -v https://example.com`, curl still accepts cipher suite TLS_AES_256_GCM_SHA384.

I choose "Medium" severity because this bug affects the Windows 11 built-in curl (C:\Windows\System32\curl.exe), and thus many batch scripts that invoke curl might be affected. If some TLS 1.3 cipher suites are found to be vulnerable in the future, this bug can give users harder time to disable such insecure TLS 1.3 cipher suites in curl.

## Steps To Reproduce:

  1. Build curl on Windows with Schannel as its TLS backend (I used `nmake /f Makefile.vc mode=static VC=22 ENABLE_SCHANNEL=yes ENABLE_UNICODE=yes` to build curl). You can also repro with Windows 11 built-in curl.exe at `C:\Windows\System32\curl.exe`
  1. Open WireShark. Capture traffic, and set filter to show traffic to example.com only
  1. Run `curl.exe --tlsv1.3 --tls13-ciphers TLS_AES_128_GCM_SHA256 -v https://example.com`
  1. View the TLS handshakes in WireShark. You can see that the Server Hello message shows it uses TLS_AES_256_GCM_SHA384.

Reproducible on these curl versions:
1. The current Windows 11 built-in curl:
```
C:\Windows\System32>curl.exe -V
curl 8.9.1 (Windows) libcurl/8.9.1 Schannel zlib/1.3 WinIDN
Release-Date: 2024-07-31
Protocols: dict file ftp ftps http https imap imaps ipfs ipns mqtt pop3 pop3s smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM SPNEGO SSL SSPI threadsafe Unicode UnixSockets
```

2. curl built from the source on GitHub. Version 8.11.0-DEV. Commit e29629a402a32e1eb92c0d8af9a3a49712df4cfb
```
curl 8.11.0-DEV (x86_64-pc-win32) libcurl/8.11.0-DEV Schannel WinIDN
Release-Date: [unreleased]
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtsp smb smbs smtp smtps telnet tftp ws wss
Features: alt-svc AsynchDNS HSTS HTTPS-proxy IDN IPv6 Kerberos Largefile NTLM SPNEGO SSL SSPI threadsafe UnixSockets
```

## Supporting Material/References:

  * https://curl.se/docs/ssl-ciphers.html

## Impact

When users specify `--tls13-ciphers` parameter, curl silently uses a TLS 1.3 cipher suite that is not selected by users. This can cause TLS connections use weak cipher suites. If in the future `TLS_AES_256_GCM_SHA384` becomes weak or broken, and users want to use `TLS_AES_128_GCM_SHA256` (or vice versa), curl can potentially leak data to man-in-the-middle attackers, because curl uses the wrong cipher.

## Attachments
No attachments
