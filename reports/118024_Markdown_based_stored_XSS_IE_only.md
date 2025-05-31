# Markdown based stored XSS (IE only)

## Report Details
- **Report ID**: 118024
- **URL**: https://hackerone.com/reports/118024
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-22T19:58:40.720Z
- **Disclosed**: 2017-05-03T22:28:08.622Z

## Reporter
- **Username**: a0xnirudh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello,

My other report #116697 deals with any browser even through its not a direct XSS as it doesn't execute in the context of the site. But here is another type of XSS using `vbscript:` which affects only IE users but executes on the context of the site (check the screenshot for POC alert(document.domain)).

### POC:

`[clickme](vbscript:alert(document.domain))`

`vbscript:` is not supported in Microsoft EDGE and updated versions of IE 11 (as per [this link](http://stackoverflow.com/questions/17483782/vbscript-support-in-internet-explorer-11) but it do works if people are working in the compatibility mode (I have read the gitlab instruction which specifically says users to turm off compatibility mode but if IE detects that the incoming webpages has some contents which is supported only on compatibility mode, it recommends that to the users I guess.).

For example, I comment the above link on one of the project/issues and then when I reloaded the page, IE detects that the incoming webpage contains scripts that might not be compatible and hence it told me to enable compatibility options by clicking a button. Usually if people see a warning like that from a browser, they will tend to enable it.

### Mitigation

Other then updated versions of IE 11, it works on IE10, 9, 8, 7. Also fixing this issue is so trivial by just blocking the keyword `vbscript` and since it executes on the context of the site, I believe this should be fixed.

## Attachments
- gitlab_vbscript_XSS.png
