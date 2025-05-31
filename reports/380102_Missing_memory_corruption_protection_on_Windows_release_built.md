# Missing memory corruption protection on Windows release built

## Report Details
- **Report ID**: 380102
- **URL**: https://hackerone.com/reports/380102
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-10T08:42:53.966Z
- **Disclosed**: 2020-08-14T06:21:00.937Z

## Reporter
- **Username**: secconsult
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,
we have noticed that the Windows Desktop Client doesn't enable the protections ASLR and DEP (and others). These protections are per-default enabled since approximately 10 years in Visual Studio and are very important because they make exploitation a lot harder (or even make some vulnerabilities not exploitable).

Please note: The Nextcloud code was updated on 4 September 2017 to enable ASLR and DEP. Here is the commit:
https://github.com/nextcloud/desktop/commit/6f270a364895d7f1f0a424c8347cd2913971cca4#diff-95e351a3805a1dafa85bf20b81d086e6

However, the current NextCloud Client (version 2.3.3.1) from 20 November 2017 from revision 57bc79 still doesn't have ASLR and DEP enabled. Here is the revision (where ASLR/DEP is also not enabled in the CMakeLists.txt file:
https://github.com/owncloud/client/commit/57bc7918d7b0650c116f3512787f7677d4e5ab17


Attached is a detailed description of the issue.

## Impact

An attacker has to find an additional vulnerability to exploit the missing memory corruption protections. For example, an attacker can search for a buffer overflow, use-after-free, type-confusion, ... vulnerability in the network communication and send a malicious payload / file from his Nextcloud server.
This vulnerability must not exist in the Nextcloud source code, for example, vulnerabilities in QT or other third-party libraries can also be used. For example, the current Nextcloud version uses QT 5.6.2 which was released on 11-Oct-2016. On 19-Oct-2016 a heap buffer overflow was found in QJsonDocument: https://www.peter.hartmann.tk/single-post/2016/11/29/Fuzzing-Qt-with-libFuzzer

## Attachments
- Nextcloud_MissingProtections.docx
