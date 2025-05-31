# curl HSTS long file name clears contents 

## Report Details
- **Report ID**: 2279759
- **URL**: https://hackerone.com/reports/2279759
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-12-10T13:40:42.485Z
- **Disclosed**: 2024-01-20T17:17:39.985Z

## Reporter
- **Username**: cxshakal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## VULNERABILITY
When saving HSTS data to an excessively long file name, curl could end up removing all contents, making subsequent requests using that file unaware of the HSTS status they should otherwise use.

## INFO
The reason for this bug is that save function appended a suffix to the file name, created a temporary file and then in the last step renamed that to the final name. When the file name length was close to the limit of what is allowed on the file system, adding the extension would make it too long and then trigger this bug.

## Hackerone ticket #2236133

## Impact

HSTS bypass

## Attachments
No attachments
