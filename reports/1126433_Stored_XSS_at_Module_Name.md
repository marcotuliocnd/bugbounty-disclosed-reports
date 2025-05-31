# Stored XSS at Module Name

## Report Details
- **Report ID**: 1126433
- **URL**: https://hackerone.com/reports/1126433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-15T19:45:30.502Z
- **Disclosed**: 2021-04-12T14:06:47.774Z

## Reporter
- **Username**: 20kilograma
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
Hello, I found stored xss at module name with this payload ```"><div onmouseover="alert('XSS');">Hello :)```

## Steps To Reproduce:
1. Add new container, it doesn't matter which is it
2. Paste this payload  in the module name```"><div onmouseover="alert('XSS');">Hello :)```
3. Update it then check the module name again in setting
4. Alert Popup

## Stored XSS
Stored cross-site scripting (also known as second-order or persistent XSS) arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

## Impact

Execute Js in victims browser

## Attachments
- xss_stripo.mov
