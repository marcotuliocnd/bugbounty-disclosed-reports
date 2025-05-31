# Deserialization of Untrusted Data in www/delivery/adxmlrpc.php

## Report Details
- **Report ID**: 512076
- **URL**: https://hackerone.com/reports/512076
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-03-19T14:41:33.473Z
- **Disclosed**: 2019-04-23T13:08:01.674Z

## Reporter
- **Username**: mbeccati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the "what" parameter in the "openads.spc" RPC method.

## Impact

Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.

It is possible, although unconfirmed, that the vulnerability has been used by some attackers in order to gain access to some Revive Adserver instances and deliver malware through them to third party websites.

## Attachments
No attachments
