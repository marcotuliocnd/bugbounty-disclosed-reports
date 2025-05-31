# Deserialization of Untrusted Data in www/delivery/dxmlrpc.php

## Report Details
- **Report ID**: 542670
- **URL**: https://hackerone.com/reports/542670
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-19T14:38:45.548Z
- **Disclosed**: 2019-04-23T13:06:06.123Z

## Reporter
- **Username**: mbeccati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the first parameter in the "pluginExecute" RPC method.

## Impact

Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.

## Attachments
No attachments
