# fix(security):Path Traversal Bug

## Report Details
- **Report ID**: 1664244
- **URL**: https://hackerone.com/reports/1664244
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-09T17:07:15.249Z
- **Disclosed**: 2022-08-11T19:53:16.714Z

## Reporter
- **Username**: bhaskar_ram
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
Unsanitized input from CLI argument flows into `io.ioutil.ReadFile`, where it is used as a path. This may result in a Path Traversal vulnerability and allow an attacker to read arbitrary files.

See this fix : https://github.com/hyperledger/fabric/pull/3573

## Impact

There is a path traversal vulnerability in the source code of fabric

## Attachments
No attachments
