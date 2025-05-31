# Local File Disclosure on the █████ (https://████████.edu/) leads to the full source code disclosure and credentials leak

## Report Details
- **Report ID**: 684836
- **URL**: https://hackerone.com/reports/684836
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-30T04:27:15.076Z
- **Disclosed**: 2024-06-27T17:31:57.334Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
During poking around `██████.00/24` range -  ██████████ looking for the Cisco devices, I came across `███` which resolved to the https://███████.edu/
While it's a not `.mil` host, it's likely related to the DoD since it hosted in the DoD-controlled ASN.

I discovered few critical vulnerabilities here, one of them is LFD (local file disclosure).

##POC
https://██████.edu/file.ashx?path=web.config
will download the website configuration file.
It exposes the DB credentials:
███

Similarly, attacker able to get content of any server-side resource, such as source code of application:
https://███.edu/file.ashx?path=UserAccountJSON.aspx.cs

## Impact

Source code & DB credentials leakage. Attacker can use it to compromise the resource.

## Attachments
No attachments
