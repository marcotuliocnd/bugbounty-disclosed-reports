# POST following PUT confusion

## Report Details
- **Report ID**: 1752146
- **URL**: https://hackerone.com/reports/1752146
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-26T14:34:05.681Z
- **Disclosed**: 2022-12-02T21:03:59.407Z

## Reporter
- **Username**: robbotic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The bug I submitted at https://github.com/curl/curl/issues/9507 can have at least a few unintended security issues:

Information Disclosure: this bug causes an HTTP PUT to occur when the user intends for an HTTP POST to occur. The user, who intended an HTTP POST, expects the POSTed information to come from CURLOPT_POSTFIELDS. However, as an HTTP PUT is performed instead, the data that is PUT comes from a buffer specified in CURLOPT_READDATA, which may be sensitive information intended for an entirely different host (host1.com below). If CURLOPT_READDATA is not specified, this data could come from stdin!
Use after free: using the description above, if the user had already freed the data specified in CURLOPT_READDATA, then the unintended HTTP PUT (which was intended to be an HTTP POST) would attempt to read the freed data specified in CURLOPT_READDATA.

## Impact

An attacker could potentially inject data, either from stdin or from an unintended buffer. Further, without even an active attacker, this could lead to segfaults or sensitive information being exposed to an unintended recipient.

## Attachments
No attachments
