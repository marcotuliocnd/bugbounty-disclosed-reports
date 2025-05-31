# Markdown parsing issue enables insertion of malicious tags

## Report Details
- **Report ID**: 116512
- **URL**: https://hackerone.com/reports/116512
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-15T08:08:07.472Z
- **Disclosed**: 2017-08-21T13:28:46.303Z

## Reporter
- **Username**: ru94mb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Markdown tags and event handlers can be used to load malicious URLs in user's profile statement.

Here is the payload that when entered in user's profile statement leads to the following HTML:

Payload: _www.attacker.com/malicious.exe_

Resulting HTML:  "html": "<p><em><a href=\"http://www.attacker.com/malicious.exe\">www.attacker.com/malicious.exe</a></em></p>\n"

See the following screenshots for more details:

"Profile.jpg"
"request.jpg"
"response.jpg"

User can be redirected to malicious URLs and malware can be hosted on gratipay.com using this vulnerability.

Fix:

Disable the functionality for these markdown tags.


## Attachments
- Response.JPG
- Request.JPG
- profile.JPG
