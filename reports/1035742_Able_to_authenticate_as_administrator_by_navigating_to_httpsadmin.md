# Able to authenticate as administrator by navigating to https://█████/admin/

## Report Details
- **Report ID**: 1035742
- **URL**: https://hackerone.com/reports/1035742
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-16T19:20:12.578Z
- **Disclosed**: 2021-01-12T21:35:13.552Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The endpoint at https://███████/admin/ authenticates the user  to the administrator user.

## Step-by-step Reproduction Instructions

1. Navigate to https://███/ and youll notice you will need to log in.
2. Navigating to https://██████████/admin/ will show you admin malformed page, with the ability to "log out"

As for now as we can see by the picture no data is present at the administrator panel, sure this might change at the future exposing sensitive ifnormation

████████


## Suggested Mitigation/Remediation Actions

Issuing 403 response when trying to access the /admin endpoint.

##Best regards
nagli

## Impact

Admin authentication bypass

## Attachments
No attachments
