# Stored XSS on https://apps.topcoder.com/wiki/pages/editpage.action

## Report Details
- **Report ID**: 867133
- **URL**: https://hackerone.com/reports/867133
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-06T12:15:53.497Z
- **Disclosed**: 2020-05-12T13:37:08.626Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
## Summary:
Hi :) There is a stored XSS on wiki pages and it executes when editing page.

## Steps To Reproduce:
After I submitted #867125, i realized that the vote macro causes stored XSS on wiki edit page. 
A user can edit wiki pages on https://apps.topcoder.com/wiki/pages/editpage.action?pageId=. Users can insert macros to pages. Vote macro is vulnerable to XSS. 

Go to a wiki page, edit it and type

```
{vote:What is your favorite vulnerability?}
RCE
SSRF
XSS"><img src=X onerror=alert(document.domain)>
{vote}
```
and save it. When an other user edit this page, XSS will execute.

PoC:
https://apps.topcoder.com/wiki/pages/editpage.action?pageId=165871793
{F817588}

Note: This only works to signed-in users. Because unauthorized users cannot edit pages. I think there is a mistake on https://apps.topcoder.com/wiki/login.action now. If you encounter an error, you can login on main site (https://accounts.topcoder.com/member) then try.

## Impact

XSS can use to steal cookies or to run arbitrary code on victim's browser.

## Attachments
- 2020-05-06_15-09-02_ekran_g_r_nt_s_.png
