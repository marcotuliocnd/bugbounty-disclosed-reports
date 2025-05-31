# HTTP MitM on Flash Player settings manager allows attacker to set sandbox settings

## Report Details
- **Report ID**: 54094
- **URL**: https://hackerone.com/reports/54094
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-03-31T20:55:29.703Z
- **Disclosed**: 2018-12-23T21:09:32.056Z

## Reporter
- **Username**: sardarox1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This vulnerability is present in both Google Chrome's PepperFlash aswell as browsers
with the NPAPI Flash Player versions.

It works by MITM'ing the Flashplayer settings manager.
Although this settings manager is served over HTTPS, it is still
possible to place or edit the local settings cookie by serving it over
HTTP over the corresponding path. 

This leads to the attacker being able to edit several sandbox settings, for example, the attacker can:
  -Give the domain/payload permanent access to webcam/microphone,
  -Permanently exempt the domain/payload from any CORS Policy restrictions
  -Effectively disable auto updates (NPAPI versions) by setting the auto-update interval to ~9999 days

For this, an attacker would only need access to the HTTP communication
of the victims network. Either embedding the remote SWF in the attackers own site, or injecting the embed code in other HTTP traffic from the victim.

The POC was peformed against Google Chrome 41.0.2272.101 (PPAPI 17.0.0.134) on Windows 8.1
MITMProxy (https://mitmproxy.org/) was used to serve the altered SWF (Without using HTTPS/Certificate modes).

This attack is demonstrated in this video: https://www.youtube.com/watch?v=2Q52q_kZtTc (unlisted)

This issue is reported to Adobe, I am currently awaiting a response from their PSIRT.

## Attachments
- poc.zip
