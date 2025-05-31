# php_snmp_parse_oid integer overflow in memory allocation

## Report Details
- **Report ID**: 178094
- **URL**: https://hackerone.com/reports/178094
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-25T21:01:23.607Z
- **Disclosed**: 2019-11-12T09:26:12.350Z

## Reporter
- **Username**: fwh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
https://bugs.php.net/bug.php?id=72708

An integer overflow in memory allocation allows to write past the allocated buffer, resulting in heap memory corruption.

Details and proof of concept are in the linked bug report; feel free to ask for more details if needed.

## Attachments
No attachments
