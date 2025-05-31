# Stored XSS in markdown file with Nextcloud Talk using Internet Explorer

## Report Details
- **Report ID**: 1023787
- **URL**: https://hackerone.com/reports/1023787
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-01T10:41:14.068Z
- **Disclosed**: 2021-02-19T12:08:10.754Z

## Reporter
- **Username**: verg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
While editing a markdown file through the text app, users can create link elements that have a javascript URL such as `javascript:alert(1)`.

Steps to reproduce:
* While editing a markdown file, select some text and click the "Add Link"  button.
* Using a web proxy, intercept the request and change the href value to `javascript:alert(1)`.

{F1060394}

* Refresh the document and click the malicious link created to fire the payload.

{F1060397}

Note that CSP blocks the javascript from running, but browsers such as IE are still vulnerable.

{F1060402}

## Impact

An attacker could execute arbitrary JavaScript code on the web browser of a victim who opens the file and clicks the malicious link.

## Attachments
- xss_markdown_1.png
- xss_markdown_2.png
- xss_markdown_3.png
