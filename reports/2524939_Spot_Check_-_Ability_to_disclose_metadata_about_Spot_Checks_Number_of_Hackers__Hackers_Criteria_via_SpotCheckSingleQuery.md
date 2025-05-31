# [Spot Check] - Ability to disclose metadata about Spot Checks (Number of Hackers + Hackers Criteria) via "SpotCheckSingleQuery"

## Report Details
- **Report ID**: 2524939
- **URL**: https://hackerone.com/reports/2524939
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-05-29T14:51:25.222Z
- **Disclosed**: 2024-06-11T13:17:51.467Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hackers are able to leak private metadata about Spot Checks (num of hackers, total budget, criteria of selection.

**Description:**
When accepting Spot Check, we are able to see the program who requested it, the budget and the description in the UI.

While navigating to the Spot Check page from Program Perspective, and adding the ID URI such as

https://hackerone.com/organizations/████/spot_checks/██████

I was able to open the Spot Check settings as a program, which leaked metadata that should be confidential such as:

████

Specifically Number of Hackers and the Hackers Selection Criteria.

The leak occurs at the SpotCheckSingleQuery parameter.

```
{"operationName":"SpotCheckSingleQuery","variables":{"id":"████████","product_area":"spot_checks","product_feature":"view"},
```

### Steps To Reproduce

On a program view, navigate to https://hackerone.com/organizations/█████████/spot_checks/█████████, and change your spot_checks ID to the one you are onboarded to.

## Remediation

Do not return the extra metadata that is rendered from program view.

Best,

@nagli

## Impact

Ability to fetch extra confidential metadata on Spot checks.

## Attachments
No attachments
