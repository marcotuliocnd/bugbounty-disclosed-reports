# Clickjacking on https://download.nextcloud.com/

## Report Details
- **Report ID**: 662155
- **URL**: https://hackerone.com/reports/662155
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-07-28T06:44:11.235Z
- **Disclosed**: 2019-11-11T15:23:42.440Z

## Reporter
- **Username**: j4tayu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
the vulnerability is Clickjacking

Steps for Reproduce:

1. Create a script like this
<title> Clickjacking! </ title>
<p> The Site is Vulnerability Clickjacking </ p>
<iframe src = "https://www.download.nextcloud.com" height = "700px" width = "700px"> </ iframe>

2. Enter a file name after saving it in the .html format
Then the web is Vuln Clickjacking

Sorry bad english (im indonesian)

## Impact

By using Clickjacking technique, an attacker hijack's click's
meant for one page and route them to another page, most likely
for another application, domain, or both.

## Attachments
No attachments
