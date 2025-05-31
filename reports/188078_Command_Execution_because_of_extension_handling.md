# Command Execution because of extension handling

## Report Details
- **Report ID**: 188078
- **URL**: https://hackerone.com/reports/188078
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-12-03T20:49:12.765Z
- **Disclosed**: 2017-08-10T05:10:31.716Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information

## Summary:

Hello,

Using this bug an attacker can execute commands as the current user using brave & gain complete shell capabilities (and all possibilities associated) 

## Details:

The issue is in the way the application handles website TLDs. typically in windows, `.com` represents an application, much similar like `.exe` - when Brave saves a website (Ctrl+S) - it uses the name of the website.

For PoC purpose I used `.bat` TLDs because they are much easier to show a poc with instead of binary application garbage data. 

So Assume a user visits http://paulos.bat with the contents of:
```js
@echo off
calc
```

And saves the page, this will save the website as `paulos.bat` - which when executed - actually opens batch and executes calculator.

## Bypassing Mitigations

In Windows, Microsoft warns users when they execute applications that are downloaded, this can simply be bypassed by sending filenames with words like `Update` or `Setup`... yeah, I can't believe this works too.

So say a user visits `https://malicioussetup.com` and saves the site - note this site changed its contents from whatever it was to binary-garbage & microsoft will allow executing it - eventually causing code execution.

This is clearly a chain of low priority issues that cause command execution. :) (POC 

## Products affected: 

 * Tested in Latest Brave Windows (I suspect OSX, iOS & Android may also be affected)

## Recommended Fix:

 Add .html/htm to the index page (/index.html) to mitigate this easily

## Supporting Material/References:

  * POC image attached
  * POC video (Private): https://youtu.be/ret4pJArYSU

I think you should fix this ASAP! as anyone can register `.com` sites to abuse it.

Thanks,
Paulos

## Attachments
- win7poc.JPG
