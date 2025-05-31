# [dy-server2] - stored Cross-Site Scripting

## Report Details
- **Report ID**: 796487
- **URL**: https://hackerone.com/reports/796487
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-14T08:08:58.486Z
- **Disclosed**: 2021-01-14T08:38:10.770Z

## Reporter
- **Username**: tuo4n8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report [Stored XSS] in [dy-server2]
It allows to steal session cookies, deface web , execute anything code javascript

# Module

**module name:** dy-server2
**version:** dy-server2
**npm page:** `https://www.npmjs.com/package/dy-server2`

## Module Description

> 这是一款轻量级http服务器，可用于文件传输，前端项目预览。

## Module Stats

> Replace stats below with numbers from npm’s module page:

[1] weekly downloads : 16

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

## Steps To Reproduce:
1. Instal package from npm : ``npm i -g dy-server2``   
2. Create folder or file with name : ``<img src=x onerror=alert(1)>``
3. Start server : ``dy-server2 -p 8888``
4. Open web and code execute

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

## Patch

> If you're able to provide a patch with the fix please post it in this section

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION] : Ubuntu
- [NODEJS VERSION] : 12.11.1
- [NPM VERSION] : 6.11.3
- [BROWSERS VERSIONS, IF APPLICABLE] : Firefox

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N]  : N
- I opened an issue in the related repository: [Y/N]  : N

> Hunter's comments and funny memes goes here

## Impact

Stored XSS allows an attacker to embed a malicious script into a vulnerable page, which is then executed when a victim views the page.

## Attachments
- 1.jpg
- 2.jpg
- 3.jpg
