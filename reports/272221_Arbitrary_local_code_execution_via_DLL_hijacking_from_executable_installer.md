# Arbitrary local code execution via DLL hijacking from executable installer

## Report Details
- **Report ID**: 272221
- **URL**: https://hackerone.com/reports/272221
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-26T20:52:06.482Z
- **Disclosed**: 2018-07-09T21:40:17.213Z

## Reporter
- **Username**: skanthak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

The executable installer BraveSetup-ia32.exe is vulnerable to DLL hijacking: it loads (at least) version.dll from its application directory (which is typically the user's "Downloads" directory %USERPROFILE%\Downloads) instead Windows' system directory %SystemRoot%\System32

## Products affected: 

Windows 7 and newer versions, Brave version 0.18.36

## Steps To Reproduce:

Place the attached version.dll in %USERPROFILE%\Downloads, download the current BraveSetup-ia32.exe and execute it: version.dll displays message boxes showing its caller.

## Supporting Material/References:

See https://skanthak.homepage.t-online.de/sentinel.dll


## Attachments
- VERSION.DLL
