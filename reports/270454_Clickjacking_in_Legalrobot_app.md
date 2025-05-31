# Clickjacking in Legalrobot app

## Report Details
- **Report ID**: 270454
- **URL**: https://hackerone.com/reports/270454
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-22T07:04:48.244Z
- **Disclosed**: 2017-11-10T11:36:03.466Z

## Reporter
- **Username**: 9it0wl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Dear Team,

#POC
Please find attached screenshots

#Steps to reproduce:

create index.html file with following content:
<iframe sandbox="allow-scripts allow-forms" src="https://app.legalrobot-uat.com/pending-verification" width="1000" height="600"></iframe>

Open index.html in browser

Actual result: Legalrobot email verification page is viewed in iframe.

#Remediation:
Frame busting technique is the better framing protection technique.
Sending the proper X-Frame-Options HTTP response headers that instruct the browser to not allow raming from other domains.

Same issue found in https://app.legalrobot.com/pending-verification as well.


## Attachments
- Clickjacking.png
- Clickjacking_uat.png
