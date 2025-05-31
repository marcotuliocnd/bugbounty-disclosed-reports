# Brave Browser potentially logs the last time a Tor window was used

## Report Details
- **Report ID**: 1024668
- **URL**: https://hackerone.com/reports/1024668
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-02T17:48:49.018Z
- **Disclosed**: 2020-11-04T18:36:48.681Z

## Reporter
- **Username**: sickcodes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

A vulnerability in the Brave Browser allows an attacker to view the last time a Tor session was used in incognito mode. A local, on-disk attacker could read the Brave Browser's "Local State" json file and identify the last time a Tor session was used, affecting the confidentiality of a user's Tor session.

For example, the "Local State" file of a user who has recently used a Tor session would list a key value pair with a timestamp as accurate as "13248493693576042". This allows an attacker to fingerprint, or prove beyond reasonable doubt, that a user was using Tor at that very specific moment in time.

## Products affected: 

Brave 1.18.27 and below

## Steps To Reproduce:

 Start a Tor session in Brave Browser

## Supporting Material/References:

As discussed with security@ team in email chain titled:

Re: [Security] CVE Request 981386 - Brave Browser (All) - Exposure of
 Sensitive Information to an Unauthorized Actor While Using Tor Feature

And fixed in PR 7010:
https://github.com/brave/brave-core/pull/7010

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Violate the confidentiality of a user's Tor session.

## Attachments
No attachments
