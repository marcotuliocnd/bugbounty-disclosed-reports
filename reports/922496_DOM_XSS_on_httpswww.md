# DOM XSS on https://www.███████

## Report Details
- **Report ID**: 922496
- **URL**: https://hackerone.com/reports/922496
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-13T12:09:37.953Z
- **Disclosed**: 2020-09-29T20:35:16.978Z

## Reporter
- **Username**: gamer7112
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Description
DOM XSS can be achieved due to missing sanitation  when setting the source of an iframe.

#POC
1. Visit https://www.████frame.html#javascript:alert(document.domain)
2. View alert

#Vulnerable Code
```javascript
function Load()
{
	str=document.location.hash,idx=str.indexOf('#')
	if(idx>=0) str=str.substr(1);
	if(str) PPTSld.location.replace(str);
}
```

## Impact

An attacker could execute arbitrary javascript on another user.

## Attachments
No attachments
