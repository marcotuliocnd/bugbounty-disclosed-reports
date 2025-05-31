# Usage of disabled protocol in curl

## Report Details
- **Report ID**: 2437131
- **URL**: https://hackerone.com/reports/2437131
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-03-27T18:16:38.575Z
- **Disclosed**: 2024-03-29T18:31:08.016Z

## Reporter
- **Username**: dfandrich
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
When a protocol selection parameter option disables all protocols without adding any then the default set of protocols would remain in the allowed set due to an error in the logic for removing protocols. The below command would perform a request to curl.se with a plaintext protocol which has been explicitly disabled.

curl --proto -all,-http http://curl.se

The flaw is only present if the set of selected protocols disables the entire set of available protocols, in itself a command with no practical use and therefore unlikely to be encountered in real situations. The curl security team has thus assessed this to be low severity bug.

## Impact

Requests can be sent on an unencrypted link even though the application explicitly disabled that.

## Attachments
No attachments
