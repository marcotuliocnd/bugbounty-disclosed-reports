# [wappalyzer] ReDoS allows an attacker to completely break Wappalyzer

## Report Details
- **Report ID**: 888021
- **URL**: https://hackerone.com/reports/888021
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-31T19:35:19.899Z
- **Disclosed**: 2020-06-18T18:01:28.187Z

## Reporter
- **Username**: vrechson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report [VULNERABILITY] in [MODULE]
It allows [DESCRIBE THE IMPACT OF THE VULNERABILITY - E.G READ ARBITRARY FILES, READ DATA FROM DATABASE ETC]

# Module

**module name:** `Wappalyzer`
**version:** 6.0.2
**npm page:** `https://www.npmjs.com/package/wappalyzer`

## Module Description

> Wappalyzer identifies technologies on websites.

## Module Stats

> Weekly downloads: 1,290
> 88 issues
> 16 pull requests
> last publish: 3 days ago

# Vulnerability

ReDoS  (Catastrophic backtracking)

## Vulnerability Description
> An attacker can make wappalyzer (all drivers, like browser extension and cli) stop working due to ReDoS in one of it's services regex . 

## Steps To Reproduce:

1. Create a web page with the following tag:
`<script src='//c.c..j..c.c..j..c.c..j..c.c..j..c.c..j..c.c..j..c.c..j..c.c..j..jskhtlcnipmos.cdnjs.cdnjs.dnjs.cdnjs.cloudflar.jsjs.cloudf'></script>`
2. Now open this page using wappalyzer extension in browser or it's cli
3. Wappalyzer will stop answering and it's CPU percentage will start to  increase to high levels

## Patch

 In order to test this issue, you can see that the problem resides in this line https://github.com/AliasIO/wappalyzer/blob/master/src/apps.json#L11644 of wappalyzer application. When this regex test the input shown, it takes process the application indefinitely, making it stop working. Running it in browser extension completely crash the extension in all tabs, and in cli/node version the execution takes forever.

To patch this issue, the current regex must be changed to a more restrict one in this piece: `(?:[^\\/]+\\.)*`

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- OS: Archlinux -  Linux 5.6.13-arch1-1 #1 SMP PREEMPT Thu, 14 May 2020 06:52:53 +0000 x86_64 GNU/Linux
- Node version: v12.16.3
- NPM version: 6.14.5
- Firefox: 76.0.1 (64-bit) - Mozilla Firefox for Arch Linux - archlinux - 1.0
- ReScuE was used to test for ReDoS (https://github.com/2bdenny/ReScue)

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker can make wappalyzer stop working in it's pages, or pages in which he has injection and make user CPU starts to throttle

## Attachments
- poc.html
