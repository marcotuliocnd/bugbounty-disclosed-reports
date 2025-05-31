# DOM XSS on 50x.html page

## Report Details
- **Report ID**: 405191
- **URL**: https://hackerone.com/reports/405191
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-04T13:00:34.756Z
- **Disclosed**: 2018-10-16T18:09:59.634Z

## Reporter
- **Username**: cujanovic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
Hello,

The is a DOM XSS vulnerability on https://duckduckgo.com/50x.html, it seems like the sink is DIV.innerHTML and the source is location.search.
The PoC url is: https://duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain);%3E

The code that is causing this XSS is located in:
https://duckduckgo.com/lib/l110.js
Line 26, Column 60903

Below is the part of the vulnerable code:
`b5.createElement("div"));
cg = (m.exec(b7) || ["", ""])[1].toLowerCase();
b4 = R[cg] || R._default;
ce.innerHTML =  b4[1]  + b7.replace(aB, "<$1></$2>") + b4[2];
cb = b4[0];
while (cb--) {
	ce=ce.lastChild
}
if(!bI.support.leadingWhitespace&&b2.test(b7))`

Screenshot:
{F342240}

## Impact

The attacker can execute JS code.

## Attachments
- domxss-ddg.png
