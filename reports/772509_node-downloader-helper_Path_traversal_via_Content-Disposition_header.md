# [node-downloader-helper] Path traversal via Content-Disposition header

## Report Details
- **Report ID**: 772509
- **URL**: https://hackerone.com/reports/772509
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-12T03:06:19.570Z
- **Disclosed**: 2020-11-11T11:59:51.144Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
# Summary

I would like to report path traversal in `node-downloader-helper`.
It allows malicious server to choose download location via `../`. It may leads remote code execution.

# Module

**module name:** `node-downloader-helper`
**version:** 1.0.11
**npm page:** `https://www.npmjs.com/package/node-downloader-helper`

## Module Description

A simple http file downloader for node.js

Features:

- No thirdparty dependecies
- Pause/Resume
- Retry on fail
- Supports http/https
- Supports http redirects
- Supports pipes
- Custom native http request options
- Usable on vanilla nodejs, electron, nwjs
- Progress stats

## Module Stats

13,911 weekly downloads

# Vulnerability

## Vulnerability Description

Since there is no sanitization of file path, malicious server is able to traversal path of victim machine.
It leads remote code execution by putting malicious executable to startup folder in Windows. (In Linux, it's possible to create authorized_key.).

## Steps To Reproduce:

1. Put `poc.php` to the server. (or you can use my server's PoC: https://exec.ga/download-test.php )
2. Modify `poc.js` to set URL of the `poc.php`
3. Execute `node poc.js`
4. `evil.txt` will be saved to parent directory of the directory which contains `poc.js`

## Supporting Material/References:

- Windows 10
- v12.13.1
- 6.12.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Attacker is able to put malicious contents anywhere of victim's machine.

## Attachments
No attachments
