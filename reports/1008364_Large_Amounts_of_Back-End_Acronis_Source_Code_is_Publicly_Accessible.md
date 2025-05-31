# Large Amounts of Back-End Acronis Source Code is Publicly Accessible

## Report Details
- **Report ID**: 1008364
- **URL**: https://hackerone.com/reports/1008364
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-14T11:28:07.829Z
- **Disclosed**: 2024-08-26T15:35:12.785Z

## Reporter
- **Username**: shadowmap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Large amounts of back-end source code for the Acronis online portals and back-end management portals are publicly exposed. Many of the source code files contain encryption keys and other secrets as well.

## Steps To Reproduce

  1. Configure your burp proxy to map api.acronis.com to IP: 91.195.23.198 (originally mapped to msg3.acronis.com)
  2. Browse the following URLs: 
https://api.acronis.com/admin/
https://api.acronis.com/Elements/
https://api.acronis.com/ajax/
https://api.acronis.com/includes/
https://api.acronis.com/private/
https://api.acronis.com/login/
https://api.acronis.com/mag/
https://api.acronis.com/redirector/
https://api.acronis.com/op/
https://api.acronis.com/psg/
https://api.acronis.com/pad/
https://api.acronis.com/scripts/
https://api.acronis.com/podcast/
https://api.acronis.com/legacy/
https://api.acronis.com/help/
https://api.acronis.com/buy/
https://api.acronis.com/check/
https://api.acronis.com/events/
https://api.acronis.com/industry/
https://api.acronis.com/var/

3. These folders contain thousands of source code files that are exposing the internal workings of several public and internal systems used by Acronis as part of its marketing, sales, etc practices. 

## Recommendations
1. Remove the virtual host configurations from the server to only allow authorized applications to be accessible.
2. Disable directory listings.
3. Disable source code to be publicly displayed (force execution or restrict access via htaccess)

## Impact

A large amount of source code for various Acronis platforms is publicly accessible. The source code includes that for their public websites and sales portals, their internal systems such as (office.acronis.com), etc.

An attacker can leverage the visibility into the source code to exploit a wide range of vulnerabilities across the different platforms.

There are also several places where secrets and encryption tokens are embedded in plain-text as part of the source code.

I've attached screenshots of some such examples but I've refrained from downloading or spidering the complete source code available as I believe it would be over-reach in this case.

## Attachments
No attachments
