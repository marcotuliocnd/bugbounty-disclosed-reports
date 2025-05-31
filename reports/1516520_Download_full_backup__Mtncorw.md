# Download full backup  [Mtn.co.rw]

## Report Details
- **Report ID**: 1516520
- **URL**: https://hackerone.com/reports/1516520
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-03-19T14:54:17.726Z
- **Disclosed**: 2022-05-14T09:54:06.558Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
I discovered few critical vulnerabilities here, one of them is exposed backup files via directory listing.


## Steps To Reproduce:

go to https://mtn.co.rw/mtn.zip and download the file
extract the file and open
you will see the full backup of the website

## Similar report:
https://hackerone.com/reports/684838

## Impact

Source code & DB credentials leakage. Attacker can use it to compromise the resource.

## Attachments
No attachments
