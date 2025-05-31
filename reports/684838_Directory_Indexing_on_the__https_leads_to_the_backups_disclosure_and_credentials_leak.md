# Directory Indexing on the ████ (https://████/) leads to the backups disclosure and credentials leak

## Report Details
- **Report ID**: 684838
- **URL**: https://hackerone.com/reports/684838
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-30T04:33:53.534Z
- **Disclosed**: 2021-01-12T21:54:20.378Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
During poking around `█████████/24` range -  █████ looking for the Cisco devices, I came across `█████` which resolved to the https://██████/
While it's a not `.mil` host, it's likely related to the DoD since it hosted in the DoD-controlled ASN.

I discovered few critical vulnerabilities here, one of them is exposed backup files via directory listing.

##POC
https://███/obj/Debug/
█████
The source code can be found here:
https://█████████/obj/Debug/Package/GLOSS2.zip
It's zipped backup.

The DB credentials exposed here:
https://█████/obj/Debug/Package/GLOSS2.SetParameters.xml
███

##Suggested fix
Disable directory indexing, restrict access to the sensitive files, and change credentials as defense-in-depth measure.

## Impact

Source code & DB credentials leakage. Attacker can use it to compromise the resource.

## Attachments
No attachments
