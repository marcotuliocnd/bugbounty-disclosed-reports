# Open redirect in ck.php and lg.php

## Report Details
- **Report ID**: 1081406
- **URL**: https://hackerone.com/reports/1081406
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T12:51:23.396Z
- **Disclosed**: 2021-01-20T11:04:49.610Z

## Reporter
- **Username**: mbeccati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
An opportunity for open redirects has been available by design since the
early versions of Revive Adserver's predecessors in the impression and
click tracking scripts to allow third party ad servers to track such
metrics when delivering ads. Historically the display advertising
industry has considered that to be a feature, not a real vulnerability.

The lg.php and ck.php delivery scripts are subject to open redirect via
either dest, oadest and/or ct0 parameters.

## Impact

Users seeing a trustworthy domain could be redirected to a malicious URL without realising.

## Attachments
No attachments
