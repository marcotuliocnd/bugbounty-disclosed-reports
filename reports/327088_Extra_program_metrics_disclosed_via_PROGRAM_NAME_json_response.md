# Extra program metrics disclosed via /PROGRAM_NAME json response

## Report Details
- **Report ID**: 327088
- **URL**: https://hackerone.com/reports/327088
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-18T16:28:00.128Z
- **Disclosed**: 2018-03-28T18:05:03.095Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
The response to www.hackerone.com/PROGRAM.json includes `sla_missed_count` `sla_failed_count` and `researcher_count`. 

**Description:**
Viewing the response from a program's json endpoint includes the values for `sla_missed_count`, `sla_failed_count` and `researcher_count`.

With regards to the SLA metrics, these are not included in the UI on the policy page and hovering over a program indicator just reveals a summary of the information, such as >=1 report has failed the SLA. There is no mention of these values being disclosed in the program settings pages and according to the SLA FAQ docs, only a `summarized version of a program’s response efficiency metric performance [will be displayed] on their hacker facing security page` https://support.hackerone.com/hc/en-us/articles/115005927583-Response-SLAs-on-Security-Pages

With regards to the researcher count, I'm including this because the information isn't disclosed in the UI when you have a pending invite to a program and I'm not sure why that might be. Nonetheless, viewing the same JSON response includes the `researcher_count`

### Steps To Reproduce

1. Log in
2. Visit any program and have Burp capture the response
3. Confirm the bottom of the JSON response includes the SLA information

### Supporting Material/References (Screenshots)

{F273408}

## Impact

The program settings page nor documentation indicates that SLA misses/fails will be disclosed. This information should be considered sensitive in nature and programs should opt into disclosing it if this is intentional since it reveals a minimum number of security vulnerabilities a program may be addressing (I say may because the SLA violation could be response / triage).

The researcher count could be considered sensitive in the context of a private invite, revealing how many vulnerabilities have been found by what number of people before having actually accepted an invitation. I recognize this is a stretch but also assume there is a reason this number isn't disclosed before accepting a private invitation.

## Attachments
- sla_metrics.png
