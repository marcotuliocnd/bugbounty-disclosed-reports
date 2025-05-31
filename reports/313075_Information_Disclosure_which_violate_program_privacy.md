# Information Disclosure which violate program privacy

## Report Details
- **Report ID**: 313075
- **URL**: https://hackerone.com/reports/313075
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-07T03:50:51.945Z
- **Disclosed**: 2018-02-20T15:42:12.559Z

## Reporter
- **Username**: eqbang
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
please refer to the following report:
https://hackerone.com/reports/311289

It was noticed that TTS changed the summary and set the domain to example.gov as not to reveal to the public. But at the bottom of the page, "britta changed the scope from https://ci.fr.cloud.gov to None."

Recommendation:
Should only provide general message for such situation: "britta changed the scope"

## Impact

not much of impact. but violate Confidentiality of the program.

## Attachments
- businessflaw.JPG
