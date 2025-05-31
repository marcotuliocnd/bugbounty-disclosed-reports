# PII/PHI data available on web https://████████Portals/22/Documents/Meetings

## Report Details
- **Report ID**: 877598
- **URL**: https://hackerone.com/reports/877598
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-18T23:11:21.209Z
- **Disclosed**: 2020-06-25T13:05:56.752Z

## Reporter
- **Username**: pvm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
https://███Portals/22/Documents/Meetings contains many internal documents which likely were reviewed on meeting/meetings preparations which should not be available for public but searchable via google/bing.  Documents include: resumes, bio data form, emails (including history of medical conditions), mails, letters. 
PII/PHI exposed: name, emails, phones, medical history/condition.

**Description:**
https://███████Portals/22/Documents/Meetings contains many internal documents which likely were reviewed on meeting/meetings preparations which should not be available for public but searchable via google/bing.  Documents include: resumes, bio data form, emails (including history of medical conditions), mails. 
PII exposed: name, emails, phones, medical history/condition.
Here you can see some examples:
- Detailed resume: https://█████████Portals/22/Documents/Meetings/m14/█████████.pdf
- long email thread including official letters (name, email, medical conditions, phone): https://█████Portals/22/Documents/Meetings/m18/████████.pdf
- Internal emails (names, emails, phones): https://██████████Portals/22/Documents/Meetings/m11/██████████.pdf
- email (name, email, medical conditions, phone): https://██████████Portals/22/Documents/Meetings/m11/█████████.pdf
- email (name, email, medical conditions, phone): https://█████████Portals/22/Documents/Meetings/m19/██████████.pdf
- an attorney email (name, email, medical conditions): https://████████Portals/22/Documents/Meetings/m13/█████████.pdf
- letter (name, medical condition): https://█████████Portals/22/Documents/Meetings/m17/████.pdf
- email/letter with medical condition: https://████████Portals/22/Documents/Meetings/m18/██████████.pdf
- statement: https://████████Portals/22/Documents/Meetings/m19/█████.pdf 
- memorandum: https://███████Portals/22/Documents/Meetings/m11/██████████.pdf
- biographic data form: https://██████████Portals/22/Documents/Meetings/m18/██████████.pdf
- biographic data form: https://█████████Portals/22/Documents/Meetings/m19/███████.pdf

Also here I've found many biographies of medical officers  with different level of details. Some of them are very detailed.

## Impact
High or Critical. 
Because of PII/PHI exposed: name, emails, phones, medical history/condition. 

## Step-by-step Reproduction Instructions

- Perform a search on Bing: site: ███ AND "https://██████████Portals/22/Documents/Meetings/" 
- OR navigate to the provided links:
  - Detailed resume: https://███████Portals/22/Documents/Meetings/m14/█████.pdf
  - long email thread including official letters (name, email, medical conditions, phone): https://███Portals/22/Documents/Meetings/m18/█████.pdf
  - Internal emails (names, emails, phones): https://███████Portals/22/Documents/Meetings/m11/██████.pdf
  - email (name, email, medical conditions, phone): https://████Portals/22/Documents/Meetings/m11/███████.pdf
  - email (name, email, medical conditions, phone): https://█████████Portals/22/Documents/Meetings/m19/███.pdf
  - an attorney email (name, email, medical conditions): https://██████Portals/22/Documents/Meetings/m13/███████.pdf
  - letter (name, medical condition): https://██████Portals/22/Documents/Meetings/m17/████.pdf
  - email/letter with medical condition: https://█████████Portals/22/Documents/Meetings/m18/███.pdf
  - statement: https://████████Portals/22/Documents/Meetings/m19/██████████.pdf 
  - memorandum: https://█████████Portals/22/Documents/Meetings/m11/██████.pdf
  - biographic data form: https://██████Portals/22/Documents/Meetings/m18/██████.pdf
  - biographic data form: https://███████Portals/22/Documents/Meetings/m19/█████████.pdf
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Remove thee files or restrict access to them. Other files in the folders should be evaluated.

## Impact

High or Critical. 
Because of PII/PHI exposed: name, emails, phones, medical history/condition.

## Attachments
No attachments
