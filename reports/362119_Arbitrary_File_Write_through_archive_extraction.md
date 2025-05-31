# Arbitrary File Write through archive extraction

## Report Details
- **Report ID**: 362119
- **URL**: https://hackerone.com/reports/362119
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-05T16:01:18.154Z
- **Disclosed**: 2018-08-12T14:50:55.133Z

## Reporter
- **Username**: danny_grander
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report arbitrary file write vulnerability in adm-zip module
It allows attackers to write arbitrary files when a malicious archive is extracted.
More info here: 
https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability#affected-libraries


# Module

**module name:** unzipper
**version:** <0.8.13
**npm page:** `https://www.npmjs.com/package/unzipper`

## Module Description
This is a fork of node-unzip which has not been maintained in a while. This fork addresses the following issues:
* finish/close events are not always triggered, particular when the input stream is slower than the receivers
* Any files are buffered into memory before passing on to entry


## Module Stats

80k downloads in the last week

# Vulnerability

## Vulnerability Description
The vulnerability is a form of directory traversal that can be exploited by extracting files from an archive. The premise of the directory traversal vulnerability is that an attacker can gain access to parts of the file system outside of the target folder in which they should reside. The attacker can then overwrite executable files and either invoke them remotely or wait for the system or user to call them, thus achieving remote command execution on the victim’s machine. The vulnerability can also cause damage by overwriting configuration files or other sensitive resources, and can be exploited on both client (user) machines and servers.

More info here: 
https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability


## Steps To Reproduce:

Sample files can be found here: https://github.com/snyk/zip-slip-vulnerability/tree/master/archives


## Patch

Vulnerability is already fixed in ver 0.8.13
We opened a fix PR on 16th of April, https://github.com/ZJONSSON/node-unzipper/pull/59

CVE id for the vuln was assigned: CVE-2018-1002203

## Supporting Material/References:

There are multiple libraries affected, across different ecosystems. 
Full list here: https://github.com/snyk/zip-slip-vulnerability#affected-libraries

https://snyk.io/research/zip-slip-vulnerability
https://github.com/snyk/zip-slip-vulnerability

# Wrap up

- I contacted the maintainer to let them know: Y, and helped fix the issue
- I opened an issue in the related repository: N

## Impact

Arbitrary file write

## Attachments
No attachments
