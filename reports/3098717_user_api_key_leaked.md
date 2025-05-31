# user api key leaked

## Report Details
- **Report ID**: 3098717
- **URL**: https://hackerone.com/reports/3098717
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-04-17T12:16:12.700Z
- **Disclosed**: 2025-05-13T14:02:20.037Z

## Reporter
- **Username**: atasec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
While testing WakaTime using the tool gau (Get All URLs), I discovered an exposed API key in one of the older URLs. Upon testing this API key, I found that it successfully authenticated requests to an endpoint that would otherwise return "401 Unauthorized" without it. This indicates that the API key is valid and grants access to restricted resources, which could lead to information disclosure or potential misuse depending on the associated permissions.

## Impact

An attacker who obtains the API key waka_edf47c40-cabf-46e7-9f88-f1b44f00431f could potentially access personal information about the user or perform unauthorized actions on their behalf via the API.

## Attachments
No attachments
