# Reflected XSS on ███

## Report Details
- **Report ID**: 1057419
- **URL**: https://hackerone.com/reports/1057419
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-12T13:25:37.224Z
- **Disclosed**: 2021-04-02T18:41:19.562Z

## Reporter
- **Username**: phibz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary 
Reflected XSS on `█████████` for invalid paths.

## Description
Requesting a non-existent path on `█████`, such as `https://██████████/chron0x` the site responds with `No jsonpage404 is /chron0x versus /chron0x./chron0x does not exist`. As it can be seen, the path is reflected. This can be exploited with an XSS. 

Note: I am reporting this here, since the foorter of `███` states `Official ███ Website. The ████████ is an Equal Opportunity Employer.`, and the █████ underlies the DoD. If this should not belong to the DoD scope I would kindly ask to self close this issue.

## Step-by-step Reproduction Instructions

1. Visit `http://█████████/<svg onload=alert("chron0x")>`


## Mitigation/Remediation Actions
Sanitize the path input or switch to a generic error message.

## Impact

Javascript can be executed to steal data, etc.

## Attachments
No attachments
