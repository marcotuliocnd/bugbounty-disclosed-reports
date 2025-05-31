# Reflected - XSS

## Report Details
- **Report ID**: 1779447
- **URL**: https://hackerone.com/reports/1779447
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-11-20T10:23:27.636Z
- **Disclosed**: 2024-10-21T10:13:27.781Z

## Reporter
- **Username**: mathara
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hi, Team I'm Found Reflected XSS

## Steps To Reproduce:

1.Nave to https://www.mtn.bj/
2.Go to Messages 
3. Enter XSS Payload :

    * <h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE

4. Reflected the popup

## Impact

Cross site scripting attacks can have devastating consequences. Code injected into a vulnerable application can exfiltrate data or install malware on the user's machine. Attackers can masquerade as authorized users via session cookies, allowing them to perform any action allowed by the user account.

## Attachments
No attachments
