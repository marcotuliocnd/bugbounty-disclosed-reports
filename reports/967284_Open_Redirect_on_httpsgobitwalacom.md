# Open Redirect on https://go.bitwala.com/

## Report Details
- **Report ID**: 967284
- **URL**: https://hackerone.com/reports/967284
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-26T05:32:39.085Z
- **Disclosed**: 2020-10-30T06:27:35.362Z

## Reporter
- **Username**: soe_htet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nuri

## Vulnerability Information
Hello 
I found  open redirect bug on https://go.bitwala.com.
I know that domain is not in scope.I just want to inform a bug.

 Steps To Reproduce:

1. go to `https://go.bitwala.com/d4ffbnr?campaign=brand-nov&adgroup=native&creative=link-liquidity%20&fallback=https%3A%2F%2Fwww.bitwala.com%2F%3Futm_source%3Dcryptomonday%26utm_campaign%3Dbrand-nov%26utm_medium%3Dnative%26utm_content%3Dlink-liquidity%20`

2. Change the url like this`https://go.bitwala.com/d4ffbnr?campaign=brand-nov&adgroup=native&creative=link-liquidity%20&fallback=https://www.google.com`

3. It will redirect to `https://www.google.com`

## Impact

An attacker can use this vulnerability to redirect  other malicious,evil websites
.
https://cwe.mitre.org/data/definitions/601.html

## Attachments
No attachments
