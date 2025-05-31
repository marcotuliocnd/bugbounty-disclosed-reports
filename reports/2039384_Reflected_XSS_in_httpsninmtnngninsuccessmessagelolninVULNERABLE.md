# Reflected XSS in https://nin.mtn.ng/nin/success?message=lol&nin=<VULNERABLE>

## Report Details
- **Report ID**: 2039384
- **URL**: https://hackerone.com/reports/2039384
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-06-26T21:02:32.073Z
- **Disclosed**: 2024-10-05T10:27:41.138Z

## Reporter
- **Username**: hazemhussien99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
###Summary:
Hello team,
Found a reflected XSS on one your domains i believe https://nin.mtn.ng/nin/success?message=msg&nin= as the nin parameter is vulnerable.
Please check the following PoC:
Run the following command from a terminal:
curl -ski "https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script>"  | grep "alert"
{F2446627}

I reported this before in report #1737682 but it was closed as resolved while still vulnerable.

## Impact

Attacker could execute js in the victim's browser.

## Attachments
- mtn.png
