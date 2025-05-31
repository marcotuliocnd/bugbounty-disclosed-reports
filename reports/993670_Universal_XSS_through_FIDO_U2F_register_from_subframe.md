# Universal XSS through FIDO U2F register from subframe

## Report Details
- **Report ID**: 993670
- **URL**: https://hackerone.com/reports/993670
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-28T21:16:34.835Z
- **Disclosed**: 2023-06-22T05:52:28.802Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

There are three weaknesses in Brave's FIDO U2F implementation.

* `u2f.register()` can be executed from cross-origin subframe by invoking [U2F.postMessage](https://github.com/brave/brave-ios/blob/e52c52495aa654584abe8172d689977756e6549d/Client/Frontend/UserContent/UserScripts/U2F.js#L264) directly
* Then, FIDO related modals show the name of top frame origin (but not caller subframe)
* The `version` parameter sent from the above `postMessage` is embedded in an [evaluateJavaScript](https://github.com/brave/brave-ios/blob/d01b8c07b8a6244af48798efe4afeccd266707e2/Client/WebAuthN/U2FExtensions.swift#L1003) without escape

The combination of these weaknesses allows cross-domain subframe to inject any JavaScript code to the top frame through fake U2F registration process.
## Products affected: 

 * Brave iOS Version 1.20 (20.09.11.20), also current Nightly

## Steps To Reproduce:

* Open [UXSS Victim](https://alice.csrf.jp/brave/uxss_victim.php) hosted on alice.csrf.jp.
  This site has a cross-origin iframe that opens evil.csrf.jp.
* Ready to Scan dialog is shown with the name of top frame
* Insert your FIDO device such as YubiKey 5Ci and touch
* Injected JavaScript `alert()` is executed on the top frame

## Supporting Material/References:

  * See attached movie file for the demonstration

## Impact

As written in summary, malicious web content in subframe can UXSS on the top frame origin.

## Attachments
- uxss_through_u2f.mp4
