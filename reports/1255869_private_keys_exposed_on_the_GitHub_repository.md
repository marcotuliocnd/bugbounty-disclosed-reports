# private keys exposed on the GitHub repository

## Report Details
- **Report ID**: 1255869
- **URL**: https://hackerone.com/reports/1255869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-09T12:00:24.861Z
- **Disclosed**: 2021-11-04T15:15:28.848Z

## Reporter
- **Username**: forcedrofes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mcuboot

## Vulnerability Information
##Summary:

When I searched Github for sensitive information I found some privet key in GitHub repository.
these are private RSA key and private server key, which could be used for unauthorized access.

Steps To Reproduce:

VISIT THESE LINKS:
Repository :

EX:
https://github.com/mcu-tools/mcuboot/blob/137d79717764ed32d5da4b4b301f32f81b2bf40f/enc-x25519-priv.pem

https://github.com/mcu-tools/mcuboot/blob/137d79717764ed32d5da4b4b301f32f81b2bf40f/root-ed25519.pem

(This is just an example)

This is the link that contains it all privet key :-

https://github.com/mcu-tools/mcuboot/search?p=1&q=extension%3Apem+private

##Supporting Material/References:
https://hackerone.com/reports/50170
https://hackerone.com/reports/638401

## Impact

1).Private key leakage
2). All of the servers using this key will be compromised

## Attachments
- privet_key.png
