# PII Information Leak at https://████████.mil/

## Report Details
- **Report ID**: 1057269
- **URL**: https://hackerone.com/reports/1057269
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-12T06:46:59.874Z
- **Disclosed**: 2021-01-12T21:56:50.102Z

## Reporter
- **Username**: savxiety
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
While making use of some recon techniques I came across this file which is leaking PII information publically on the Internet. In the description section, I explain the contents of the file and why it shouldn't be public like this.

**Description:**
The file in the POC section contains more than 100 or 200 people as records. With their names, there are several other information classes present. The PII leak in this file is mainly the Names of the Individuals and their **Personal** Emails. If there were only official emails here, it would not be considered a PII leak because those emails are for official purposes and they are generally publically available. But in this case, not only their official emails are being leaked but also their personal emails. Personal emails belong only to the people and nothing official is related to those, an attacker should not have access to these emails because this is something private. This is a clear privacy violation for those who have lost their personal information to the public. The leaking file is perfect to be added into a database maintained by an attacker because it is arranged neatly in rows and columns. 

██████


## POC

https://██████████.mil/████████

## Step-by-step Reproduction Instructions

1. Go to https://█████████.mil/████████

2. Download the file.
3. View the PII


## Suggested Mitigation/Remediation Actions

- Take the file down from the Internet.
- Add an authentication mechanism to view the file.

## Impact

PII Information Leak.

## Attachments
No attachments
