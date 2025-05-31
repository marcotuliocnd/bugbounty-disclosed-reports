# Download of (later executed) .NET installer over insecure channel

## Report Details
- **Report ID**: 272231
- **URL**: https://hackerone.com/reports/272231
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-26T21:47:39.145Z
- **Disclosed**: 2018-07-09T21:37:45.155Z

## Reporter
- **Username**: skanthak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

Execution of file NDP-KB2901954-Web.exe fetched via http://go.microsoft.com/fwlink/?LinkId=397707

On Windows installations without .NET Framework 4.5.2 or later, the executable installers BraveSetup-x64.exeand BraveSetup-ia32.exe offer to download and install this component.
They but start the download from http://go.microsoft.com/fwlink/?LinkId=397707 (redirected to http://download.microsoft.com/download/9/A/7/9A78F13F-FD62-4F6D-AB6B-1803508A9F56/51209.34209.03/web/NDP452-KB2901954-Web.exe), i.e. over an insecure channel: a MITM can intercept both HTTP requests and deliver an arbitrary executable.

## Products affected: 

All versions of Windows without .NET Framework 4.5.2 or newer

## Steps To Reproduce:
Run the executable installer

## Supporting Material/References:

See https://insights.sei.cmu.edu/cert/2017/06/the-consequences-of-insecure-software-updates.html


## Attachments
No attachments
